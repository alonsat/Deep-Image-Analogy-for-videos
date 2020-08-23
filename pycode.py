#Video to frames
import os
import cv2
import sys
import torch
import subprocess
import shutil
import time
import array
import numpy as np
import datetime as dt
def read_tensor(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    arr = array.array('f')
    arr.frombytes(data)
    return torch.tensor(arr, dtype=torch.float)
def write_tensor(filename, tens):
    with open(filename, 'wb') as f:
        arr = array.array('f')
        arr.fromlist(list(tens.numpy()))
        arr.tofile(f)
def update_layers(frame_num,img_dim,SIZES,frames_folder_output):
  img_dim_inv= img_dim[1],img_dim[0]
  for layer in [0,1,2,3,4,5]:
    dim=(SIZES[layer][1],SIZES[layer][2]) #13,26
    inv_dim=dim[1],dim[0]


    opticalflow=read_tensor('/content/Deep-Image-Analogy-for-videos/flows/opticalflow_%d'%frame_num).view(img_dim[0], img_dim[1], 2)
    opticalflow=opticalflow.to(dtype=torch.long)
    
    pre_layer = read_tensor(frames_folder_output+"/files/fileap%d.txt"%layer).view(SIZES[layer])
    
    pre_layer_fit_dim=cv2.resize(pre_layer.permute(1,2,0).numpy(),img_dim_inv,interpolation=cv2.INTER_NEAREST) #25,50,512
    
    pre_layer_torch= (torch.FloatTensor(pre_layer_fit_dim)).unsqueeze(0).to('cpu') #1, 25,50,512
    

    
    '''opticalflow=cv2.resize(np.array(opticalflow),(dim[1],dim[0]),interpolation=cv2.INTER_NEAREST) 
    opticalflow[:,:, 0]=np.floor(opticalflow[:,:, 0]*dim[1]/(img_dim[1]))
    opticalflow[:,:, 1]=np.floor(opticalflow[:,:, 1]*dim[0]/(img_dim[0]))'''
    
    post_layer = pre_layer_torch[:, opticalflow[:,:, 1], opticalflow[:,:, 0], :].view(pre_layer_torch.size())


    post_layer_back=cv2.resize(post_layer[0].numpy(),inv_dim,interpolation=cv2.INTER_NEAREST)
    post_layer_back=torch.FloatTensor(post_layer_back).permute(2,0,1)




    write_tensor('fileap%d.txt'%layer,torch.tensor(post_layer_back).reshape(-1))
def copyfiles(path1,path2):
    '''
        a function for copying the feature maps and patches of the starting frame
    '''
    shutil.copyfile(path1+"/filea0.txt",path2+"/filea0.txt")
    shutil.copyfile(path1+"/filea1.txt",path2+"/filea1.txt")
    shutil.copyfile(path1+"/filea2.txt",path2+"/filea2.txt")
    shutil.copyfile(path1+"/filea3.txt",path2+"/filea3.txt")
    shutil.copyfile(path1+"/filea4.txt",path2+"/filea4.txt")
    shutil.copyfile(path1+"/filea5.txt",path2+"/filea5.txt")
    shutil.copyfile(path1+"/fileap0.txt",path2+"/fileap0.txt")
    shutil.copyfile(path1+"/fileap1.txt",path2+"/fileap1.txt")
    shutil.copyfile(path1+"/fileap2.txt",path2+"/fileap2.txt")
    shutil.copyfile(path1+"/fileap3.txt",path2+"/fileap3.txt")
    shutil.copyfile(path1+"/fileap4.txt",path2+"/fileap4.txt")
    shutil.copyfile(path1+"/fileap5.txt",path2+"/fileap5.txt")
    shutil.copyfile(path1+"/fileb0.txt",path2+"/fileb0.txt")
    shutil.copyfile(path1+"/fileb1.txt",path2+"/fileb1.txt")
    shutil.copyfile(path1+"/fileb2.txt",path2+"/fileb2.txt")
    shutil.copyfile(path1+"/fileb3.txt",path2+"/fileb3.txt")
    shutil.copyfile(path1+"/fileb4.txt",path2+"/fileb4.txt")
    shutil.copyfile(path1+"/fileb5.txt",path2+"/fileb5.txt")
    shutil.copyfile(path1+"/filebp0.txt",path2+"/filebp0.txt")
    shutil.copyfile(path1+"/filebp1.txt",path2+"/filebp1.txt")
    shutil.copyfile(path1+"/filebp2.txt",path2+"/filebp2.txt")
    shutil.copyfile(path1+"/filebp3.txt",path2+"/filebp3.txt")
    shutil.copyfile(path1+"/filebp4.txt",path2+"/filebp4.txt")
    shutil.copyfile(path1+"/filebp5.txt",path2+"/filebp5.txt")
    shutil.copyfile(path1+"/patchab.txt",path2+"/patchab.txt")
    shutil.copyfile(path1+"/patchba.txt",path2+"/patchba.txt")

def remfiles(frames_folder_output):
    '''
        a function for deleting the feature maps and patches of the previous frame used when we return to starting frame when we don't use the first frame as the starting frame
    '''
    os.remove(frames_folder_output+"/filea0.txt")
    os.remove(frames_folder_output+"/filea1.txt")
    os.remove(frames_folder_output+"/filea2.txt")
    os.remove(frames_folder_output+"/filea3.txt")
    os.remove(frames_folder_output+"/filea4.txt")
    os.remove(frames_folder_output+"/filea5.txt")
    os.remove(frames_folder_output+"/fileap0.txt")
    os.remove(frames_folder_output+"/fileap1.txt")
    os.remove(frames_folder_output+"/fileap2.txt")
    os.remove(frames_folder_output+"/fileap3.txt")
    os.remove(frames_folder_output+"/fileap4.txt")
    os.remove(frames_folder_output+"/fileap5.txt")
    os.remove(frames_folder_output+"/fileb0.txt")
    os.remove(frames_folder_output+"/fileb1.txt")
    os.remove(frames_folder_output+"/fileb2.txt")
    os.remove(frames_folder_output+"/fileb3.txt")
    os.remove(frames_folder_output+"/fileb4.txt")
    os.remove(frames_folder_output+"/fileb5.txt")
    os.remove(frames_folder_output+"/filebp0.txt")
    os.remove(frames_folder_output+"/filebp1.txt")
    os.remove(frames_folder_output+"/filebp2.txt")
    os.remove(frames_folder_output+"/filebp3.txt")
    os.remove(frames_folder_output+"/filebp4.txt")
    os.remove(frames_folder_output+"/filebp5.txt")
    os.remove(frames_folder_output+"/patchab.txt")
    os.remove(frames_folder_output+"/patchba.txt")



def deep_image_video_analogy_forward(startframe,NumberOfFrames,exe_path,path_to_models,frames_folder_input,image_semantic,recursive_flag,frames_folder_output,Flag_Flow,semi_recursive):
    '''a function that runs deep image analogy for videos starting form start frame until the last frame '''
    img0=cv2.imread('/content/Deep-Image-Analogy-for-videos/frames_inp/frame0.png')
    img_dim= img0.shape[0], img0.shape[1]
    
    os.system("python /content/Deep-Image-Analogy-for-videos/compute_flows.py")
    for count in range(startframe,NumberOfFrames):
      if(count>0 and recursive_flag and not(semi_recursive)): 
          image_semantic='{}/frame{}.png'.format(frames_folder_output,count-1)
      if(count==1 and semi_recursive):
          image_semantic='{}/frame{}.png'.format(frames_folder_output,count-1)
          recursive_flag=False
          #semi_recursive=False
          print("I AM RUNNING SEMI RECURSIVE")
      p1=exe_path
      p2=path_to_models
      p3='{}/frame{}.png'.format(frames_folder_input,count)
      p4=image_semantic
      p5=frames_folder_output+"/"
      p6='0'
      p7=(sys.argv[7])
      p8=(sys.argv[8])
      p9=(sys.argv[9])
      if count==0:
          p10='0'
          p11='0'
          p12=sys.argv[11]        
      else:
          p10=sys.argv[10]
          p11=sys.argv[11]
          p12=sys.argv[11]
      starttime=dt.datetime.now()
      if(os.system(p1+" "+p2+" "+p3+" "+p4+" "+p5+" "+p6+" "+p7+" "+p8+" "+p9+" "+p10+" "+p11+" "+p12)):
          print("FAIL")
      print('frame num. %d:'%count,dt.datetime.now()-starttime)
      os.rename(frames_folder_output+"/resultAB.png",frames_folder_output+"/frame{}.png".format(count))
      if count==startframe:
          copyfiles(frames_folder_output+"/files",frames_folder_output+"/n")
      if Flag_Flow:
          SIZES=[]
          with open('/content/Deep-Image-Analogy-for-videos/sizes.txt') as f:
              for line in f:
                  nums=[int(x) for x in line.split()]
                  for i in range(6):
                      SIZES.append((nums[3*i],nums[3*i+1],nums[3*i+2]))
          if count!=NumberOfFrames-1:# and  not(count==0 and semi_recursive) and  not (recursive_flag):
              update_layers(count+1,img_dim,SIZES,frames_folder_output)
def deep_image_video_analogy_backward(startframe,NumberOfFrames,exe_path,path_to_models,frames_folder_input,image_semantic,recursive_flag,frames_folder_output,Flag_Flow):

    for count in range(startframe-1,-1,-1):
      if count>0 and recursive_flag:
          image_semantic='{}/frame{}.png'.format(frames_folder_output,count+1)
          if semi_recursive:
              recursive_flag=False
          
      p1=exe_path
      p2=path_to_models
      p3='{}/frame{}.png'.format(frames_folder_input,count)
      p4=image_semantic
      p5=frames_folder_output
      p6='0'
      p7=(sys.argv[7])
      p8=(sys.argv[8])
      p9=(sys.argv[9])
      if count==0:
          p10='0'
          p11='0'
          p12=sys.argv[11]        
      else:
          p10=sys.argv[10]
          p11=sys.argv[11]
          p12=sys.argv[11]
      starttime=dt.datetime.now()
      if os.system(p1+" "+p2+" "+p3+" "+p4+" "+p5+" "+p6+" "+p7+" "+p8+" "+p9+" "+p10+" "+p11+" "+p12):
          print("FAIL")
      print('frame num. %d:'%count,dt.datetime.now()-starttime)
      os.rename(frames_folder_output+"/resultAB.png",frames_folder_output+"/frame{}.png".format(count))
      
if __name__ == "__main__":
    exe_path="/content/Deep-Image-Analogy-for-videos/demo"#path to executable
    path_to_models="/content/Deep-Image-Analogy-for-videos/deep_image_analogy/models/"#path to models folder
    input_video_path=sys.argv[1] #path to video
    frames_folder_input="/content/Deep-Image-Analogy-for-videos/frames_inp" #folder to contain the frames of the original video
    image_semantic=sys.argv[2] #path to style file
    frames_folder_output="/content/Deep-Image-Analogy-for-videos/output" #path to folder that would contatin the frames of the output video
    output_video_path=sys.argv[3] #path for the output video
    startframe=0 #the start frame that we use
    is_two_sided=sys.argv[5]=='True' # a flag to signify if we want to run the algorithm in a two sided way starting from an arbitrary frame
    if int(sys.argv[4])==1:
        recursive_flag=True #recursive flag for running the algorithm in recursive way
        semi_recursive=False
    elif int(sys.argv[4])==2:
        recursive_flag=False 
        semi_recursive=True #a flag for running the algorithm in a semi recursive (first frame recursive) way
    else:
        recursive_flag=False
        semi_recursive=False
    Flag_Flow=sys.argv[6]=='True' #flag to mark if we use optical flow

    if not os.path.exists(frames_folder_input):
        os.mkdir(frames_folder_input)
    #split the original video to frames
    vidcap = cv2.VideoCapture(input_video_path)
    success,image = vidcap.read()
    count = 0 #frame counter
    while success:
      cv2.imwrite(frames_folder_input+"/frame{}.png".format(count), image)  # save frame as PNG file      
      success,image = vidcap.read()
      count += 1
    print('%d frames were read' % count)

    fps=int(vidcap.get(5)) # get the frame rate per second of the video
    vidcap.release()

    NumberOfFrames=count


    if not os.path.exists(frames_folder_output): #create the output folder
        os.mkdir(frames_folder_output)


    img_BP=cv2.imread(image_semantic) #read B_prime image

    height, width=img_BP.shape[0],img_BP.shape[1]
    
    deep_image_video_analogy_forward(startframe,NumberOfFrames,exe_path,path_to_models,frames_folder_input,image_semantic,recursive_flag,frames_folder_output,Flag_Flow,semi_recursive)
    
    remfiles(frames_folder_output+"/files")

    copyfiles(frames_folder_output+"/n",frames_folder_output+"/files")
    if is_two_sided:
        deep_image_video_analogy_backward(startframe,NumberOfFrames,exe_path,path_to_models,frames_folder_input,image_semantic,recursive_flag,frames_folder_output,Flag_Flow)
    
    #convert the frames to video

    temp_img=cv2.imread(frames_folder_output+"/frame0.png")

    frame_width = temp_img.shape[1]
    frame_height = temp_img.shape[0]
    fourcc = cv2.VideoWriter_fourcc(*'VP90')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height), isColor=True)
    count = 0
    while True:
      img=cv2.imread(frames_folder_output+"/frame{}.png".format(count))
      if img is None:
        break
      out.write(img)
      print('wrote frame: ', count)
      count += 1

    print('%d frames were written' % count)
    print(output_video_path)
    out.release()
 

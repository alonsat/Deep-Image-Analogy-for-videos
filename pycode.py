#Video to frames
import os
import cv2
import sys
import subprocess
import shutil
import time
if __name__ == "__main__":
    input_video_path="/content/Deep-Image-Analogy-for-videos/eagle.mp4"
    output_frames_folder_path="/content/Deep-Image-Analogy-for-videos/frames_inp"
    image_semantic="/content/Deep-Image-Analogy-for-videos/fly.png"
    frames_folder_output="/content/Deep-Image-Analogy-for-videos/output"
    output_video_path="/content/Deep-Image-Analogy-for-videos/output"

    image_orig_semantic=image_semantic
    if not os.path.exists(output_frames_folder_path):
        os.mkdir(output_frames_folder_path)
    vidcap = cv2.VideoCapture(input_video_path)
    success,image = vidcap.read()
    count = 0
    frame_limit=1000 #if more than frame_limit frames, they will not be saved
    while success:
      cv2.imwrite(output_frames_folder_path+"/frame{}.png".format(count), image)     # save frame as JPEG file      
      success,image = vidcap.read()
      #print('Read a new frame: ', success)
      count += 1
      if(count==frame_limit): #
        break
    print('%d frames were read' % count)

    fps=int(vidcap.get(5))
    fourcc=int(vidcap.get(6))
    vidcap.release()

    NumberOfFrames=count
    flag_google_drive=False
    frames_folder_input=output_frames_folder_path


    if not os.path.exists(frames_folder_output): #create the output folder
        os.mkdir(frames_folder_output)


    img_BP=cv2.imread(image_semantic) #read B_prime image



    height, width=img_BP.shape[0],img_BP.shape[1]
    startframe=0
    recursive_flag=True

    for count in range(startframe,NumberOfFrames):
      #img_A=cv2.imread(frames_folder_input+"/frame%d.jpg" % count) #read new frame (A)
      #if(img_A is None): #just a test to when we are out of images (maybe we can switch to a counter)
      #  break

      print(count)
      #if you delete next 2 lines, it is the frame by frame method, otherwise recursive:
      if(count>0 and recursive_flag):
          
          image_semantic='{}/frame{}.png'.format(frames_folder_output,count-1)
          recursive_flag=False
      p1="/content/Deep-Image-Analogy-for-videos/demo"#"C:\\Users\\User\\Downloads\\Deep-Image-Analogy-master\\Deep-Image-Analogy-master\\Build\\x64\\Release\\deep_image_analogy.exe"
      p2="/content/Deep-Image-Analogy-for-videos/deep_image_analogy/models/"#"C:\\Users\\User\\Downloads\\Deep-Image-Analogy-master\\Deep-Image-Analogy-master\\windows\\deep_image_analogy\\models\\"
      p3='{}/frame{}.png'.format(output_frames_folder_path,count)
      p4=image_semantic
      p5=frames_folder_output+"/"#"C:\\Users\\User\\Downloads\\Deep-Image-Analogy-master\\Deep-Image-Analogy-master\\Build\\x64\\Release\\"
      p6='0'
      p7='1'
      p8='3'
      p9='0'
      p13='/content/Deep-Image-Analogy-for-videos/flows/opticalflow_{}'.format(count)#flowfile
      p15='0.5'#lambda
      if(count==0):
          p10='0'
          p11='0'
          p12='3'        
          p14='0'
      else:
          p10='1'
          p11='3'
          p12='3'
          p14='0'
      starttime=time.time()
      if(os.system(p1+" "+p2+" "+p3+" "+p4+" "+p5+" "+p6+" "+p7+" "+p8+" "+p9+" "+p10+" "+p11+" "+p12+" "+p13+" "+p14+" "+p15)):
          print("FAIL")
      print(time.time()-starttime)
      os.rename(frames_folder_output+"/resultAB.png",frames_folder_output+"/frame{}.png".format(count))
      if(count==startframe):
          shutil.copyfile(frames_folder_output+"/flowAB.txt",frames_folder_output+"/n/flowAB.txt")
          shutil.copyfile(frames_folder_output+"/flowBA.txt",frames_folder_output+"/n/flowBA.txt")
          shutil.copyfile(frames_folder_output+"/filea0.txt",frames_folder_output+"/n/filea0.txt")
          shutil.copyfile(frames_folder_output+"/filea1.txt",frames_folder_output+"/n/filea1.txt")
          shutil.copyfile(frames_folder_output++"/filea2.txt",frames_folder_output+"/n/filea2.txt")
          shutil.copyfile(frames_folder_output+"/filea3.txt",frames_folder_output+"/n/filea3.txt")
          shutil.copyfile(frames_folder_output+"/filea4.txt",frames_folder_output+"/n/filea4.txt")
          shutil.copyfile(frames_folder_output+"/filea5.txt",frames_folder_output+"/n/filea5.txt")
          shutil.copyfile(frames_folder_output+"/fileap0.txt",frames_folder_output+"/n/fileap0.txt")
          shutil.copyfile(frames_folder_output+"/fileap1.txt",frames_folder_output+"/n/fileap1.txt")
          shutil.copyfile(frames_folder_output+"/fileap2.txt",frames_folder_output+"/n/fileap2.txt")
          shutil.copyfile(frames_folder_output+"/fileap3.txt",frames_folder_output+"/n/fileap3.txt")
          shutil.copyfile(frames_folder_output+"/fileap4.txt",frames_folder_output+"/n/fileap4.txt")
          shutil.copyfile(frames_folder_output+"/fileap5.txt",frames_folder_output+"/n/fileap5.txt")
          shutil.copyfile(frames_folder_output+"/fileb0.txt",frames_folder_output+"/n/fileb0.txt")
          shutil.copyfile(frames_folder_output+"/fileb1.txt",frames_folder_output+"/n/fileb1.txt")
          shutil.copyfile(frames_folder_output+"/fileb2.txt",frames_folder_output+"/n/fileb2.txt")
          shutil.copyfile(frames_folder_output+"/fileb3.txt",frames_folder_output+"/n/fileb3.txt")
          shutil.copyfile(frames_folder_output+"/fileb4.txt",frames_folder_output+"/n/fileb4.txt")
          shutil.copyfile(frames_folder_output+"/fileb5.txt",frames_folder_output+"/n/fileb5.txt")
          shutil.copyfile(frames_folder_output+"/filebp0.txt",frames_folder_output+"/n/filebp0.txt")
          shutil.copyfile(frames_folder_output+"/filebp1.txt",frames_folder_output+"/n/filebp1.txt")
          shutil.copyfile(frames_folder_output+"/filebp2.txt",frames_folder_output+"/n/filebp2.txt")
          shutil.copyfile(frames_folder_output+"/filebp3.txt",frames_folder_output+"/n/filebp3.txt")
          shutil.copyfile(frames_folder_output+"/filebp4.txt",frames_folder_output+"/n/filebp4.txt")
          shutil.copyfile(frames_folder_output+"/filebp5.txt",frames_folder_output+"/n/filebp5.txt")
      
      if(flag_google_drive):
        cv2.imwrite(drive_path+"/frame%d.png" % count, img) #write new result
      #print('write a new frame: ', success, count)
    os.remove(frames_folder_output+"/flowAB.txt")
    os.remove(frames_folder_output+"/flowBA.txt")
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




    shutil.copyfile(frames_folder_output+"/n/flowAB.txt",frames_folder_output+"/flowAB.txt")
    shutil.copyfile(frames_folder_output+"/n/flowBA.txt",frames_folder_output+"/flowBA.txt")
    shutil.copyfile(frames_folder_output+"/n/filea0.txt",frames_folder_output+"/filea0.txt")
    shutil.copyfile(frames_folder_output+"/n/filea1.txt",frames_folder_output+"/filea1.txt")
    shutil.copyfile(frames_folder_output+"/n/filea2.txt",frames_folder_output+"/filea2.txt")
    shutil.copyfile(frames_folder_output+"/n/filea3.txt",frames_folder_output+"/filea3.txt")
    shutil.copyfile(frames_folder_output+"/n/filea4.txt",frames_folder_output+"/filea4.txt")
    shutil.copyfile(frames_folder_output+"/n/filea5.txt",frames_folder_output+"/filea5.txt")
    shutil.copyfile(frames_folder_output+"/n/fileap0.txt",frames_folder_output+"/fileap0.txt")
    shutil.copyfile(frames_folder_output+"/n/fileap1.txt",frames_folder_output+"/fileap1.txt")
    shutil.copyfile(frames_folder_output+"/n/fileap2.txt",frames_folder_output+"/fileap2.txt")
    shutil.copyfile(frames_folder_output+"/n/fileap3.txt",frames_folder_output+"/fileap3.txt")
    shutil.copyfile(frames_folder_output+"/n/fileap4.txt",frames_folder_output+"/fileap4.txt")
    shutil.copyfile(frames_folder_output+"/n/fileap5.txt",frames_folder_output+"/fileap5.txt")
    shutil.copyfile(frames_folder_output+"/n/fileb0.txt",frames_folder_output+"/fileb0.txt")
    shutil.copyfile(frames_folder_output+"/n/fileb1.txt",frames_folder_output+"/fileb1.txt")
    shutil.copyfile(frames_folder_output+"/n/fileb2.txt",frames_folder_output+"/fileb2.txt")
    shutil.copyfile(frames_folder_output+"/n/fileb3.txt",frames_folder_output+"/fileb3.txt")
    shutil.copyfile(frames_folder_output+"/n/fileb4.txt",frames_folder_output+"/fileb4.txt")
    shutil.copyfile(frames_folder_output+"/n/fileb5.txt",frames_folder_output+"/fileb5.txt")
    shutil.copyfile(frames_folder_output+"/n/filebp0.txt",frames_folder_output+"/filebp0.txt")
    shutil.copyfile(frames_folder_output+"/n/filebp1.txt",frames_folder_output+"/filebp1.txt")
    shutil.copyfile(frames_folder_output+"/n/filebp2.txt",frames_folder_output+"/filebp2.txt")
    shutil.copyfile(frames_folder_output+"/n/filebp3.txt",frames_folder_output+"/filebp3.txt")
    shutil.copyfile(frames_folder_output+"/n/filebp4.txt",frames_folder_output+"/filebp4.txt")
    shutil.copyfile(frames_folder_output+"/n/filebp5.txt",frames_folder_output+"/filebp5.txt")
    for count in range(startframe-1,-1,-1):
      #img_A=cv2.imread(frames_folder_input+"/frame%d.jpg" % count) #read new frame (A)
      #if(img_A is None): #just a test to when we are out of images (maybe we can switch to a counter)
      #  break

      print(count)
      #if you delete next 2 lines, it is the frame by frame method, otherwise recursive:
      if(count>0 and recursive_flag):
          
          image_semantic='{}/frame{}.png'.format(frames_folder_output,count+1)
          recursive_flag=False
      p1="/content/De/content/Deep-Image-Analogy-for-videos/demo"#"C:\\Users\\User\\Downloads\\Deep-Image-Analogy-master\\Deep-Image-Analogy-master\\Build\\x64\\Release\\deep_image_analogy.exe"
      p2="/content/Deep-Image-Analogy-for-videos/deep_image_analogy/models/"#"C:\\Users\\User\\Downloads\\Deep-Image-Analogy-master\\Deep-Image-Analogy-master\\windows\\deep_image_analogy\\models\\"
      p3='{}/frame{}.png'.format(output_frames_folder_path,count)
      p4=image_semantic
      p5=frames_folder_output#"C:\\Users\\User\\Downloads\\Deep-Image-Analogy-master\\Deep-Image-Analogy-master\\Build\\x64\\Release\\"
      p6='0'
      p7='1'
      p8='3'
      p9='0'
      p13='/content/Deep-Image-Analogy-for-videos/flows/opticalflow_{}'.format(count)#flowfile
      p15='0.5'#lambda
      if(count==0):
          p10='0'
          p11='0'
          p12='3'        
          p14='0'
      else:
          p10='1'
          p11='3'
          p12='3'
          p14='0'
      starttime=time.time()
      if(os.system(p1+" "+p2+" "+p3+" "+p4+" "+p5+" "+p6+" "+p7+" "+p8+" "+p9+" "+p10+" "+p11+" "+p12+" "+p13+" "+p14+" "+p15)):
          print("FAIL")
      print(time.time()-starttime)
      os.rename(frames_folder_output+"/resultAB.png",frames_folder_output+"/frame{}.png".format(count))
    #frames to video
    frames_folder_path=frames_folder_output#"C:\\Users\\User\\Downloads\\Deep-Image-Analogy-master\\Deep-Image-Analogy-master\\Build\\x64\\Release\\"

    print(fps)
    #fps=3 #Delete later

    temp_img=cv2.imread(frames_folder_output+"/frame0.png")#"C:\\Users\\User\\Downloads\\Deep-Image-Analogy-master\\Deep-Image-Analogy-master\\Build\\x64\\Release"+"/frame0.png")

    frame_width = temp_img.shape[1] #int(vidcap.get(3))
    frame_height = temp_img.shape[0] #int(vidcap.get(4))
    fps = fps
    fourcc = cv2.VideoWriter_fourcc(*'VP90')#cv2.VideoWriter_fourcc('H','2','6','4')
    out = cv2.VideoWriter(output_video_path+"eagle.mp4", fourcc, fps, (frame_width, frame_height), isColor=True)#"C:\\Users\\User\\Downloads\\Deep-Image-Analogy-master\\Deep-Image-Analogy-master\\Build\\x64\\Release\\eagle_regular.mp4", fourcc, fps, (frame_width, frame_height), isColor=True)
    count = 0
    while True:
      img=cv2.imread(frames_folder_output+"/frame{}.png".format(count))#"C:\\Users\\User\\Downloads\\Deep-Image-Analogy-master\\Deep-Image-Analogy-master\\Build\\x64\\Release"+"/frame{}.png".format(count))
      if(img is None):
        break
      out.write(img)
      print('write a new frame: ', success, count)
      count += 1
      '''if(count==10):
        break'''

    print('%d frames were written' % count)
    print(output_video_path)
    out.release()
    cv2.destroyAllWindows()

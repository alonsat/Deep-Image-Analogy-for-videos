import torch
import cv2
import numpy as np
import datetime as dt
import array
import os

def write_loc_tensor(filename, tens):
    with open(filename, 'wb') as f:
        arr = array.array('I')
        data_list = [(int(tens[x,y,1]) << 11) | (int(tens[x,y,0]) & 0x7FF) for x, y in np.ndindex(tens.shape[:2])]
        arr.fromlist(data_list)
        arr.tofile(f)


def warp_flow(img, flow):
    h, w = flow.shape[:2]
    flow = -flow
    flow[:,:,0] += np.arange(w)
    flow[:,:,1] += np.arange(h)[:,np.newaxis]
    res = cv2.remap(img, flow, None, cv2.INTER_LINEAR)
    return res

def write_tensor(filename, tens):
    with open(filename, 'wb') as f:
        arr = array.array('f')
        arr.fromlist(list(tens.numpy()))
        arr.tofile(f)

def read_tensor(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    arr = array.array('f')
    arr.frombytes(data)
    
    return torch.tensor(arr, dtype=torch.float)

if __name__ == '__main__':
  device='cuda'

  original_dia=0

  img_dim= (160,330)
  img_dim_inv= img_dim[1],img_dim[0]
  path, dirs, files = next(os.walk("/content/Deep-Image-Analogy-for-videos/frames_inp"))
  for frame_num in range(1,len(files)):
    img_A=cv2.resize(cv2.imread('/content/Deep-Image-Analogy-for-videos/frames_inp/frame%d.png'%(frame_num-1)),img_dim_inv,interpolation=cv2.INTER_CUBIC)
    img_BP=cv2.resize(cv2.imread('/content/Deep-Image-Analogy-for-videos/frames_inp/frame%d.png'%frame_num),img_dim_inv,interpolation=cv2.INTER_CUBIC )
  
    img_A_tensor = (torch.FloatTensor(img_A.transpose(2, 0, 1))/255).unsqueeze(0).to(device)
    img_BP_tensor = (torch.FloatTensor(img_BP.transpose(2, 0, 1))/255).unsqueeze(0).to(device)

    img_BP_gray=cv2.cvtColor(img_BP,cv2.COLOR_BGR2GRAY)
    img_A_gray=cv2.cvtColor(img_A,cv2.COLOR_BGR2GRAY)

    opticalflow=cv2.calcOpticalFlowFarneback(img_BP_gray,img_A_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0) #optical flow B to A

    i_range=torch.arange(0,opticalflow.shape[0])
    j_range=torch.arange(0,opticalflow.shape[1])
    i_ten, j_ten=torch.meshgrid(i_range,j_range)
    opticalflow_torch=torch.Tensor(opticalflow)
    opticalflow_torch[:,:,0]=torch.clamp(opticalflow_torch[:,:,0]+j_ten,0,opticalflow.shape[1]-1)
    opticalflow_torch[:,:,1]=torch.clamp(opticalflow_torch[:,:,1]+i_ten,0,opticalflow.shape[0]-1)
    opticalflow=opticalflow_torch.numpy()
  
    opticalflow=(opticalflow).astype(int)
    print(frame_num, opticalflow.shape)

    write_tensor('/content/Deep-Image-Analogy-for-videos/flows/opticalflow_%d'%frame_num,torch.tensor(opticalflow).view(-1))

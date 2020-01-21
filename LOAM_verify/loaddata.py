import h5py
import os
import numpy as np

## You can change the dataseve_path  ##
## Data link is: https://drive.google.com/open?id=1esEEPgc7vZ3nWBNOMjt7uqQWs3exs2_U

datasave_path="/mnt/VOL1/czheng/LiDAR/ours/"
f = h5py.File(os.path.join(datasave_path, "ply_data_all0.h5"), "r")
for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
    
## Input data is 4540*1000*6 ##
##  first entry is 4540 continuous frames, eg: i frame to 1+1 frame, sequence 0 have 4541 frames, thus here have 4540 continuous frames
## second entry is 1000, means for each continuous frames(i and i+1 frame), we find 1000 data matching pairs
## third entry is 6, x1,y1,z1,x2,y2,z2. x1,y1,z1 is the location of the matching point in i frame and x2,y2,z2 is the location of the matching point in i+1 frame
data = np.array(f['data'])

## Label is 4540*7 
## first entry is 4540 continuous frames, eg: i frame to 1+1 frame,
## second entry is 7, 1st to 4th is rotation with quaternion representation, 5th to 7th is translation
label = np.array(f['label'])

## ge_pose_12dim is 4540*12 ##
## first entry is 4540 continuous frames, eg: i frame to 1+1 frame,
## second entry is 12, as ground truth posed provided by Kitti, 9 for rotation and 3 for translation
ge_pose_12dim = np.array(f['ge_pose_12dim'])
f.close()


import h5py
import os
import numpy as np
from scipy.spatial.transform import Rotation as R

############### you can change the dataseve_path############
datasave_path="/mnt/VOL1/czheng/LiDAR/ours/"
f = h5py.File(os.path.join(datasave_path, "ply_data_all0.h5"), "r")
for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
##############  Input data is 4540*1000*6, #############################
#######  first entry is 4540 continuous frames, eg: i frame to 1+1 frame, sequence 0 have 4541 frames, thus here have 4540 continuous frames
####### second entry is 1000, means for each continuous frames(i and i+1 frame), we find 1000 data matching pairs
####### third entry is 6, x1,y1,z1,x2,y2,z2. x1,y1,z1 is the location of the matching point in i frame and x2,y2,z2 is the location of the matching point in i+1 frame
data = np.array(f['data'])

#############  Label is 4540*7 ##########################################
#######  first entry is 4540 continuous frames, eg: i frame to 1+1 frame,
#######  second entry is 7, 1st to 4th is rotation with quaternion representation, 5th to 7th is translation
label = np.array(f['label'])

############## ge_pose_12dim is 4540*12 ########################################
#######  first entry is 4540 continuous frames, eg: i frame to 1+1 frame,
#######  second entry is 12, as ground truth posed provided by Kitti, 9 for rotation and 3 for translation
gt_pose_12dim = np.array(f['gt_pose_12dim'])
f.close()

def RQTtopose(RQT):
    RQT[:, :3] = RQT[:, :3] / 10  # (normlize back 1,2,3th entry to fit others)
    rotation_q_all = RQT[:, :4]
    translation_all = RQT[:, 4:]
    rotation_all = np.zeros((rotation_q_all.shape[0], 9))
    for i in range(rotation_q_all.shape[0]):
        r = R.from_quat(rotation_q_all[i, :])
        rotation_all[i, :] = r.as_matrix().reshape(9)

    rota = np.array([0, 1, 2, 4, 5, 6, 8, 9, 10])
    trans = np.array([3, 7, 11])
    gt_pose = np.zeros((rotation_q_all.shape[0], 12))
    gt_pose[:, rota] = rotation_all
    gt_pose[:, trans] = translation_all

    return gt_pose


############ you can get the predicted label and pose here. 
##  https://drive.google.com/open?id=1XkzaMXs0X1WdFGuoalzhHFRlZRMkY3U-
datasave_path="/mnt/VOL1/czheng/LiDAR/ours/Pointnet_tf2/Quat"
f = h5py.File(os.path.join(datasave_path, "pred_label_filtered.h5"), "r")
pred_label = np.array(f['predict_label'])
pred_pose = f['predict_pose'] 
f.close()



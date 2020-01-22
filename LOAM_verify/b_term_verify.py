import numpy as np
import h5py
import os
from numpy.linalg import lstsq
from numpy.linalg import inv
from scipy.spatial.transform import Rotation as R
#%% prepare training and testing datasets
os.environ['CUDA_VISIBLE_DEVICES']='7'

n = 5   #### number of frames pair to verify

#################### data selected from testset############################

datasave_path="/mnt/VOL1/czheng/LiDAR/ours/Pointnet_tf2"
f = h5py.File(os.path.join(datasave_path, "ply_data_all0.h5"), "r")
pose_12dim = np.array(f['gt_pose_12dim'])
f.close()


def posetoRET(gt_pose):
    rota = np.array([0, 1, 2, 4, 5, 6, 8, 9, 10])
    trans = np.array([3, 7, 11])

    rotation_all = gt_pose[:, rota]
    translation_all = gt_pose[:, trans]

    rotation_q_all = np.zeros((rotation_all.shape[0],3))
    for i in range(rotation_all.shape[0]):
        rotation = rotation_all[i, :].reshape(3, 3)
        r = R.from_matrix(rotation)
        rotation_q_all[i, :] = r.as_euler('zyx')

    RET = np.hstack((rotation_q_all, translation_all))
    return RET

pose_euler = posetoRET(pose_12dim)

datasave_path="/mnt/VOL1/czheng/LiDAR/ours/Pointnet_tf2"
f = h5py.File(os.path.join(datasave_path, "pose_6_12dim.h5"), "w")
f['pose_12dim'] = pose_12dim
f['pose_euler'] = pose_euler
for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
f.close()



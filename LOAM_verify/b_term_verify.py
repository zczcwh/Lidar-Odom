import numpy as np
import h5py
import os
from numpy.linalg import lstsq
from numpy.linalg import inv
from scipy.spatial.transform import Rotation as R
#%% prepare training and testing datasets
os.environ['CUDA_VISIBLE_DEVICES']='7'

#################### data selected from testset############################

datasave_path="/mnt/VOL1/czheng/LiDAR/ours/Pointnet_tf2"
f = h5py.File(os.path.join(datasave_path, "ply_data_all0.h5"), "r")
pose_12dim = np.array(f['gt_pose_12dim'])
data = np.array(f['data'])
label = np.array(f['label'])
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

x_all = data
y_all = label

pose_ab = np.zeros((len(pose_12dim),4))
pose_ab[:,-1] = 1
pose = np.hstack((pose_12dim, pose_ab))
##############################################################

##### convert pose to 7dim representation
def posetoRQT(gt_pose):
    rota = np.array([0, 1, 2, 4, 5, 6, 8, 9, 10])
    trans = np.array([3, 7, 11])

    rotation_all = gt_pose[rota]
    translation_all = gt_pose[trans]

    rotation_q_all = np.zeros(4)
    rotation = rotation_all[:].reshape(3, 3)
    r = R.from_matrix(rotation)
    rotation_q_all[:] = r.as_quat()

    RQT = np.hstack((rotation_q_all, translation_all))
    RQT[:3] = RQT[:3] * 10  # (normlize 1,2,3th entry to fit others)
    return RQT


#### use odomtery to select feature
def findbias(x_test, pose):
    b = np.zeros((len(x_test),1000,4))
    for i in range(len(x_test)):
        #############data_previous: x,y,z in frame i
        data_previous = np.zeros((1000,4))
        data_previous[:,-1] = 1

        #############data_later: x,y,z in frame i+1
        data_later = np.zeros((1000,4))
        data_later[:,-1] = 1

        data_previous[:,:3] = x_test[i, :, :3]
        data_later[:,:3] = x_test[i, :, 3:]

        ### odom: ground truth pose value
        odom = pose[i,:].reshape(4,4)
        ### map point in frame i+1 to frame i with ground truth pose value
        predict_data_later = np.dot(odom, data_previous.T).T

        b[i,:,:] = (predict_data_later - data_later)
        # dist = (np.square(predict_data_previous - data_previous)).mean(axis=1)
    return b


b = findbias(x_all, pose)
mean_b = b.mean(axis=0)
max_b = b.max(axis=0)
min_b = b.min(axis=0)
std_b = b.std(axis=0)

pose_euler = posetoRET(pose_12dim)
mean_pose_euler = pose_euler.mean(axis=0)
max_pose_euler = pose_euler.max(axis=0)
min_pose_euler = pose_euler.min(axis=0)
std_pose_euler = pose_euler.std(axis=0)

# datasave_path="/mnt/VOL1/czheng/LiDAR/ours/Pointnet_tf2"
# f = h5py.File(os.path.join(datasave_path, "pose_6_12dim.h5"), "r+")
# f['pose_12dim'] = pose_12dim
# f['pose_euler'] = pose_euler
# for key in f.keys():
#     print(f[key].name)
#     print(f[key].shape)
# f.close()
trans = np.array([3, 7, 11])
error = (b.mean(axis=1)[:,:3] - pose_12dim[:, trans])

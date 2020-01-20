import numpy as np
import os
import h5py
from numpy.linalg import inv
from scipy.spatial.transform import Rotation as R

datasave_path="/mnt/VOL1/czheng/LiDAR/ours/Pointnet_tf2/Quat/odom_eval"
f = h5py.File(os.path.join(datasave_path, "pred_label.h5"), "r")
pred_label = np.array(f['predict_label'])
for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
f.close()

from scipy.spatial.transform import Rotation as R

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

p_frame0 = np.array([1.000000e+00,  9.043680e-12,  2.326809e-11,  5.551115e-17,
                     9.043683e-12,  1.000000e+00,  2.392370e-10,  3.330669e-16,
                     2.326810e-11,  2.392370e-10,  9.999999e-01, -4.440892e-16])

pred_pose = RQTtopose(pred_label)
#print(pred_pose.shape)
pred_pose = np.vstack([p_frame0, pred_pose])

def convertbackgt(gt_pose):
    ab = np.zeros((gt_pose.shape[0], 4))
    ab[:, -1] = 1
    gt_pose = np.hstack((gt_pose, ab))
    pose = np.zeros((gt_pose.shape[0], 16))
    pose[0, :] = gt_pose[0, :]
    for i in range(gt_pose.shape[0] - 1):
        pose1 = pose[i, :].reshape(4, 4)
        pose2_gt = gt_pose[i + 1, :].reshape(4, 4)
        pose[i + 1, :] = np.dot(pose1, inv(pose2_gt)).reshape(1, 16)
    poseall = pose[:, :12]
    return poseall
pred_poseall = convertbackgt(pred_pose)

np.savetxt('00_pred.txt', pred_poseall)

posepath = "/mnt/VOL1/czheng/LiDAR/dataset/poses/00.txt"
pose00 = np.loadtxt(posepath)
pose00 = pose00[:2401,:]
np.savetxt('00.txt', pose00)
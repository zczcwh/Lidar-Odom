
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 22:30:03 2019

@author: Zheng
"""

import numpy as np
import os
import h5py
from numpy.linalg import inv
from scipy.spatial.transform import Rotation as R


posepath = "/mnt/VOL1/czheng/LiDAR/dataset/poses/00.txt"
poseall = np.loadtxt(posepath)
# pose1 = poseall[1:len(bin_path),:]
def gtconvert(poseall):
    gt_pose = np.zeros((poseall.shape[0], 12))
    ab = np.zeros((1, 4))
    ab[:, -1] = 1

    gt_pose[0, :] = poseall[0, :]
    for i in range(poseall.shape[0] - 1):
        pose1_ab = np.vstack((poseall[i, :].reshape(3, 4), ab))
        pose2_ab = np.vstack((poseall[i + 1, :].reshape(3, 4), ab))
        gt_pose[i + 1, :] = np.dot(inv(pose2_ab), pose1_ab).reshape(1, 16)[:, :12]
    return gt_pose


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



def posetoRQT(gt_pose):
    rota = np.array([0, 1, 2, 4, 5, 6, 8, 9, 10])
    trans = np.array([3, 7, 11])

    rotation_all = gt_pose[:, rota]
    translation_all = gt_pose[:, trans]

    rotation_q_all = np.zeros((rotation_all.shape[0],4))
    for i in range(rotation_all.shape[0]):
        rotation = rotation_all[i, :].reshape(3, 3)
        r = R.from_matrix(rotation)
        rotation_q_all[i, :] = r.as_quat()

    RQT = np.hstack((rotation_q_all, translation_all))
    RQT[:, :3] = RQT[:, :3] * 10  # (normlize 1,2,3th entry to fit others)
    return RQT

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

gt_pose =  gtconvert(poseall)
RQT = posetoRQT(gt_pose)
gt_pose_RQT = RQT[1:, :]
################
# To do posetoRET and RETtopose
# verify
# Normlization
################

##############all data with increasing order###############
datasave_path="/mnt/VOL1/czheng/LiDAR/ours"
f = h5py.File(os.path.join(datasave_path, "ply_data_all0.h5"), "r+")
# del f['label_1to800']
del f['label_1to2400']
del f['label']
f['label_1to2400'] = gt_pose_RQT[:2400, :]
################# here choose first 801 frame############
f['label'] = gt_pose_RQT[:2400, :]
f['label_all'] = gt_pose_RQT

del f['data']
del f['data_all']
data_pair1 = np.array(f['data_1to800'])
data_pair2 = np.array(f['data_801to1200'])
data_pair3 = np.array(f['data_1201to2400'])

data_1to2400 = np.vstack((data_pair1, data_pair2, data_pair3))
f['data_1to2400'] = data_1to2400
f['data'] = data_1to2400

for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
f.close()



datasave_path="/mnt/VOL1/czheng/LiDAR/ours"
f = h5py.File(os.path.join(datasave_path, "ply_data_all0.h5"), "r+")
data_pair = np.array(f['data_1to2400'])
gt_pose = np.array(f['label_1to2400'])
# del f['data']
# del f['label']
# f['data'] = data_pair
# f['label'] = gt_pose
# for key in f.keys():
#     print(f[key].name)
#     print(f[key].shape)
f.close()

################ Train test split ########################
def shuffle_data(data, labels):
    idx = np.arange(labels.shape[0])
    np.random.shuffle(idx)
    return data[idx,:,:], labels[idx, ...], idx

data, labels, idx = shuffle_data(data_pair, gt_pose)
num = len(idx)
split = int(num*0.8)

data0 = data[:split,:,:]
label0 = labels[:split,:12]
idx0 = idx[:split]

data1 = data_pair[split:,:,:]
label1 = gt_pose[split:,:12]
idx1 = idx[split:]

f = h5py.File(os.path.join(datasave_path, "ply_data_train0.h5"), "r+")
del f['data']
del f['label']
del f['idx']
f['data'] = data0
f['label'] = label0
f['idx'] = idx0
for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
f.close()

f = h5py.File(os.path.join(datasave_path, "ply_data_test0.h5"), "r+")
del f['data']
del f['label']
del f['idx']
f['data'] = data1
f['label'] = label1
f['idx'] = idx1
for key in f.keys():
    print(f[key].name)
    print(f[key].shape)

f.close()

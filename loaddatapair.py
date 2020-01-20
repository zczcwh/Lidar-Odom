
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 22:30:03 2019

@author: Zheng
"""

import numpy as np
import find_matchpair as fmp
import os
import h5py
from numpy.linalg import inv
from scipy.spatial.transform import Rotation as R

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "5,6,7"
######## Load Lidar data######################################
def load_pc_from_bin(bin_path):
    obj = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 4)
    return obj

path = "/mnt/VOL1/czheng/LiDAR/dataset/sequences/00/velodyne"
files = os.listdir(path)
files.sort(key=lambda x: int(x[:-4]))
s = []

for file in files:
    s.append(os.path.splitext(file)[0])

# ss = np.asarray(s)
# j = np.zeros((len(files)))

bin_path = []
for i in range(len(files)):
    bin_path.append(os.path.join(path, "{}.bin").format(s[i]))

###############################################################
############################Load calib data####################
calib_path = "/mnt/VOL1/czheng/LiDAR/dataset/sequences/00/calib.txt"

def read_calib_file(filepath):
    """Read in a calibration file and parse into a dictionary."""
    calib_data = {}

    with open(filepath, 'r') as f:
        for line in f.readlines():
            key, value = line.split(':', 1)
            # The only non-float values in these files are dates, which
            # we don't care about anyway
            try:
                calib_data[key] = np.array([float(x) for x in value.split()])
            except ValueError:
                pass

    return calib_data

calib_data = read_calib_file(calib_path)

Tr = np.zeros((4, 4))
Tr[:3, :] = calib_data['Tr'].reshape((3, 4))
Tr[3, 3] = 1

data_pair = []
#pose1 = []
#### choosing 1000 pair of each image matching
#for i in range(len(files)-1):
for i in range(1200, 2400):
    velo1 = load_pc_from_bin(bin_path[i])
    velo2 = load_pc_from_bin(bin_path[i+1])
    cxyz1,cxyz2 = fmp.get_matchpair(velo1, velo2, rescale_factor=1)

    cxyz1 =  np.dot(cxyz1, Tr.T)
    cxyz2 =  np.dot(cxyz2, Tr.T)

    cxyz12 = np.hstack((cxyz1[:,:3],cxyz2[:,:3]))
    cxyz_pair = np.zeros((1000,6))
    if len(cxyz1)>1000:
        cxyz_pair = cxyz12[:1000,:]
    else:
        cxyz_pair[:len(cxyz1),:]=cxyz12

#    f['/frame'+str(i)+'and'+str(i+1)] = cxyz_pair  # or f.create_group('grp1')
    data_pair.append(cxyz_pair)
    print(i)

# Input data pair normalization (all divide 100)
# data_pair =data_pair / 100

##############all data with increasing order###############
datasave_path="/mnt/VOL1/czheng/LiDAR/ours"
f = h5py.File(os.path.join(datasave_path, "ply_data_all0.h5"), "r+")
f['data_1201to2400'] = data_pair
################# here choose first 801 frame############

for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
f.close()
################################################################
# Load pose data################################################
# posepath = "/mnt/VOL1/czheng/LiDAR/dataset/poses/00.txt"
# poseall = np.loadtxt(posepath)
# # pose1 = poseall[1:len(bin_path),:]
# def gtconvert(poseall):
#     gt_pose = np.zeros((poseall.shape[0], 12))
#     ab = np.zeros((1, 4))
#     ab[:, -1] = 1
#
#     gt_pose[0, :] = poseall[0, :]
#     for i in range(poseall.shape[0] - 1):
#         pose1_ab = np.vstack((poseall[i, :].reshape(3, 4), ab))
#         pose2_ab = np.vstack((poseall[i + 1, :].reshape(3, 4), ab))
#         gt_pose[i + 1, :] = np.dot(inv(pose2_ab), pose1_ab).reshape(1, 16)[:, :12]
#     return gt_pose
#
#
# def convertbackgt(gt_pose):
#     ab = np.zeros((gt_pose.shape[0], 4))
#     ab[:, -1] = 1
#     gt_pose = np.hstack((gt_pose, ab))
#     pose = np.zeros((gt_pose.shape[0], 16))
#     pose[0, :] = gt_pose[0, :]
#     for i in range(gt_pose.shape[0] - 1):
#         pose1 = pose[i, :].reshape(4, 4)
#         pose2_gt = gt_pose[i + 1, :].reshape(4, 4)
#         pose[i + 1, :] = np.dot(pose1, inv(pose2_gt)).reshape(1, 16)
#     poseall = pose[:, :12]
#     return poseall
#
#
# poseall_gt = gtconvert(poseall)
#
#
# # poseall1 = convertbackgt(gt_pose)
#
# def posetoRQT(poseall):
#     ab = np.zeros((len(poseall), 4))
#     ab[:, -1] = 1
#     pose_ab = np.hstack((poseall, ab))
#     ##### get the ground truth pose(i th frame to i frame)######
#     gt_pose = np.zeros((len(pose_ab), 16))
#     gt_pose[0, :] = pose_ab[0, :]
#     for i in range(len(poseall) - 1):
#         a = pose_ab[i + 1, :].reshape(4, 4)
#         b = pose_ab[i, :].reshape(4, 4)
#         x = np.dot(a, inv(b)).reshape(16, )
#         gt_pose[i + 1, :] = x
#
#     rota = np.array([0, 1, 2, 4, 5, 6, 8, 9, 10])
#     trans = np.array([3, 7, 11])
#
#     rotation_all = gt_pose[:, rota]
#     translation_all = gt_pose[:, trans]
#
#     rotation_q_all = np.zeros((rotation_all.shape[0],4))
#     for i in range(rotation_all.shape[0]):
#         rotation = rotation_all[i, :].reshape(3, 3)
#         r = R.from_matrix(rotation)
#         rotation_q_all[i, :] = r.as_quat()
#
#     RQT = np.hstack((rotation_q_all, translation_all))
#     RQT[:, :3] = RQT[:, :3] * 100  # (normlize 1,2,3th entry to fit others)
#     return RQT
#
# def RQTtopose(RQT):
#     RQT[:, :3] = RQT[:, :3] / 100  # (normlize back 1,2,3th entry to fit others)
#     rotation_q_all = RQT[:, :4]
#     translation_all = RQT[:, 4:]
#     rotation_all = np.zeros((rotation_q_all.shape[0], 9))
#     for i in range(rotation_q_all.shape[0]):
#         r = R.from_quat(rotation_q_all[i, :])
#         rotation_all[i, :] = r.as_matrix().reshape(9)
#
#     rota = np.array([0, 1, 2, 4, 5, 6, 8, 9, 10])
#     trans = np.array([3, 7, 11])
#     gt_pose = np.zeros((rotation_q_all.shape[0], 16))
#     gt_pose[:,-1] = 1
#     gt_pose[:, rota] = rotation_all
#     gt_pose[:, trans] = translation_all
#     pose_ab = np.zeros((rotation_q_all.shape[0], 16))
#     pose_ab[0, :] = gt_pose[0, :]
#     for i in range(len(gt_pose) - 1):
#         x = gt_pose[i + 1, :].reshape(4, 4)
#         b = pose_ab[i, :].reshape(4, 4)
#         a = np.dot(x, b).reshape(16, )
#         pose_ab[i + 1, :] = a
#     poseall = pose_ab[:, :12]
#
#     return poseall
#
# def posetoRET(poseall):
#     poseall[:, :3] = poseall[:, :3]
#     ab = np.zeros((len(poseall), 4))
#     ab[:, -1] = 1
#     pose_ab = np.hstack((poseall, ab))
#     ##### get the ground truth pose(i th frame to i frame)######
#     gt_pose = np.zeros((len(pose_ab), 16))
#     gt_pose[0, :] = pose_ab[0, :]
#     for i in range(len(poseall) - 1):
#         a = pose_ab[i + 1, :].reshape(4, 4)
#         b = pose_ab[i, :].reshape(4, 4)
#         x = np.dot(a, inv(b)).reshape(16, )
#         gt_pose[i + 1, :] = x
#
#     rota = np.array([0, 1, 2, 4, 5, 6, 8, 9, 10])
#     trans = np.array([3, 7, 11])
#
#     rotation_all = gt_pose[:, rota]
#     translation_all = gt_pose[:, trans]
#
#     rotation_e_all = np.zeros((rotation_all.shape[0], 3))
#     for i in range(rotation_all.shape[0]):
#         rotation = rotation_all[i, :].reshape(3, 3)
#         r = R.from_matrix(rotation)
#         rotation_e_all[i, :] = r.as_euler('zyx', degrees=True)
#
#     RET = np.hstack((rotation_e_all, translation_all))
#
#     return RET
#
# def RETtopose(RET):
#     rotation_q_all = RET[:, :3]
#     translation_all = RET[:, 3:]
#     rotation_all = np.zeros((rotation_q_all.shape[0], 9))
#     for i in range(rotation_q_all.shape[0]):
#         r = R.from_euler('zyx', rotation_q_all[i, :], degrees=True)
#         rotation_all[i, :] = r.as_matrix().reshape(9)
#
#     rota = np.array([0, 1, 2, 4, 5, 6, 8, 9, 10])
#     trans = np.array([3, 7, 11])
#     gt_pose = np.zeros((rotation_q_all.shape[0], 16))
#     gt_pose[:,-1] = 1
#     gt_pose[:, rota] = rotation_all
#     gt_pose[:, trans] = translation_all
#     pose_ab = np.zeros((rotation_q_all.shape[0], 16))
#     pose_ab[0, :] = gt_pose[0, :]
#     for i in range(len(gt_pose) - 1):
#         x = gt_pose[i + 1, :].reshape(4, 4)
#         b = pose_ab[i, :].reshape(4, 4)
#         a = np.dot(x, b).reshape(16, )
#         pose_ab[i + 1, :] = a
#     poseall = pose_ab[:, :12]
#     return poseall
#
# RQT = posetoRQT(poseall_gt)
# gt_pose_RQT = RQT[1:, :]
################
# To do posetoRET and RETtopose
# verify
# Normlization
################


# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:56:41 2019

@author: Zheng
"""
import numpy as np
#import matplotlib.pyplot as plt
import cv2
##""" load LiDAR points """
#    velo = np.fromfile(LiDAR_dir+file_name+'.bin', dtype=np.float32)
#    velo = velo.reshape((-1, 4))
#   
##    """ build correspondences between LiDAR and camera coordinate """
#    x=velo[:,0]
#    y=velo[:,1]
#    z=velo[:,2]
#    intensity = velo[:,3]

##""" load LiDAR points """
#velo1 = np.fromfile('000000.bin', dtype=np.float32)
#velo1 = velo1.reshape((-1, 4))
#
#velo2 = np.fromfile('000050.bin', dtype=np.float32)
#velo2 = velo2.reshape((-1, 4))
 
##    """ build correspondences between LiDAR and camera coordinate """
#x=velo[:,0]
#y=velo[:,1]
#z=velo[:,2]
#intensity = velo[:,3]

def do_range_projection(points):

    proj_H=64
    proj_W=1024
    proj_fov_up=3.0  
    proj_fov_down=-25.0

    # laser parameters
    fov_up = proj_fov_up / 180.0 * np.pi      # field of view up in rad
    fov_down = proj_fov_down / 180.0 * np.pi  # field of view down in rad
    fov = abs(fov_down) + abs(fov_up)  # get field of view total in rad

    xyz = points[:,0:3]

    # get depth of all points
    data = np.linalg.norm(xyz, 2, axis=1)

    # get scan components
    scan_x = points[:, 0]
    scan_y = points[:, 1]
    scan_z = points[:, 2]

    # get angles of all points
    yaw = -np.arctan2(scan_y, scan_x)
    #pitch = np.arcsin(scan_z / depth)         #norm x,y
    pitch = np.arcsin(scan_z /  data)     #####madi said depth is same as data

    # get projections in image coords
    proj_x = 0.5 * (yaw / np.pi + 1.0)          # in [0.0, 1.0]
    proj_y = 1.0 - (pitch + abs(fov_down)) / fov        # in [0.0, 1.0]

    # scale to image size using angular resolution
    proj_x *= proj_W                              # in [0.0, W]
    proj_y *= proj_H                              # in [0.0, H]

    # round and clamp for use as index
    proj_x = np.floor(proj_x)
    proj_x = np.minimum(proj_W - 1, proj_x)
    proj_x = np.maximum(0, proj_x).astype(np.int32)   # in [0,W-1]

    proj_y = np.floor(proj_y)
    proj_y = np.minimum(proj_H - 1, proj_y)
    proj_y = np.maximum(0, proj_y).astype(np.int32)   # in [0,H-1]

    # order in decreasing data
    indices = np.arange(data.shape[0])
    order = np.argsort(data)[::-1]
    data = data[order]
    indices = indices[order]
    points = points[order]
    proj_y = proj_y[order]
    proj_x = proj_x[order]

    #proj_range = np.full((proj_H, proj_W), -1, dtype=np.float32)
    proj_range_all = np.full((proj_H, proj_W, 4), 0, dtype=np.float32)

    # assing to images
    proj_range_all[proj_y, proj_x, 0] = data
    proj_range_all[proj_y, proj_x, 1:4] = points[:,0:3]
    #######  I divide 100 here. ###########
    #proj_range = proj_range/100.0

    return proj_range_all


def nearest_point(refined_lidar):  
    value_mask=np.asarray(1.0-np.squeeze(refined_lidar)>0.1).astype(np.uint8)
    dt,lbl = cv2.distanceTransformWithLabels(value_mask, cv2.DIST_L1, 5, labelType=cv2.DIST_LABEL_PIXEL)
    return dt,lbl



def DT_complete_batch(lidar_batch):
    h = np.shape(lidar_batch)[0]
    w = np.shape(lidar_batch)[1]
    lidar_batch = np.expand_dims(lidar_batch,axis=-1)
    lidar_batch = np.expand_dims(lidar_batch,axis=0)
    
    batch_size=np.shape(lidar_batch)[0]
    new_batch=[]
   
    for i in range(batch_size):

        lidar_single=lidar_batch[i,:,:,0]
        
        dt,lbl=nearest_point(lidar_single)
        with_value=np.squeeze(lidar_single)>0.1

        depth_list=np.squeeze(lidar_single)[with_value]
        label_list=np.reshape(lbl,[1,w*h])
        depth_list_all=depth_list[label_list-1]      
        depth_map=np.reshape(depth_list_all,(h,w))
        new_batch.append(depth_map)  

    new_batch=np.asarray(new_batch)
    new_batch=np.expand_dims(new_batch,axis=-1)

    refined_lidar=new_batch.astype(np.float32)
    refined_lidar = np.squeeze(refined_lidar)/100

    return refined_lidar


#def DT_complete_batch(lidar_batch):
#    batch_size=np.shape(lidar_batch)[0]
#    new_batch=[]
#   
#    for i in range(batch_size):
#
#        lidar_single=lidar_batch[i,:,:,0]
#               
#        dt,lbl=nearest_point(lidar_single)
#        with_value=np.squeeze(lidar_single)>0.1
#
#        depth_list=np.squeeze(lidar_single)[with_value]
#        label_list=np.reshape(lbl,[1,1216*352])
#        depth_list_all=depth_list[label_list-1]      
#        depth_map=np.reshape(depth_list_all,(352,1216))
#        new_batch.append(depth_map)  
#
#    new_batch=np.asarray(new_batch)
#    new_batch=np.expand_dims(new_batch,axis=-1)
#
#    refined_lidar=new_batch.astype(np.float32)
#
#    return refined_lidar
    

def sphericaltocaetesian(proj_range_all1, x1_mhis, y1_mhis):
    cxyz = proj_range_all1[y1_mhis,x1_mhis,1:4]
    #cxyz = cxyz[~(cxyz==0).all(axis=1), :]
    
    return cxyz


def caetesiantospherical(points):
    proj_H=64
    proj_W=1024
    proj_fov_up=3.0  
    proj_fov_down=-25.0

    # laser parameters
    fov_up = proj_fov_up / 180.0 * np.pi      # field of view up in rad
    fov_down = proj_fov_down / 180.0 * np.pi  # field of view down in rad
    fov = abs(fov_down) + abs(fov_up)  # get field of view total in rad

    xyz = points[:,0:3]

    # get depth of all points
    data = np.linalg.norm(xyz, 2, axis=1)

    # get scan components
    scan_x = points[:, 0]
    scan_y = points[:, 1]
    scan_z = points[:, 2]

    # get angles of all points
    theta = -np.arctan2(scan_y, scan_x)
    #pitch = np.arcsin(scan_z / depth)         #norm x,y
    phi = np.arcsin(scan_z /  data)     #####madi said depth is same as data
    
    #proj_y = (phi + 25) * 64
    
    
    # get projections in image coords
    proj_x = 0.5 * (theta / np.pi + 1.0)          # in [0.0, 1.0]
    proj_y = 1.0 - (phi + abs(fov_down)) / fov        # in [0.0, 1.0]

    # scale to image size using angular resolution
    proj_x *= proj_W                              # in [0.0, W]
    proj_y *= proj_H                              # in [0.0, H]

    # round and clamp for use as index
    proj_x = np.floor(proj_x)
    proj_x = np.minimum(proj_W - 1, proj_x)
    proj_x = np.maximum(0, proj_x).astype(np.int32)   # in [0,W-1]

    proj_y = np.floor(proj_y)
    proj_y = np.minimum(proj_H - 1, proj_y)
    proj_y = np.maximum(0, proj_y).astype(np.int32)   # in [0,H-1]
    
    
    return proj_y, proj_x
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:13:24 2019

@author: Zheng
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:42:40 2019

@author: Zheng
"""

import numpy as np
import range_projection as rp
import match_functions as mf
import utils as utl
import cv2
from numpy.linalg import inv

#""" load LiDAR points """
#velo1 = np.fromfile('000001.bin', dtype=np.float32)
#velo1 = velo1.reshape((-1, 4))

#velo2 = np.fromfile('000002.bin', dtype=np.float32)
#velo2 = velo2.reshape((-1, 4))

#velo3 = np.fromfile('000002.bin', dtype=np.float32)
#velo3 = velo3.reshape((-1, 4))

def get_matchpair(velo1, velo2, rescale_factor=1):
    proj_range_all1 =  rp.do_range_projection(velo1)
    proj_range_all2 =  rp.do_range_projection(velo2)
    #proj_range_all3 =  rp.do_range_projection(velo3)

    proj_range1 = proj_range_all1[:,:,0]
    proj_range2 = proj_range_all2[:,:,0]
    #proj_range3 = proj_range_all3[:,:,0]

    proj_range1_dc =  rp.DT_complete_batch(proj_range1)
    proj_range2_dc =  rp.DT_complete_batch(proj_range2)
    #############histogram normalization

    ###################################proj_range1_dc
    proj_range1his = cv2.equalizeHist((proj_range1_dc*255).astype(np.uint8)) 
    proj_range2his = cv2.equalizeHist((proj_range2_dc*255).astype(np.uint8)) 
    proj_range1his = (proj_range1his/255).astype(np.float32)
    proj_range2his = (proj_range2his/255).astype(np.float32) 
    #
    #####image rescale with Nearest-neighbor, only rescale columns 
    proj_range1his_re = mf.imagerescale(proj_range1his, rescale_factor)
    proj_range2his_re = mf.imagerescale(proj_range2his, rescale_factor)
    #

    # width and height of each local feature, in pixels. 
    feature_width = 16
    x1_mhis, y1_mhis, x2_mhis, y2_mhis = mf.image_match(proj_range1, proj_range2, feature_width)
    #####add rescale factor##########
    cxyz1 = rp.sphericaltocaetesian(proj_range_all1, x1_mhis, y1_mhis)
    cxyz2 = rp.sphericaltocaetesian(proj_range_all2, x2_mhis, y2_mhis)
    
    ####################################### remove rows with all 0
    cxyz2 = cxyz2[~(cxyz1==0).all(axis=1), :]
    cxyz1 = cxyz1[~(cxyz1==0).all(axis=1), :]

    cxyz1 = cxyz1[~(cxyz2==0).all(axis=1), :]
    cxyz2 = cxyz2[~(cxyz2==0).all(axis=1), :]

    bias = np.ones((cxyz2.shape[0],1)).astype(float)
    cxyz1 = np.hstack((cxyz1,bias))
    cxyz2 = np.hstack((cxyz2,bias))
    
    return cxyz1,cxyz2
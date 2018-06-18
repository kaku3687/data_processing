# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 08:57:34 2018

@author: trandhawa
"""

import os
import numpy as np

model_ = np.asarray([])
sn_ = np.asarray([])

#model_ = ['16356']
#sn_ = ['0002','0004','0005','0006']
#test_ = ['peak','preload']
#speed_ = ['60','100','150']

dir_ = 'C:/Users/trandhawa/My SecuriSync/MastCAM/REVB_Testing/Data/'

motor_dirs_ = os.listdir(dir_)

for i in range(len(motor_dirs_)):
    split_ = motor_dirs_[i].split('-')
    
    if np.any(model_ == split_[0]):
        pass
    else:
        model_ = np.append(model_, split_[0])
    
    if np.any(sn_ == split_[1]):
        pass
    else:
        sn_ = np.append(sn_, split_[1])

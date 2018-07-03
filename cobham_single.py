#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import re

def convert_np(pd_):
	pd_c = pd_.astype(float)
	pd_c = pd_c.as_matrix()

	return pd_c

#directories

#dir_ = 'C:/Users/Owner/My SecuriSync/MastCAM/REVB_Testing/Data/16356-0006/'
#dir_ = 'C:/Users/trandhawa/My SecuriSync/MastCAM/REVB_Testing/Data/'
dir_ =  'P:/MSSS/1041_Mastcam-Z_Flight_Development/04_Test/Cobham_Motor_Checkout/REVB_Testing/Data/'
#dir_ = 'C:/Users/trandhawa/My SecuriSync/MastCAM/REVB_Testing/Data/16358-0009/test/'


#filenames
os.chdir(dir_)

#tests/parameters
test_type_ = ['peak, preload']
speed_ = ['100, 60, 150']
cw_ = ['cw','ccw']

#sn listing
#sn_ = ['0005', '0006', '0009', '0010', '0011', '0012', '0013', '0014', '0015', '0016', '0017', '0018', '0019', '0020', '0021']
#sn_ = sys.argv[1]
#if(len(sn_) == 1):
#    sn_ = ['000' + str(sn_)]
#elif(len(sn_) == 2):
#    sn_ = ['00' + str(sn_)]
#else:
#    print ('Invalid SN entered')

sn_ = ['0006']

#model listing
model_ = ['16358']

file_sort = []

k = 0
p = 0
idx_ = 0

def sort_stuff(array_, start_, stop_, index_):
    k = start_
    idx_ = index_
    for k in range(start_,stop_):
        check_ = array_[k]
        p = k - 1
        
        while (p>(start_-1)) & (array_[p][index_] > check_[index_]):
            array_[p+1] = array_[p]
            p = p-1
        array_[p+1] = check_
        
    return array_

for motor_ in sn_:

    #import excel as panda object
    test_files_ = os.listdir(dir_ + model_[0] + '-' + motor_ + '/')
    os.chdir(dir_ + model_[0] + '-' + motor_ + '/')
    files_ =  []
    not_files = []
    
    for file in test_files_:
        if (model_[0] in file) and ('mdf' in file) and not ('xlsx' in file) and not ('png' in file):
    
            filename_ = file
            files_.append(file)
            
            
for file in files_:
    
    split_ = file.split('_')
    rm_ext = split_[len(split_) - 1].split('.')
    split_[len(split_) - 1] = rm_ext[0]
    
    file_sort.append(split_)
    
j = 1
for j in range(len(file_sort)):
    check_ = file_sort[j]
    i = j - 1
    
    while (i>0) & (file_sort[i][1] > check_[1]):
        file_sort[i+1] = file_sort[i]
        i = i-1
    file_sort[i+1] = check_


for file_ in file_sort:
    if 'preload' in file_[1]:
        duty_ = file_[3].replace('-', '.')
        file_[3] = duty_

i_60cw = []
i_60ccw = []
i_100cw = []
i_100ccw = []
i_150cw = []
i_150ccw = []

for file_ in file_sort:
    if 'preload60cw' in file_:
        i_60cw.append(file_sort.index(file_))
    if 'preload60ccw' in file_:

file_sort = sort_stuff(file_sort, 31, 35, 3)
    
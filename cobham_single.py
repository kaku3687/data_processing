#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import re

def plt_fig(title_, x_arr, y_arr, fig_, file_, axis_ = 0, txt_ = 0, loc_ = 0, save_ = False, grid_ = False, minor_ = False, _dpi_ = 600):
	plt.figure(fig_)
	plt.title(title_)
	plt.ylabel(y_arr[0])
	plt.xlabel(x_arr[0])
	plt.grid(grid_, which='major')
	if minor_ == True:
		plt.grid(minor_, which='minor', color='r', linestyle='--')
		plt.minorticks_on()
	else:
		pass
	if txt_ == 0:
		pass
	else:
		plt.text(loc_[0], loc_[1], txt_)
	if axis_ == 0:
		pass
	else:
		plt.axis(axis_)

	plt.plot(x_arr[1:len(y_arr)], y_arr[1:])

	if save_ == True:
		plt.savefig(title_ + '_' + file_ + '.png', dpi = _dpi_)
	else:
#   pass
		plt.show()

def convert_np(pd_):
	pd_c = pd_.astype(float)
	pd_c = pd_c.as_matrix()

	return pd_c

#directories

dir_ = 'C:/Users/Owner/My SecuriSync/MastCAM/REVB_Testing/Data/'
#dir_ = 'C:/Users/trandhawa/My SecuriSync/MastCAM/REVB_Testing/Data/'
#dir_ =  'P:/MSSS/1041_Mastcam-Z_Flight_Development/04_Test/Cobham_Motor_Checkout/REVB_Testing/Data/'
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

def convert_np(pd_):
    pd_c = pd_.astype(float)
    pd_c = pd_c.as_matrix()

    return pd_c


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


def skip_torque(dir_, motor_, filename_):
    dyno_data = pd.read_csv(dir_ + model_[0] + '-' + motor_ + '/' + filename_, sep='\t')
    #extract torque, angle2 and time arrays
    fields = ['Torque 1 (oz.in)', 'Angle 1', 'Angle 2', 'Time']
       
    u_torq_ = dyno_data.loc[1:, fields[0]]
    u_ang2_ = dyno_data.loc[1:, fields[2]]
    u_time_ = dyno_data.loc[1:, fields[3]]

       
    #Single plot for both Torque and Position
            
    torq_ = convert_np(u_torq_)
    ang2_ = convert_np(u_ang2_)
    time_ = convert_np(u_time_)

    return torq_, ang2_, time_


def velocity(time_, pos_, delta_ = 200):
    slope_ = []
    peak_t_ = []
    stall_i = []
    avg_pt = 0  

    for i in range(len(time_) - delta_):
        slope_.append((pos_[i] - pos_[i+delta_])/(time_[i] - time_[i+delta_]))
               
    velocity_ = np.asarray(slope_)

    return velocity_


def dt_torque(time_, torque_, delta_ = 200):
    slope_ = []
    peak_t_ = []
    stall_i = []
    avg_pt = 0  

    for i in range(len(time_) - delta_):
        slope_.append((torque_[i] - torque_[i+delta_])/(time_[i] - time_[i+delta_]))
               
    dt_torque_ = np.asarray(slope_)

    return dt_torque_




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
        i_60ccw.append(file_sort.index(file_))
    if 'preload100cw' in file_:
        i_100cw.append(file_sort.index(file_))
    if 'preload100ccw' in file_:
        i_100ccw.append(file_sort.index(file_))
    if 'preload150cw' in file_:
        i_150cw.append(file_sort.index(file_))
    if 'preload150ccw' in file_:
        i_150ccw.append(file_sort.index(file_))
    
#idx_rate = [i_60cw, i_60ccw, i_100cw, i_100ccw, i_150cw, i_150ccw]
idx_rate = [i_60cw]


for rate_ in idx_rate:
    file_sort = sort_stuff(file_sort, min(rate_), max(rate_), 3)
    
pk_60 = []
pk_100 = []
pk_150 = []
pr_60 = []
pr_100 = []
pr_150 = []

for test_f in file_sort:
    
    print (test_f)
    f_idx = [n for n, s in enumerate(files_) if test_f[1] and test_f[2] in s]
    for run_ in f_idx:
        f_torq, f_pos, f_time = skip_torque(dir_, sn_[0], files_[run_])
        
        f_vel = velocity(f_time, f_pos)
        f_dt_torq = dt_torque(f_time, f_torq, 500)
        v_avg = []
        
        for i in range(len(f_vel) - 100):
            v_avg.append(np.average(f_vel[i:i+100]))
        
                   
        v_i = 1
        while np.abs(np.abs(f_vel[v_i]) - np.abs(f_vel[v_i + 50])) <= 2 and np.abs(f_vel[v_i]) > 3:
            v_i = v_i + 1
            
        sk_t = f_torq[v_i]       
        sk_t_ = 'Skipping Torque: ' + str(sk_t) + ' For: ' + str(test_f)
        
        print (sk_t_)
        
#        plt_fig('Velocity', f_time, f_vel, 1, test_f)
#        plt_fig('Torque', f_time, f_dt_torq, 2, test_f)
#        plt_fig('V Average', f_time - 100, v_avg, 3, test_f)
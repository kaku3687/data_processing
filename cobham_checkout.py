#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def convert_np(pd_):
	pd_c = pd_.astype(float)
	pd_c = pd_c.as_matrix()

	return pd_c

#directories
dir_ = 'C:/Users/Owner/My SecuriSync/MastCAM/REVB_Testing/Data/16356-0006/'

#filenames
os.chdir(dir_)

#tests/parameters
test_type_ = ['peak, preload']
speed_ = ['100, 60, 150']
cw_ = ['cw','ccw']

#sn listing
sn_ = ['0002, 0004, 0005, 0006']

#model listing
model_ = ['16356']

#import excel as panda object
test_files_ = os.listdir(dir_)
files_ =  []
not_files = []

for file in test_files_:
    if (model_[0] in file) and ('mdf' in file) and not ('xlsx' in file):

        filename_ = file
        files_.append(file)
        
        dyno_data = pd.read_csv(dir_ + '/' + filename_, sep='\t')
        
        #extract torque, angle2 and time arrays
        fields = ['Torque 1 (oz.in)', 'Angle 1', 'Angle 2', 'Time']
           
        u_torq_ = dyno_data.loc[1:, fields[0]]
        u_ang2_ = dyno_data.loc[1:, fields[2]]
        u_time_ = dyno_data.loc[1:, fields[3]]
           
        #generate torque vs time
#        plt.figure()
#        plt.title('Torque' + ' ' + filename_)
#        plt.ylabel('torque (in-oz)')
#        plt.xlabel('time (sec)')
#        plt.scatter(u_time_, u_torq_)
#        plt.grid(True, which='major')
#        plt.savefig('Torque' + '_' + filename_ + '.png', dpi = 600)
#        plt.show()
#        
#        #generate position vs time
#        plt.figure()
#        plt.title('Position' + ' ' + filename_)
#        plt.ylabel('position (deg)')
#        plt.xlabel('time (sec)')
#        plt.scatter(u_time_, u_ang2_)
#        plt.grid(True, which='major')
#        plt.savefig('Position' + '_' + filename_ + '.png', dpi = 600)
#        plt.show()
           
        #Single plot for both Torque and Position
        fig, ax1 = plt.subplots()
                
        ax1.set_xlabel('time (sec)')
        ax1.set_ylabel('position (deg)', color = 'tab:blue')
        ax1.plot(u_time_, u_ang2_, color = 'tab:blue')
        ax1.tick_params(axis='y', labelcolor='tab:blue')
        
        ax2 = ax1.twinx()
        
        ax2.set_ylabel('torque (in-oz)', color='tab:red')
        ax2.plot(u_time_, u_torq_, color='tab:red')
        ax2.tick_params(axis='y', labelcolor='tab:red')
        
        fig.tight_layout()
        plt.savefig(filename_ + '.png', dpi=600)
        plt.show()
        
#        torq_ = convert_np(u_torq_)
#        time_ = convert_np(u_time_)
#           
#        delta_ = 50
#        slope_ = []
#           
#        for i in range(len(time_) - delta_):
#            slope_.append((torq_[i] - torq_[i+delta_])/(time_[i] - time_[i+delta_]))
           
        #generate slopes of angle2 (i.e. speed)
#        plt.figure()
#        plt.title('Velocity' + ' ' + filename_)
#        plt.ylabel('velocity (deg/s)')
#        plt.xlabel('time (sec)')
#        plt.scatter(time_[:(len(time_) - delta_)], slope_)
#        plt.grid(True, which='major')
#        plt.show()
    
    else:
        not_files.append(file)
#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys


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
sn_ = sys.argv[1]
if(len(sn_) == 1):
    sn_ = ['000' + str(sn_)]
elif(len(sn_) == 2):
    sn_ = ['00' + str(sn_)]
else:
    print ('Invalid SN entered')

#model listing
model_ = ['16358']

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
                  
            print (filename_)
            
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
               
            delta_ = 200
            slope_ = []
            peak_t_ = []
            stall_i = []
            avg_pt = 0  
            
            for i in range(len(time_) - delta_):
                slope_.append((ang2_[i] - ang2_[i+delta_])/(time_[i] - time_[i+delta_]))
               
            velocity_ = np.asarray(slope_)
            
            stall_i = np.asarray(np.where((velocity_ < 0.4) & (velocity_ > 0.05) & (torq_[:len(velocity_)] > 0.5)))
            stall_i = stall_i[0,:]
            
            if len(stall_i) > 1:
                peak_t_ = torq_[stall_i]
                avg_pt = np.max(peak_t_)
                pt_txt = 'Peak Torque: ' + str(avg_pt)
            else:
                pt_txt = 'Did not test to stall'
                
            fig, ax1 = plt.subplots()
            plt.title('Torque and Position')        
            ax1.set_xlabel('time (sec)')
            ax1.set_ylabel('position (deg)', color = 'tab:blue')
            ax1.scatter(u_time_, u_ang2_, color = 'tab:blue')
            ax1.tick_params(axis='y', labelcolor='tab:blue')
            
            ax2 = ax1.twinx()
            
            ax2.set_ylabel('torque (in-oz)', color='tab:red')
            ax2.scatter(u_time_, u_torq_, color='tab:red')
            ax2.text(np.max(u_time_) - 20, 0, pt_txt)
            ax2.tick_params(axis='y', labelcolor='tab:red')
            
            fig.tight_layout()
            plt.grid(True, which='major')
#            plt.savefig(filename_ + '_Torque.png', dpi=600)
            plt.show()
            
    #        generate slopes of angle2 (i.e. speed)
            plt.figure()
            plt.title('Velocity')
            plt.ylabel('velocity (deg/s)')
            plt.xlabel('time (sec)')
            plt.scatter(time_[:(len(time_) - delta_)], slope_)
            plt.grid(True, which='major')
#            plt.savefig(filename_ + '_Velocity.png', dpi=600)
            plt.show()
    
            
        else:
            not_files.append(file)
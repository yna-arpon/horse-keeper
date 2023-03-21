import numpy as np #most likely need
import tensorflow as tf #may need
import pandas as pd

import DataSorter as ds
import AudioCalculator as auc
import AccelerometerCalculator as acc
import AnswerGenerator as ans

# #assuming 8kHz (16000 data points for 2s, 32000 for 4s) for data collection this is how we slice an array into parts
# i = 0
# for i =< data_array.shape//16000:
#     c = slice(i, i+32000, 1) #the number 1 can be changed to 2 (or larger) which skips over every other data point (this can be used to speed up the algorithm)
#     data_slice = data_array[0][c]
#     #do things with slice
#     #append info to data_array (in the correct area)
#     i += 16000
# return data_array

def main():
    time_stamp = 'Yes' #user inputs Yes or No
    flag = 'Yes' #user inputs Yes or No
    flag_path = 'Path to export the flag CSV file' #user inputs 'Path to export the flag CSV file\' usually done with = input('Enter filepath name: ') in python
    audio_file_path = 'Path where the audio CSV file is stored\File name.csv' #user inputs 'Path where the CSV file is stored\File name.csv' usually done with = input('Enter filepath name: ') in python
    accel_m_file_path = 'Path where the accel magnitude CSV file is stored\File name.csv' #user inputs 'Path where the CSV file is stored\File name.csv' usually done with = input('Enter filepath name: ') in python
    accel_v_file_path = 'Path where the accel vector CSV file is stored\File name.csv' #user inputs 'Path where the CSV file is stored\File name.csv' usually done with = input('Enter filepath name: ') in python
    
    cough_num = [[],[]] # [[number of coughs],[global max point numbers at each cough]]
    flag_num = [[],[]] # [[number of flags],[global max point numbers at each flag]]
    audio_data = [[],[],[],[],[]] # [[vibration/mic data],[# of data points],[local max average],[global max],[global max point #]]
    accel_data = [[],[],[],[],[],[],[],[]] # [[accelerometer magnitude data],[accelerometer vector data],[# of data points],[local max average],[global max],[global max point #],[local min average],[global min]]

    audio_data[0] = pd.read_csv(audio_file_path)
    accel_data[0] = pd.read_csv(accel_m_file_path)
    accel_data[1] = pd.read_csv(accel_v_file_path)

    audio_data = [ds.audio_data, ds.num_of_points]
    accel_data = [ds.accel_mag_data, ds.accel_vec_data, ds.num_of_points]

    audio_data.append(auc.local_max_avg(audio_data), auc.global_max(audio_data), auc.max_point(audio_data))
    accel_data.append(acc.local_max_avg(accel_data), acc.global_max(accel_data), acc.max_point(accel_data), acc.local_min_avg(accel_data), acc.global_min(accel_data))

    cough_num = ans.count_coughs(audio_data, accel_data)
    print(cough_num[0])

    # if time_stamp == True:
    #     print(cough_num[1])
    

if __name__ == "__main__":
    main()
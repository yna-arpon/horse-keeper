import numpy as np
import csv

audio_file_path = input('Enter filepath name: ') #user inputs 'Path where the CSV file is stored\File name.csv' usually done with = input('Enter filepath name: ') in python
accel_file_path = input('Enter filepath name: ') #user inputs 'Path where the CSV file is stored\File name.csv' usually done with = input('Enter filepath name: ') in python

df = np.loadtxt(audio_file_path, delimiter=',')
audio_data = df
df = np.loadtxt(accel_file_path, delimiter=',')
accel_data = df

data_new = np.append(audio_data, accel_data) #8s
data_new = np.append(data_new, data_new) #16
data_new = np.append(data_new, data_new) #32
# data_new = np.append(data_new, data_new) #64
# data_new = np.append(data_new, data_new) #128
# data_new = np.append(data_new, data_new) #256
# data_new = np.append(data_new, data_new) #512
# data_new = np.append(data_new, data_new) #1024
# data_new = np.append(data_new, data_new) #2048
# data_new = np.append(data_new, data_new) #4096
# data_new = np.append(data_new, data_new) #8192
# data_new = np.append(data_new, data_new) #16384
# data_new = np.append(data_new, data_new) #32768

with open('output1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data_new)

print('done')
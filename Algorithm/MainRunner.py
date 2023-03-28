import numpy as np #most likely need
# import tensorflow as tf #may need
import pandas as pd

from AnswerGenerator import AnswerGen
from AccelerometerCalculator import accel_data_calculator
from AudioCalculator import audio_data_calculator

def main():
    audio_file_path = input('Enter filepath name: ') #user inputs 'Path where the CSV file is stored\File name.csv' usually done with = input('Enter filepath name: ') in python
    accel_file_path = input('Enter filepath name: ') #user inputs 'Path where the CSV file is stored\File name.csv' usually done with = input('Enter filepath name: ') in python
   
    cough_num = [[],[]] # [[number of coughs],[global max point numbers at each cough]]
    flag_num = [[],[]] # [[number of flags],[global max point numbers at each flag]]
    audio_data = [[],[],[],[]] # [[vibration/mic data],[local max average],[global max],[global max index]]
    accel_data = [[],[],[],[],[],[],[]] # [[accelerometer data],[local max average],[global max],[global max index],[local min average],[global min],[global min index]]

    audio_data[0] = pd.read_csv(audio_file_path) #works
    accel_data[0] = pd.read_csv(accel_file_path) #works
    
    # print(audio_data)
    # print(accel_data)

    #Get calculations
    #assuming 8kHz (16000 data points for 2s, 32000 for 4s) for data collection this is how we slice an array into parts
    # i = 0
    #   for i =< data_array.shape//16000:
    #     c = slice(i, i+32000, 1) #the number 1 can be changed to 2 (or larger) which skips over every other data point (this can be used to speed up the algorithm)
    #     data_slice = data_array[0][c]
    #     #do things with slice
    #     #append info to data_array (in the correct area)
    #     i += 16000
    # return data_array
    audio_calculations = audio_data_calculator(audio_data)
    print(audio_calculations.audio_datafreq)
    # audio_calculations.local_max_average()
    # audio_data[1] =
    # audio_calculations.global_max()
    # audio_data[2] = 
    #

    # audio_data[1] = audio_data_calculator.local_max_average(audio_data) #local max average
    # audio_data[2] = audio_data_calculator.global_max(audio_data) #global max
    # audio_data[3] = audio_data_calculator.global_max_index(audio_data) #global max index
    # accel_data[1] = accel_data_calculator.local_max_average(accel_data) #local max average
    # accel_data[2] = accel_data_calculator.global_max(accel_data)
    # accel_data[3] = accel_data_calculator.global_max_index(accel_data)
    # accel_data[4] = accel_data_calculator.local_min_average(accel_data)
    # accel_data[5] = accel_data_calculator.global_min(accel_data)

    #Get Answers
    cough_num = AnswerGen.answer(audio_data, accel_data)

    print(cough_num[0])
    for x in cough_num[1]:
        print(cough_num[1][x])


    # if time_stamp == True:
    #     print(cough_num[1])
    

if __name__ == "__main__":
    main()
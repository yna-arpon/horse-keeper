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

    df = np.loadtxt(audio_file_path, delimiter=',')
    audio_data[0] = df
    #print("this is audio", audio_data[0])

    df = np.loadtxt(accel_file_path, delimiter=',')
    accel_data[0] = df
    #print("this is audio", accel_data[0])

    #Get calculations
    #assuming 8kHz (16000 data points for 2s, 32000 for 4s) for data collection this is how we slice an array into parts
    x = 0
    for i in range(0, len(audio_data[0])//5000):

        #slice the audio data
        audio_slice = audio_data[0][x:x+9999:10] #the number 1 can be changed to 2 (or larger) which skips over every other data point (this can be used to speed up the algorithm)
        accel_slice = accel_data[0][x:x+9999:10]

        #make calculation class for audio slices
        audio_calculations = audio_data_calculator(audio_slice)
        accel_calculations = accel_data_calculator(accel_slice)

        #do calculations with class
        audio_calculations.audio_return()
        #print(audio_calculations.audio_returnarr)
        accel_calculations.accel_return()
        #print(accel_calculations.accel_returnarr)

        #append info to audio_data (in the correct area)
        audio_data[1].append(audio_calculations.audio_returnarr[0])
        audio_data[2].append(audio_calculations.audio_returnarr[1])
        audio_data[3].append(audio_calculations.audio_returnarr[2])

        accel_data[1].append(accel_calculations.accel_returnarr[0])
        accel_data[2].append(accel_calculations.accel_returnarr[2])
        accel_data[3].append(accel_calculations.accel_returnarr[3])
        accel_data[4].append(accel_calculations.accel_returnarr[1])
        accel_data[5].append(accel_calculations.accel_returnarr[4])
        accel_data[6].append(accel_calculations.accel_returnarr[5])

        x += 5000

    print("This is audio array", audio_data)
    #print("This is acclerometer array", accel_data)

    #Get Answers
    for j in range(0, len(audio_data[1])):

        #slice the audio data calculations
        audio_calc_slice = []
        audio_calc_slice.append(audio_data[1][j])
        audio_calc_slice.append(audio_data[2][j])
        audio_calc_slice.append(audio_data[3][j])

        accel_calc_slice = []
        accel_calc_slice.append(accel_data[1][j])
        accel_calc_slice.append(accel_data[2][j])
        accel_calc_slice.append(accel_data[3][j])
        accel_calc_slice.append(accel_data[4][j])
        accel_calc_slice.append(accel_data[5][j])
        accel_calc_slice.append(accel_data[6][j])
    

    # print(cough_num[0])
    # for x in cough_num[1]:
    #     print(cough_num[1][x])

    # if time_stamp == True:
    #     print(cough_num[1])
    

if __name__ == "__main__":
    main()
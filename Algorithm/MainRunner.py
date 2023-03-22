import numpy as np #most likely need
# import tensorflow as tf #may need
import pandas as pd

from AnswerGenerator import AnswerGen

def main():
    # audio_file_path = 'Path where the audio CSV file is stored\File name.csv' #user inputs 'Path where the CSV file is stored\File name.csv' usually done with = input('Enter filepath name: ') in python
    # accel_file_path = 'Path where the x accel CSV file is stored\File name.csv' #user inputs 'Path where the CSV file is stored\File name.csv' usually done with = input('Enter filepath name: ') in python
   
    cough_num = [[],[]] # [[number of coughs],[global max point numbers at each cough]]
    flag_num = [[],[]] # [[number of flags],[global max point numbers at each flag]]
    audio_data = [[],[],[],[]] # [[vibration/mic data],[local max average],[global max],[global max index]]
    accel_data = [[],[],[],[],[],[],[]] # [[accelerometer data],[local max average],[global max],[global max index],[local min average],[global min],[global min index]]

    # audio_data[0] = pd.read_csv(audio_file_path)
    # accel_data[0] = pd.read_csv(accel_x_file_path)
    
    #Get calculations
    audio_data[1] = function1(audio_data)
    audio_data[2] = function2(audio_data)
    audio_data[3] = function3(audio_data)
    accel_data[1] = func1(accel_data)
    accel_data[2] = func1(accel_data)
    accel_data[3] = func1(accel_data)
    accel_data[4] = func1(accel_data)
    accel_data[5] = func1(accel_data)

    #Get Answers
    cough_num = AnswerGen.answer(audio_data, accel_data)

    print(cough_num[0])
    for x in cough_num[1]:
        print(cough_num[1][x])


    # if time_stamp == True:
    #     print(cough_num[1])
    

if __name__ == "__main__":
    main()
import numpy as np #most likely need
# import tensorflow as tf #may need

from .AnswerGenerator import AnswerGen
from .AccelerometerCalculator import accel_data_calculator
from .AudioCalculator import audio_data_calculator

def main(audio_file_path, accel_file_path):
    # audio_file_path = input('Enter filepath name: ') #user inputs 'Path where the CSV file is stored\File name.csv' usually done with = input('Enter filepath name: ') in python
    # accel_file_path = input('Enter filepath name: ') #user inputs 'Path where the CSV file is stored\File name.csv' usually done with = input('Enter filepath name: ') in python
   
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
    for i in range(0, len(audio_data[0])//20000):

        #slice the audio data
        audio_slice = audio_data[0][x:x+39999:10] #the number 1 can be changed to 2 (or larger) which skips over every other data point (this can be used to speed up the algorithm)
        accel_slice = accel_data[0][x:x+39999:10]

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
        audio_data[3].append(audio_calculations.audio_returnarr[2] + x)

        accel_data[1].append(accel_calculations.accel_returnarr[0])
        accel_data[2].append(accel_calculations.accel_returnarr[2])
        accel_data[3].append(accel_calculations.accel_returnarr[3] + x)
        accel_data[4].append(accel_calculations.accel_returnarr[1])
        accel_data[5].append(accel_calculations.accel_returnarr[4])
        accel_data[6].append(accel_calculations.accel_returnarr[5] + x)

        x += 20000

    # print("This is audio array", audio_data)
    # print("This is accelerometer array", accel_data)
    # print("This is a min avg array", accel_data[1])
    # print("This is a global min array", accel_data[4])

    #Get Answers
    #make answer class for data slices
    cough_answers = AnswerGen(audio_data, accel_data)

    #calculate answers for data slices
    cough_answers.answer_return()
    answer = cough_answers.cough

    #print number of coughs
    num_coughs = int (answer[0])
    print("Number of horse coughs counted: ", num_coughs)
    
    #print time-stamps of coughs
    cough_time = np.array(answer[1])/10000
    cough_h = cough_time//3600
    cough_m = (cough_time - (cough_h*3600))//60
    cough_s = (cough_time - (cough_h*3600) - (cough_m*60))
    # print("The flag time stamps are: ", cough_h, "h ", cough_m, "m ", cough_s, "s")

    final_cough_time_arr = []

    if(len(cough_h)==0):
        cough_result = "There are no cough time stamps"
        final_cough_time_arr.append([cough_result])

    for i in range(len(cough_h)):
        cough_time_num = "Timestamp " + str(i+1) + ":"
        cough_hour = str(cough_h[i]) + "h"
        cough_min = str(cough_m[i]) + "m"
        cough_sec = str(cough_s[i]) + "s"
        final_cough_time_arr.append([cough_time_num, cough_hour, cough_min, cough_sec])
    
    print(final_cough_time_arr)

    #print number of flags
    num_flags = int(answer[2])
    print("Number of flags counted: ", num_flags)
    
    #print time-stamps of flags
    flag_time = np.array(answer[3])/10000
    flag_h = flag_time//3600
    flag_m = (flag_time - (flag_h*3600))//60
    flag_s = (flag_time - (flag_h*3600) - (flag_m*60))

    final_flag_time_arr = []

    if(len(flag_h)==0):
        flag_result = "There are no flag time stamps"
        final_flag_time_arr.append([flag_result])

    for i in range(len(flag_h)):
        flag_time_num = "Time Stamp " + str(i+1) + ":"
        flag_hour = str(flag_h[i]) + "h"
        flag_min = str(flag_m[i]) + "m"
        flag_sec = str(flag_s[i]) + "s"
        final_flag_time_arr.append([flag_time_num, flag_hour, flag_min, flag_sec])

    print(final_flag_time_arr)

    return (num_coughs, num_flags, final_cough_time_arr, final_flag_time_arr)



if __name__ == "__main__":
    main()
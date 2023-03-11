import numpy as np #most likely need
import tensorflow as tf #may need

import DataSorter as ds
import AudioCalculator as auc
import AccelerometerCalculator as acc
import AnswerGenerator as ans


def main():
    time_stamp = True

    cough_num = [[],[]] # [[cough number],[global max point numbers at each cough]]
    audio_data = [[],[],[],[],[]] # [[vibration/mic data],[# of data points],[local max average],[global max],[global max point #]]
    accel_data = [[],[],[],[],[],[],[],[]] # [[accelerometer magnitude data],[accelerometer vector data],[# of data points],[local max average],[global max],[global max point #],[local min average],[global min]]

    audio_data = [ds.audio_data, ds.num_of_points]
    accel_data = [ds.accel_mag_data, ds.accel_vec_data, ds.num_of_points]

    audio_data.append(auc.local_max_avg(audio_data), auc.global_max(audio_data), auc.max_point(audio_data))
    accel_data.append(acc.local_max_avg(accel_data), acc.global_max(accel_data), acc.max_point(accel_data), acc.local_min_avg(accel_data), acc.global_min(accel_data))

    cough_num = ans.count_coughs(audio_data, accel_data)
    print(cough_num[0])

    if time_stamp == True:
        print(cough_num[1])
    

if __name__ == "__main__":
    main()
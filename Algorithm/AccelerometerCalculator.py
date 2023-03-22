# #assuming 8kHz (16000 data points for 2s, 32000 for 4s) for data collection this is how we slice an array into parts
# i = 0
# for i =< data_array.shape//16000:
#     c = slice(i, i+32000, 1) #the number 1 can be changed to 2 (or larger) which skips over every other data point (this can be used to speed up the algorithm)
#     data_slice = data_array[0][c]
#     #do things with slice
#     #append info to data_array (in the correct area)
#     i += 16000
# return data_array

import numpy as np 


class accel_data_calculator:
    
    def __init__ (self,accel_data):
        accel_datapt = accel_data[2]
        accel_data_magnitude = accel_data[0]
        
        self.accel_datapt = accel_datapt
        self.accel_data_magnitude = accel_data_magnitude
        
    def local_max_points(cls, accel_data_magnitude):

        local_max_points = []

        local_max_points = np.where((accel_data_magnitude[1:1] > accel_data_magnitude[0:-2]) * (accel_data_magnitude[1:-1] > accel_data_magnitude[2:]))[0] + 1

        return local_max_points
    
    def local_max_average(cls, local_max_points):

        # averages the local max points
        local_max_average = np.average(local_max_points)

        return local_max_average
    
    def local_min_points(cls, accel_data_magnitude):
        
        local_min_points = np.where((accel_data_magnitude[1:1] < accel_data_magnitude[0:-2]) * (accel_data_magnitude[1:-1] < accel_data_magnitude[2:]))[0] + 1

        return local_min_points
    
    def local_min_average(cls, local_min_points):

        local_min_average = np.average(local_min_points)

        return local_min_points
    
    def global_max(cls,accel_data_magnitude):

        global_max = np.max(accel_data_magnitude)
            
        return global_max
    
    def global_max_point(cls, global_max, accel_data_magnitude, accel_datapt):

        global_max_index= np.where(accel_data_magnitude == global_max)

        global_max_point = accel_datapt[global_max_index]

        return global_max_point
    
    def global_min(cls, accel_data_magnitude):

        global_min = np.min(accel_data_magnitude)
            
        return global_min

         
    def peak_period(cls, global_min, global_max_point, accel_datapt,accel_data_magnitude):

        #find the difference betwee the global_min and global_max time points

        global_min_index = np.where(accel_data_magnitude == global_min)

        global_min_point = accel_datapt[global_min_index]

        peak_period = (global_min_point - global_max_point)


        return peak_period
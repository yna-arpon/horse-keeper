# #assuming 8kHz (16000 data points for 2s, 32000 for 4s) for data collection this is how we slice an array into parts
# i = 0
# for i =< data_array.shape//16000:
#     c = slice(i, i+32000, 1) #the number 1 can be changed to 2 (or larger) which skips over every other data point (this can be used to speed up the algorithm)
#     data_slice = data_array[0][c]
#     #do things with slice
#     #append info to data_array (in the correct area)
#     i += 16000
# return data_array

# Audio Calculator
import numpy as np

#function to access the audio calculator
class audio_data_calculator:

    def __init__(self,audio_data):
        audio_datapt = audio_data[1]
        audio_datafreq = audio_data[0]

        self.audio_datapt = audio_datapt
        self.audio_datafreq = audio_datafreq
        
    
    #identifies and collects points of local maximum
    def local_max_points(cls,audio_datafreq): 
        # peaks: makes a list of all indices where the value of y[i] is greater than
        # both of its negihbours. Does not check the endpoints, which only have one
        # neighbour each. 
        # +1 finds the indices within the slice y[1:-1], not the full array y
        # [0] returns a tuple of arrays, where the first element is the array we want
        local_max_points = [] 
        
        local_max_points = np.where((audio_datafreq[1:1] > audio_datafreq[0:-2]) * (audio_datafreq[1:-1] > audio_datafreq[2:]))[0] + 1 
        
        return local_max_points

    def local_max_average(cls, local_max_points):

        # averages the local max points
        local_max_average = np.average(local_max_points)

        return local_max_average

    def global_max(cls, audio_data_freq):

        global_max = np.max(audio_data_freq)
            
        return global_max
    
    def global_max_point(cls, global_max, audio_data_freq, audio_datapt):

        #gives index of the arrat in audio_data_freq
        global_max_index = np.where(audio_data_freq == global_max)

        #assuming that the arrays have the same length:

        global_max_point = audio_datapt[global_max_index]

        return global_max_point
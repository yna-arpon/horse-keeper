
# Audio Calculator
import numpy as np

#function to access the audio calculator
class audio_data_calculator:

    def __init__(self,audio_data):
        self.audio_datafreq = audio_data[0]
        self.audio_returnarr = [[],[],[]] #[[localmaxave],[globalmax],[globalmaxindex]]
        self.localmaxpts = []

    def audio_return(self):
        
        self.localmaxpts = self.local_max_points(self)
        self.audio_returnarr[0] = self.local_max_average(self)
        self.audio_returnarr[1] = self.global_max(self)
        self.audio_returnarr[2] = self.global_max_index(self)

        return self.audio_returnarr # returns the audio return array to the main: can be called by audiodataarray = audio_data_calculator.audio_return(audio_data)
    
    # localmaxavg = audiodataarray[0]

    def local_max_points(self): 

        local_max_points = [] 

        for i in range(1, len(self.audio_datafreq)-1):
            if self.audio_datafreq[i-1] < self.audio_datafreq[i] and self.audio_datafreq[i] > self.audio_datafreq[i+1]:
                local_max_points.append(self.audio_datafreq[i])
            else:
                pass

            self.local_max_points = local_max_points

    def local_max_average(self):

        local_max_points = local_max_points(self.audio_datafreq)

        local_max_average = np.average(local_max_points)

        self.local_max_average = local_max_average

    def global_max(self):
        
        global_max = np.max(self.audio_datafreq)
            
        self.global_max = global_max
    
    def global_max_index(self):

        global_max = global_max(self.audio_datafreq)

        global_max_index = np.where(self.audio_datafreq == global_max)

        self.global_max_index = global_max_index
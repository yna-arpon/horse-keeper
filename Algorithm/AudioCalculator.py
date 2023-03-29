
# Audio Calculator
import numpy as np

#function to access the audio calculator
class audio_data_calculator:

    def __init__(self,audio_data):
        self.audio_datafreq = audio_data
        self.audio_returnarr = [[],[],[]] #[[localmaxave],[globalmax],[globalmaxindex]]
        self.localmaxpts = []

    def audio_return(self):
        
        self.local_max_points()
        self.local_max_average()
        self.global_max()
        self.global_max_index()

    def local_max_points(self): 

        local_max_points = [] 

        for i in range(1, len(self.audio_datafreq)-1):
            if self.audio_datafreq[i-1] < self.audio_datafreq[i] and self.audio_datafreq[i] > self.audio_datafreq[i+1]:
                local_max_points.append(self.audio_datafreq[i])
            
            else:
                pass

            self.localmaxpts = local_max_points


    def local_max_average(self):

        local_max_average = np.average(self.localmaxpts)
    
        self.audio_returnarr[0] = local_max_average

    def global_max(self):
        
        global_max = np.max(self.audio_datafreq)
            
        self.audio_returnarr[1] = global_max
    
    def global_max_index(self):

        global_max_index = np.where(self.audio_datafreq == self.audio_returnarr[1])[0][0]

        self.audio_returnarr[2] = global_max_index

import numpy as np 


class accel_data_calculator:
    
    def __init__ (self,accel_data):
        self.accel_data = accel_data [0]
        self.accel_returnarr = [[],[],[],[],[],[]] #[[localmaxave],[localminave],[globalmax],[globalmaxindex],[globalmin],[globalminindex]]
        self.localmaxpoints = []
        self.localminpoints = []


    def accel_return(self):

        self.local_max_points()
        self.local_min_points()
        self.local_max_average()
        self.local_min_average()
        self.global_max()
        self.global_max_index()
        self.global_min()
        self.global_min_index()

        return self.accel_returnarr
        
    def local_max_points(self):

        local_max_points = []

        for i in range(1, len(self.accel_data)-1):
            if self.accel_data[i-1] < self.accel_data[i] and self.accel_data[i] > self.accel_data[i+1]:
                local_max_points.append(self.accel_data[i])
            else:
                pass

            self.localmaxpoints = local_max_points
    
    def local_max_average(self):

        local_max_average = np.average(self.localmaxpoints)

        self.local_max_average = local_max_average
    
    def local_min_points(self):
        
        local_min_points = []

        for i in range(1, len(self.accel_data)-1):
            if self.accel_data[i-1] > self.accel_data[i] and self.accel_data[i] < self.accel_data[i+1]:
                local_min_points.append(self.accel_data[i])
            else:
                pass

            self.localminpoints = local_min_points

    
    def local_min_average(self):

        local_min_average = np.average(self.localminpoints)

        self.local_min_average = local_min_average
    
    def global_max(self):

        global_max = np.max(self.accel_data)
            
        self.global_max = global_max
    
    def global_max_index(self):

        global_max_index= np.where(self.accel_data == self.global_max)

        self.global_max_index = global_max_index
    
    def global_min(self):

        global_min = np.min(self.accel_data)
            
        self.global_min = global_min

    def global_min_index(self):

        global_min_index = np.where(self.accel_data == self.global_min)

        self.global_min_index = global_min_index

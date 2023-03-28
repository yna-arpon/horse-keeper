
import numpy as np 


class accel_data_calculator:
    
    def __init__ (self,accel_data):
        self.accel_data = accel_data [0]
        self.accel_returnarr = [[],[],[],[],[],[]] #[[localmaxave],[localminave],[globalmax],[globalmaxindex],[globalmin],[globalminindex]]
        self.localpoints = [[],[]] #[[localmaxpts],[localminpts]]


    def accel_return(self):
        self.localpoints[0] = self.local_max_points(self)
        self.localpoints[1] = self.local_min_points(self)
        self.accel_returnarr[0] = self.local_max_average(self)
        self.accel_returnarr[1] = self.local_min_average(self)
        self.accel_returnarr[2] = self.global_max(self)
        self.accel_returnarr[3] = self.global_max_index(self)
        self.accel_returnarr[4] = self.global_min(self)
        self.accel_returnarr[5] = self.global_min_index(self)

        return self.accel_returnarr
        
    def local_max_points(self):

        local_max_points = []

        for i in range(1, len(self.accel_data)-1):
            if self.accel_data[i-1] < self.accel_data[i] and self.accel_data[i] > self.accel_data[i+1]:
                local_max_points.append(self.accel_data[i])
            else:
                pass

            self.local_max_points = local_max_points
    
    def local_max_average(self):

        local_max_points = local_max_points (self.accel_data)

        local_max_average = np.average(local_max_points)

        self.local_max_average = local_max_average
    
    def local_min_points(self):
        
        local_min_points = []

        for i in range(1, len(self.accel_data)-1):
            if self.accel_data[i-1] > self.accel_data[i] and self.accel_data[i] < self.accel_data[i+1]:
                local_min_points.append(self.accel_data[i])
            else:
                pass

            self.local_min_points = local_min_points

    
    def local_min_average(self):

        local_min_points = local_min_points (self.accel_data)
        local_min_average = np.average(local_min_points)

        self.local_min_average = local_min_average
    
    def global_max(self):

        global_max = np.max(self.accel_data)
            
        self.global_max = global_max
    
    def global_max_index(self):

        global_max = global_max (self.accel_data)

        global_max_index= np.where(self.accel_data == global_max)

        self.global_max_index = global_max_index
    
    def global_min(self):

        global_min = np.min(self.accel_data)
            
        self.global_min = global_min

    def global_min_index(self):
        
        global_min = global_min(self.accel_data)

        global_min_index = np.where(self.accel_data == global_min)

        self.global_min_index = global_min_index

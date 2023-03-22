import numpy as np

class AnswerGen:
    def __init__(self, audiodata, acceldata):
        self.data1 = audiodata
        self.data2 = acceldata
        self.trues = [[],[],[],[]] # [[max audio],[max accel],[min],[time between max and min]]

    def answer (self):  
        self.trues[0] = self.audio_answer(self)
        self.trues[1] = self.accel_max_answer(self)
        self.trues[2] = self.accel_min_answer(self)
        self.trues[3] = self.accel_time_answer(self)
        result = np.add(self.trues[0], self.trues[1], self.trues[2], self.trues[3])
        cough = 0
        for x in result:
            if result > 2 :
                cough + cough + 1
        return cough   

    def audio_answer (self):
        audio_result = []
        for x in self.data1[2]:
            if self.data1[2] > 2*self.data1[1]:
                audio_result.append(1)
            else:
                audio_result.append(0)
        return audio_result        

    def accel_max_answer (self):
        accel_max_result = []
        for x in self.data2[2]:
            if self.data2[2] > 2*self.data2[1]:
                accel_max_result.append(1)
            else:
                accel_max_result.append(0)
        return accel_max_result
   
    def accel_min_answer (self):
        accel_min_result = []
        for x in self.data2[5]:
            if self.data2[5] > 2*self.data2[4]:
                accel_min_result.append(1)
            else:
                accel_min_result.append(0)
        return  accel_min_result    

    def accel_time_answer (self):
        accel_time_result = []

        return accel_time_result

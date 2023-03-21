class AnswerGen:
    def __init__(self, audiodata, acceldata):
        self.data1 = audiodata
        self.data2 = acceldata
        self.trues = [[],[],[],[]] # []

    def answer (self):
        self.audio_answer(self)
        self.accel_answer(self)


    def audio_answer (self):
        audio_result = []
        for x in self.data1[3]:
            if self.data1[3] > 2*self.data1[2]:
                audio_result[x] = 1
            else:
                audio_result[x] = 0
        return audio_result        

    def accel_answer (self):
        accel_max_result = []
        accel_min_result = []
        for x in self.data2[4]:
            if self.data2[4] > 2*self.data2[3]:
                accel_max_result[x] = 1
            else:
                accel_max_result[x] = 0
        return accel_max_result
        for x in data2[7]:
            if data2[7] > 2*data2[6]:
                accel_min_result[x] = 1
            else:
                accel_min_result[x] = 0
        return accel_min_result    

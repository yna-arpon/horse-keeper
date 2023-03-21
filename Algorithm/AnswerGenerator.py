class AnswerGenerator:
    def __init__(self, audiodata, acceldata, counter):
        self.data1 = audiodata
        self.data2 = acceldata
        self.counter = counter

    def audio_answer_generator (data1):
        audio_result = []
        for x in data1[3]:
            if data1[3] > 1.5*data1[2]:
                audio_result[x] = 1
            else:
                audio_result[x] = 0
        return audio_result        

    def accel_answer_generator (data2):
        accel_max_result = []
        accel_min_result = []
        for x in data2[4]:
            if data2[4] > 1.5*data2[3]:
                accel_max_result[x] = 1
            else:
                accel_max_result[x] = 0
        return accel_max_result
        for x in data2[7]:
            if data2[7] > 1.5*data2[6]:
                accel_min_result[x] = 1
            else:
                accel_min_result[x] = 0
        return accel_min_result    

import numpy as np

class AnswerGen:
    def __init__(self, audiodata, acceldata):
        self.data1 = audiodata
        self.data2 = acceldata
        self.trues = [[],[],[],[]] # [[max audio],[max accel],[min accel],[time between max and min]]
        self.cough = [[],[]]

    def answer_return(self):
        
        self.audio_answer()
        self.accel_max_answer()
        self.accel_min_answer()
        self.accel_time_answer()
        self.answer()

    def answer(self):  

        result = self.trues[0] + self.trues[1] + self.trues[2] + self.trues[3]

        z = 0
        for x in result:
            if result > 2 and x in self.trues[1] == 1 and x != z:
                self.cough[0] += 1
                self.cough[1].append(self.data2[3][np.where(x)])
                z=x   

    def audio_answer(self):

        audio_result = []

        for x in self.data1[2]:

            if x > 1.2*self.data1[1][np.where(self.data1[2] == x)[0][0]]:
                audio_result.append(1)

            else:
                audio_result.append(0)

        print(audio_result) #works

        self.trues[0] = audio_result        

    def accel_max_answer(self):

        accel_max_result = []

        for x in self.data2[2]:

            if x > 1.2*self.data2[1][np.where(self.data2[2] == x)[0][0]]:
                accel_max_result.append(1)

            else:
                accel_max_result.append(0)

        print(accel_max_result) #works

        self.trues[1] = accel_max_result
   
    def accel_min_answer(self):

        accel_min_result = []

        for x in self.data2[5]:

            if x < 0.8*self.data2[4][np.where(self.data2[5] == x)[0][0]]:
                accel_min_result.append(1)

            else:
                accel_min_result.append(0)

        print(accel_min_result) #works

        self.trues[2] = accel_min_result    

    def accel_time_answer(self):

        accel_time_result = []

        for x, y in zip(self.data2[3],self.data2[6]):

            if (x-y) < 2000 and (x-y) > 1000:
                accel_time_result.append(1)

            else:
                accel_time_result.append(0)

        print(accel_time_result) #works

        self.trues[3] = accel_time_result

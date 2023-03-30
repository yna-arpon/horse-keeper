import numpy as np

class AnswerGen:
    def __init__(self, audiodata, acceldata):
        self.data1 = audiodata
        self.data2 = acceldata
        self.trues = [[],[],[],[]] # [[max audio],[max accel],[min accel],[time between max and min]]
        self.cough = [[],[],[],[]] # [[cough count],[cough index],[flag count],[cough flag index]]

    def answer_return(self):
        
        self.audio_answer()
        self.accel_max_answer()
        self.accel_min_answer()
        self.accel_time_answer()
        self.answer()

    def answer(self):  

        trues1 = np.array(self.trues[0])
        trues2 = np.array(self.trues[1])
        trues3 = np.array(self.trues[2])
        trues4 = np.array(self.trues[3])
        
        result = trues1 + trues2 + trues3 + trues4
        cough_index = []
        flag_index = []

        z = -1
        for i in range(0, len(result)):

            if result[i] > 2:
                if trues2[i] != 0:
                    if i != z:
                        cough_index.append(self.data2[3][i])
                        z = i + 1

            if result[i] > 1:
                flag_index.append(self.data2[3][i])

        flag_index = list(set(flag_index)) # removes duplicate flags

        self.cough[0] = len(cough_index)
        self.cough[1] = cough_index
        self.cough[2] = len(flag_index)
        self.cough[3] = flag_index

    def audio_answer(self):

        audio_result = []

        for x in self.data1[2]:

            if x > 1.2*self.data1[1][np.where(self.data1[2] == x)[0][0]]:
                audio_result.append(1)

            else:
                audio_result.append(0)

        #print(audio_result) #works

        self.trues[0] = audio_result        

    def accel_max_answer(self):

        accel_max_result = []

        for x in self.data2[2]:

            if x > 1.2*self.data2[1][np.where(self.data2[2] == x)[0][0]]:
                accel_max_result.append(1)

            else:
                accel_max_result.append(0)

        #print(accel_max_result) #works

        self.trues[1] = accel_max_result
   
    def accel_min_answer(self):

        accel_min_result = []

        for x in self.data2[5]:

            if x < 0.8*self.data2[4][np.where(self.data2[5] == x)[0][0]]:
                accel_min_result.append(1)

            else:
                accel_min_result.append(0)

        #print(accel_min_result) #works

        self.trues[2] = accel_min_result    

    def accel_time_answer(self):

        accel_time_result = []

        for x, y in zip(self.data2[3],self.data2[6]):

            if (x-y) < 2000 and (x-y) > 1000:
                accel_time_result.append(1)

            else:
                accel_time_result.append(0)

        #print(accel_time_result) #works

        self.trues[3] = accel_time_result

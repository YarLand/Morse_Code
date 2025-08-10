import csv

class MorseDict:
    # def __init__(self):
    #     self.m_dict = dict
    #     self.m_quiz = dict

    def MorseInit(self,filename):
        with open(filename, mode='r') as file:
            iter_reader = iter(csv.reader(file, delimiter='\t'))
            next(iter_reader)
            return {rows[0]:rows[1] for rows in iter_reader}
        # print(self.m_dict)

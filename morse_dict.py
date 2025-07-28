import csv

class MorseDict:
    def __init__(self):
        self.m_dict = dict

    def MorseInit(self):
        with open("morse_dict.tsv", mode='r') as file:
            iter_reader = iter(csv.reader(file, delimiter='\t'))
            next(iter_reader)
            self.m_dict = {rows[0]:rows[1] for rows in iter_reader}
        # print(self.m_dict)

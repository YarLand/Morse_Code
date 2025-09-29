import csv

class MorseDict:
    def MorseInit(self,filename):
        with open(filename, mode='r') as file:
            iter_reader = iter(csv.reader(file, delimiter='\t'))
            next(iter_reader)
            return {rows[0]:rows[1] for rows in iter_reader}

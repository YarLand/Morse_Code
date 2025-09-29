import errno
import csv
import os

class MorseDict:
    def MorseInit(self,filename):
        if os.path.isfile(filename):
            with open(filename, mode='r') as file:
                iter_reader = iter(csv.reader(file, delimiter='\t'))
                next(iter_reader)
                return {rows[0]:rows[1] for rows in iter_reader}
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)

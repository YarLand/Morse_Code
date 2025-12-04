import csv
import errno
import os


class MorseDict:
    # Initialize the relevant morse dictionary ".tsv" file
    def MorseInit(self,filename):
        # Detect if the file exists
        if os.path.isfile(filename):
            # If the file exists, open it in "Read" mode
            with open(filename, mode='r') as file:
                # Read the ".tsv" file
                dict_reader = csv.DictReader(file,delimiter='\t')
                # Skip the header line of the file
                dict_reader_no_header = list(dict_reader)[1:]
                return {rows["Character"]:rows["MorseCode"] for rows in dict_reader_no_header}
        # If the file does not exist,
        # Raise an error and stop the program.
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)

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
                # and place the result into an iterator
                iter_reader = iter(csv.reader(file, delimiter='\t'))
                # Skip the header line of the file
                next(iter_reader)
                return {rows[0]:rows[1] for rows in iter_reader}
        # If the file does not exist,
        # Raise an error and stop the program.
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)

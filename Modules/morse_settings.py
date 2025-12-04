import csv
import errno
import os


class MorseSettings:
    # Initialize the relevant morse dictionary ".tsv" file
    def SettingsInit(self):
        filename = "Data/morse_settings.tsv"
        # Detect if the file exists
        if os.path.isfile(filename):
            # If the file exists, open it in "Read" mode
            with open(filename, mode='r') as file:
                # Read the ".tsv" file using DictReader,
                # which skip the header line of the file
                dict_reader = csv.DictReader(file,delimiter='\t')
                return {rows["default_characters"]:rows["value"] for rows in dict_reader}
        # If the file does not exist,
        # Raise an error and stop the program.
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)

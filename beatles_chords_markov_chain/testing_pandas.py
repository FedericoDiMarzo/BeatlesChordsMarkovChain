import pandas as pd
import numpy as np
import os

if __name__ == '__main__':
    # paths to the database
    root = os.path.join('..', 'beatles_chords_database')
    rootkey_path = os.path.join(root, 'rootkey')
    chords_path = os.path.join(root, 'chords')

    # this dictionary will contain a list of root notes
    # of chords for each song
    chords_sequence_dict = {}

    # iterating inside the chord_path folder
    for filename in os.listdir(chords_path):
        # reading the file
        new_dataframe = pd.read_csv(os.path.join(chords_path, filename), sep=' ', header=None)

        # removing the rows with N as a chord (because the rests are not needed)
        new_dataframe = new_dataframe.drop(new_dataframe[new_dataframe[2] == 'N'].index)

        # extracting a list from the chord row
        chord_sequence = list(new_dataframe[2])

        # removing everything after ":" for each chord symbol
        chord_sequence_processed = [x.split(':', 1)[0] for x in chord_sequence]

        # removing everything after '/' for each chord symbol
        # this removes the slash chords
        chord_sequence_processed = [x.split('/', 1)[0] for x in chord_sequence_processed]

        # finally, adding the chord sequence to the dictionary
        chords_sequence_dict[filename] = chord_sequence_processed

import pandas as pd
import os
import melodically
import beatles_chords_markov_chain

# paths to the database
cwd = os.path.dirname(beatles_chords_markov_chain.__file__)
root = os.path.join(cwd, '..', 'beatles_chords_database')
rootkey_path = os.path.join(root, 'rootkey')
chords_path = os.path.join(root, 'chords')


def get_chord_roots():
    """
    Gets a dictionary containing for each song
    the sequence of roots of the chords.

    :return: chord roots dictionary
    """
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

    return chords_sequence_dict


def get_rootkeys():
    """
    Gets a dictionary containing for each song
    its root note.

    :return: rootkey dictionary
    """
    # this dictionary will contain the rootkey of each song
    # only songs in major key will be preserved
    rootkey_dict = {}

    # iterating inside the chord_path folder
    for filename in os.listdir(rootkey_path):
        # reading the file
        new_dataframe = pd.read_csv(os.path.join(rootkey_path, filename), sep='\t', header=None)

        # keeping only the songs without a key change
        if new_dataframe.shape[0] == 1:
            key = list(new_dataframe[3])[0]
            if ':' not in key:
                rootkey_dict[filename] = key

    return rootkey_dict


def convert_notes_to_numbers(notes_dict):
    """
    Maps each chord root inside the sequences into values between 0 and 11.

    :param notes_dict: dictionary of chord roots lists
    :return: dictionary of numeric notes list
    """
    chord_numbers = {}
    for song, chords in notes_dict.items():
        if isinstance(chords, list):
            # creates a new list with the new mapping
            chord_numbers[song] = [melodically.std_to_midi(x) for x in chords]
        else:
            chord_numbers[song] = melodically.std_to_midi(chords)

    return chord_numbers

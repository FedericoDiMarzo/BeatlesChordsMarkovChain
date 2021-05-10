from database_preprocessing import get_chord_roots, get_rootkeys, convert_notes_to_numbers
from intervals import get_intervals

# one list of chord roots for each song
chord_roots_dict = get_chord_roots()

# one list of numeric note values (between 0 and 11) for each song
chord_numbers_dict = convert_notes_to_numbers(chord_roots_dict)

# one rootkey for each song
rootkey_dict = get_rootkeys()

# one rootkey as a numeric value (between 0 and 11) for each song
rootkey_numbers_dict = convert_notes_to_numbers(rootkey_dict)

# one list of intervals for each song
intervals_dict = {}

# filling intervals_dict
for song, rootkey_number in rootkey_numbers_dict.items():
    intervals_dict[song] = get_intervals(chord_numbers_dict[song], rootkey_number)

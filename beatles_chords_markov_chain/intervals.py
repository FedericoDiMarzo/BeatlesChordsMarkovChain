interval_symbols = {
    0: 'I',
    2: 'II',
    4: 'III',
    5: 'IV',
    7: 'V',
    9: 'VI',
    11: 'VII'
}


def get_intervals(chords_numbers, root_number):
    # TODO: masking
    intervals = [x - root_number for x in chords_numbers]
    intervals = [x + 11 if x < 0 else x for x in intervals]
    intervals = [interval_symbols[x] for x in intervals if x in interval_symbols.keys()]
    return intervals

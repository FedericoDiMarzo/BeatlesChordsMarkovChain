# symbols used to represent chord intervals
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
    """
    Given a certain chord number list and the keyroot number, it returns
    the list of intervals for that progression. The progression is supposed
    to be in Ionian mode.

    :param chords_numbers: list of midi value (between 0 and 11) of the root of the chord
    :param root_number: midi value (between 0 and 11) of the keyroot
    :return: list of intervals
    """
    intervals = [x - root_number for x in chords_numbers]
    intervals = [x + 11 if x < 0 else x for x in intervals]
    intervals = [interval_symbols[x] for x in intervals if x in interval_symbols.keys()]
    return intervals

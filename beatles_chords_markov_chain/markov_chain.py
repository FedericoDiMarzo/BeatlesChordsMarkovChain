import pomegranate as pg
from processed_data import intervals_dict

# order of the markov chain
markov_chain_order = 3


def train_markov_chain(intervals_sample_dict):
    """
    given the dictionary containing the lists of intervals for each song,
    it returns the markov chain object trained with the data.

    :param intervals_sample_dict: dictionary having the song names as keys and lists of intervals as values
    :return: trained markov chain object
    """
    samples = intervals_sample_dict.values()
    return pg.MarkovChain.from_samples(samples, k=markov_chain_order)


# trained markov chain object
chords_markov_chain = train_markov_chain(intervals_dict)

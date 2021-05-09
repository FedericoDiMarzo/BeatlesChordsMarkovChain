import pomegranate as pg
from processed_data import intervals_dict


def train_markov_chain(intervals_sample_dict):
    samples = intervals_sample_dict.values()
    return pg.MarkovChain.from_samples(samples)


chords_markov_chain = train_markov_chain(intervals_dict)

# Introduction
This python module was born after a week of experiments with the pomegranate library, that offers a nice implementation of a Markov chains (https://github.com/jmschrei/pomegranate), and the Beatles chords library, that contains chord annotations of the discography of the band The Beatles (the original database can be found here: http://isophonics.net/content/reference-annotations-beatles). The result is an easy to install module, that can be reused by anyone that want to experiment with automatic music composition and chord generation.

## Installation
The package can easily be installed using the pip package manager.
```shell
pip install beatles_chords_markov_chain
```

# Notation
In order to represent a chord progression, without being constrained to a particular scale or mode, a symbolic approach using intervals is employed.

```python
# the roman notation is used to represent the chords of a generic mode
chord_notation = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
```

## Usage

The trained markov chain contained in the module, is able to generate sequences of variable lenghts. A generated sequence is a list of symbols that can be used to create interesting chord progressions based on the style of The Beatles.

```python
from beatles_chords_markov_chain import chords_markov_chain
number_of_chords = 6
chords_for_your_next_song = chords_markov_chain.sample(number_of_chords)
```

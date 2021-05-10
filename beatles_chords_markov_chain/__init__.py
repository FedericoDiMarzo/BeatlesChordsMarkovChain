import pickle
import os
from beatles_chords_markov_chain.database_preprocessing import cwd

# In order to pack the trained markov chain into a python package
# a bin file containing the markov chain object must be generated before
# deploying the package. When the package will be imported the binary file
# will be loaded back into the object.
binary_path = os.path.join(cwd, 'chords_markov_chain.bin')

if os.path.isfile(binary_path):
    chords_markov_chain = pickle.load(open(binary_path, 'rb'))
else:
    from beatles_chords_markov_chain.markov_chain import chords_markov_chain

    pickle.dump(chords_markov_chain, open(binary_path, 'wb'))

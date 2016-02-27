#!/usr/bin/python

"""
generator.py
    A simple markov chain text generator written in python

Usage:
    generator.py (--load|-l) <dump> -n <number>

Options:
    --help -h   Print this message.
    --load -l   Pickle dump to load.
    -n          Number of sentences to generate.

"""

import pickle
import random
from docopt import docopt
from model import Markov

punc = ['.', '!', '?']

class Generator:

    def __init__(self, model, n):
        self.model = model
        self.max_sentences = n
        self.tab = []

    def prefix(self):
        return " ".join(self.tab)

    def shift(self, w):
        if len(self.tab) > 1:
            self.tab = self.tab[1:]
        self.tab.append(w)

    def generate_sentence(self):
        self.tab = []
        maj = random.choice(self.model.majs)
        sentence = [maj]
        self.shift(maj)
        dot = False
        while not dot:
            pref = self.prefix()
            nxt = random.choice(self.model.chain[pref])
            sentence.append(nxt)
            self.shift(nxt)
            dot = nxt[-1] in punc
        return sentence

    def generate(self):
        for i in range(n):
            print((' '.join(self.generate_sentence())))


if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.1')
    dump = arguments['<dump>']
    n = int(arguments['<number>'])
    with open(dump, 'rb') as p:
        m = pickle.loads(pickle.load(p, encoding="ASCII"))
    g = Generator(m, n)
    g.generate()

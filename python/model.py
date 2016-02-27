#!/usr/bin/python

"""
model.py

A simple markov chains model generator.

Usage:
    model.py (--file|-f) <file> [(--save|-s) <save>]

Options:
    --help -h   Print this message.
    --file -f   Text file to use as input.
    --save -s   Binary file to store the pickle dump into.
"""

import sys
import pickle
from pprint import pprint as print
from docopt import docopt

punc = ['.', '!', '?']

class Markov:

    def __init__(self, f = None):
        self.tab = []
        self.chain = {}
        self.majs = []
        if f:
            self.read_file(f)

    def prefix(self):
        return " ".join(self.tab)

    def shift(self, w):
        if len(self.tab) > 1:
            self.tab = self.tab[1:]
        self.tab.append(w)

    def read_file(self, f):
        l = []
        with open(f, 'r') as f:
            l = f.readlines()
            for i in l:
                i = i.strip()
            l = " ".join(l).split()
        for i in range(len(l) - 1):
            self.shift(l[i])
            pref = self.prefix()
            nxt = l[i+1]
            if pref[-1] in punc:
                self.majs.append(nxt)
                self.tab = []
            if not pref in self.chain.keys():
                self.chain[pref] = [nxt]
            else:
                self.chain[pref].append(nxt)


if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.1')
    f = arguments['<file>']
    s = arguments['<save>']
    m = Markov(f)
    if s:
        with open(s, 'wb') as p:
            pickle.dump(pickle.dumps(m), p)

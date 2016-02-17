#!/usr/bin/python

"""
model.py

A simple markov chains model generator.

Usage:
    model.py -f <file> [(--save|-s)]
    
"""

from pprint import pprint as print
import sys

class Markov:

    def __init__(self, f = None):
        self.tab = []
        self.chain = {}
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
            if not pref in self.chain.keys():
                self.chain[pref] = [nxt]
            else:
                self.chain[pref].append(nxt)


if __name__ == "__main__":
    s, f = sys.argv
    m = Markov(f)
    print(m.chain)

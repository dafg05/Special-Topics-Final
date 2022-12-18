from constants import DOMAIN
from nfl import f_from_int
import random as rand

# TODO: redefine to algorithms.py

def parity_map(x):
# DEPRECATED: not actually an algorithm
    if x % 2 == 0:
        return 1
    else:
        return 0

def always_one_algo(S):
    def f(x):
        return 1
    return f

def always_zero_algo(S):
    def f(x):
        return 0
    return f

def random_algo(S):
    i = rand.randint(0, DOMAIN)
    return f_from_int(i, DOMAIN)

def parity_algo(S):
    def f(x):
        if x % 2 == 0:
            return 1
        else:
            return 0
    return f


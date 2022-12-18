from constants import DOMAIN
import random as rand

# TODO: redefine to algorithms.py

def parity_map(x):
# DEPRECATED: not actually an algorithm
    if x % 2 == 0:
        return 1
    else:
        return 0

def die_by_one(S):
    def f(x):
        return 1
    return f

def die_by_zero(S):
    def f(x):
        return 0
    return f

        
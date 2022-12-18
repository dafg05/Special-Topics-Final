from constants import DOMAIN
from nfl import f_from_int
import random as rand

def always_one_algo(S):
    def f(x):
        return 1
    return f

def always_zero_algo(S):
    def f(x):
        return 0
    return f

def random_algo(S):
    """
    Outputs a random function for every different dataset S
    """
    rand.seed(hash(tuple(S)))
    i = rand.randint(2**len(DOMAIN))
    return f_from_int(i, DOMAIN)

def parity_algo(S):
    def f(x):
        if x % 2 == 0:
            return 1
        else:
            return 0
    return f


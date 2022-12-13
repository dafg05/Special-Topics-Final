from fractions import Fraction
from typing import Callable

DOMAIN = range(10)

def dist_from_Map(map: Callable):
    """
    Define a distribution where the probabilities are uniform over all
    values that agree with mapping, zero otherwise
    @param
    map: a function from DOMAIN to {0,1}
    dist: a joint distribution: variables are Domain and {0,1}
    """
    
    p = 1/len(DOMAIN) 
    dist = {}
    for x in DOMAIN:
        b = map(x)
        dist[(x, b)] = p
        dist[(x, not b)] = 0
    return dist

def parity_map(x):
    if x % 2 == 0:
        return True
    else:
        return False

def compute_mappings(map):
    mappings = {}
    for x in DOMAIN:
        mappings[x] = map(x)
    return mappings

if __name__ == "__main__":
    raise NotImplementedError

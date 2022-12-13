from typing import Callable
from constants import DOMAIN

def dist_from_map(f: Callable):
    """
    Define a distribution where the probabilities are uniform over all
    values that agree with map, zero otherwise
    @param
    map: a function from DOMAIN to {0,1}
    dist: a joint distribution: variables are c.DOMAIN and {0,1}
    """
    p = 1/len(DOMAIN) 
    dist = {}
    for x in DOMAIN:
        b = f(x)
        dist[(x, b)] = p
        dist[(x, not b)] = 0
    return dist

def compute_mappings(f):
    """
    Convert map to dictionary
    """
    mappings = {}
    for x in DOMAIN:
        mappings[x] = f(x)
    return mappings

def loss_over_dist(f, dist):
    """
    Sum of all instances of joint distribution 
    that don't agree with map
    """
    loss = 0
    for x in DOMAIN:
        b = f(x)
        loss += dist[(x, not b)]
    return loss

def no_free_lunch(algo, size):
    """
    Given an algorithm, and a size m, show that there
    is a distribution D over DOMAIN x {0,1} such that:
    1. there exists a function with zero loss
    2. With probablity of at least 1/7 over the choice of a dataset S
    drawn from D, the loss of algo(S) >= 1/8

    @param
    algo: an algorithm that takes in a dataset and outputs a function from DOMAIN to {0,1}
    size: cardinality of S, must be less than size of DOMAIN/2
    
    @return
    nothing

    @print
    - Distribution D at which our learner sucks at
    - A function with zero loss on D
    - Expected loss algo(S), where S is drawn 
    from D. Should be greater than 1/4.
    """
    raise NotImplementedError


if __name__ == "__main__":
    raise NotImplementedError

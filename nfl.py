import itertools
from typing import Callable
from constants import DOMAIN
import random as rand
import algos


def dist_from_map(f: Callable, domain, funcDomain):
    """
    Define a distribution where the probabilities are uniform over all
    values that agree with map, zero otherwise
    @param
    f: a function f: funcDomain -> {0,1}
    @return
    dist: a joint distribution: variables are x and {0,1}, where x in domain

    Note that funcDomain must be a subset of newDomain
    """
    p = 1 / len(funcDomain)
    dist = {}
    for x in domain:
        b = f(x)
        if b == -1:  # if f is not defined for that point
            dist[(x, 0)] = 0
            dist[(x, 1)] = 0
        else:
            dist[(x, b)] = p
            dist[(x, int(not b))] = 0
    return dist


def compute_mappings(f: Callable):
    """
    Convert map to dictionary
    """
    mappings = {}
    for x in DOMAIN:
        mappings[x] = f(x)
    return mappings


def loss_over_dist(f: Callable, domain, dist: dict):
    """
    Sum of all instances of joint distribution
    that don't agree with map
    """
    loss = 0
    for x in domain:
        b = f(x)
        if b >= 0:  # if f is defined at x
            loss += dist[(x, not b)]
    return loss


def f_from_int(i: int, funcDomain):
    """
    Define a function: funcDomain -> {0,1} from a
    bitstring
    """
    def new_f(x):
        if x not in funcDomain:
            return -1
        index = funcDomain.index(x)
        return (i >> index) & 1

    return new_f


def extrapolate_f(f, newDomain):
    """
    For an f: funcDomain -> {0,1}
    Define a new function h: newDomain -> {0,1}
    s.t. the functions are identical except that
    h is defined for points in newDomain but not in funcDomain

    Note that funcDomain must be a subset of newDomain
    """
    def h(x):
        if (f(x) == -1) and (x in newDomain):
            return 1
        return f(x)
    return h


def exp_loss_over_convinient_dist(algo, dist, algo_domain, m):
    """
    A convenient distribution is defined as distribution uniform over
    a subset C of DOMAIN. Thus, if we sample a dataset S of size m iid
    from a convenient distribution,
    it is equivalent to choosing m random elements from C.

    Expected loss: mean loss of algo(S) over all possible dataset S.
    """
    loss = 0
    subsets = list(itertools.combinations(algo_domain, m))
    k = len(subsets)
    for subset in subsets:
        loss = loss + loss_over_dist(algo(subset), algo_domain, dist)
    return loss*float(1/k)


def no_free_lunch(algo: Callable, m: int):
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

    # Get a random subset C of X of size 2m
    c_set = rand.sample(DOMAIN, 2 * m)
    print(c_set)
    numFunctions = 2 ** (2 * m)
    print(numFunctions)
    f_argmax = None
    d_argmax = None
    maxLoss = 0
    # For every possible function f_i: C -> {0,1}:
    for i in range(numFunctions):
        f_i = f_from_int(i, c_set)
        print(f_i)
        # the "convenient" distribution
        dist_i = dist_from_map(f_i, DOMAIN, c_set)
        print(dist_i)
        loss = exp_loss_over_convinient_dist(algo, dist_i, c_set, m)
        print(loss)
        if loss > maxLoss:
            maxLoss = loss
            f_argmax = f_i
            d_argmax = dist_i
    f_argmax = extrapolate_f(f_argmax, DOMAIN)
    assert loss_over_dist(f_argmax, DOMAIN,
                          d_argmax) == 0, "The extrapolated function does not have zero loss on distribution"
    print(f"Our prized distribution:\n{d_argmax}")
    print(f"A function with zero loss on that distribution:", compute_mappings(f_argmax))

    print(f"Expected loss: {maxLoss}")

if __name__ == "__main__":
    no_free_lunch(algos.random_algo,2)
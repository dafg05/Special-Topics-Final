# Special Topics in Learning Theory Final: No Free Lunch Theorem simulation

A program that demonstrates the No Free Lunch theorem for machine learning.

## Example

Let the domain be the integers from 1 to 10, and let the size of the example dataset be m = 4. Define the learning algorithm as an algoritm that inputs a subset of size m of our domain and randomly outputs a binary classifier.
aka:
let A be a "random" algorithm, S denote a subset of size m, f_i denote a binary classifier. Note that A maps S to f_i: 
A(S) = f_i
where f_i assigns a value of 1 or 0 to each integer x in the domain.

In code:
```
def random_algo(S):
  rand.seed(hash(tuple(S))):
  i = rand.randint(0, 2 ** len(DOMAIN))
  return f_from_int(i, DOMAIN)
```

If we run the `no_free_lunch(algo, size)` on this random algorithm and size = 4:

Our program would output:
1. A distribution D in which there exists a function with zero loss on D:

- Distribution formatting: ({x in domain}, f(x)): probability(({x in domain}, f(x)))
-  {(1, 0): 0, (1, 1): 0, (2, 0): 0, (2, 1): 0, (3, 1): 0.25, (3, 0): 0, (4, 0): 0.25, (4, 1): 0,
(5, 0): 0.25, (5, 1): 0, (6, 0): 0, (6, 1): 0, (7, 0): 0, (7, 1): 0, (8, 0): 0, (8, 1): 0, (9, 1):
0.25, (9, 0): 0, (10, 0): 0, (10, 1): 0}
   
2. The function that has zero loss on D:
- Function formatting: (x in domain): f(x)
- {1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}

3. And expected loss of algo(S), where S is drawn from D (Should be greater than ¼)
-  example expected loss: 0.7083333333333333




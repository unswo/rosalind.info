from itertools import permutations
from math import factorial

n = 6
# +1 as range is not inclusive of n
# alternatively use xrange
posint_to_n = list(range(1, n+1))
perm = permutations(posint_to_n)
perm = list(perm)

print(factorial(n))

for x in perm:
    x = [str(x) for x in x]
    print(' '.join(x))


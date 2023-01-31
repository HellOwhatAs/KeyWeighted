# ---------------------- bisect ---------------------- #
import KeyWeighted.bisect as kbisect

a = [-1, -2, -3, -4, -5, -6, -7]
print(kbisect.bisect_left(a, abs(-5), key = abs))
# 4

# ---------------------- heapq ----------------------- #

import KeyWeighted.heapq as kheapq

a = ["cat", "apple", "Bob", "SJTU"]
kheapq.heapify(a, key = lambda x: -len(x))
print(a)
# ['apple', 'SJTU', 'Bob', 'cat']

while a:
    print(kheapq.heappop(a, key = lambda x: -len(x)))
# apple
# SJTU
# cat
# Bob
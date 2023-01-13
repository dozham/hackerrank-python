# An elegant solution
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    """A Counter that preserves order"""


d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())

## A naive solution
# if __name__ == "__main__":
#     n = int(input())
#     d = dict()
#
#     for _ in range(n):
#         word = input()
#         if d.get(word):
#             d[word] += 1
#         else:
#             d[word] = 1
#
#     print(d)

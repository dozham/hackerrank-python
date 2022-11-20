## Sample input
# 3 2
# 1 5 3
# 3 1
# 5 7

n, m = 3, 2  # map(int, input().split())
array = [1, 5, 3]  # list(map(int, input().split()))
A = [3, 1]  # list(map(int, input().split()))
B = [5, 7]  # list(map(int, input().split()))

# print(sum([1 if (x in A) else -1 if (x in B) else 0 for x in array]))
print([(x in A) for x in array])
print([(x in B) for x in array])
print([((x in A) - (x in B)) for x in array])
print(sum([((x in A) - (x in B)) for x in array]))

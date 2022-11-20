import itertools

string = '1222311'

groups = []
unique_keys = []
# data = sorted(data, key=keyfunc)
# for k, g in groupby(data, keyfunc):
for k, g in itertools.groupby(string):
    groups.append(list(g))      # Store group iterator as a list
    unique_keys.append(k)

print(groups)
print(unique_keys)

from itertools import combinations

inpt = input().split()

k = inpt[0]
n = inpt[1]

k_ls = [char for char in k]

k_ls.sort()

for i in range(1, (int(n) + 1)):
    for perm in combinations(k_ls, i):
        line = ''
        for item in perm:
            line += item
        print(line)
from itertools import combinations_with_replacement

inpt = input().split()
k = inpt[0]
n = inpt[1]

k_ls = [char for char in k]
k_ls.sort()

for perm in combinations_with_replacement(k_ls, int(n)):
    line = ''
    for item in perm:
        line += item
    print(line)
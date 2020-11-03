import itertools

A = map(int, input().split())
B = map(int, input().split())

ls = list(itertools.product(A, B))
for item in ls:
    print(item, end=' ')
    
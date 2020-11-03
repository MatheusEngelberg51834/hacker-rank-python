n = int(input())
N = set(list(map(int, input().split())))

m = int(input())
M = set(list(map(int, input().split())))

print(len(N.symmetric_difference(M)))
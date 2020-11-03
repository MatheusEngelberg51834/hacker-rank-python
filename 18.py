import collections

k = int(input())
rooms = list(map(int, input().split()))
n_r_item = [item for item, count in collections.Counter(rooms).items() if count == 1]

print(n_r_item[0])
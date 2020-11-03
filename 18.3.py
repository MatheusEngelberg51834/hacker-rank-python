k = int(input())

rooms = list(map(int, input().split()))

s = set(rooms)

for element in s:
    if rooms.count(element) == 1:
        print(element)
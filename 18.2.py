k = int(input())

rooms = list(map(int, input().split()))

numbers1 = []

numbers2 = []

for room in rooms:
    if room not in numbers1:
        numbers1.append(room)
        rooms.remove(room)

for room in rooms:
    if room not in numbers2:
        numbers2.append(room)

for num in numbers1:
    if num not in numbers2:
        print(num)

# for room in rooms:
#     if room in numbers:
#         numbers.remove(room)

#print(numbers[0])
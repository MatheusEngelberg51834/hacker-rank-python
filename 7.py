m = int(input())
M = [number for number in input().split()]

n = int(input())
N = [number for number in input().split()]

newM = list(map(int, M))
newN = list(map(int, N))

setM = set(newM)
setN = set(newN)

out = []

for res in setM.symmetric_difference(setN):
    out.append(res)

int_out = list(map(int, out))

int_out.sort()

for element in int_out:
    print(element)

#print(out.sort())

# for output in out.sort():
#     print(output)
import numpy

n = list(map(int, input().split()))

ls = []

for _ in range(n[0]):
    arr = list(map(int, input().split()))
    ls.append(arr)

array = numpy.array(ls)

print(numpy.prod(numpy.sum(array, axis=0)))
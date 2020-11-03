import numpy

inpt = list(map(int, input().split()))

ls = []

for _ in range(inpt[0]):
    ls.append(list(map(int, input().split())))

npls = numpy.array(ls)

mix = numpy.min(npls, axis=1)

print(numpy.max(mix, axis=0))


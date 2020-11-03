import numpy

inpt = list(map(int, input().split()))

ls = []
ls2 = []

for _ in range(inpt[0]):
    ls.append(list(map(int, input().split())))


# numpy.append(ls, list(map(int, input().split())), axis=0)

for _ in range(inpt[1]):
    ls2.append(list(map(int, input().split())))

#numpy.append(ls2, list(map(int, input().split())), axis=0)

npls = numpy.array(ls)
npls2 = numpy.array(ls2)

print(numpy.concatenate((npls, npls2), axis=0))
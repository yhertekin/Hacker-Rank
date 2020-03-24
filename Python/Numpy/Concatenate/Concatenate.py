import numpy

a, b, c = map(int,input().split())

array1 = numpy.array([(input().split()) for _ in range(a)], int)
array2 = numpy.array([input().split() for _ in range(b)], int)

print(numpy.concatenate((array1, array2), axis=0))

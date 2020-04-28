from timeit import timeit

def in_test(iterable):
    for i in range(1000):
        if i in iterable:
            pass

def timeFunc(iterable, number=1000):
    print(iterable, timeit("in_test(iterable)", setup="from __main__ import in_test; iterable = "+iterable,number=number))


timeFunc("set(range(1000))")
timeFunc("list(range(1000))")
timeFunc("tuple(range(1000))")
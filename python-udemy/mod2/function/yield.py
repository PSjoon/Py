def generator(n):
    print(n)
    yield 1
    print('continuando')
    yield 2

gen = generator(n=0)
print(next(gen))
print(next(gen)) 
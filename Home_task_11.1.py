from typing import Generator

def prime_generator(end: int) -> Generator[int, None, None]:
    for number in range(2, end +1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
        if prime:
            yield number



from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
def difference(*numbers: float) -> float:
    if not numbers:
        return 0
    minimum = min(numbers)
    maximum = max(numbers)
    summation = maximum - minimum
    return round(summation, 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

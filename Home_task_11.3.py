def is_even(number: int) -> bool:
    last_digit = int(str(number)[-1])
    if last_digit in (0, 2, 4, 6, 8):
        return True
    else: return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

def add_one(some_list):
    some_list_str = int("".join(str(number) for number in some_list))
    some_list_str += 1
    some_list_str = [int(number) for number in str(some_list_str)]
    return some_list_str



assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


def common_elements():
    first_list = []
    second_list = []
    for item in range(0,101):
        if item % 3 == 0:
            first_list.append(item)
        if item % 5 == 0:
            second_list.append(item)


    first_list = set(first_list)
    second_list = set(second_list)
    same_elements = first_list.intersection(second_list)
    return same_elements

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("ОК")



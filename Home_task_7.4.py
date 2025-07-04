

def common_elements():
    first_list = []
    second_list = []
    for item in range(100):
        first_list.append(item*3)
        second_list.append(item*5)

    first_list = set(first_list)
    second_list = set(second_list)
    same_elements = first_list.intersection(second_list)
    return same_elements

print(common_elements())





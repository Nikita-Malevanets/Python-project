my_list = [1,2,3,4,5,6,7,8,9]
part = (len(my_list)+1) // 2
first_element = my_list[:part]
second_element = my_list[part:]
new_list = [first_element, second_element]
print(new_list)
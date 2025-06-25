# my_list = [1,2,3,4,5,6,7,8,9]     # Перший варіант рішення Д.З.
# if len(my_list) == 0:
#     result = 0
# else:
#     new_list = my_list[::2]
#     sum_list = sum(new_list)
#     last_element = new_list[-1]
#     result = sum_list * last_element
#     print(result)


my_list = [1,2,3,4,5,6,7,8,9]   # Другий варіант рішення Д.З.
if len(my_list) == 0:
    result = 0
else:
    sum_list = 0
    for i in range(0, len(my_list), 2):
        sum_list += my_list[i]
    result = my_list[-1] * sum_list
print(result)



my_list = [1,2,0,3,4,0,5,6,7,0,8,9,-2]
new_list = []
for element in my_list:
    if element != 0:
        new_list.append(element)
zero_count = my_list.count(0)
for i in range(zero_count):
    new_list.append(0)
print(new_list)



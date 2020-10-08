my_list = [12, 4, 4, 2, 3, 2, 8, 10, 8, 25, 23,21,23,8]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)
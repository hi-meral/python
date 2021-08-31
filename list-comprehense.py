

h_letters = [letter for letter in 'human']
print(h_letters)


##########


num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)


##########


list1 = [[1, 2], [3, 4], [5, 6], [7, 8]]


list2 = [[row[i] for row in list1] for i in range(0, 2)]


print(list2)

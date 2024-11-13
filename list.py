# 1. create an empty list
my_list = []
print(f'my_list before appending values: {my_list}')

# 2. appending multiple elements to the list using for loop
elements = [10,20,30,40]
for element in  elements:
    my_list.append(element)
print(f'my_list after appending values: {my_list}')

# 3. insert value 15 in second position in the list
my_list.insert(1,15)
print(f'my_list when value 15 was inserted in the second position: {my_list}')

# 4.Extend my_list with another list: [50, 60, 70].
another_list = [50,60,70]
my_list.extend(another_list)
print(f'my_list when extended: {my_list}')

# 5.Remove the last element from my_list.
my_list.pop()
print(f'my_list when last element is removed: {my_list}')

# 6.Sort my_list in ascending order.
my_list.sort()
print(f'my_list after sorted in ascending order: {my_list}')

# 7.Find and print the index of the value 30 in my_list.
print(f'Index of value 30 in my_list is: {my_list.index(30)}')

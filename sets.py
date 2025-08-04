#Sets
'''
my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)  # Adding an element
print(my_set)

my_set.remove(2)  # Removing an element
print(my_set)
'''
set1 = {1, 2, 3}
set2 = {3, 4, 6}
# Union of two sets
set_union = set1.union(set2)
print(set_union)

# Intersection of two sets
set_intersection = set1.intersection(set2)
print(set_intersection)

# Difference of two sets
set_difference = set1.difference(set2)  
print(set_difference)

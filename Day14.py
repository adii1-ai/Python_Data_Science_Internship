# Set

# -Set is a collection of similar type or different type oof element
# -Set is unordered collection of data
# -There is no indexing or position in set
# -Set is Mutable
# -Data is Stored inside {}
# -No duplicate values allowed in Set, When we add any duplicate it automatically removes it
# -Used to perform mathematical operation like union/intersection and difference
# It does not maintain order

sets={"onkar","Aditya","nishant","om","snehit","nishant"}
print(type(sets))  # set
print(sets)

# creating empty set
tup = ()
print(type(tup))

tup1 = tuple()
print(type(tup1))



set_1 = {}  # Creates a empty Dictionary
set_2 = ()  # creates empty Tuple
set_3 = set()  # creates empty set
print(type(set_1))
print(type(set_2))
print(type(set_3))

# =============================================

# union - It returns the combination of both the sets
# intersection - it returns a common elements from both sets
# Difference - Elements of a which is not present in b 

movie_1 = {"Dhurandar","Saiyarra","Dhadak 2","Marco","Pushpa 2","KGF"}
movie_2 = {"Zindagi Na Milegi Dobara", "Mission Impossible","Saiyarra",}

print(movie_1)
print(movie_2)


# union()

print(movie_1.union(movie_2))

# intersection()

print(movie_1.intersection(movie_2))

# differennce()

print(movie_1.difference(movie_2))

# Symmetric Difference

a = {1,2,5,8,3}
b = {8, 9, 10,1,3}
print(a ^ b)
# or
print(a.symmetric_difference(b))

# =====================================

# pop()
# add()
# update()

# pop()
# -removes the random element from set

emp_3= {"Partiksha","Payal","shrushti","OM","Esha"}
print(emp_3)
emp_3.pop()
print(emp_3)

# - removing particular element
emp_3.remove("Esha")
print(emp_3)

# add()
# -Add single element if not exists in set

emp = {"Partiksha","Payal","shrushti","OM"}
print(emp)
emp.add("Esha")
print(emp)

# update()
# -add multiple elemnt

emp_1 = {"Partiksha","Payal","Kajal","shrushti","OM"}
print(emp_1)
emp_1.update(["Kavya", "Divya","Nova"])
print(emp_1)


# ========================================

# discard()
# -It is used to remove the specific element from the set
# -If elemet is not present then it will not raise an error.

emp_1.discard("Divya")
print(emp_1)

# ========================================

# copy()
# - copy() method is used to make Shallow copy of of a data
# - copy() method creates an independent copy od a set

x = {1,2,3,4}
y = x.copy()

y.update(["A", "B","C"])
print(y)  # Shallow copy does not able to make changes in both the sets
print(x)

# ===========================================

# frozenset
 
# - frozenset is  immutable 
# - frozenset is a set that cannot be changed like tuple
# - frozenset([])

numbers = frozenset([1,2,3,4,5,6])
print(numbers)

# numbers.add(10) # Gives error because frozenset is Immutable

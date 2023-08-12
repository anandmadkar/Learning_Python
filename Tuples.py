# Creating a Tuple using ()

# Note : Tuple is immutable data type in python (immutable means it can't be change)

t = (1, 22, 10, 11, 25, 6)

t1 = ()               # this is empty tuple 

t1 = (1)              # this is wrong way to declare a tuple with single element.

print(t1)

t1 = (1,)             # this is a right way to declare a tuple with single element means you have always a comma for single element.


print(t1)

# To print the one element from tuple 

print(t[2])     # 2nd index will get print.

# Cannot update the values of a tuple.

t[0] = 5       # it will throw an error.
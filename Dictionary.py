# Dictionary is a collection of Key : Value Pairs

# It is mentioned in { } curly brackets.

# Example : 
# {
#     "Name"   : "Anand",     --Key : Value 
#     "Gender" : "Male",      --Key : Value 
#     "Age"    : "25"         --Key : Value 
#   }

# ----------------------------------------------------------------------

# Example 1 -

# myfirstdict = {
#     "Fast" : "In a quick Manner",
#     "Anand" : "Software Engineer"
# }

# print(myfirstdict["Fast"])   
# print(myfirstdict["Anand"])   

# # ---------------------------------------------------------------------

# # Example 2 - Nested Dictionary
# # In this there is dictionary inside dictionary is created.
# # And, also we have used integer numbers in the form of list.

mySeconddict = {
    "Book" : "The Secret",
    "Author" : "Anand",
    "Marks" : [1, 2, 3],
    "anotherdict" : { "Overview" :"This is dictionary inside dictionary"}
      }

print(mySeconddict["Book"])
print(mySeconddict["Author"])
print(mySeconddict["Marks"])
print(mySeconddict["anotherdict"]["Overview"])

# ------------------------------------------------------------------------------
# Example 3 - To print only keys

mySeconddict = {
    "Book" : "The Secret",
    "Author" : "Anand",
    "Marks" : [1, 2, 3],
    "anotherdict" : { "Overview" :"This is dictionary inside dictionary"},
    1 : 2
      }
 
print(mySeconddict.keys())  # To print the keys.

print(mySeconddict.values()) # To print the values.

print(mySeconddict.items())  # To print the keys and values in {key : Value} pair

print(list([mySeconddict.keys()]))  # To print the keys in the list format

print(type(mySeconddict.keys()))   # To see the class type.



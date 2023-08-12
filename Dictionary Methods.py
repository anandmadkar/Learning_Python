

# Example -----------------------------

mySeconddict = {
    "Book" : "The Secret",
    "Author" : "Anand",
    "Marks" : [1, 2, 3],
    "anotherdict" : { "Overview" :"This is dictionary inside dictionary"},
    1 : 2
      }
 

#-----------------------------------------------   DICTIONARY METHODS ---------------------------------


print(mySeconddict.keys())  # To print the keys.

print(mySeconddict.values()) # To print the values.

print(mySeconddict.items())  # To print the keys and values in {key : Value} pair

print(list([mySeconddict.keys()]))  # To print the keys in the list format

print(type(mySeconddict.keys()))   # To see the class type.

#  To update the dictionary with new key and values in the existing.

Updatedict = {
    "Author" : "Omkar",
    "Book" : "Blue Moon"
}
mySeconddict.update(Updatedict)    # To update dictionary with key : Values pair
print(mySeconddict)

print(mySeconddict.get("Author"))  # To get the exact and direct value of particular key from the dictionary.
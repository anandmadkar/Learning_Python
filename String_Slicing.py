# String Slicing give a small part from string

name = "AnandBhaskarMadkar"

slice = name[3 : 25 : 6]     # this is [Index : Total Length of String : Skipvalue]

slice = name[1 : 3]   # This is [Index : Skipvalue]

slice = name[ : 3]  # Blank index will consider as 0.

slice = name[1 : ]  # Blank skipvalue will consider till last letter of string.

print(slice)







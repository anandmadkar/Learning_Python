# Types of Loops in Python ---
#         While Loop
#         For Loop

# While Loop - 
# The block of this loop keeps executing until the condition is true.
#        *Note -(If condition is not true it will go infinite)

# For Loop - 
# This is used to iterate through a sequence like a list, tuple or string in iteration manner.

# --------------------------------------------------------------------------------------------------------------------------------------------
    
# Examples 1  - While Loop 

i = 1

while i<11 :
    
  print(i)
  i = i + 1

  print("Done") 
# ---------------------------------------------------------------------------------------------------------------------------------------
#  Example 2 -

Fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']

i = 1

while i < len(Fruits) :
  print(Fruits[i])
  i = i + 1
# ---------------------------------------------------------------------------------------------------------------------------------------
 
# Examples - For Loop

# Example 1 - Using Item

Fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']

for item in Fruits :
    print(item)

# --------------------------------------------------------

# Example 2 - Using Range

for i in range(8) :
    print(i)

# Similarly,

for i in range(1, 26) :
    print(i)


# --------------------------------------------------------------------------------------------------------------------------------------
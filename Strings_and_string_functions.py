# # -------------------------------Ways of Writing a Strings----------------------------------------------

# A = "Anand " 
     
# a = 'Anand'

# a = "Anand's"

# a = "Anand's"

# a = '''Anand'''

# C = ' Hi my Name is Anand'

# # print(type(a))  #Data type of 'a'

# # print(a)


# # Concatenation of Strings 

# d = a + C

# print(d)

# # Different Way

# name = "Anand"

# Company = " Infosys"

# Technology = " Developer"

# Complete_details = name + Company + Technology

# print(Complete_details)


#------------------------------------------------String Functions------------------------------------------------------------------

Story = "i am learning Python with Harry dedicatedly and passionately with full focus"

# --------------To calculate length of a string-------------------------

print(len(Story))



# --------------To see the string ends with in (true or false)-------------------

print(Story.endswith("focus"))



# ----------------To count the letters in the strings-----------------------------

print(Story.count('a'))



# ----------------To count the words in the strings------------------------------

print(Story.count('with'))




# ----------------To capitalize the first letter of first word in the strings------------------------------

print(Story.capitalize())




# ----------------To find the words in the strings------------------------------

print(Story.find('learning'))  # it calculates like letter and trailing spaces



# ----------------To replace words in the strings------------------------------

print(Story.replace('learning','Studying')) 






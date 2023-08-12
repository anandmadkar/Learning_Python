# If and else conditions in python............

# Syntax - 
        #                   if(condition 1) : 
        #                           print("Yes")
        #                   elif(condition 2) :
        #                           print("No")
        #                   else
        #                           print("Maybe")


# Example 1 :- 
# if-elif-else ladder in python --
a = 22
if (a>30) :
    print("Yes it is greater than 30"),
elif(a>40) :
    print("No, it is greater than 40"),
elif(a>35):
    print("No, it is not greater than 35")
elif(a>21) :
    print("Yes it is greater than 21")
else:
    print("Not Sure")

# ---------------------------------------------------------------------------------------------------------------------------------------------------

#   Muliple if Statements --

a = 22
if (a>30) :
    print("Yes it is greater than 30"),

if(a>40) :
    print("yes it is greater than 40"),

if(a>23):
    print("Yes, it is greater than 23"),

if(a>35) :
    print("Yes, it is greater than 35"),
else:
    print("No, It is not greater than 35 or 40")

# ----------------------------------------------------------------------------------------------------------------------------------

# Examples based on Relational Opeartors 

# Using >=, >, <= 

age = int(input("Enter your age\n"))

if age>18 or age>=18 :
    print("You are eligible for driving license")
else :
    print("You are not eligible for license")


# Examples based on Logical Opeartors 

# Example 1 : Using AND

age = int(input("Enter your age\n"))
age = 20

if age>18 and age<21 :
    print("You are eligible for Interview")
else :
    print("You are not eligible for Interview")


# Example 2 : Using OR
age = 20
if (age > 18) or (age >= 18) :
    print("You are eligible for driving license")
else :
    print("You are not eligible for license")

# Example 3 : Using IN

a = [10, 20, 30]
print(20 in a)      

# Example 4 : Using IS

a = None
if (a == None) :
    print ("Yes a is None")   
else :
    print("No")        

# -------------------------------------------------------------------------------------------------------------------------------------

#  Example from Practice Set

text = input("Enter the text\n")

if ("make a lot of money" in text):
    spam = True
elif ("Buy now" in text):
    spam = True

elif ("Click this" in text):
    spam = True

elif ("Subscribe this" in text):
    spam = True

else :
    spam = False

if (spam) :
    print("This text is Spam")
else :
    print("This text is not spam")


# -------------------------------------------------------------------------------------------------------------------------------------------

marks = int(input("Enter the marks\n"))

if (marks>=90 and marks<=100) :           
    print("Grade is Ex")
elif (marks>=80 and marks<=90) :           
    print("Grade is A")
elif (marks>=70 and marks<=80) :           
    print("Grade is B")
elif (marks>=60 and marks<=70) :           
    print("Grade is C")
elif (marks>=50 and marks<=60) :           
    print("Grade is D")
else :
    print("Grade is F")



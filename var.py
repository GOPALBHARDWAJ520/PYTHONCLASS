
#type function

# a= True
# print(type(a))
# a=None
# print(type(a))
# a=10
# type(a)

# #input fun used for user input

# a=10
# print(a)

# # input function

# a=input("enter the no ")
# print(a)
# print(type(a))

# type casting

#int to str

# a=245
# a=str(a)
# print(a)
# print(type(a))


# type castig from str to int valid only if str is in whole numbers

# str to int

# a="4589"
# a=int(a)
# print(a)
# print(type(a))

# float to int

# a=19.5
# a=int(a)
# print(a)
# print(type(a))

# 1 ArithmeticError

# a=int(input("enter a:"))
# b=int(input("enter b:"))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a)
# print(b)


# area of circle

# pi=3.14
# a=int(input("enter a"))
# print(pi*a**2)

# import module maths
#eliyas name of maths is a

# import math as a
# r=int(input("enter the number:"))
# print(a.pi*r**2)

# 2 assignment operator

# a=10
# a+=10 # a= a+10
# print(a)

# 3 comparison operator / relational operator
# ==, <, > , <=, >=

# a=int(input("enter value of a :"))
# b=int(input("enter value of b :"))
# print(a==b)
# print(a>b)
# print(a<b)
# print(a<=b)
# print(a>=b)

# logical operator
# and ,not

#######and######
# t and t = t
# t and f = t
# f and f = f

# a=10
# b=20
# print(a<b and b==a)
# print(a<b and b>a)
# print(a==b and b<a)


# a=int(input("enter the value of a :"))
# print(not(a<18))

#membership---
# in notin
# a='ravi'
# print('r' in a)
# print('r' not in a)

# identity
# a=10
# print(10 in a)
# print(10 not in a)

#condation

# age=int(input("enter your age:"))
# if age >=18:
#     print("elegible for vote")
# else:
#     print("not")




# year = int(input("Enter a year: "))

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


# #Calculate the total bill amount if a meal costs $45 and you want to leave a 15% tip. Use multiplication and addition.#
# """MEAL=45
# TIP =MEAL*0.15
# TOTAL= MEAL+TIP
# print(TOTAL)"""

# You have a total of 345 minutes. Convert this into full hours and remaining minutes using floor division (//) and modulo (%).
# keywords
# print(help("keywords"))




# a=int(input("enter a number a:"))
# b=int(input("enter a number b:"))
# c=int(input("enter a number c:"))

# if a>b:
    
# Check whether a number is greater than 50.
# Check whether two numbers are equal.
# Check whether two numbers are different.
# Check whether a number is greater than or equal to 18.
# Find the greater of two numbers.
# Find the smaller of two numbers.
# Check whether marks are greater than or equal to 40.
# Check whether a number is between 10 and 100.
# Check whether two strings are equal.
# Check whether a number is not equal to 0.


# a=int(input("Enter the number:"))
# c=a
# b=0
# while a>0:
#     last=a%10
#     b=last+b*10
#     a//=10
# print(b)
# if c==b:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# a=input("Enter the string:")
# b=a[::-1]
# if a==b:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# a="ravi kumar"
# print(a[9:3:-1])
# a=int(input("enter the year"))
# if a%4==0 or a%400==0:
#     print('leap year')
# else:
#     print('not')

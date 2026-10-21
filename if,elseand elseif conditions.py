
# if condition :
#    stm    

# age  = 18 
# if age >= 18:
#   print("you are eligible to vote ")


# value  =  44
# 
# if value % 2  == 0:
#     print("Even Number ")
# else :
#     print("Odd Number ")    


# marks   = 90
# 
# if marks >= 90:
#     print("Grade :  A")
# elif marks >= 75:
#     print("Grade :  B") 
# elif marks >= 50:
#     print("Grade : C")
# else:
#     print("Grade :   F")           

# num  =  0

# age  =  45
# if age < 12:
#     ticket_price = 8
# elif age >= 65:
#    ticket_price = 10
# else:
#    ticket_price = 15
# print("Ticket Price :  ", ticket_price)

# user_role = "Editor"
# is_logged_in =  False
# 
# if not is_logged_in:
#     print("please login first")
# elif user_role == "Admin":
#     print("Full Access ")
# elif user_role == "Editor":
#     print("Edit Access")
# elif user_role == "viewrs":
#     print("Read-Only") 
# else:
#      print("Access Denied")               


# num  = 15
# if  num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num %3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)      


# num   =  0
# if num >=  0:
#     print("the number is positive ")    
#     if num == 0:
#              print("the number is zero ")     
# 
# else:
#     print("the number is negative ")    
# 
# Questions 1 :   School Attendance & Exam
# Scenario: A student wants to give their final exam. First, check if their attendance is 75% or higher. If it is, then check if they have paid their exam fees.
# 
# Variables to create: attendance_percentage (number) and fees_paid (boolean True/False).
# 
# Task: Write a nested if-else to print if they can sit for the exam.

# attendance  = 75
# fees_paid  = False
# 
# if attendance >= 75:
#     print("attendance is good")
#     if fees_paid == True:
#         print("You can sit")
#     else:
#         print("you cannot sit ")
# 
# else:
#     print("attendance is too low")    

# is_logged_in = True
# cart_items = 5
# 
# if is_logged_in == True:
#     print("Welcome Back ")
#     if cart_items > 0:
#       print("proceeding to checkout with your items")
#     else:
#        print("your cart is empty")
# else:
#     print("Please login first ")    


# year  = 1600
# 
# if  year  % 4  ==  0:
#     if year % 100  == 0:
#         if year % 400 == 0:
#            print(year , "is a Leap year ")
#         else :
#             print( year  ,  "is not a leap year ")    
#     else:
#         print(year , "is a leap year ")
# else:
#     print( year  ,  "is not a leap year ")    
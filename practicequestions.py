#Question attendance and fees program

# attendance = 75
# fees_paid = True
# if attendance >= 75:
#     print("attendance is good")
#     if fees_paid == True:
#       print("you can sit")
#     else:
#          print("you can not sit")
# else:
#    print("attandance is low")





#Question a kid wants to ride a rollercaster. The kid must be at least 12 years old and if they are older enough , they must also be taller than 120cm 
#task print weather they are allowes on the ride based on these two rues

# kid_age = int(input("Enter the age of the kid: "))
# kid_height = int(input("Enter the height of the kid in meters: "))
# if kid_age >= 12:
#     if kid_height > 1.2:
#         print("The kid is allowed on the ride.")
#     else:
#         print("The kid is not allowed on the ride due to height restriction.")


#Question a person at atm , first , atm checks if there atm card is valid(not expired) if the card is valid if check if there account balance is greater than or 
# equal to amount they want to withdrawl

# atm_card_valid = True  # Assume the ATM card is valid
# account_balance = float(input("Enter the account balance: "))
# withdrawal_amount = float(input("Enter the amount to withdraw: "))
# if atm_card_valid:
#     if account_balance >= withdrawal_amount:
#         print("Withdrawal approved.")
#     else:
#         print("Insufficient funds.")
# else:
#     print("Invalid ATM card.")



#Question leap year program

# a=int(input("enter the year:"))
# if a%4==0:
#     if a%100==0:
#         if a%400==0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print(a,"is not a leap year")




#Question make calculator

# if True:
#     num1 = float (input("Enter first number: "))
#     operator = input("Enter operator (+, -, *, /): ")
#     num2 = float(input("Enter second number: "))

#     if operator == "+":
#         a=num1 + num2
#         print("The result is: a",a)
#     elif operator == "-":
#          b=num1 - num2
#          print("The result is: b",b)
#     elif operator == "*":
#         c=num1 * num2
#         print("The result is: num1 * num2",c)
#     elif operator == "/":
#         if num2 != 0:
#             d=num1 / num2
#             print(f"The result is: num1 / num2",d)
#         else:
#             print("Error: Division by zero is not allowed.")
#     else:
#         print("Invalid operator. Please use +, -, *, or /.")
# else:
#     print("Calculator is not active.")


# Question1  = Quiz
# The game asks a question. If you give the wrong answer (else), you lose immediately.
#  If you give the correct answer (if), you unlock the next level and the game asks you Question 2 (nested if).

# question= "what is your name?"
# print(question)
# answer = input("Enter your answer:")
# if answer == "Gopal Bhardwaj":
#     print("you unlock the next level")
#     question2 = "what is your age?:"
#     print(question2)
#     answer2 = input("Enter your answer:")
#     if answer2 == "20":
#         print("you win the game")
#     else:
#         print("you lose")
# else:
#     print("you lose ")



# Question2  = The Monster Fight
# A monster appears! You have 3 weapons: Sword, Bow, or Magic (if-elif). Each does different damage. 
# But there is a catch: to use Magic, the game must first check if you have enough energy/mana (nested if).

# wepon = input("Choose your weapon (Sword, Bow, Magic): ")
# if wepon == "Sword":
#     print("You swing your sword and deal 50 damage!")
# elif wepon == "bow":
#     print("You shoot an arrow and deal 30 damage!")
# elif wepon == "Magic":
#     print("You cast a spell and deal 70 damage!")
# else:
#     print("Invalid weapon choice. You lose your turn!")




#Question find if  number is positive or negative

# num=int(input("enter the number:"))
# if num>0:
#     print("number is positive")
#     if num == 0:
#         print("the number is zero")
# else:
#  print("the number is negative")



#Question attandance and fees program

# attandance=int(input("enter your attandance:"))
# fees_paid=bool(input("enter weather fees paid or not(true or false):"))
# if attandance >= 75:
#    print("attandance is good")
#    if fees_paid:
#       print("you can sit in the exam")
#    else:
#       print("you can not sit in exam")
# else:
#    print("your attandance is low")
    


#Question Calculate the total bill amount if a meal costs $45 and you want to leave a 15% tip. Use multiplication and addition.


#Question You have a total of 345 minutes. Convert this into full hours and remaining minutes using floor division (//) and modulo (%)

# total_minutes= 345
# hours=total_minutes//60
# minutes=total_minutes%60
# print(hours,"hours and",minutes,"minutes")


#Question Write a condition that triggers an alert True if a server's temperature is outside the safe operating range of 15°C to 25°C.


# temprature = 30
# if temprature<15 or temprature>25:
#     alert=True
# else:
#     alert=False
# print("alert is :",alert)


#Question A customer gets a discount if they are a student OR if they are 65 or older. 
# They must NOT be a premium member (premium members have a separate system).

# customer= input("enter customer type: ")
# age= int(input("enter your age:"))
# premium = input("Are you a premium member? (yes/no): ")

# if (customer=="student" or age>=65) and premium=="no":
#     print("you are eligible for discount")
# else:
#     print("not eligible")



#Question Calculate the volume of a cube with a side length of 7 using the exponentiation operator (**).

# cudeside= float(input("side of cube : "))
# volume=cudeside**3
# print("volume of cube is : ", volume)

#Question Use the + operator to join "Warning!" and " ", then use the * operator to repeat that combined string 3 times.


# message = "Warning!" + " "
# print(message * 3)

#Question Evaluate the expression 5 + 4 * 3 ** 2 / 2 - 1 without running it first, then write the code to check your mental math.




# Question 1  - Calculate a ticket price based on age. Children under 12 pay $8, seniors 65 and older pay $10, and everyone else pays $15.

# Question2 -  Assign dashboard permissions based on a user's role. Admins get full access, editors can modify content, and viewers can only read.

# Question 3  - Traffic Light Logic
# Determine a driver's action based on the color of a traffic light. Include a fallback else to catch invalid inputs.

# Question 4 -  FizzBuzz (The Classic Interview Question)
# For a given number, print "Fizz" if it is divisible by 3, "Buzz" if divisible by 5, and "FizzBuzz" if divisible by both 3 and 5. Otherwise, print the number.

# Question5  - Shipping Cost Calculator
# Calculate delivery charges based on the weight of a package. Under 5kg costs $5, between 5kg and 20kg costs $10, and anything over 20kg costs $20.

# Question6 - BMI (Body Mass Index) Category
# Print a health category based on a person's BMI number.

# Question7 - Shopping Discount System
# Give a customer a discount based on how much they spend. $1000 or more gets a 20% discount, $500 or more gets 10%, and under $500 gets 0%

# Question8- Speeding Ticket Checker
# Check a driver's speed to determine their fine. Speed limit is 60.



# num=int(input("enter the number"))
# if num=0
#   print("the number is zero")
# if num>= 0
#   print("the number is positive")
# else:
#   if num<=0
# print("the number is negative")

# attendance = 75
# pees_paid = True
# if attandance >= 75:
#    print("attendance is good")
#    if fees_paid = true:
#       print("you can sit")
#       else:
#          print("you can not sit")
# else:
#    print("attandance is low")



# """
# num=int(input("enter the no :"))
# if num%2==0:
#     if num%3==0:
#      if num%4==0:
#         print("num div 2,3,4")
#      else:
#         print("div 2,3")
#     else:
#        print("only 2")
# else:
#    print("not")


# num=int(input("enter the no :"))
# if num%2==0:
#     if num%3==0:
#      if num%4==0:
#         print("num div 2,3,4")
#      else:
#         print("div 2,3")
#     else:
#        print("only 2")
# else:
#   if num%3==0:
#      print("div 3")
#     else:
#      print("not")
# """

# """
# a=int(input("a:"))
# b=int(input("b:"))
# c=int(input("c:"))
# if a>b:
#    if a>c:
#       print("a is greatest")
#    else:
#       print("c is greatest")
# else: 
#   if b>c:
#       print("b is greatest")
#   else:
#      print("c is greatest")
# """
# """
# a=int(input("a:"))
# b=int(input("b:"))
# c=int(input("c:"))

# if a>=80:
#    if b>=80:
#       if c >=80:
#           print("pass")
#       else:
#         print("pass only in hindi and maths")
#    else:
#       print("fail")
# else:
#    print("failby")
# """


# import random

# print("Welcome to Rock , paper , Scissors")

# options  =  ["rock", "paper", "scissors"]

# while True:
#     print("Options  :  rock , paper , scissors ,  (Type 'Quit' to exit)")
#     user_choice  =  input("Enter your value ")

#     if user_choice == "quit":
#         print("Game over ") 
#         break

#     if user_choice not in options:
#         print("Wrong spelling , please check ")  
#         continue

#     computer_choice  =  random.choice(options)
#     print('computer choice  :  ' ,  computer_choice)

#     if user_choice  == computer_choice:
#         print("Tie")

#     elif user_choice == "rock" and computer_choice == "scissors":
#         print(" user win")

#     elif user_choice == "paper" and computer_choice == "rock":
#             print(" user win")   
#     elif user_choice == "scissors" and computer_choice == "paper":
#                 print(" user win")    
#     else:
#           print("Computer Win ")                 


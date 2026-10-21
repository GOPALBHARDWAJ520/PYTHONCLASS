# num1  =  [1,2,1,3,1,4,5,1]

# print(num1.count(1))

# num1.index(2)
# print(num1.index(2))
# num1.append(10)
# print(num1)
# num2 = [6,7,8,9,10]
# num3  =  [3,12,15,8,9,1]
# num3.sort()
# print(num3)
# num1.extend(num2)
# print(num1[3])
# num1.remove(3)

# num1.pop(2)
# num1.clear()

# nums.insert(3,"Python")
# nums.append(6)
# print(num1)



# listValue  =  ["n1" ,  "n2" ,  "n3" ,  "n4" ,  "n5" ,  "n6" ,  "n7" ,  "n8" ,  "n9" ,  "n10"]

# listValue[start:end]
# listValue[start:end : step]

# print(listValue[0:6:2])

# print(listValue[::-1])

# print(listValue[1:4])
# print(listValue[1:])
# print(listValue[:4])
# print(listValue[:])

# listValue[1] = "Python"
# print(listValue)
# for i in listValue:
#     print(i)

# 
# for i in range(len(listValue)):
#     print(i ,  " : ",listValue[i])

#append method in list

# num=[1,2,3,4,5,6,7,8,9,10]
# num.append(11)
# print(num)

# extend method in list

# num1=[1,2,3,4,5]
# num2=[6,7,8,9,10]
# num1.extend(num2)
# print(num1)

# num1  =  [1,2,3,4,5]
# num1.append(10)
# print(num1)
# num2 = [6,7,8,9,10]
# num3  =  [3,12,15,8,9,1]
# num3.sort()
# print(num3)
# num1.extend(num2)
# print(num1[3])
# num1.remove(3)

# num1.pop(2)
# num1.clear()

# nums.insert(3,"Python")
# nums.append(6)
# print(num1)

# num1= [1,5,2,2,2,5,4,7,6]
# print(num1.count(2))

# name= input("Enter your name: ")
# print("Hello " + name + " Welcome to our cafe")
# print("Please select your order from the menu below: coffess(50), tea(30), cold drinks(40), snacks(60)")
# choice= input("what would you like to order? ")
# if choice=="coffess":
#     print("Your order is coffess and the price is 50")
# elif choice=="tea":
#     print("Your order is tea and the price is 30")
# elif choice=="cold drinks":
#     print("Your order is cold drinks and the price is 40")
# else:
#     print("sorry we don't have that item in our menu")


# choice  =  input("what would you like to order? : ")
# if choice == "Coffee":
#    price  = 50
# elif choice == "Tea":
#    price = 10
# elif choice == "Cold Coffee":
#    price = 30
# elif choice == "Cold Drink":
#    price = 40
# elif choice == "Milkshake":
#    price = 12
# else:
#     print("Sorry, we don't have that item on the menu.")    
#     price = 0
# if price > 0 :
#     quantity  =  int(input("How many would you like to order? : "))
#     total_price  =  price * quantity
#     print("Your total bill is: $" + str(total_price))
# while True:
#     choice  =  input("Do you want to order again? (y/n): ")
#     if choice == "y":
#         print("Please select your order from the menu below: Coffee(50), Tea(10), Cold Coffee(30), Cold Drink(40), Milkshake(12)")
#         choice  =  input("What would you like to order? : ")
#         if choice == "Coffee":
#             price  = 50
#         elif choice == "Tea":
#             price = 10
#         elif choice == "Cold Coffee":
#             price = 30
#         elif choice == "Cold Drink":
#             price = 40
#         elif choice == "Milkshake":
#             price = 12
#         else:
#             print("Sorry, we don't have that item on the menu.")
#             price = 0

#         if price > 0 :
#             quantity  =  int(input("How many would you like to order? : "))
#             total_price  =  price * quantity
#             print("Your total bill is: $" + str(total_price))
#     elif choice == "n":
#         print("Thank you for visiting our cafe. Have a great day!")
#         break
#     else:
#         print("Invalid input. Please enter 'y' or 'n'.")

#remove form list

# x=[1,2,3,1,4,3,4,5,6,7,8,1,9,10]
# pop_value=x.pop(0)
# print(pop_value)
# print(x)


# x=[1,2,3,1,4,3,4,5,6,7,8,1,9,10,1,1,1,1,1,1,1,1,1,1,]
# for i in range(x.count(1)):
#     x.remove(1)
# print(x)


# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# x=[1,2,3,4,5,6,7,8,9,10]
# target= 10
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i]+x[j]==target:
#             print(i,j)



# a =  [12,34,56,89,45,34]
# import random

# a =  random.randint(1,7)
# print(a)



# listValue  =  ["a","b","c","d","e"]
# print(listValue)
# randomValue  =  random.choice(listValue)
# print(randomValue)

# listValue  =  ["a","b","c","d","e"]
# print(listValue)
# 
# random.shuffle(listValue)
# print(listValue)
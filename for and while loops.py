# for loop ( for finite loop)

# from 1 to 100 counting
# start = 1
# end = 101 (n-1)

# for i in range(1, 101):
#     print(i)

# even numbers from 2 to 20

# for i in range(2,21,2):
#     print(i)




#while loop (for infinite loop)

#loop from 40 to 100

# i=40
# while i<=100:
#     print(i)
#     i=i+1



# for horizontal printing

# for i in range(11):
#     print(i,end=" ")

# i=1
# while i<=100:
#     print(i,end=" ")
#     i=i+1


# name="PYTHON"
# for i in name:
#     print(i)


# sum 0 to 20 
# sum=0
# for i in range(21):
#     sum=sum+i
# print("Sum of 0 to 20 is:",sum)

#fectorial of 5

# fact=1
# num=5
# for i in range(1,num+1):
#     fact=fact*i
#     print(fact)

# PRINT VOWEL COUNT IN A STRING
# word="GOPAL BHARDWAJ"
# vowel_count=0
# for i in word:
#     if i in "AEIOUaeiou":
#         vowel_count=vowel_count+1
# print(vowel_count)


# while True:
#     p=input("do you want to run a programm(y/n): ")
#     if p=="y":
#         print("program is running")
#         print( "your task is completed")

#     elif p=="n":
#         print("program is shutdown")
#         break
#     else:
#         print("invalid input")
# print("program is stopped")




#-----------LOOPS QUESTIONS-----------------


#primary number check 
# checking if a given number is prime or not
#(DEVIDE BY ONLY 1 ITSELF) USING BREAK STATEMENT

# num=int(input("Enter a number: "))
# if num>=1:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"is not a prime number")
#             break
#     else:
#         print(num,"is a prime number")

# the even number jumper (using step)
# print all even numbers from 2 to 20 by using a loop or step value of 2 in the range function.

# for i in range(2,21,2):
#     print(i)
#     i=i+1

# remove space from all strings using for loop
# name="  GOPAL  BHARDWAJ  "
# for i in name:
#     if i!=" ":
#         print(i,end=" ")


#list values using for loop

# listvalues=[1,2,3,4,5,6,7,8,9,10]
# for i in listvalues:
#     print(i , end=" ")


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

# num  =  11
# is_prime =  True 
# 
# for i in  range(2,num):
#    if num % i == 0:
#     is_prime = False 
#     break
# 
# if is_prime:
#   print(num , "is a Prime Number ")
# else:
#   print(num , "is not a Prime Number" )  

# row  =  7
# 
# for i in range(1 , row + 1):
#     print(i* "*")

# name  =  "PYTHON"
# reversed_name  =  ""
# 
# for i in name:
#     reversed_name =  i + reversed_name
# print(reversed_name) 
# 
# table  =  15
# for i in range(1 , 11):
#      print( table , " * " , i , " = " ,i * table)

# 3 * 1 = 3
# 3 * 2  = 6
#  "P"+"" =  "p"
# "Y"+"P" =  "yp"
# "t"+"yp" =  "typ"
# "h"+"typ" = "htyp"
# "o"+"htyp" =  "ohtyp"
# "n"+ "ohtyp" =  "nohtyp"
#  output  =  "nohtyp"

    # nohtyp

# a = 0
# b  = 1
# for i in range(10):
#   print(a , end=" ")
#   next_value  = a + b
#   a = b
#   b= next_value



# a     b    = next_value
# 0     1    = 1
# 1     1    = 2
# 1     2    = 3

# total_sum = 0
# for i in  range(1 , 6):
#     square  =  i * i
#     total_sum = total_sum + square
#     # total_sum =+square
#     print(i , " :  " ,square)
# print(total_sum)    


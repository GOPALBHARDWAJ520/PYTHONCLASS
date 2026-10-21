

# def fun(a+b)
#   sum=a+b
# return sum
# print(fun(2,3))




#  def notify_user():
#     print("your order is ready")

# def order_user():
#     print("your order is placed")
#     print("your order in process")
#     notify_user()
# order_user()



# def notify_user():
#     print("your order is ready")

# def order_user(collingfunctiom):
#     print("your order is placed")
#     print("your order in process")
#     collingfunctiom()
# order_user(notify_user)


# def notify_user():
#    a= "your order is ready"
#    return a

# def order_user(collingfunctiom):
#    result=collingfunctiom()
#    return result

# def fun():
#     a=["candy1", "candy2", "candy3"]
#     return a
# output=fun()
# print(output)




# def fun():
#     yield "candy1"
#     yield "candy2"
#     yield "candy3"
# ouutput=fun()
# print(next(ouutput))


#calculator program using function
# def sum(a,b):
#     s=a+b
#     return s
# def sub(a,b):
#     su=a-b
#     return su
# def mul(a,b):
#     m=a*b
#     return m
# def div(a,b):
#     d=a/b
#     return d
# def calculator(a,b,fun):
#     output=fun(a,b)
#     print("output:", output)
# calculator(10,5,sum)


# def enter():
#     a= "welcome to our store"
#     return a
# def exit():
#     b="thanks for shoping with us"
#     return b

# def store(fun):
#     result=fun()
#     return result

# store(enter)
# store(exit)


# def delivery_boy():
#     return "food delivered sucessfully"

# def restaurant(calback):
#     print(" order in process")
#     print("order is ready to deliver")
#     status=calback()
#     return status
# order=restaurant(delivery_boy)
# print(order)

# a =  7
# b =  5 
# c  = a + b
# print(c)
# 
# a1 =  5
# b1  = 10
# c1  = a1+b1
# print(c1)

# def fun():
#     print("Hello function ")

# fun()


# def greetFunction(name):
#     print("Hello " ,  name)
# 
# 
# greetFunction("Ganesh Dutt")     

# def sum(a , b):
#     total  =  a + b
#     print(total)

# sum(12, 45)  
# sum(90,7)  

# def multiply(a,b):
#     answer  =  a * b
#     return "Hello "
# 
# output  =   multiply(12,2)
# print(output)

# print(multiply(34,2))

# def fun(name =  "Ganesh Dutt"):
#     print("Hello ", name)
# 
# fun("Pooja")



# def fun(a):
#     if a % 2 == 0 :
#        print("Even")
#     else:
#        print("Odd")    
# 
# fun(47)

# item name  ,  price  , total 
# print()
# 
# def bill(item , price  , Quantity):
#     total  =  price * Quantity
#     print("you bought" , Quantity , item )
#     print("Total :  ",  total)
# 
# bill("noteBook" ,  100 , 3)

# Create a function  that take a word as input and counts how many vowels (A,E,I ,O,U)
# name   =  "Rahul"
# for i in name :
#     print(i)

# def count_vowels(word):
#     count  = 0
#     for letter in word:
#         if letter in "aeiouAEIOU":
#             count = count+1
#     return count  
# 
# output  =  count_vowels("Hello")
# print(output)    


# Create a function that takes a list of numbers as a parameter, adds them all together, and returns the total sum.
# a  =  [12,45,67,97,43,2]
# total =  0
# for i in a :
#    total  =  total + i
# print(total)   

# def sumOfList(numberList):
#     total  =  0
#     for i in numberList:
#       total  =  total + i
#     return total
# 
# a  =  [12,43,2]
# b  =  [9,3,3,2,2,2]
# print(sumOfList(b))

# 
# def funWithReturn(a , b):
#        sum  =   a + b       
#        return  sum
# 
# 
# def funWithOutReturn(a , b):
#        sum  =   a + b       
#        print(sum)
# 
# # output  = funWithReturn(12,56)
# output  = funWithOutReturn(12,56)
# 
# print(output)       

# def notify_user():
#     a  =  "calling user ring ring , pizza is ready to eat  "
#     return a
# 
# def order_user(callingFunction):
#     print("Taking your order ")
#     print("making...")
#     fun  =   callingFunction()
#     return fun
# 
# output  =   order_user(notify_user)
# print(output)

# ATM 

# def fun():
#     a  =  ["candy1" , "candy2" , "candy3" , "candy4"]
#     return a
# 
# output  =  fun()
# print(output)

# def fun():
#     yield "candy1"
#     yield "candy2"
#     yield "candy3"
#     yield "candy4"
# 
# output =  fun()    

# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))

# print(next(output))

# 
# def add(a,b):
#     return a + b
# 
# def mul(a , b):
#     return a*b
# 
# def div(a,b):
#     return a /b
# 
# def sub(a,b):
#     return a -b
# # 
# def cal(a,b,fun):
#     otuput  =  fun(a,b)
#     print(otuput)
# 
# cal(12,5,div)    


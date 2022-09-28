# def factorial(n):
#     if (n==1 or n==0):
#         return 1
#     return n * factorial(n-1)

# num = int(input("Enter the Number : "))
# a = factorial(num)
# print(a)

def fibonacci(n):
    if n==1 :
        return 1
    if n==0 : 
        return 0
    
    return fibonacci(n-1)+ fibonacci(n-2)
    

num = int(input("Enter a number upto which the fibonacci terms you want to print : "))
print(fibonacci(num))


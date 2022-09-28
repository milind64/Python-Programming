
#*************************  FUNCTIONS & METHODS ***************************#

#* Using Math module
# import math 

#* Math module ke functions jaanne ke liye 
# print(dir(math))
        #* ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 
        #* 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
        #*  'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 
        #* 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc'



#* Mann lo yaha se hummein __sqrt()__ ka use krna ho
# from math import sqrt
# print(sqrt(4))

#* Aur Mannlo saare ke saare functions chahiye toh type-->  from math import *

# from math import *
# print(sqrt(16))
# print(factorial(5))  

#* Asli function Aagya def print_Sum(n1,n2):

# def print_Sum(n1,n2): 
#     print(n1+n2)

# print_Sum(2,3)

#* Recursion

def recurse(a):
    if a<10:
        print(a)
        recurse(a+1)

recurse(1)
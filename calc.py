import math, cmath
from functools import reduce
## Allow list of numbers in number 1
## float, integer or complex number, check numbers is a type of number
## if type is not a number then it returns ValueError exception
def add(number1, number2=0):
    number_types = (int, float, complex)
    if (type(number1) == list) and (all(isinstance(item, number_types) for item in number1)):
        return reduce(lambda a,b: a+b, number1)
    if isinstance(number1, number_types) and isinstance(number2, number_types):
        return number1 + number2
    else:
        raise ValueError
  
## Allow list of numbers in number 1
## if a list then the first number in number1 is divided by one or more number from 2 onwards.
## Divide two numbers the first by the second, check both number 1 and 2 are either a 
## float, integer or complex number, once number1 and 2 have a type of number
## then number 1 and 2 are divided and returned as the result
## if type is not a number then it returns ValueError exception
def divide(number1, number2=1):
    number_types = (int, float, complex)
    if (type(number1) == list) and (all(isinstance(item, number_types) for item in number1)):
        return reduce(lambda a,b: a/b, number1)
    if isinstance(number1, number_types) and isinstance(number2, number_types):
        if number2 == 0:
            return 'Division by zero not allowed'
        return number1 / number2
    else:
        raise ValueError
        
## Allow list of numbers in number1 
## if a list then the first number in number1 is the number that becomes the power of 2nd number in number1 and onwards
## To power of, number is to the power of number 2, check both number 1 and 2 are either a 
## float, integer or complex number, once number1 and 2 have a type of number
## then number 2 is the power of number 1 and returned as the result
## if type is not a number then it returns ValueError exception
def exponent(number1, number2=1):
    number_types = (int, float, complex)
    if (type(number1) == list) and (all(isinstance(item, number_types) for item in number1)):
        return reduce(lambda a,b: a**b, number1)
    if isinstance(number1, number_types) and isinstance(number2, number_types):
        return number1 ** number2
    else:
        raise ValueError
 
## Allow list of numbers in number1 
## if a list then each number in the list is muiplied by the one next to it      
## Muitlply two number together, check both number 1 and 2 are either a 
## float, integer or complex number, once number1 and 2 have a type of number
## then number 1 and 2 are Muitliplied together and returned as the result
## if type is not a number then it returns ValueError exception
def multiply(number1, number2=1):
    number_types = (int, float, complex)
    if (type(number1) == list) and (all(isinstance(item, number_types) for item in number1)):
        return reduce(lambda a,b: a*b, number1)
    if isinstance(number1, number_types) and isinstance(number2, number_types):
        return number1 * number2
    else:
        raise ValueError

## Allow list of numbers in number1 
## if a list then each number subsequent number is subtracted from the first number in the number1 list      
## subtract  number2 from number 1, check both number 1 and 2 are either a 
## float, integer or complex number, once number1 and 2 have a type of number
## then number2 is taken from number 1  and returned as the result
## if type is not a number then it returns ValueError exception        
def subtract(number1, number2=0):
    number_types = (int, float, complex)
    if (type(number1) == list) and (all(isinstance(item, number_types) for item in number1)):
        return reduce(lambda a,b: a-b, number1)
    if isinstance(number1, number_types) and isinstance(number2, number_types):
        return number1 - number2
    else:
        raise ValueError

## Allow list of numbers in number1 
## if a list then each number in the list is square rooted 
## square root of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 has the square root taken of it and returned as the result
## if type is not a number then it returns ValueError exception
## cMath is used for negative numbers
def sqroot(number1):
    number_types = (int, float, complex)
    if (type(number1) == list) and (all(isinstance(item, number_types) for item in number1)):
        return list(map(lambda a: cmath.sqrt(a), number1))
    if isinstance(number1, number_types):
        return cmath.sqrt(number1)
    else:
        raise ValueError
 
## Allow list of numbers in number1 
## if a list then each number in the list is squared 
## square of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 is squared and returned as the result
## if type is not a number then it returns ValueError exception   
## math is used for pow function
def square(number1):
    number_types = (int, float, complex)
    if (type(number1) == list) and (all(isinstance(item, number_types) for item in number1)):
        return list(map(lambda a: math.pow(a, 2), number1))
    if isinstance(number1, number_types):
        return math.pow(number1, 2)
    else:
        raise ValueError

## Allow list of numbers in number1 
## if a list then each number in the list is cubed 
## cube of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 is cubed and returned as the result
## if type is not a number then it returns ValueError exception   
## math is used for pow function     
def cube(number1):
    number_types = (int, float, complex)
    if (type(number1) == list) and (all(isinstance(item, number_types) for item in number1)):
        return list(map(lambda a: math.pow(a, 3), number1))
    if isinstance(number1, number_types):
        return math.pow(number1, 3)
    else:
        raise ValueError

## Allow list of numbers in number1 
## if a list then each number in the list is cubed 
##Generator        
def cubic_generator(number1):
    number_types = (int, float, complex)
    if (type(number1) == list) and (all(isinstance(item, number_types) for item in number1)):
        yield list(map(lambda a: math.pow(a, 3), number1))
    else:
        if isinstance(number1, number_types):
            intRes =math.pow(number1, 3)
            yield intRes
        else:
            raise ValueError


## Allow list of numbers in number1 
## sine of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 has the sine take of it and returned as the result
## if type is not a number then it returns ValueError exception   
## math is used for sin function       
def sin(number1):
    number_types = (int, float, complex)
    if (type(number1) == list) and all(isinstance(item, number_types) for item in number1):
            rad = math.pi / 180
            return list(map(lambda a: math.sin(a* rad), number1))
    if isinstance(number1, number_types):
        rad = math.pi / 180
        return math.sin(number1* rad)
    else:
        raise ValueError

## Allow list of numbers in number1 
## cosine of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 has the cosine take of it and returned as the result
## if type is not a number then it returns ValueError exception   
## math is used for cos function        
def cos(number1):
    number_types = (int, float, complex)
    if (type(number1) == list) and all(isinstance(item, number_types) for item in number1):
            rad = math.pi / 180
            return list(map(lambda a: math.cos(a* rad), number1))
    if isinstance(number1, number_types):
        rad = math.pi / 180
        return math.cos(number1* rad)
    else:
        raise ValueError

## Allow list of numbers in number1 
## tangent of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 has the tangent take of it and returned as the result
## if type is not a number then it returns ValueError exception   
## math is used for tan function            
def tan(number1):
    number_types = (int, float, complex)
    if (type(number1) == list) and all(isinstance(item, number_types) for item in number1):
            rad = math.pi / 180
            return list(map(lambda a: math.tan(a* rad), number1))
    if isinstance(number1, number_types):
        rad = math.pi / 180
        return math.tan(number1* rad)
    else:
        raise ValueError

## Allow list of numbers in number1 
## factorial of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 has the factorial take of it and returned as the result
## if type is not a number then it returns ValueError exception  
##if number1 is negative or a float then it returns ValueError exception 
## math is used for factorial function            
def factorial(number1):
    number_types = (int, float, complex)
    if (type(number1) == list) and all(isinstance(item, number_types) for item in number1):
        if not list(filter(lambda a: a < 0, number1)):
            return list(map(lambda a: math.factorial(a), number1))
        else:
            print('23423423423423')
    if isinstance(number1, number_types):
        return math.factorial(number1)
    else:
        raise ValueError

# Calculate the list assigned to the temp variable into fahrenheit        
def fahrenheit(number1):
    return ((float(9)/5)*number1 + 32)

# Calculate the list assigned to the temp variable into celsius  
def celsius(number1):
    return (float(5)/9*(number1 - 32))

        
#cubGen=(cubic_generator([8,6]))
#for i in cubGen:
#    print(i)
	
# Set temp variable as a list of numbers 	
#temp = (36.5, 40, 37.5, 39)

# Calculate the list assigned to the temp variable into fahrenheit and assign it to the variable 'F'
#F = list(map(fahrenheit, temp))
# Reverse the calculations and assign to the variable 'C' and output the variable 
#C = list(map(celsius, F))
#print (C)

        
        
        


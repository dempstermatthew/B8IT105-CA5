import math, cmath
from functools import reduce
## Allow list of numbers 
## float, integer or complex number, check numbers is a type of number
## 
## if type is not a number then it returns ValueError exception
def add(numbers):
    number_types = (int, float, complex)
    if all(isinstance(item, number_types) for item in numbers):
        return reduce(lambda a,b: a+b, numbers)
    else:
        raise ValueError
        
## Divide two numbers the first by the second, check both number 1 and 2 are either a 
## float, integer or complex number, once number1 and 2 have a type of number
## then number 1 and 2 are divided and returned as the result
## if type is not a number then it returns ValueError exception
def divide(number1, number2):
    number_types = (int, float, complex)
    if isinstance(number1, number_types) and isinstance(number2, number_types):
        if number2 == 0:
            return 'Division by zero not allowed'
        return number1 / number2
    else:
        raise ValueError

## To power of, number is to the power of number 2, check both number 1 and 2 are either a 
## float, integer or complex number, once number1 and 2 have a type of number
## then number 2 is the power of number 1 and returned as the result
## if type is not a number then it returns ValueError exception
def exponent(number1, number2):
    number_types = (int, float, complex)
    if isinstance(number1, number_types) and isinstance(number2, number_types):
        return number1 ** number2
    else:
        raise ValueError
        
## Muitlply two number together, check both number 1 and 2 are either a 
## float, integer or complex number, once number1 and 2 have a type of number
## then number 1 and 2 are Muitliplied together and returned as the result
## if type is not a number then it returns ValueError exception
def multiply(number1, number2):
    number_types = (int, float, complex)
    if isinstance(number1, number_types) and isinstance(number2, number_types):
        return number1 * number2
    else:
        raise ValueError

## subtract  number2 from number 1, check both number 1 and 2 are either a 
## float, integer or complex number, once number1 and 2 have a type of number
## then number2 is taken from number 1  and returned as the result
## if type is not a number then it returns ValueError exception        
def subtract(number1, number2):
    number_types = (int, float, complex)
    if isinstance(number1, number_types) and isinstance(number2, number_types):
        return number1 - number2
    else:
        raise ValueError

## square root of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 has the square root taken of it and returned as the result
## if type is not a number then it returns ValueError exception
## cMath is used for negative numbers
def sqroot(number1):
    number_types = (int, float, complex)
    if isinstance(number1, number_types):
        return cmath.sqrt(number1)
    else:
        raise ValueError
 
## square of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 is squared and returned as the result
## if type is not a number then it returns ValueError exception   
## math is used for pow function
def square(number1):
    number_types = (int, float, complex)
    if isinstance(number1, number_types):
        return math.pow(number1, 2)
    else:
        raise ValueError

## cube of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 is cubed and returned as the result
## if type is not a number then it returns ValueError exception   
## math is used for pow function     
def cube(number1):
    number_types = (int, float, complex)
    if isinstance(number1, number_types):
        return math.pow(number1, 3)
    else:
        raise ValueError

## sine of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 has the sine take of it and returned as the result
## if type is not a number then it returns ValueError exception   
## math is used for sin function       
def sin(number1):
    number_types = (int, float, complex)
    if isinstance(number1, number_types):
        return math.sin(number1)
    else:
        raise ValueError

## cosine of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 has the cosine take of it and returned as the result
## if type is not a number then it returns ValueError exception   
## math is used for cos function        
def cos(number1):
    number_types = (int, float, complex)
    if isinstance(number1, number_types):
        return math.cos(number1)
    else:
        raise ValueError

## tangent of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 has the tangent take of it and returned as the result
## if type is not a number then it returns ValueError exception   
## math is used for tan function            
def tan(number1):
    number_types = (int, float, complex)
    if isinstance(number1, number_types):
        return math.tan(number1)
    else:
        raise ValueError

## factorial of number 1, check number 1 is either a 
## float, integer or complex number, once number1 is of a type of number
## then number1 has the factorial take of it and returned as the result
## if type is not a number then it returns ValueError exception  
##if number1 is negative or a float then it returns ValueError exception 
## math is used for factorial function            
def factorial(number1):
    number_types = (int, float, complex)
    if isinstance(number1, number_types):
        return math.factorial(number1)
    else:
        raise ValueError
        
        
        
        


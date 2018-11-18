import unittest
from calc import add, multiply, subtract, divide, exponent, sqroot, square 
from calc import cube, sin, cos, tan, factorial, cubic_generator, fahrenheit, celsius

class CalculatorTest(unittest.TestCase):
	
    def testAdd(self):
        ## positive tests
        self.assertEqual(4, add(2, 2)) 
        self.assertEqual(3, add(-1, 4))
        self.assertEqual(5, add(5, 0))
        self.assertEqual(2.2, add(1.2, 1))
        ## negative tests
        self.assertNotEqual(6, add(5, 0)) 
        self.assertNotEqual(5, add(5, -1))
        ## exception tests
        self.assertRaises(ValueError, add, 5, 'three') 
        self.assertRaises(ValueError, add, 'five', 3)
        self.assertRaises(ValueError, add, 'five', 'three')
        ## list of numbers
        self.assertEqual(9.2, add([1,2,1.2,5])) 
    
        
    def testDivide(self):
        ## positive tests
        self.assertEqual(1, divide(2, 2)) 
        self.assertEqual(4, divide(2, 0.5))
        self.assertEqual(-1, divide(6, -6))
        self.assertEqual(6, divide(-30, -5))
        self.assertEqual('Division by zero not allowed', divide(5, 0))
        ## negative tests
        self.assertNotEqual(6, divide(5, 1))
        self.assertNotEqual(-6, divide(-30, -5))
        ## exception tests
        self.assertRaises(ValueError, divide, 5, 'zero')
        self.assertRaises(ValueError, divide, 'five', 0)
        self.assertRaises(ValueError, divide, 'five', 'zero')
         ## list of numbers
        self.assertEqual(2, divide([12,2,3])) 
    
    def testExponent(self):
        ## positive tests
        self.assertEqual(32, exponent(2, 5))
        self.assertEqual(2, exponent(2, 1))
        self.assertEqual(25, exponent(5, 2))
        self.assertEqual(-27, exponent(-3, 3))
        self.assertEqual(0.0625, exponent(0.5, 4))
        ## negative tests
        self.assertNotEqual(6, exponent(5, 1))
        self.assertNotEqual(0.06, exponent(0.5, 4))
        ## exception tests
        self.assertRaises(ValueError, exponent, 5, 'two')
        self.assertRaises(ValueError, exponent, 'five', 2)
        self.assertRaises(ValueError, exponent, 'five', 'two')
         ## list of numbers
        self.assertEqual(729, exponent([3,3,2])) 
 
    def testMuliply(self):
        ## positive tests
        self.assertEqual(4, multiply(2, 2))
        self.assertEqual(1, multiply(5, 0.2))
        self.assertEqual(-15, multiply(5, -3))
        self.assertEqual(5, multiply(5, 1))
        ## negative tests
        self.assertNotEqual(6, multiply(5, 1))
        self.assertNotEqual(-1, multiply(-1, -1))
        ## exception tests
        self.assertRaises(ValueError, multiply, 5, 'one')
        self.assertRaises(ValueError, multiply, 'five', 1)
        self.assertRaises(ValueError, multiply, 'five', 'one')
         ## list of numbers
        self.assertEqual(18, multiply([3,3,2])) 
        
    def testSubtract(self):
        ## positive tests
        self.assertEqual(0, subtract(2, 2))
        self.assertEqual(5, subtract(5, 0))
        self.assertEqual(3.5, subtract(4, 0.5))
        self.assertEqual(2.5, subtract(3.5, 1))
        self.assertEqual(-1, subtract(1, 2))
        ## negative tests
        self.assertNotEqual(6, subtract(5, 1))
        self.assertNotEqual(-0.5, subtract(-1.5, 1))
        ## exception tests
        self.assertRaises(ValueError, subtract, 5, 'zero')
        self.assertRaises(ValueError, subtract, 'five', 0)
        self.assertRaises(ValueError, subtract, 'five', 'zero')
         ## list of numbers
        self.assertEqual(-1, subtract([3,2,2])) 
    
    def testSquareRoot(self):
        ## positive tests
        self.assertEqual(3, sqroot(9))
        self.assertEqual(5, sqroot(25))
        self.assertEqual(6, sqroot(36))
        self.assertEqual(2.5, sqroot(6.25))
        self.assertEqual(3j, sqroot(-9))
        
        ## negative tests
        self.assertNotEqual(36, sqroot(6.25))
        self.assertNotEqual(-3, sqroot(-9))
        ## exception tests
        self.assertRaises(ValueError, sqroot, 'zero')
         ## list of numbers
        self.assertEqual([3,9] ,sqroot([9,81])) 
        
    def testSquare(self):
        ## positive tests
        self.assertEqual(81, square(9))
        self.assertEqual(25, square(5))
        self.assertEqual(36, square(6))
        self.assertEqual(6.25, square(2.5))
        self.assertEqual(81, square(-9))
        
        ## negative tests
        self.assertNotEqual(36, square(6.25))
        self.assertNotEqual(-81, square(-9))
        ## exception tests
        self.assertRaises(ValueError, square, 'zero')
         ## list of numbers
        self.assertEqual([9,81, 4,16] ,square([3,9, 2, 4])) 
    
    def testCube(self):
        ## positive tests
        self.assertEqual(729, cube(9))
        self.assertEqual(125, cube(5))
        self.assertEqual(216, cube(6))
        self.assertEqual(15.625, cube(2.5))
        self.assertEqual(-729, cube(-9))
        
        ## negative tests
        self.assertNotEqual(36, cube(6.25))
        self.assertNotEqual(729, cube(-9))
        ## exception tests
        self.assertRaises(ValueError, cube, 'zero')
        ## list of numbers
        self.assertEqual([729,125,216] ,cube([9, 5, 6])) 
        ##generator single
        for i, elem in enumerate(cubic_generator(4)):
            result = elem
        self.assertEqual(64, result) 
        ##generator single list
        cubGen=(cubic_generator([8,6]))
        for i in cubGen:
            result =i
        self.assertEqual([512, 216] ,result) 
        
    
    def testSine(self):
        ## positive tests
        self.assertEqual(0.052335956242943835, sin(3))
        ## list of numbers
        self.assertEqual(-0.052335956242943835, sin(-3))
                       
        ## negative tests
        self.assertNotEqual(36, sin(6.25))
        self.assertNotEqual(729, sin(-9))
        ## exception tests
        self.assertRaises(ValueError, sin, 'zero')
        ## list of numbers
        self.assertEqual([0.052335956242943835,0.08715574274765817, 0.10452846326765347] ,sin([3, 5, 6])) 
        
    def testCosine(self):
        ## positive tests
        self.assertEqual(0.9986295347545738, cos(3))
        self.assertEqual(0.9986295347545738, cos(-3))
        self.assertEqual(0.9990482215818578, cos(2.5))
                
        ## negative tests
        self.assertNotEqual(-0.14, cos(-3))
        self.assertNotEqual(-0.14, cos(3))
        ## exception tests
        self.assertRaises(ValueError, cos, 'zero')
        ## list of numbers
        self.assertEqual([0.9986295347545738,0.9961946980917455, 0.9945218953682733] ,cos([3, 5, 6])) 
        
    def testTangent(self):
        ## positive tests
        self.assertEqual(0.05240777928304121, tan(3))
        self.assertEqual(-0.05240777928304121, tan(-3))
        self.assertEqual(0.04366094290851206, tan(2.5))
                
        ## negative tests
        self.assertNotEqual(-0.14, tan(-3))
        self.assertNotEqual(-0.14, tan(3))
        ## exception tests
        self.assertRaises(ValueError, tan, 'zero')
         ## list of numbers
        self.assertEqual([0.05240777928304121,0.08748866352592401, 0.10510423526567647] ,tan([3, 5, 6])) 
        
    def testFactorial(self):
        ## positive tests
        self.assertEqual(24, factorial(4))
        self.assertEqual(362880, factorial(9))
        self.assertEqual(1, factorial(0))
                
        ## negative tests
        self.assertNotEqual(5041, factorial(7))
        self.assertNotEqual(0.14, factorial(3))
        ## exception tests
        self.assertRaises(ValueError, factorial, 'zero')
        self.assertRaises(ValueError, factorial, -3)
        self.assertRaises(ValueError, factorial, 2.5)
          ## list of numbers
        self.assertEqual([24, 362880, 1] ,factorial([4, 9, 0])) 
     
    
    ## #r = map(func, seq)
    def testFahrenheitCelsius(self):
        temp = (36.5, 40, 37.5, 39)
        F = list(map(fahrenheit, temp))
        self.assertEqual([97.7, 104.0, 99.5, 102.2], F)
        C = list(map(celsius, F))
        self.assertEqual([36.5, 40.0, 37.5, 39.0], C)
       
    
    
		
		
		
unittest.main()

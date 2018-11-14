import unittest
from calc import add, multiply, subtract, divide, exponent, sqroot, square 
from calc import cube, sin, cos, tan, factorial

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
    
    def testSine(self):
        ## positive tests
        self.assertEqual(0.1411200080598672, sin(3))
        self.assertEqual(-0.1411200080598672, sin(-3))
        self.assertEqual(0.5984721441039565, sin(2.5))
                
        ## negative tests
        self.assertNotEqual(36, sin(6.25))
        self.assertNotEqual(729, sin(-9))
        ## exception tests
        self.assertRaises(ValueError, sin, 'zero')
        
    def testCosine(self):
        ## positive tests
        self.assertEqual(-0.9899924966004454, cos(3))
        self.assertEqual(-0.9899924966004454, cos(-3))
        self.assertEqual(-0.8011436155469337, cos(2.5))
                
        ## negative tests
        self.assertNotEqual(-0.14, sin(-3))
        self.assertNotEqual(-0.14, sin(3))
        ## exception tests
        self.assertRaises(ValueError, sin, 'zero')
        
    def testTangent(self):
        ## positive tests
        self.assertEqual(-0.1425465430742778, tan(3))
        self.assertEqual(0.1425465430742778, tan(-3))
        self.assertEqual(-0.7470222972386603, tan(2.5))
                
        ## negative tests
        self.assertNotEqual(-0.14, tan(-3))
        self.assertNotEqual(-0.14, tan(3))
        ## exception tests
        self.assertRaises(ValueError, tan, 'zero')
        
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
       
    
    
		
		
		
unittest.main()

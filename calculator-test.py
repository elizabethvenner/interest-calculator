import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def testCalculatorReturnsCorrectResult(self):
        calculator = Calculator()
        result = calculator.calculate(1000, 1.3, 100)
        self.assertEqual(result, 3.561643835616439)


if __name__ =='__main__':
    unittest.main()

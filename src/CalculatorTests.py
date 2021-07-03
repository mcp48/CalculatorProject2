import unittest
from Calculator import Calculator
from CSVReader import CSVReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        test_data = CSVReader('/src/UnitTests/Unit_Tests_Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(5, 2), 10)
        self.assertEqual(self.calculator.result, 10)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_squareRoot_method_calculator(self):
        self.assertEqual(self.calculator.squareRoot(25), 5)
        self.assertEqual(self.calculator.result, 5)


if __name__ == '__main__':
    unittest.main()

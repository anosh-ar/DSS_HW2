import unittest
from math_quiz import randomNumberGenerator, randomMathOperation, calculatOperation



class TestMathGame(unittest.TestCase):

    def test_randomNumberGenerator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomNumberGenerator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_randomMathOperation(self):
        for _ in range(100):  # Test a large number of random values
            operation = randomMathOperation()
            self.assertTrue(operation == "+" or operation == "-" or operation == "*")

    def test_calculatOperation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (2, 8, '+', '2 + 8', 10),
                (7, 3, '*', '7 * 3', 21),
                (8, 2, '-', '8 - 2', 6)

            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculatOperation(num1,num2,operator)
                self.assertEqual(answer,expected_answer)
                self.assertEqual(problem,expected_problem)

if __name__ == "__main__":
    unittest.main()

import unittest
from src.fizzbuzz import *


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        pass

    def test_if_divisible_by_3_return_fizz(self):
        fizz_result = divisible_by_3_and_5(9)
        self.assertEqual("Fizz", fizz_result)

    def test_if_divisible_by_5_return_buzz(self):
        buzz_result = divisible_by_3_and_5(10)
        self.assertEqual("Buzz", buzz_result)

    def test_if_not_divisible_by_3_or_5_return_number(self):
        buzz_result = divisible_by_3_and_5(11)
        self.assertEqual("11", buzz_result)

    def test_if_divisible_by_3_and_5_return_fizz_buzz(self):
        fizz_buzz_result = divisible_by_3_and_5(15)
        self.assertEqual("FizzBuzz", fizz_buzz_result)

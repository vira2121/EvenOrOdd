import unittest


def check(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"


def CheckDivisibleby7(x):
    if x%7 == 0:
        return True
    else:
        return False

class CheckDivisible(unittest.TestCase):
    def test_case_divisible(self):
        x = 14
        result = CheckDivisibleby7(x)
        self.assertTrue(result)

    def test_case_divisible1(self):
        x = 9
        result = CheckDivisibleby7(x)
        self.assertFalse(result)


class EvenOrOddApp(unittest.TestCase):
    def test_case_even_check(self):
        x = 10
        result = check(x)
        self.assertEqual("even", result)

    def test_case_odd_check(self):
        x = 15
        result = check(x)
        self.assertNotEqual("even", result)


if __name__ == "__main__":
        unittest.main()
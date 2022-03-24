import unittest


def check(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"


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
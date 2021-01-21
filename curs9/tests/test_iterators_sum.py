import unittest
from functions import iterators_sum


class TestIteratorsSum(unittest.TestCase):
    def test_iterators_sum(self):
        results = iterators_sum([1, 2, 3], (4, 5), "abc")
        expected_results = [6, 9, 0]

        self.assertEqual(results, expected_results)


if __name__ == '__main__':
    unittest.main()


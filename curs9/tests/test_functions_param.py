import unittest
from functions import MyIterator, iter_sum, iterators_sum
from parameterized import parameterized, param


class TestIterSum(unittest.TestCase):
    @parameterized.expand((
        param([1, 2, 3]),
        param([3, 2, 1]),
        param(MyIterator())
    ))
    def test_iter_sum(self, iterator):
        result = iter_sum(iterator)
        expected_result = 6

        self.assertEqual(result, expected_result)

    @parameterized.expand((
            param("abc"),
            param(27),
            param(None),
            param(True),
    ))
    def test_iter_sum_with_exception(self, non_iterator):
        with self.assertRaises(TypeError) as type_error:
            iter_sum(non_iterator)
        print("type_error:", type_error.exception)


class TestIteratorsSum(unittest.TestCase):
    def test_iterators_sum(self):
        results = iterators_sum([1, 2, 3], (4, 5), "abc")
        expected_results = [6, 9, 0]

        self.assertEqual(results, expected_results)


if __name__ == '__main__':
    unittest.main()


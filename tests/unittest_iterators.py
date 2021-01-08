import unittest
from helpers.iterators import MyIterator


class TestIterators(unittest.TestCase):
    def test_iterator_init(self):
        n = 5
        init_value = 2

        my_iterator = MyIterator(n, init_value)
        self.assertEqual(n, my_iterator.numbers)
        self.assertEqual(init_value, my_iterator.first_value)

    def test_iterator_values(self):
        n = 5
        init_value = 2
        expected_values = [2, 4, 16]

        my_iterator = MyIterator(n, init_value)
        for expected_value, result_value in zip(expected_values, iter(my_iterator)):
            self.assertEqual(expected_value, result_value)


if __name__ == "__main__":
    unittest.main()
import json
import unittest
from unittest.mock import patch
from parameterized import parameterized, param
from helpers.functions import iterator_sum, yes_no_api_response, is_yes_answer
from helpers.iterators import MyIterator


class TestFunctions(unittest.TestCase):
    @parameterized.expand([
        param([1, 2, 3], 6),
        param((1, 2, 3, 4), 10),
        param(MyIterator(3, 2), 22),
    ])
    def test_iterator_sum(self, iterator, expected_result):
        result = iterator_sum(iterator)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        param("abc"),
        param([1, 2, 3, 'abc', 4, 5])
    ])
    def test_iterator_sum_exception(self, wrong_input):
        with self.assertRaises(TypeError) as my_exception:
            iterator_sum(wrong_input)

        # prints the exception message
        print(my_exception.exception)

    def test_yes_no_api_response(self):
        result = yes_no_api_response()

        self.assertIn("answer", result)
        self.assertIn(result["answer"], ["yes", "no"])
        self.assertIn("code", result)
        self.assertEqual(200, result["code"])

    # @parameterized.expand([
    #     param("yes", 200, True),
    #     param("yes", 404, False),
    #     param("no", 200, False),
    #     param("no", 404, False),
    # ])
    # @patch('helpers.functions.requests.get')
    # def test_is_yes_answer(self, param_answer, param_code, expected_result, mocked_get_request):
    #     mocked_get_request.return_value.text = json.dumps({
    #         "answer": param_answer
    #     })
    #     mocked_get_request.return_value.status_code = param_code
    #
    #     result = is_yes_answer()
    #     self.assertEqual(expected_result, result)

    @parameterized.expand([
        param("yes", 200, True),
        param("yes", 404, False),
        param("no", 200, False),
        param("no", 404, False),
    ])
    @patch('helpers.functions.yes_no_api_response')
    def test_is_yes_answer(self, param_answer, param_code, expected_result, mocked_yes_no_api_response):
        mocked_yes_no_api_response.return_value = {
            "answer": param_answer,
            "code": param_code
        }

        result = is_yes_answer()
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()

import json
import pytest
from helpers.functions import iterator_sum, is_yes_answer
from helpers.iterators import MyIterator


@pytest.mark.parametrize(("iterator", "expected_result"), [
    pytest.param([1, 2, 3], 6),
    pytest.param((1, 2, 3, 4), 10),
    pytest.param(MyIterator(3, 2), 22),
])
def test_iterator_sum(iterator, expected_result):
    result = iterator_sum(iterator)

    assert result == expected_result


@pytest.mark.parametrize('wrong_input', [
    pytest.param('abc'),
    pytest.param([1, 2, 3, 'abc', 4, 5])
])
def test_iterator_sum_exception(wrong_input):
    with pytest.raises(TypeError) as type_error_exception:
        iterator_sum(wrong_input)

    # prints the exception message
    print(type_error_exception.value)


@pytest.mark.parametrize(("param_answer", "param_code", "expected_result"), [
    pytest.param("yes", 200, True),
    pytest.param("yes", 400, False),
    pytest.param("no", 200, False),
    pytest.param("no", 500, False),
])
def test_is_yes_answer(requests_mock, param_answer, param_code, expected_result):
    requests_mock.get(
        "https://yesno.wtf/api",
        text=json.dumps({
            "answer": param_answer
        }),
        status_code=param_code
    )

    result = is_yes_answer()

    assert result is expected_result

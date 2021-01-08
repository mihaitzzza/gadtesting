import json
import requests


def iterator_sum(iterator):
    iterable = iter(iterator)
    my_sum = 0

    for element in iterable:
        my_sum += element

    return my_sum


def sum_of_iterators(*args):
    sums = []

    for arg in args:
        arg_sum = iterator_sum(arg)
        sums.append(arg_sum)

    return sums


def yes_no_api_response():
    api_response = requests.get("https://yesno.wtf/api")
    api_response_data = json.loads(api_response.text)

    return {
        "answer": api_response_data["answer"],
        "code": api_response.status_code
    }


def is_yes_answer():
    result = yes_no_api_response()
    return result["answer"] == "yes" and result["code"] == 200

import pytest
from calculator import add, subtract, multiply, calculator, lambda_handler

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, -1) == 1
    assert multiply(-1, 1) == -1

def test_calculator():
    assert calculator(3, 2, '+') == 5
    assert calculator(5, 3, '-') == 2
    assert calculator(2, 3, '*') == 6
    assert calculator(5, 3, '/') == "Invalid operator"  # Test for invalid operator
    assert calculator(0, 0, '+') == 0
    assert calculator(1, 0, '-') == 1
    assert calculator(0, 1, '*') == 0

def test_lambda_handler():
    event = {
        "x": "3",
        "y": "2",
        "operator": "+"
    }
    response = lambda_handler(event, None)
    assert response['statusCode'] == 200
    assert response['body']['result'] == 5

    # Test invalid operator
    event["operator"] = "/"
    response = lambda_handler(event, None)
    assert response['body'] == "Invalid operator"

    # Test missing parameter
    event = {"x": "3", "operator": "+"}  # Missing "y"
    response = lambda_handler(event, None)
    assert response['statusCode'] == 400
    assert 'Missing parameter' in response['body']

    # Test invalid input
    event = {"x": "abc", "y": "2", "operator": "+"}
    response = lambda_handler(event, None)
    assert response['statusCode'] == 500

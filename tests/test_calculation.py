# test_calculation.py

import pytest
from src.calculation import add, subtract, multiply, divide

@pytest.fixture(scope="function")
def resource():
    return (1,2)

@pytest.fixture(scope="class")
def resource_class():
    return (3,4)

@pytest.fixture(scope="module")
def resource_module():
    return (5,6)

@pytest.fixture(scope="session")
def resource_session():
    return (7,14)

@pytest.fixture
def setup_and_teardown():
    # Setup code before each test function
    print("單獨一個 funcion 設定")
    yield
    # Teardown code after each test function
    print("單獨一個 funcion 清理")
    
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (10, -10, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.group1
def test_subtract(setup_and_teardown, resource_class):
    assert subtract(resource_class[0], resource_class[1]) == -1
    
@pytest.mark.skip("skip this test for no reason")
@pytest.mark.group2
def test_multiply(setup_and_teardown, resource_module):
    assert multiply(resource_module[0], resource_module[1]) == 30

@pytest.mark.group2
def test_divide(setup_and_teardown, resource_session):
    assert divide(resource_session[0], resource_session[1]) == 0.5
import pytest
from myapp.app import add, subtract, multiply, divide, power, modulo, floor_division, absolute

def test_add():
    assert add(3, 5) == 8

def test_subtract():
    assert subtract(10, 4) == 6

# def test_multiply():
#     assert multiply(3, 7) == 21

# def test_divide():
#     assert divide(10, 2) == 5
#     with pytest.raises(ValueError):
#         divide(10, 0)

# def test_power():
#     assert power(2, 3) == 8

# def test_modulo():
#     assert modulo(10, 3) == 1
#     with pytest.raises(ValueError):
#         modulo(10, 0)

# def test_floor_division():
#     assert floor_division(9, 2) == 4
#     with pytest.raises(ValueError):
#         floor_division(9, 0)

# def test_absolute():
#     assert absolute(-5) == 5
#     assert absolute(7) == 7

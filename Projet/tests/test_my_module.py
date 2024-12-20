# test_my_module.py
"""
Tests unitaires pour le module my_module.
"""
import pytest
from my_module import add, subtract, multiply, divide, modulo, power

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(0, 3) == 0

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)

def test_modulo():
    assert modulo(10, 3) == 1
    with pytest.raises(ValueError):
        modulo(10, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

if __name__ == "__main__":
    pytest.main()

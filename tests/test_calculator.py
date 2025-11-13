import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_divide():
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        calculator.divide(1, 0)


import pytest
from main import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

if __name__ == "__main__":
    pytest.main()

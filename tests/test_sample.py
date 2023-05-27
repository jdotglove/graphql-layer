import pytest

# Example test
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4
    
# Example test for error
def failure():
    raise SystemExit(1)


def test_failure():
    with pytest.raises(SystemExit):
        failure()
        
# Example test class for test grouping
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        with pytest.raises(AssertionError):
            x = "hello"
            assert hasattr(x, "check")
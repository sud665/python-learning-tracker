"""
TDD 예제: 계산기 테스트

Step 1: Red - 실패하는 테스트를 먼저 작성
"""
import pytest
from calculator import Calculator, add, subtract, multiply, divide


class TestCalculator:
    """Calculator 클래스 테스트"""
    
    def test_add(self):
        """덧셈 테스트"""
        calc = Calculator()
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0
        assert calc.add(10.5, 2.5) == 13.0
    
    def test_subtract(self):
        """뺄셈 테스트"""
        calc = Calculator()
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(0, 5) == -5
        assert calc.subtract(10, 10) == 0
    
    def test_multiply(self):
        """곱셈 테스트"""
        calc = Calculator()
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(0, 100) == 0
    
    def test_divide(self):
        """나눗셈 테스트"""
        calc = Calculator()
        assert calc.divide(10, 2) == 5.0
        assert calc.divide(9, 3) == 3.0
        assert calc.divide(1, 2) == 0.5
    
    def test_divide_by_zero(self):
        """0으로 나누기 예외 처리 테스트"""
        calc = Calculator()
        with pytest.raises(ValueError, match="0으로 나눌 수 없습니다"):
            calc.divide(10, 0)
    
    def test_power(self):
        """거듭제곱 테스트"""
        calc = Calculator()
        assert calc.power(2, 3) == 8
        assert calc.power(5, 0) == 1
        assert calc.power(10, 2) == 100


class TestCalculatorFunctions:
    """함수형 계산기 테스트"""
    
    def test_add_function(self):
        """덧셈 함수 테스트"""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
    
    def test_subtract_function(self):
        """뺄셈 함수 테스트"""
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
    
    def test_multiply_function(self):
        """곱셈 함수 테스트"""
        assert multiply(3, 4) == 12
        assert multiply(-2, 3) == -6
    
    def test_divide_function(self):
        """나눗셈 함수 테스트"""
        assert divide(10, 2) == 5.0
        assert divide(9, 3) == 3.0
    
    def test_divide_by_zero_function(self):
        """0으로 나누기 예외 처리 테스트"""
        with pytest.raises(ValueError):
            divide(10, 0)


# Parametrize를 사용한 테스트
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
    (1.5, 2.5, 4.0),
])
def test_add_parametrized(a, b, expected):
    """매개변수화된 덧셈 테스트"""
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (1, 2, 0.5),
    (100, 4, 25.0),
])
def test_divide_parametrized(a, b, expected):
    """매개변수화된 나눗셈 테스트"""
    assert divide(a, b) == expected


@pytest.mark.parametrize("a,b", [
    (10, 0),
    (5, 0),
    (-10, 0),
])
def test_divide_by_zero_parametrized(a, b):
    """매개변수화된 0으로 나누기 테스트"""
    with pytest.raises(ValueError):
        divide(a, b)

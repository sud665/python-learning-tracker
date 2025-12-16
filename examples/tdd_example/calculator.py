"""
TDD 예제: 계산기 구현

Step 2: Green - 테스트를 통과시키는 최소한의 코드 작성
Step 3: Refactor - 코드 개선
"""
from typing import Union


class Calculator:
    """계산기 클래스"""
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """두 숫자를 더합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            덧셈 결과
        """
        return a + b
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """두 숫자를 뺍니다.
        
        Args:
            a: 피감수
            b: 감수
            
        Returns:
            뺄셈 결과
        """
        return a - b
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """두 숫자를 곱합니다.
        
        Args:
            a: 첫 번째 숫자
            b: 두 번째 숫자
            
        Returns:
            곱셈 결과
        """
        return a * b
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """두 숫자를 나눕니다.
        
        Args:
            a: 피제수
            b: 제수
            
        Returns:
            나눗셈 결과
            
        Raises:
            ValueError: 제수가 0일 때
        """
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다")
        return a / b
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """거듭제곱을 계산합니다.
        
        Args:
            base: 밑
            exponent: 지수
            
        Returns:
            거듭제곱 결과
        """
        return base ** exponent


# 함수형 인터페이스
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """두 숫자를 더합니다."""
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """두 숫자를 뺍니다."""
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """두 숫자를 곱합니다."""
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """두 숫자를 나눕니다.
    
    Raises:
        ValueError: 제수가 0일 때
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b

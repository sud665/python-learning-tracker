"""
Challenge 04: 반복문

TODO: 다음 함수들을 완성하세요

힌트:
- for문: for i in range(n)
- while문: while 조건:
- break, continue 사용 가능
"""

def count_down(n):
    """
    TODO: n부터 1까지 카운트다운 리스트 반환
    
    Args:
        n (int): 시작 숫자
        
    Returns:
        list: [n, n-1, ..., 1]
    """
    pass

def sum_numbers(n):
    """
    TODO: 1부터 n까지의 합 계산
    
    Args:
        n (int): 마지막 숫자
        
    Returns:
        int: 합계
    """
    pass

def factorial(n):
    """
    TODO: n! (팩토리얼) 계산
    
    Args:
        n (int): 숫자
        
    Returns:
        int: n!
    """
    pass

def find_primes(limit):
    """
    TODO: limit 이하의 모든 소수 찾기
    
    Args:
        limit (int): 상한값
        
    Returns:
        list: 소수 리스트
    """
    pass

def multiplication_table(n):
    """
    TODO: n단 구구단을 문자열 리스트로 반환
    예: ["2 x 1 = 2", "2 x 2 = 4", ...]
    
    Args:
        n (int): 단 수
        
    Returns:
        list: 구구단 문자열 리스트
    """
    pass

def fibonacci(n):
    """
    TODO: 피보나치 수열의 첫 n개 항 반환
    
    Args:
        n (int): 항의 개수
        
    Returns:
        list: 피보나치 수열
    """
    pass

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        print("count_down(5):", count_down(5))
        
        print("sum_numbers(10):", sum_numbers(10))
        
        print("factorial(5):", factorial(5))
        
        print("find_primes(20):", find_primes(20))
        
        print("multiplication_table(3):", multiplication_table(3))
        
        print("fibonacci(8):", fibonacci(8))
    except Exception as e:
        print(f"오류 발생: {e}")
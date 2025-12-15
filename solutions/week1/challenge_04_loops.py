"""
Challenge 04: 반복문 - 솔루션

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
    return list(range(n, 0, -1))

def sum_numbers(n):
    """
    TODO: 1부터 n까지의 합 계산
    
    Args:
        n (int): 마지막 숫자
        
    Returns:
        int: 합계
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def factorial(n):
    """
    TODO: n! (팩토리얼) 계산
    
    Args:
        n (int): 숫자
        
    Returns:
        int: n!
    """
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def find_primes(limit):
    """
    TODO: limit 이하의 모든 소수 찾기
    
    Args:
        limit (int): 상한값
        
    Returns:
        list: 소수 리스트
    """
    if limit < 2:
        return []
    
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    return primes

def multiplication_table(n):
    """
    TODO: n단 구구단을 문자열 리스트로 반환
    예: ["2 x 1 = 2", "2 x 2 = 4", ...]
    
    Args:
        n (int): 단 수
        
    Returns:
        list: 구구단 문자열 리스트
    """
    result = []
    for i in range(1, 10):
        result.append(f"{n} x {i} = {n * i}")
    return result

def fibonacci(n):
    """
    TODO: 피보나치 수열의 첫 n개 항 반환
    
    Args:
        n (int): 항의 개수
        
    Returns:
        list: 피보나치 수열
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

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
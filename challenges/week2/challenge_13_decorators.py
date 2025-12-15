"""
Challenge 13: 데코레이터

TODO: 다음 함수들과 데코레이터들을 완성하세요

힌트:
- @decorator_name
- functools.wraps 사용하여 메타데이터 보존
- 데코레이터는 함수를 받아서 함수를 반환
"""

def timing_decorator(func):
    """
    TODO: 함수 실행 시간을 측정하는 데코레이터
    
    Args:
        func: 데코레이팅할 함수
        
    Returns:
        function: 래핑된 함수
    """
    pass

def logging_decorator(func):
    """
    TODO: 함수 호출을 로깅하는 데코레이터
    함수명과 인자들을 출력
    
    Args:
        func: 데코레이팅할 함수
        
    Returns:
        function: 래핑된 함수
    """
    pass

def retry_decorator(max_attempts=3):
    """
    TODO: 실패 시 재시도하는 데코레이터
    매개변수를 받는 데코레이터 (데코레이터 팩토리)
    
    Args:
        max_attempts (int): 최대 시도 횟수
        
    Returns:
        function: 데코레이터 함수
    """
    pass

def validate_types(*types):
    """
    TODO: 함수 인자들의 타입을 검증하는 데코레이터
    
    Args:
        *types: 각 인자의 예상 타입들
        
    Returns:
        function: 데코레이터 함수
    """
    pass

def memoize(func):
    """
    TODO: 결과를 캐싱하는 메모이제이션 데코레이터
    
    Args:
        func: 데코레이팅할 함수
        
    Returns:
        function: 래핑된 함수
    """
    pass

class CountCalls:
    """
    TODO: 클래스 기반 데코레이터 - 함수 호출 횟수 카운트
    """
    
    def __init__(self, func):
        pass
    
    def __call__(self, *args, **kwargs):
        pass
    
    @property
    def call_count(self):
        pass

def permission_required(required_role):
    """
    TODO: 권한 검사 데코레이터
    함수 실행 전에 사용자 권한을 확인
    
    Args:
        required_role (str): 필요한 권한
        
    Returns:
        function: 데코레이터 함수
    """
    pass

# 데코레이터들을 테스트할 함수들

@timing_decorator
def slow_function():
    """시간 측정 테스트용 함수"""
    import time
    time.sleep(0.1)
    return "완료"

@logging_decorator
def add_numbers(a, b):
    """로깅 테스트용 함수"""
    return a + b

@retry_decorator(max_attempts=3)
def unreliable_function(success_rate=0.3):
    """재시도 테스트용 함수"""
    import random
    if random.random() < success_rate:
        return "성공"
    else:
        raise Exception("실패")

@validate_types(int, str)
def process_data(number, text):
    """타입 검증 테스트용 함수"""
    return f"{text}: {number}"

@memoize
def fibonacci_memoized(n):
    """메모이제이션 테스트용 피보나치"""
    if n < 2:
        return n
    return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)

@CountCalls
def count_test_function():
    """호출 횟수 카운트 테스트용 함수"""
    return "호출됨"

# 권한 시스템 시뮬레이션
current_user = {"role": "admin"}  # 테스트용 전역 변수

@permission_required("admin")
def admin_function():
    """관리자 권한 필요 함수"""
    return "관리자 작업 완료"

@permission_required("user")  
def user_function():
    """사용자 권한 필요 함수"""
    return "사용자 작업 완료"

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        print("=== Timing Decorator ===")
        result = slow_function()
        print("Result:", result)
        
        print("\n=== Logging Decorator ===")
        result = add_numbers(5, 3)
        print("Result:", result)
        
        print("\n=== Retry Decorator ===")
        try:
            result = unreliable_function(0.8)  # 높은 성공률
            print("Result:", result)
        except Exception as e:
            print("최종 실패:", e)
        
        print("\n=== Type Validation ===")
        try:
            result = process_data(42, "숫자")
            print("Result:", result)
        except Exception as e:
            print("타입 오류:", e)
            
        print("\n=== Memoization ===")
        result = fibonacci_memoized(10)
        print("Fibonacci(10):", result)
        
        print("\n=== Call Counter ===")
        count_test_function()
        count_test_function()
        count_test_function()
        print("Call count:", count_test_function.call_count)
        
        print("\n=== Permission Decorator ===")
        try:
            result = admin_function()
            print("Admin function:", result)
            
            result = user_function()
            print("User function:", result)
        except Exception as e:
            print("권한 오류:", e)
        
    except Exception as e:
        print(f"오류 발생: {e}")
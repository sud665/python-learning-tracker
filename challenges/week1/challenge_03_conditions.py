"""
Challenge 03: 조건문

TODO: 다음 함수들을 완성하세요

힌트:
- if, elif, else 사용
- 비교 연산자: ==, !=, <, >, <=, >=
- 논리 연산자: and, or, not
"""

def check_grade(score):
    """
    TODO: 점수에 따른 등급 반환
    - 90 이상: "A"
    - 80 이상: "B" 
    - 70 이상: "C"
    - 60 이상: "D"
    - 60 미만: "F"
    
    Args:
        score (int): 점수
        
    Returns:
        str: 등급
    """
    pass

def is_even_odd(number):
    """
    TODO: 숫자가 짝수인지 홀수인지 판단
    
    Args:
        number (int): 숫자
        
    Returns:
        str: "even" 또는 "odd"
    """
    pass

def check_login(username, password):
    """
    TODO: 로그인 검증
    올바른 계정: username="admin", password="1234"
    
    Args:
        username (str): 사용자명
        password (str): 비밀번호
        
    Returns:
        bool: 로그인 성공 여부
    """
    pass

def categorize_age(age):
    """
    TODO: 나이대별 분류
    - 0-12: "어린이"
    - 13-19: "청소년"
    - 20-64: "성인"
    - 65 이상: "시니어"
    
    Args:
        age (int): 나이
        
    Returns:
        str: 나이대 분류
    """
    pass

def check_triangle(a, b, c):
    """
    TODO: 삼각형이 될 수 있는지 확인
    삼각형 조건: 가장 긴 변 < 나머지 두 변의 합
    
    Args:
        a, b, c (float): 삼각형의 세 변
        
    Returns:
        bool: 삼각형 가능 여부
    """
    pass

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        print("check_grade(95):", check_grade(95))
        print("check_grade(73):", check_grade(73))
        
        print("is_even_odd(8):", is_even_odd(8))
        print("is_even_odd(7):", is_even_odd(7))
        
        print("check_login('admin', '1234'):", check_login("admin", "1234"))
        print("check_login('user', 'wrong'):", check_login("user", "wrong"))
        
        print("categorize_age(10):", categorize_age(10))
        print("categorize_age(25):", categorize_age(25))
        
        print("check_triangle(3, 4, 5):", check_triangle(3, 4, 5))
        print("check_triangle(1, 2, 5):", check_triangle(1, 2, 5))
    except Exception as e:
        print(f"오류 발생: {e}")
"""
Challenge 02: 함수

TODO: 다음 함수들을 완성하세요

힌트:
- def 키워드로 함수 정의
- return으로 값 반환
- 매개변수에 기본값 설정 가능
"""

def greet(name):
    """
    TODO: 인사말을 반환하는 함수
    
    Args:
        name (str): 이름
        
    Returns:
        str: "안녕하세요, {name}님!"
    """
    pass

def calculate_area(length, width=1):
    """
    TODO: 직사각형의 넓이를 계산
    width의 기본값은 1 (정사각형 처리)
    
    Args:
        length (float): 길이
        width (float): 너비 (기본값: 1)
        
    Returns:
        float: 넓이
    """
    pass

def get_max_min(*args):
    """
    TODO: 가변 인수에서 최대값과 최소값을 반환
    
    Args:
        *args: 숫자들
        
    Returns:
        tuple: (최대값, 최소값)
    """
    pass

def create_profile(**kwargs):
    """
    TODO: 키워드 인수로 프로필 딕셔너리 생성
    
    Args:
        **kwargs: 임의의 키워드 인수들
        
    Returns:
        dict: 프로필 딕셔너리
    """
    pass

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        print("greet('김철수'):", greet("김철수"))
        
        print("calculate_area(5):", calculate_area(5))
        print("calculate_area(5, 3):", calculate_area(5, 3))
        
        print("get_max_min(1, 5, 3, 9, 2):", get_max_min(1, 5, 3, 9, 2))
        
        profile = create_profile(name="홍길동", age=25, city="서울")
        print("create_profile():", profile)
    except Exception as e:
        print(f"오류 발생: {e}")
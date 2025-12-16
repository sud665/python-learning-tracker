"""
Challenge 01: 변수와 타입

TODO: 다음 함수들을 완성하세요

힌트:
- Python의 변수는 타입 선언 없이 사용
- type() 함수로 타입 확인 가능
- __name__ 속성을 사용하여 타입명을 문자열로 가져올 수 있음
"""

def create_variables():
    """
    TODO: 다음 변수들을 만드세요
    - name: 당신의 이름 (문자열)
    - age: 당신의 나이 (정수)
    - height: 당신의 키 (실수)
    - is_student: 학생 여부 (불리언)
    return: 딕셔너리로 반환
    """
    name = "John"
    age = 20
    height = 175.5
    is_student = True
    return {
        "name": name,
        "age": age,
        "height": height,
        "is_student": is_student
    }

def check_types(value):
    """
    TODO: 값의 타입을 문자열로 반환
    예: 123 → "int", "hello" → "str"
    
    Args:
        value: 타입을 확인할 값
        
    Returns:
        str: 타입명
    """
    pass

def convert_types():
    """
    TODO: 다음 변환을 수행하세요
    - 문자열 "123"을 정수로
    - 정수 456을 문자열로  
    - 문자열 "3.14"를 실수로
    - 정수 0을 불리언으로
    
    Returns:
        tuple: (int_val, str_val, float_val, bool_val)
    """
    pass

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    # 테스트 코드
    try:
        result = create_variables()
        print("create_variables():", result)
        
        print("check_types(123):", check_types(123))
        print("check_types('hello'):", check_types("hello"))
        
        converted = convert_types()
        print("convert_types():", converted)
    except Exception as e:
        print(f"오류 발생: {e}")
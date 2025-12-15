"""
Challenge 01: 변수와 타입 - 정답
"""

def create_variables():
    name = "홍길동"
    age = 25
    height = 175.5
    is_student = True
    
    return {
        "name": name,
        "age": age,
        "height": height,
        "is_student": is_student
    }

def check_types(value):
    return type(value).__name__

def convert_types():
    int_val = int("123")
    str_val = str(456)
    float_val = float("3.14")
    bool_val = bool(0)
    
    return (int_val, str_val, float_val, bool_val)

if __name__ == "__main__":
    try:
        result = create_variables()
        print("create_variables():", result)
        
        print("check_types(123):", check_types(123))
        print("check_types('hello'):", check_types("hello"))
        
        converted = convert_types()
        print("convert_types():", converted)
    except Exception as e:
        print(f"오류 발생: {e}")
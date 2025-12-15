"""
Challenge 10: 예외 처리 - 솔루션

TODO: 다음 함수들을 완성하세요

힌트:
- try, except, finally, else
- 특정 예외: ValueError, TypeError, ZeroDivisionError, FileNotFoundError
- raise: 예외 발생시키기
"""

def safe_divide(a, b):
    """
    TODO: 안전한 나눗셈
    0으로 나누는 경우 예외 처리
    
    Args:
        a (float): 피제수
        b (float): 제수
        
    Returns:
        tuple: (결과값, 성공여부)
        예: (2.5, True) 또는 (None, False)
    """
    try:
        result = a / b
        return (result, True)
    except ZeroDivisionError:
        return (None, False)
    except Exception:
        return (None, False)

def safe_convert_to_int(value):
    """
    TODO: 안전한 정수 변환
    변환할 수 없는 경우 예외 처리
    
    Args:
        value: 변환할 값
        
    Returns:
        tuple: (변환된값, 성공여부)
    """
    try:
        converted = int(value)
        return (converted, True)
    except (ValueError, TypeError):
        return (None, False)
    except Exception:
        return (None, False)

def safe_list_access(lst, index):
    """
    TODO: 안전한 리스트 접근
    인덱스가 범위를 벗어난 경우 예외 처리
    
    Args:
        lst (list): 리스트
        index (int): 인덱스
        
    Returns:
        tuple: (값, 성공여부)
    """
    try:
        value = lst[index]
        return (value, True)
    except IndexError:
        return (None, False)
    except Exception:
        return (None, False)

def validate_age(age):
    """
    TODO: 나이 검증
    - 음수이면 ValueError 발생
    - 150 초과이면 ValueError 발생
    - 올바른 경우 True 반환
    
    Args:
        age (int): 나이
        
    Returns:
        bool: 유효성 검사 통과 여부
        
    Raises:
        ValueError: 나이가 유효하지 않은 경우
    """
    if age < 0:
        raise ValueError("나이는 음수일 수 없습니다")
    if age > 150:
        raise ValueError("나이는 150세를 초과할 수 없습니다")
    return True

def file_operations_with_exceptions(filename, content=None):
    """
    TODO: 예외 처리를 포함한 파일 작업
    - content가 None이면 파일 읽기
    - content가 있으면 파일 쓰기
    - 파일 관련 예외들 처리
    
    Args:
        filename (str): 파일명
        content (str, optional): 쓸 내용
        
    Returns:
        tuple: (결과, 성공여부, 오류메시지)
    """
    try:
        if content is None:
            # 파일 읽기
            with open(filename, 'r', encoding='utf-8') as f:
                result = f.read()
            return (result, True, None)
        else:
            # 파일 쓰기
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            return ("파일 쓰기 완료", True, None)
    except FileNotFoundError:
        return (None, False, "파일을 찾을 수 없습니다")
    except PermissionError:
        return (None, False, "파일에 대한 권한이 없습니다")
    except Exception as e:
        return (None, False, f"알 수 없는 오류: {str(e)}")

def chain_operations(numbers):
    """
    TODO: 연속된 작업에서 예외 처리
    1. 리스트에서 첫 번째 요소를 문자열로 변환
    2. 변환된 문자열을 정수로 변환  
    3. 10을 해당 수로 나누기
    각 단계에서 발생할 수 있는 예외 처리
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        dict: {"result": 결과, "success": 성공여부, "error": 오류타입}
    """
    try:
        # 1단계: 첫 번째 요소를 문자열로 변환
        if not numbers:
            return {"result": None, "success": False, "error": "IndexError"}
        
        first_element = numbers[0]
        str_value = str(first_element)
        
        # 2단계: 문자열을 정수로 변환
        int_value = int(str_value)
        
        # 3단계: 10을 해당 수로 나누기
        result = 10 / int_value
        
        return {"result": result, "success": True, "error": None}
        
    except IndexError:
        return {"result": None, "success": False, "error": "IndexError"}
    except ValueError:
        return {"result": None, "success": False, "error": "ValueError"}
    except ZeroDivisionError:
        return {"result": None, "success": False, "error": "ZeroDivisionError"}
    except Exception as e:
        return {"result": None, "success": False, "error": type(e).__name__}

def multiple_exception_handler(operation, a, b):
    """
    TODO: 여러 예외 타입 처리
    operation에 따라 다른 연산 수행:
    - "add": a + b
    - "divide": a / b  
    - "power": a ** b
    - "invalid": 잘못된 연산
    
    Args:
        operation (str): 연산 타입
        a: 첫 번째 값
        b: 두 번째 값
        
    Returns:
        dict: {"result": 결과, "exception_type": 예외타입 또는 None}
    """
    try:
        if operation == "add":
            result = a + b
        elif operation == "divide":
            result = a / b
        elif operation == "power":
            result = a ** b
        elif operation == "invalid":
            raise ValueError("잘못된 연산입니다")
        else:
            raise ValueError("지원하지 않는 연산입니다")
            
        return {"result": result, "exception_type": None}
        
    except ZeroDivisionError:
        return {"result": None, "exception_type": "ZeroDivisionError"}
    except ValueError:
        return {"result": None, "exception_type": "ValueError"}
    except TypeError:
        return {"result": None, "exception_type": "TypeError"}
    except OverflowError:
        return {"result": None, "exception_type": "OverflowError"}
    except Exception as e:
        return {"result": None, "exception_type": type(e).__name__}

def finally_demo(test_case):
    """
    TODO: finally 절 사용 데모
    다양한 케이스에 대해 finally가 실행되는지 확인
    
    Args:
        test_case (str): 테스트 케이스
        - "success": 정상 실행
        - "exception": 예외 발생
        - "return": 중간에 return
        
    Returns:
        list: 실행된 단계들의 리스트
    """
    steps = []
    
    try:
        steps.append("try 블록 시작")
        
        if test_case == "success":
            steps.append("정상 실행")
            
        elif test_case == "exception":
            steps.append("예외 발생 시뮬레이션")
            raise ValueError("테스트 예외")
            
        elif test_case == "return":
            steps.append("중간에 return")
            return steps + ["finally 실행"]
            
        else:
            steps.append("알 수 없는 케이스")
            
    except ValueError:
        steps.append("except 블록 실행")
        
    else:
        steps.append("else 블록 실행")
        
    finally:
        steps.append("finally 블록 실행")
    
    return steps

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        print("Safe divide (10, 2):", safe_divide(10, 2))
        print("Safe divide (10, 0):", safe_divide(10, 0))
        
        print("Safe convert ('123'):", safe_convert_to_int("123"))
        print("Safe convert ('abc'):", safe_convert_to_int("abc"))
        
        lst = [1, 2, 3]
        print("Safe list access (lst, 1):", safe_list_access(lst, 1))
        print("Safe list access (lst, 5):", safe_list_access(lst, 5))
        
        try:
            validate_age(25)
            print("Age 25: Valid")
        except ValueError as e:
            print(f"Age 25: {e}")
            
        try:
            validate_age(-5)
            print("Age -5: Valid")
        except ValueError as e:
            print(f"Age -5: {e}")
        
        file_result = file_operations_with_exceptions("nonexistent.txt")
        print("File operations:", file_result)
        
        chain_result = chain_operations([2])
        print("Chain operations:", chain_result)
        
        mult_result = multiple_exception_handler("divide", 10, 0)
        print("Multiple exception handler:", mult_result)
        
        finally_result = finally_demo("exception")
        print("Finally demo:", finally_result)
        
    except Exception as e:
        print(f"오류 발생: {e}")
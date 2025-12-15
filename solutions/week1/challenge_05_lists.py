"""
Challenge 05: 리스트 - 솔루션

TODO: 다음 함수들을 완성하세요

힌트:
- 리스트 생성: [1, 2, 3] 또는 list()
- 인덱싱: lst[0], lst[-1]
- 슬라이싱: lst[1:3], lst[:2], lst[2:]
- 메서드: append(), remove(), sort(), reverse()
"""

def create_number_list(start, end):
    """
    TODO: start부터 end까지의 숫자 리스트 생성
    
    Args:
        start (int): 시작 숫자
        end (int): 끝 숫자 (포함)
        
    Returns:
        list: 숫자 리스트
    """
    return list(range(start, end + 1))

def list_operations(numbers):
    """
    TODO: 리스트에 대한 기본 연산 수행
    - 첫 번째 요소
    - 마지막 요소  
    - 중간 요소들 (첫 번째와 마지막 제외)
    - 리스트 길이
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        tuple: (first, last, middle, length)
    """
    if not numbers:
        return (None, None, [], 0)
    
    first = numbers[0]
    last = numbers[-1]
    middle = numbers[1:-1] if len(numbers) > 2 else []
    length = len(numbers)
    
    return (first, last, middle, length)

def modify_list(items):
    """
    TODO: 리스트 수정 연산
    1. 마지막에 "new" 추가
    2. 첫 번째 요소 제거
    3. "target"이 있으면 제거
    4. 리스트 정렬
    
    Args:
        items (list): 수정할 리스트
        
    Returns:
        list: 수정된 리스트 (원본 수정하지 말고 복사본 사용)
    """
    # 복사본 생성
    modified_items = items.copy()
    
    # 1. 마지막에 "new" 추가
    modified_items.append("new")
    
    # 2. 첫 번째 요소 제거 (리스트가 비어있지 않은 경우)
    if modified_items:
        modified_items.pop(0)
    
    # 3. "target"이 있으면 제거
    if "target" in modified_items:
        modified_items.remove("target")
    
    # 4. 리스트 정렬
    modified_items.sort()
    
    return modified_items

def find_max_min(numbers):
    """
    TODO: 리스트에서 최대값과 최소값 찾기
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        tuple: (최대값, 최소값)
    """
    if not numbers:
        return (None, None)
    
    return (max(numbers), min(numbers))

def remove_duplicates(items):
    """
    TODO: 리스트에서 중복 제거 (순서 유지)
    
    Args:
        items (list): 원본 리스트
        
    Returns:
        list: 중복이 제거된 리스트
    """
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

def list_statistics(numbers):
    """
    TODO: 리스트 통계 계산
    - 합계
    - 평균 
    - 최대값
    - 최소값
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        dict: {"sum": 합계, "avg": 평균, "max": 최대값, "min": 최소값}
    """
    if not numbers:
        return {"sum": 0, "avg": 0, "max": None, "min": None}
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return {
        "sum": total,
        "avg": average,
        "max": maximum,
        "min": minimum
    }

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        print("create_number_list(1, 5):", create_number_list(1, 5))
        
        numbers = [1, 2, 3, 4, 5]
        print("list_operations([1,2,3,4,5]):", list_operations(numbers))
        
        items = ["apple", "target", "banana", "cherry"]
        print("modify_list(['apple', 'target', 'banana', 'cherry']):", modify_list(items))
        
        numbers = [3, 1, 4, 1, 5, 9, 2, 6]
        print("find_max_min([3,1,4,1,5,9,2,6]):", find_max_min(numbers))
        
        items = [1, 2, 3, 2, 4, 3, 5]
        print("remove_duplicates([1,2,3,2,4,3,5]):", remove_duplicates(items))
        
        numbers = [10, 20, 30, 40, 50]
        print("list_statistics([10,20,30,40,50]):", list_statistics(numbers))
    except Exception as e:
        print(f"오류 발생: {e}")
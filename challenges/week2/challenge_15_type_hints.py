"""
Challenge 15: 타입 힌트

TODO: 다음 함수들에 적절한 타입 힌트를 추가하세요

힌트:
- from typing import List, Dict, Optional, Union, Callable, Tuple
- 변수: variable_name: type = value
- 함수: def func(param: type) -> return_type:
- 제네릭: List[int], Dict[str, int]
"""

from typing import List, Dict, Optional, Union, Callable, Tuple, Any

def greet_user(name, age=None):
    """
    TODO: 타입 힌트 추가
    name은 문자열, age는 정수 또는 None, 반환값은 문자열
    """
    if age:
        return f"안녕하세요, {age}세 {name}님!"
    return f"안녕하세요, {name}님!"

def process_numbers(numbers):
    """
    TODO: 타입 힌트 추가  
    numbers는 정수 리스트, 반환값은 정수들의 딕셔너리
    """
    return {
        "sum": sum(numbers),
        "count": len(numbers),
        "average": sum(numbers) / len(numbers) if numbers else 0
    }

def find_user_by_id(users, user_id):
    """
    TODO: 타입 힌트 추가
    users는 딕셔너리 리스트 (각 딕셔너리는 문자열 키, Any 값)
    user_id는 정수
    반환값은 딕셔너리 또는 None
    """
    for user in users:
        if user.get("id") == user_id:
            return user
    return None

def apply_operation(value, operation):
    """
    TODO: 타입 힌트 추가
    value는 정수
    operation은 정수를 받아서 정수를 반환하는 함수
    반환값은 정수
    """
    return operation(value)

def parse_coordinates(coord_string):
    """
    TODO: 타입 힌트 추가
    coord_string은 문자열 (예: "10,20")
    반환값은 두 개의 실수 튜플
    """
    x, y = coord_string.split(",")
    return float(x), float(y)

def merge_configs(default_config, user_config=None):
    """
    TODO: 타입 힌트 추가
    default_config는 문자열 키, Any 값의 딕셔너리
    user_config는 문자열 키, Any 값의 딕셔너리 또는 None
    반환값은 문자열 키, Any 값의 딕셔너리
    """
    if user_config is None:
        user_config = {}
    
    merged = default_config.copy()
    merged.update(user_config)
    return merged

def process_mixed_data(data):
    """
    TODO: 타입 힌트 추가
    data는 문자열 또는 정수 또는 실수의 리스트
    반환값은 문자열 리스트
    """
    return [str(item) for item in data]

class DataProcessor:
    """
    TODO: 클래스와 메서드에 타입 힌트 추가
    """
    
    def __init__(self, name):
        """name은 문자열"""
        self.name = name
        self.data = []
    
    def add_item(self, item):
        """item은 Any 타입, 반환값 없음"""
        self.data.append(item)
    
    def get_items(self):
        """반환값은 Any 타입의 리스트"""
        return self.data
    
    def process_with_callback(self, callback):
        """
        callback은 Any를 받아서 Any를 반환하는 함수
        반환값은 Any 타입의 리스트
        """
        return [callback(item) for item in self.data]

def create_multiplier(factor):
    """
    TODO: 타입 힌트 추가 - 고차 함수
    factor는 정수
    반환값은 정수를 받아서 정수를 반환하는 함수
    """
    def multiply(x):
        return x * factor
    return multiply

def batch_process(items, processor, batch_size=10):
    """
    TODO: 타입 힌트 추가
    items는 Any 타입의 리스트
    processor는 Any 리스트를 받아서 Any 리스트를 반환하는 함수
    batch_size는 정수
    반환값은 Any 타입의 리스트
    """
    results = []
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        batch_results = processor(batch)
        results.extend(batch_results)
    return results

# 타입 별칭 정의
UserInfo = Dict[str, Union[str, int, bool]]
ProcessingResult = Dict[str, Union[int, float, List[Any]]]

def create_user_profile(name, age, email, is_premium=False):
    """
    TODO: 타입 별칭을 사용한 타입 힌트
    UserInfo 타입 별칭 사용
    """
    return {
        "name": name,
        "age": age,
        "email": email,
        "is_premium": is_premium
    }

def analyze_data(data):
    """
    TODO: 타입 별칭을 사용한 타입 힌트
    data는 정수 리스트
    반환값은 ProcessingResult 타입 별칭 사용
    """
    if not data:
        return {"count": 0, "sum": 0, "average": 0.0, "items": []}
    
    return {
        "count": len(data),
        "sum": sum(data),
        "average": sum(data) / len(data),
        "items": data
    }

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        print("=== Type Hints Testing ===")
        
        # greet_user 테스트
        print("Greet user:", greet_user("김철수", 25))
        print("Greet user (no age):", greet_user("이영희"))
        
        # process_numbers 테스트
        numbers = [1, 2, 3, 4, 5]
        print("Process numbers:", process_numbers(numbers))
        
        # find_user_by_id 테스트
        users = [{"id": 1, "name": "김철수"}, {"id": 2, "name": "이영희"}]
        user = find_user_by_id(users, 1)
        print("Find user:", user)
        
        # apply_operation 테스트
        result = apply_operation(5, lambda x: x * 2)
        print("Apply operation:", result)
        
        # parse_coordinates 테스트
        coords = parse_coordinates("10.5,20.3")
        print("Parse coordinates:", coords)
        
        # merge_configs 테스트
        default = {"debug": False, "timeout": 30}
        user_conf = {"debug": True}
        merged = merge_configs(default, user_conf)
        print("Merge configs:", merged)
        
        # process_mixed_data 테스트
        mixed = [1, "hello", 3.14, True]
        processed = process_mixed_data(mixed)
        print("Process mixed:", processed)
        
        # DataProcessor 테스트
        processor = DataProcessor("test")
        processor.add_item("item1")
        processor.add_item(42)
        items = processor.get_items()
        print("Data processor items:", items)
        
        processed_items = processor.process_with_callback(str)
        print("Processed with callback:", processed_items)
        
        # create_multiplier 테스트
        multiply_by_3 = create_multiplier(3)
        result = multiply_by_3(5)
        print("Multiplier result:", result)
        
        # batch_process 테스트
        items = list(range(25))
        batched = batch_process(items, lambda batch: [x * 2 for x in batch], 10)
        print("Batch process (first 10):", batched[:10])
        
        # 타입 별칭 테스트
        profile = create_user_profile("홍길동", 30, "hong@example.com", True)
        print("User profile:", profile)
        
        analysis = analyze_data([1, 2, 3, 4, 5])
        print("Data analysis:", analysis)
        
        print("\n타입 힌트가 올바르게 추가되었습니다!")
        
    except Exception as e:
        print(f"오류 발생: {e}")
"""
Challenge 08: 모듈과 패키지 - 솔루션

TODO: 다음 함수들을 완성하세요

힌트:
- import 모듈명
- from 모듈명 import 함수명
- 내장 모듈: math, random, datetime, os
"""

import math
import random
import datetime
import os
import json
import sys
from collections import Counter

def use_math_functions():
    """
    TODO: math 모듈 사용하기
    - 3.7의 올림값 (ceil)
    - 3.7의 내림값 (floor)  
    - 2의 3제곱 (pow)
    - 16의 제곱근 (sqrt)
    
    Returns:
        tuple: (ceil_val, floor_val, pow_val, sqrt_val)
    """
    ceil_val = math.ceil(3.7)
    floor_val = math.floor(3.7)
    pow_val = math.pow(2, 3)
    sqrt_val = math.sqrt(16)
    
    return (ceil_val, floor_val, pow_val, sqrt_val)

def generate_random_data():
    """
    TODO: random 모듈 사용하기
    - 1~10 사이의 랜덤 정수
    - 0~1 사이의 랜덤 실수  
    - [1,2,3,4,5]에서 랜덤 선택
    - [1,2,3,4,5]를 섞은 리스트
    
    Returns:
        tuple: (random_int, random_float, random_choice, shuffled_list)
    """
    random_int = random.randint(1, 10)
    random_float = random.random()
    random_choice = random.choice([1, 2, 3, 4, 5])
    
    # 원본 리스트를 변경하지 않기 위해 복사
    numbers = [1, 2, 3, 4, 5]
    shuffled_list = numbers.copy()
    random.shuffle(shuffled_list)
    
    return (random_int, random_float, random_choice, shuffled_list)

def get_current_time_info():
    """
    TODO: datetime 모듈 사용하기
    - 현재 날짜와 시간
    - 현재 연도
    - 현재 월
    - 현재 일
    
    Returns:
        tuple: (current_datetime, year, month, day)
    """
    now = datetime.datetime.now()
    current_datetime = now
    year = now.year
    month = now.month
    day = now.day
    
    return (current_datetime, year, month, day)

def file_operations():
    """
    TODO: os 모듈 사용하기 
    - 현재 작업 디렉토리 경로
    - 현재 디렉토리의 파일/폴더 목록 (최대 5개)
    - 이 파일의 존재 여부 확인 (__file__ 사용)
    
    Returns:
        tuple: (current_dir, file_list, file_exists)
    """
    current_dir = os.getcwd()
    file_list = os.listdir(current_dir)[:5]  # 최대 5개만
    file_exists = os.path.exists(__file__)
    
    return (current_dir, file_list, file_exists)

def create_custom_module_demo():
    """
    TODO: 사용자 정의 함수들로 모듈처럼 사용하기
    다음 함수들을 만들어서 활용:
    - greet(name): "Hello, {name}!" 반환
    - add_numbers(a, b): a + b 반환
    - get_even_numbers(limit): limit까지의 짝수 리스트 반환
    
    Returns:
        dict: {"greeting": greet("Python"), "sum": add_numbers(5, 3), "evens": get_even_numbers(10)}
    """
    def greet(name):
        return f"Hello, {name}!"
    
    def add_numbers(a, b):
        return a + b
    
    def get_even_numbers(limit):
        return [i for i in range(2, limit + 1, 2)]
    
    return {
        "greeting": greet("Python"),
        "sum": add_numbers(5, 3),
        "evens": get_even_numbers(10)
    }

def import_demonstration():
    """
    TODO: 다양한 import 방식 데모
    1. import json - JSON 문자열을 딕셔너리로 파싱
    2. from collections import Counter - 리스트 요소 개수 세기
    3. import sys - Python 버전 정보 가져오기
    
    Returns:
        dict: 각 모듈 사용 결과
    """
    # 1. json 모듈 사용
    json_string = '{"name": "Python", "version": 3.9}'
    parsed_json = json.loads(json_string)
    
    # 2. Counter 사용
    sample_list = ['a', 'b', 'a', 'c', 'b', 'a']
    counter_result = dict(Counter(sample_list))
    
    # 3. sys 모듈 사용
    python_version = sys.version_info
    
    return {
        "json_parsing": parsed_json,
        "counter_result": counter_result,
        "python_version": f"{python_version.major}.{python_version.minor}.{python_version.micro}"
    }

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        print("Math functions:", use_math_functions())
        
        print("Random data:", generate_random_data())
        
        print("Time info:", get_current_time_info())
        
        print("File operations:", file_operations())
        
        print("Custom module demo:", create_custom_module_demo())
        
        print("Import demonstration:", import_demonstration())
        
    except Exception as e:
        print(f"오류 발생: {e}")
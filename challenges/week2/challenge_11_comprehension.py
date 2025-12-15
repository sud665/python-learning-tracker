"""
Challenge 11: 리스트 컴프리헨션

TODO: 다음 함수들을 완성하세요

힌트:
- 리스트 컴프리헨션: [expression for item in iterable if condition]
- 딕셔너리 컴프리헨션: {key: value for item in iterable}
- 셋 컴프리헨션: {expression for item in iterable}
"""

def squares_of_evens(n):
    """
    TODO: 1부터 n까지 숫자 중 짝수들의 제곱을 리스트 컴프리헨션으로 구하기
    
    Args:
        n (int): 범위
        
    Returns:
        list: 짝수들의 제곱 리스트
    """
    pass

def filter_and_transform(words):
    """
    TODO: 단어 리스트에서 길이가 3 이상인 단어들을 대문자로 변환
    
    Args:
        words (list): 단어 리스트
        
    Returns:
        list: 변환된 단어 리스트
    """
    pass

def nested_list_comprehension():
    """
    TODO: 중첩 리스트 컴프리헨션으로 구구단 테이블 생성
    1단부터 9단까지, 1부터 9까지의 곱
    
    Returns:
        list: [[1*1, 1*2, ..., 1*9], [2*1, 2*2, ..., 2*9], ...]
    """
    pass

def word_lengths_dict(sentence):
    """
    TODO: 문장에서 각 단어의 길이를 딕셔너리로 만들기
    공백으로 분리, 중복 단어는 마지막 값 사용
    
    Args:
        sentence (str): 입력 문장
        
    Returns:
        dict: {단어: 길이}
    """
    pass

def unique_characters(text):
    """
    TODO: 텍스트에서 유니크한 문자들의 집합 (공백 제외)
    
    Args:
        text (str): 입력 텍스트
        
    Returns:
        set: 유니크한 문자들의 집합
    """
    pass

def matrix_transpose(matrix):
    """
    TODO: 리스트 컴프리헨션으로 행렬 전치
    
    Args:
        matrix (list): 2차원 리스트
        
    Returns:
        list: 전치된 행렬
    """
    pass

def conditional_mapping(numbers):
    """
    TODO: 숫자 리스트를 조건에 따라 매핑
    - 양수: 제곱
    - 0: 0
    - 음수: 절댓값
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        list: 매핑된 숫자 리스트
    """
    pass

def nested_dict_comprehension():
    """
    TODO: 중첩 딕셔너리 컴프리헨션
    1-3의 숫자에 대해 각각 1-3까지의 곱셈표
    
    Returns:
        dict: {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}
    """
    pass

def flatten_with_condition(nested_list, threshold):
    """
    TODO: 중첩 리스트를 평면화하되 threshold보다 큰 값만
    
    Args:
        nested_list (list): 중첩 리스트
        threshold (int): 임계값
        
    Returns:
        list: 조건을 만족하는 평면화된 리스트
    """
    pass

def group_by_length(words):
    """
    TODO: 단어들을 길이별로 그룹화 (딕셔너리 컴프리헨션 + 조건부 로직)
    
    Args:
        words (list): 단어 리스트
        
    Returns:
        dict: {길이: [해당 길이의 단어들]}
    """
    pass

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        print("Squares of evens (1-10):", squares_of_evens(10))
        
        words = ["a", "hello", "world", "hi", "python"]
        print("Filter and transform:", filter_and_transform(words))
        
        multiplication_table = nested_list_comprehension()
        print("Multiplication table (first row):", multiplication_table[0])
        
        sentence = "hello world python hello"
        print("Word lengths:", word_lengths_dict(sentence))
        
        text = "Hello World!"
        print("Unique characters:", unique_characters(text))
        
        matrix = [[1, 2, 3], [4, 5, 6]]
        print("Matrix transpose:", matrix_transpose(matrix))
        
        numbers = [-2, -1, 0, 1, 2]
        print("Conditional mapping:", conditional_mapping(numbers))
        
        nested_dict = nested_dict_comprehension()
        print("Nested dict (key 2):", nested_dict[2])
        
        nested = [[1, 2], [3, 4, 5], [6]]
        print("Flatten with condition (>3):", flatten_with_condition(nested, 3))
        
        words = ["cat", "dog", "elephant", "bee", "python"]
        print("Group by length:", group_by_length(words))
        
    except Exception as e:
        print(f"오류 발생: {e}")
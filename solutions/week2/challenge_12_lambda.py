"""
Challenge 12: 람다 함수와 함수형 프로그래밍 - 솔루션

TODO: 다음 함수들을 완성하세요

힌트:
- lambda 인수: 표현식
- map(), filter(), reduce() 함수와 함께 사용
- functools.reduce import 필요
"""

from functools import reduce

def basic_lambda_operations():
    """
    TODO: 기본 람다 함수들 생성
    - 제곱하는 람다
    - 두 수를 더하는 람다
    - 문자열의 길이를 반환하는 람다
    
    Returns:
        tuple: (square_func, add_func, length_func)
    """
    square_func = lambda x: x ** 2
    add_func = lambda x, y: x + y
    length_func = lambda s: len(s)
    
    return (square_func, add_func, length_func)

def use_map_with_lambda(numbers):
    """
    TODO: map과 람다를 사용하여 리스트의 각 요소에 3을 곱하기
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        list: 3을 곱한 결과 리스트
    """
    return list(map(lambda x: x * 3, numbers))

def use_filter_with_lambda(words):
    """
    TODO: filter와 람다를 사용하여 길이가 4 이상인 단어만 필터링
    
    Args:
        words (list): 단어 리스트
        
    Returns:
        list: 길이가 4 이상인 단어들
    """
    return list(filter(lambda word: len(word) >= 4, words))

def use_reduce_with_lambda(numbers):
    """
    TODO: reduce와 람다를 사용하여 리스트의 모든 요소의 곱 구하기
    
    Args:
        numbers (list): 숫자 리스트
        
    Returns:
        int: 모든 요소의 곱
    """
    return reduce(lambda x, y: x * y, numbers)

def sort_with_lambda(students):
    """
    TODO: 람다를 사용하여 학생 리스트를 나이순으로 정렬
    
    Args:
        students (list): [{"name": "이름", "age": 나이}, ...] 형태의 리스트
        
    Returns:
        list: 나이순으로 정렬된 학생 리스트
    """
    return sorted(students, key=lambda student: student["age"])

def complex_lambda_operations(data):
    """
    TODO: 복잡한 람다 연산들
    1. 각 딕셔너리에서 'score' 키의 값들을 추출
    2. 70 이상인 점수들만 필터링
    3. 필터링된 점수들의 평균 계산
    
    Args:
        data (list): [{"name": "이름", "score": 점수}, ...] 형태의 리스트
        
    Returns:
        float: 70 이상 점수들의 평균
    """
    # 1. score 값들을 추출
    scores = list(map(lambda item: item["score"], data))
    
    # 2. 70 이상인 점수들만 필터링
    high_scores = list(filter(lambda score: score >= 70, scores))
    
    # 3. 평균 계산
    if not high_scores:
        return 0.0
    return sum(high_scores) / len(high_scores)

def lambda_with_multiple_conditions(products):
    """
    TODO: 여러 조건을 가진 람다로 제품 필터링
    가격이 100 이상이고 재고가 10 이상인 제품들만 선택
    
    Args:
        products (list): [{"name": "제품명", "price": 가격, "stock": 재고}, ...]
        
    Returns:
        list: 조건을 만족하는 제품들
    """
    return list(filter(lambda product: product["price"] >= 100 and product["stock"] >= 10, products))

def higher_order_function_demo():
    """
    TODO: 람다를 반환하는 함수 만들기
    multiplier(n)을 호출하면 n을 곱하는 람다 함수를 반환
    
    Returns:
        tuple: (multiplier_function, result_of_multiplier_3_applied_to_5)
    """
    def multiplier(n):
        return lambda x: x * n
    
    multiplier_function = multiplier
    multiply_by_3 = multiplier(3)
    result = multiply_by_3(5)
    
    return (multiplier_function, result)

def lambda_with_zip(list1, list2):
    """
    TODO: zip과 람다를 사용하여 두 리스트의 요소들을 조합
    각 위치의 요소들의 합을 구하기
    
    Args:
        list1 (list): 첫 번째 리스트
        list2 (list): 두 번째 리스트
        
    Returns:
        list: 각 위치별 합의 리스트
    """
    return list(map(lambda pair: pair[0] + pair[1], zip(list1, list2)))

def nested_lambda_operations(matrix):
    """
    TODO: 중첩된 람다와 map을 사용하여 2차원 리스트의 모든 요소에 2를 곱하기
    
    Args:
        matrix (list): 2차원 리스트
        
    Returns:
        list: 모든 요소에 2를 곱한 2차원 리스트
    """
    return list(map(lambda row: list(map(lambda x: x * 2, row)), matrix))

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        square, add, length = basic_lambda_operations()
        print("Lambda functions:", square(5), add(3, 4), length("hello"))
        
        numbers = [1, 2, 3, 4, 5]
        print("Map with lambda:", use_map_with_lambda(numbers))
        
        words = ["hi", "hello", "world", "python", "code"]
        print("Filter with lambda:", use_filter_with_lambda(words))
        
        numbers = [1, 2, 3, 4]
        print("Reduce with lambda:", use_reduce_with_lambda(numbers))
        
        students = [{"name": "김철수", "age": 20}, {"name": "이영희", "age": 18}, {"name": "박민수", "age": 22}]
        print("Sort with lambda:", sort_with_lambda(students))
        
        data = [{"name": "A", "score": 85}, {"name": "B", "score": 60}, {"name": "C", "score": 92}]
        print("Complex lambda operations:", complex_lambda_operations(data))
        
        products = [{"name": "A", "price": 150, "stock": 5}, {"name": "B", "price": 80, "stock": 15}, {"name": "C", "price": 200, "stock": 20}]
        print("Multiple conditions:", lambda_with_multiple_conditions(products))
        
        multiplier_func, result = higher_order_function_demo()
        print("Higher order function:", result)
        
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        print("Lambda with zip:", lambda_with_zip(list1, list2))
        
        matrix = [[1, 2], [3, 4], [5, 6]]
        print("Nested lambda operations:", nested_lambda_operations(matrix))
        
    except Exception as e:
        print(f"오류 발생: {e}")
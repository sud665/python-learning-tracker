"""
Challenge 06: 딕셔너리

TODO: 다음 함수들을 완성하세요

힌트:
- 딕셔너리 생성: {"key": "value"} 또는 dict()
- 접근: dict[key], dict.get(key, default)
- 메서드: keys(), values(), items(), update()
"""

def create_student(name, age, grade, subjects):
    """
    TODO: 학생 정보 딕셔너리 생성
    
    Args:
        name (str): 이름
        age (int): 나이
        grade (int): 학년
        subjects (list): 수강 과목 리스트
        
    Returns:
        dict: 학생 정보 딕셔너리
    """
    pass

def get_student_info(student, key, default=None):
    """
    TODO: 학생 정보에서 특정 키의 값을 안전하게 가져오기
    
    Args:
        student (dict): 학생 딕셔너리
        key (str): 찾을 키
        default: 키가 없을 때 반환할 기본값
        
    Returns:
        값 또는 기본값
    """
    pass

def update_grades(student, subject_grades):
    """
    TODO: 학생의 성적 정보를 업데이트
    기존 student 딕셔너리에 "grades" 키를 추가하거나 업데이트
    
    Args:
        student (dict): 학생 딕셔너리
        subject_grades (dict): 과목별 성적 {"수학": 90, "영어": 85}
        
    Returns:
        dict: 업데이트된 학생 딕셔너리
    """
    pass

def calculate_average(grades):
    """
    TODO: 과목별 성적의 평균 계산
    
    Args:
        grades (dict): 과목별 성적 딕셔너리
        
    Returns:
        float: 평균 점수
    """
    pass

def merge_dictionaries(*dicts):
    """
    TODO: 여러 딕셔너리를 합치기
    나중에 오는 딕셔너리의 값이 우선
    
    Args:
        *dicts: 합칠 딕셔너리들
        
    Returns:
        dict: 합쳐진 딕셔너리
    """
    pass

def count_words(text):
    """
    TODO: 텍스트에서 단어 빈도 계산
    공백으로 분리, 대소문자 구분 안함
    
    Args:
        text (str): 분석할 텍스트
        
    Returns:
        dict: 단어별 빈도수
    """
    pass

def invert_dictionary(original):
    """
    TODO: 딕셔너리의 키와 값을 바꾸기
    값이 유일하다고 가정
    
    Args:
        original (dict): 원본 딕셔너리
        
    Returns:
        dict: 키와 값이 바뀐 딕셔너리
    """
    pass

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        student = create_student("김철수", 16, 2, ["수학", "영어", "과학"])
        print("create_student():", student)
        
        name = get_student_info(student, "name")
        print("get_student_info(student, 'name'):", name)
        
        updated = update_grades(student, {"수학": 90, "영어": 85, "과학": 88})
        print("update_grades():", updated)
        
        if "grades" in updated:
            avg = calculate_average(updated["grades"])
            print("calculate_average():", avg)
        
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        merged = merge_dictionaries(dict1, dict2)
        print("merge_dictionaries():", merged)
        
        text = "hello world hello python world"
        word_count = count_words(text)
        print("count_words():", word_count)
        
        original = {"name": "김철수", "age": 20, "city": "서울"}
        inverted = invert_dictionary(original)
        print("invert_dictionary():", inverted)
    except Exception as e:
        print(f"오류 발생: {e}")
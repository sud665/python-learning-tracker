"""
Challenge 09: 파일 처리

TODO: 다음 함수들을 완성하세요

힌트:
- open(filename, mode): 파일 열기
- with open(...) as f: 자동으로 파일 닫기  
- modes: 'r' (읽기), 'w' (쓰기), 'a' (추가)
- 메서드: read(), readline(), readlines(), write(), writelines()
"""

def create_sample_file(filename, content):
    """
    TODO: 파일에 내용 쓰기
    
    Args:
        filename (str): 파일명
        content (str): 파일에 쓸 내용
        
    Returns:
        bool: 성공 여부
    """
    pass

def read_entire_file(filename):
    """
    TODO: 파일 전체 내용 읽기
    
    Args:
        filename (str): 파일명
        
    Returns:
        str: 파일 내용 (파일이 없으면 None)
    """
    pass

def read_file_lines(filename):
    """
    TODO: 파일을 줄별로 읽어서 리스트로 반환
    각 줄의 끝 개행문자는 제거
    
    Args:
        filename (str): 파일명
        
    Returns:
        list: 줄별 내용 리스트 (파일이 없으면 빈 리스트)
    """
    pass

def append_to_file(filename, content):
    """
    TODO: 파일에 내용 추가
    
    Args:
        filename (str): 파일명
        content (str): 추가할 내용
        
    Returns:
        bool: 성공 여부
    """
    pass

def count_file_stats(filename):
    """
    TODO: 파일 통계 계산
    - 총 줄 수
    - 총 단어 수 (공백으로 분리)
    - 총 문자 수
    
    Args:
        filename (str): 파일명
        
    Returns:
        dict: {"lines": 줄수, "words": 단어수, "characters": 문자수}
        파일이 없으면 None
    """
    pass

def search_in_file(filename, search_term):
    """
    TODO: 파일에서 특정 단어가 포함된 줄 찾기
    
    Args:
        filename (str): 파일명  
        search_term (str): 검색할 단어
        
    Returns:
        list: 검색된 줄들의 리스트 (줄번호, 내용) 튜플
        예: [(1, "첫 번째 줄"), (3, "세 번째 줄")]
    """
    pass

def process_csv_like_data(filename, delimiter=','):
    """
    TODO: CSV 형태의 데이터 처리
    첫 번째 줄은 헤더, 나머지는 데이터로 처리
    
    Args:
        filename (str): 파일명
        delimiter (str): 구분자 (기본값: ',')
        
    Returns:
        dict: {"headers": [...], "data": [[...], [...]]}
        파일이 없으면 None
    """
    pass

def backup_file(source_filename, backup_filename):
    """
    TODO: 파일 백업 (복사)
    
    Args:
        source_filename (str): 원본 파일명
        backup_filename (str): 백업 파일명
        
    Returns:
        bool: 성공 여부
    """
    pass

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        # 테스트용 파일 생성
        test_content = """첫 번째 줄입니다.
두 번째 줄에는 Python이 포함되어 있습니다.
세 번째 줄입니다.
네 번째 줄에도 Python이 있습니다."""
        
        print("파일 생성:", create_sample_file("test.txt", test_content))
        
        print("파일 읽기:", read_entire_file("test.txt")[:50] + "..." if read_entire_file("test.txt") else None)
        
        lines = read_file_lines("test.txt")
        print("줄별 읽기:", len(lines), "줄")
        
        print("파일 추가:", append_to_file("test.txt", "\n다섯 번째 줄을 추가했습니다."))
        
        stats = count_file_stats("test.txt")
        print("파일 통계:", stats)
        
        search_results = search_in_file("test.txt", "Python")
        print("검색 결과:", search_results)
        
        # CSV 테스트용 파일
        csv_content = "이름,나이,도시\n김철수,25,서울\n이영희,30,부산\n박민수,28,대구"
        create_sample_file("test.csv", csv_content)
        csv_data = process_csv_like_data("test.csv")
        print("CSV 처리:", csv_data)
        
        print("파일 백업:", backup_file("test.txt", "test_backup.txt"))
        
    except Exception as e:
        print(f"오류 발생: {e}")
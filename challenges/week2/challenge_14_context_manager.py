"""
Challenge 14: 컨텍스트 매니저

TODO: 다음 컨텍스트 매니저들을 완성하세요

힌트:
- with 문과 함께 사용
- __enter__와 __exit__ 메서드 구현
- contextlib 모듈의 @contextmanager 데코레이터
"""

import time
from contextlib import contextmanager

class Timer:
    """
    TODO: 시간 측정 컨텍스트 매니저
    with Timer() as t: 형태로 사용
    """
    
    def __enter__(self):
        """
        TODO: 컨텍스트 진입 시 시작 시간 기록
        
        Returns:
            self: 컨텍스트 매니저 자신
        """
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        TODO: 컨텍스트 종료 시 경과 시간 출력
        
        Args:
            exc_type: 예외 타입
            exc_val: 예외 값
            exc_tb: 예외 트레이스백
            
        Returns:
            bool: 예외를 처리했는지 여부 (False = 예외 전파)
        """
        pass
    
    @property
    def elapsed_time(self):
        """경과 시간 반환"""
        pass

class FileManager:
    """
    TODO: 파일 관리 컨텍스트 매니저
    파일을 안전하게 열고 닫기
    """
    
    def __init__(self, filename, mode='r'):
        """
        Args:
            filename (str): 파일명
            mode (str): 파일 모드
        """
        pass
    
    def __enter__(self):
        """
        TODO: 파일 열기
        
        Returns:
            file object: 열린 파일 객체
        """
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        TODO: 파일 닫기
        예외가 발생해도 파일이 닫히도록 보장
        """
        pass

class DatabaseConnection:
    """
    TODO: 데이터베이스 연결 시뮬레이션 컨텍스트 매니저
    """
    
    def __init__(self, connection_string):
        """
        Args:
            connection_string (str): 연결 문자열
        """
        pass
    
    def __enter__(self):
        """
        TODO: 데이터베이스 연결
        
        Returns:
            self: 컨텍스트 매니저 자신
        """
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        TODO: 데이터베이스 연결 해제
        예외 발생 시 롤백 수행
        """
        pass
    
    def execute(self, query):
        """
        TODO: 쿼리 실행 시뮬레이션
        
        Args:
            query (str): SQL 쿼리
            
        Returns:
            str: 실행 결과
        """
        pass

@contextmanager
def temporary_directory():
    """
    TODO: 임시 디렉토리 생성/삭제 컨텍스트 매니저
    @contextmanager 데코레이터 사용
    
    Yields:
        str: 임시 디렉토리 경로
    """
    pass

@contextmanager
def error_handler(error_message="오류가 발생했습니다"):
    """
    TODO: 예외 처리 컨텍스트 매니저
    예외를 잡고 사용자 정의 메시지 출력
    
    Args:
        error_message (str): 오류 시 출력할 메시지
    """
    pass

@contextmanager  
def change_directory(path):
    """
    TODO: 디렉토리 변경 컨텍스트 매니저
    임시로 디렉토리를 변경했다가 원래대로 복구
    
    Args:
        path (str): 변경할 디렉토리 경로
    """
    pass

class ResourcePool:
    """
    TODO: 리소스 풀 컨텍스트 매니저
    제한된 리소스의 할당과 해제를 관리
    """
    
    def __init__(self, max_resources=3):
        """
        Args:
            max_resources (int): 최대 리소스 수
        """
        pass
    
    def __enter__(self):
        """
        TODO: 리소스 할당
        가용한 리소스가 없으면 대기
        
        Returns:
            str: 할당된 리소스 ID
        """
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        TODO: 리소스 해제
        """
        pass

def demonstrate_context_managers():
    """
    TODO: 다양한 컨텍스트 매니저 사용 데모
    
    Returns:
        dict: 각 데모의 결과
    """
    results = {}
    
    # Timer 사용
    pass
    
    # FileManager 사용 (테스트 파일 생성)
    pass
    
    # DatabaseConnection 사용
    pass
    
    # temporary_directory 사용
    pass
    
    # error_handler 사용
    pass
    
    # ResourcePool 사용
    pass
    
    return results

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        print("=== Timer Context Manager ===")
        with Timer() as timer:
            time.sleep(0.1)
            print(f"작업 중... 경과 시간: {timer.elapsed_time:.4f}초")
        
        print(f"\n총 경과 시간: {timer.elapsed_time:.4f}초")
        
        print("\n=== File Manager ===")
        # 테스트 파일 생성
        with open("test_context.txt", "w") as f:
            f.write("컨텍스트 매니저 테스트")
            
        with FileManager("test_context.txt", "r") as file:
            content = file.read()
            print("파일 내용:", content)
        
        print("\n=== Database Connection ===")
        with DatabaseConnection("test://localhost:5432/testdb") as db:
            result = db.execute("SELECT * FROM users")
            print("쿼리 결과:", result)
        
        print("\n=== Temporary Directory ===")
        with temporary_directory() as temp_dir:
            print("임시 디렉토리:", temp_dir)
        
        print("\n=== Error Handler ===")
        with error_handler("사용자 정의 오류 메시지"):
            # raise ValueError("테스트 오류")  # 주석 해제하여 테스트
            print("정상 실행됨")
        
        print("\n=== Resource Pool ===")
        pool = ResourcePool(2)
        with pool as resource1:
            print(f"리소스 할당: {resource1}")
            with pool as resource2:
                print(f"리소스 할당: {resource2}")
        
        print("\n=== Demonstration ===")
        demo_results = demonstrate_context_managers()
        print("Demo results:", demo_results)
        
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        # 정리 작업
        import os
        try:
            os.remove("test_context.txt")
        except:
            pass
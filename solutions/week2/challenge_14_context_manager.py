"""
Challenge 14: 컨텍스트 매니저 - 솔루션

TODO: 다음 컨텍스트 매니저들을 완성하세요

힌트:
- with 문과 함께 사용
- __enter__와 __exit__ 메서드 구현
- contextlib 모듈의 @contextmanager 데코레이터
"""

import time
import os
import tempfile
import shutil
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
        self.start_time = time.time()
        return self
    
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
        self.end_time = time.time()
        self._elapsed = self.end_time - self.start_time
        print(f"실행 시간: {self._elapsed:.4f}초")
        return False  # 예외를 전파
    
    @property
    def elapsed_time(self):
        """경과 시간 반환"""
        return getattr(self, '_elapsed', time.time() - self.start_time if hasattr(self, 'start_time') else 0)

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
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """
        TODO: 파일 열기
        
        Returns:
            file object: 열린 파일 객체
        """
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        TODO: 파일 닫기
        예외가 발생해도 파일이 닫히도록 보장
        """
        if self.file and not self.file.closed:
            self.file.close()
        return False  # 예외를 전파

class DatabaseConnection:
    """
    TODO: 데이터베이스 연결 시뮬레이션 컨텍스트 매니저
    """
    
    def __init__(self, connection_string):
        """
        Args:
            connection_string (str): 연결 문자열
        """
        self.connection_string = connection_string
        self.connected = False
        self.transaction_active = False
    
    def __enter__(self):
        """
        TODO: 데이터베이스 연결
        
        Returns:
            self: 컨텍스트 매니저 자신
        """
        print(f"데이터베이스 연결: {self.connection_string}")
        self.connected = True
        self.transaction_active = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        TODO: 데이터베이스 연결 해제
        예외 발생 시 롤백 수행
        """
        if self.transaction_active:
            if exc_type is not None:
                print("예외 발생으로 인한 롤백 수행")
            else:
                print("정상 커밋")
            self.transaction_active = False
        
        if self.connected:
            print("데이터베이스 연결 해제")
            self.connected = False
        
        return False  # 예외를 전파
    
    def execute(self, query):
        """
        TODO: 쿼리 실행 시뮬레이션
        
        Args:
            query (str): SQL 쿼리
            
        Returns:
            str: 실행 결과
        """
        if not self.connected:
            raise RuntimeError("데이터베이스가 연결되지 않았습니다")
        
        print(f"쿼리 실행: {query}")
        return f"쿼리 '{query}' 실행 완료"

@contextmanager
def temporary_directory():
    """
    TODO: 임시 디렉토리 생성/삭제 컨텍스트 매니저
    @contextmanager 데코레이터 사용
    
    Yields:
        str: 임시 디렉토리 경로
    """
    temp_dir = tempfile.mkdtemp()
    try:
        print(f"임시 디렉토리 생성: {temp_dir}")
        yield temp_dir
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"임시 디렉토리 삭제: {temp_dir}")

@contextmanager
def error_handler(error_message="오류가 발생했습니다"):
    """
    TODO: 예외 처리 컨텍스트 매니저
    예외를 잡고 사용자 정의 메시지 출력
    
    Args:
        error_message (str): 오류 시 출력할 메시지
    """
    try:
        yield
    except Exception as e:
        print(f"{error_message}: {e}")

@contextmanager  
def change_directory(path):
    """
    TODO: 디렉토리 변경 컨텍스트 매니저
    임시로 디렉토리를 변경했다가 원래대로 복구
    
    Args:
        path (str): 변경할 디렉토리 경로
    """
    original_cwd = os.getcwd()
    try:
        os.chdir(path)
        print(f"디렉토리 변경: {path}")
        yield path
    finally:
        os.chdir(original_cwd)
        print(f"디렉토리 복구: {original_cwd}")

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
        self.max_resources = max_resources
        self.available_resources = [f"resource_{i}" for i in range(max_resources)]
        self.allocated_resources = set()
    
    def __enter__(self):
        """
        TODO: 리소스 할당
        가용한 리소스가 없으면 대기
        
        Returns:
            str: 할당된 리소스 ID
        """
        if not self.available_resources:
            raise RuntimeError("사용 가능한 리소스가 없습니다")
        
        resource = self.available_resources.pop(0)
        self.allocated_resources.add(resource)
        print(f"리소스 할당: {resource}")
        return resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        TODO: 리소스 해제
        """
        # 가장 최근에 할당된 리소스 해제 (간단한 구현)
        if self.allocated_resources:
            resource = self.allocated_resources.pop()
            self.available_resources.append(resource)
            print(f"리소스 해제: {resource}")
        return False

def demonstrate_context_managers():
    """
    TODO: 다양한 컨텍스트 매니저 사용 데모
    
    Returns:
        dict: 각 데모의 결과
    """
    results = {}
    
    # Timer 사용
    print("=== Timer 데모 ===")
    with Timer() as timer:
        time.sleep(0.1)
    results["timer"] = f"Timer 작동: {timer.elapsed_time:.2f}초"
    
    # FileManager 사용 (테스트 파일 생성)
    print("\n=== FileManager 데모 ===")
    test_file = "context_test.txt"
    with FileManager(test_file, "w") as file:
        file.write("컨텍스트 매니저 테스트")
    
    with FileManager(test_file, "r") as file:
        content = file.read()
        results["file_manager"] = f"파일 내용: {content}"
    
    # 파일 정리
    if os.path.exists(test_file):
        os.remove(test_file)
    
    # DatabaseConnection 사용
    print("\n=== DatabaseConnection 데모 ===")
    with DatabaseConnection("test://localhost:5432/testdb") as db:
        db_result = db.execute("SELECT * FROM users")
        results["database"] = db_result
    
    # temporary_directory 사용
    print("\n=== Temporary Directory 데모 ===")
    with temporary_directory() as temp_dir:
        results["temp_dir"] = f"임시 디렉토리 생성됨: {os.path.exists(temp_dir)}"
    
    # error_handler 사용
    print("\n=== Error Handler 데모 ===")
    with error_handler("사용자 정의 오류 메시지"):
        results["error_handler"] = "정상 실행됨"
    
    # ResourcePool 사용
    print("\n=== Resource Pool 데모 ===")
    pool = ResourcePool(2)
    with pool as resource1:
        results["resource_pool"] = f"리소스 할당됨: {resource1}"
    
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
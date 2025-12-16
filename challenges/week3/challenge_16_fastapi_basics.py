"""
Challenge 16: FastAPI 기초

TODO: 다음 FastAPI 기본 기능들을 구현하세요

힌트:
- from fastapi import FastAPI
- app = FastAPI()
- @app.get("/") 데코레이터 사용
- uvicorn으로 서버 실행: uvicorn main:app --reload
"""

from fastapi import FastAPI

# FastAPI 앱 인스턴스 생성
app = FastAPI()

def create_fastapi_app():
    """
    TODO: FastAPI 애플리케이션을 생성하고 기본 설정을 추가하세요
    - title: "Python Learning API"
    - description: "FastAPI 학습용 API"
    - version: "1.0.0"
    
    Returns:
        FastAPI: 설정된 FastAPI 앱 인스턴스
    """
    pass

@app.get("/")
def read_root():
    """
    TODO: 루트 경로(/)에 대한 GET 엔드포인트를 구현하세요
    
    Returns:
        dict: {"message": "Hello, FastAPI!", "status": "success"}
    """
    pass

@app.get("/health")
def health_check():
    """
    TODO: 헬스 체크 엔드포인트를 구현하세요
    
    Returns:
        dict: {"status": "healthy", "service": "Python Learning API"}
    """
    pass

@app.get("/info")
def get_info():
    """
    TODO: API 정보를 반환하는 엔드포인트를 구현하세요
    
    Returns:
        dict: API 이름, 버전, 설명 정보
    """
    pass

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """
    TODO: Path Parameter를 사용하여 특정 사용자 정보를 반환하세요
    
    Args:
        user_id (int): 사용자 ID
        
    Returns:
        dict: 사용자 정보 {"user_id": user_id, "name": f"User {user_id}", "active": True}
    """
    pass

@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    """
    TODO: Query Parameter를 사용하여 아이템 목록을 반환하세요
    
    Args:
        skip (int): 건너뛸 개수 (기본값: 0)
        limit (int): 제한 개수 (기본값: 10)
        
    Returns:
        dict: {"items": [...], "skip": skip, "limit": limit}
    """
    pass

@app.get("/calculate/add/{a}/{b}")
def add_numbers(a: int, b: int):
    """
    TODO: 두 숫자를 더하는 계산기 엔드포인트를 구현하세요
    
    Args:
        a (int): 첫 번째 숫자
        b (int): 두 번째 숫자
        
    Returns:
        dict: {"a": a, "b": b, "result": a + b, "operation": "addition"}
    """
    pass

@app.get("/status/{status_code}")
def get_status_info(status_code: int):
    """
    TODO: HTTP 상태 코드에 대한 정보를 반환하세요
    
    Args:
        status_code (int): HTTP 상태 코드
        
    Returns:
        dict: 상태 코드 정보
    """
    pass

# 서버 실행용 (개발시에만 사용)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
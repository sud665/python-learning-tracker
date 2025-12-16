"""
FastAPI TDD 예제 애플리케이션

테스트를 통과시키기 위한 최소한의 구현
"""
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI TDD Example",
    description="TDD 방식으로 개발한 FastAPI 예제",
    version="1.0.0"
)


@app.get("/")
def read_root():
    """루트 엔드포인트"""
    return {
        "message": "Hello, FastAPI!",
        "status": "success"
    }


@app.get("/health")
def health_check():
    """헬스 체크 엔드포인트"""
    return {
        "status": "healthy",
        "service": "Python Learning API"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    """사용자 조회 엔드포인트"""
    return {
        "user_id": user_id,
        "name": f"User {user_id}",
        "active": True
    }


@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    """아이템 목록 조회 엔드포인트"""
    return {
        "items": [],
        "skip": skip,
        "limit": limit
    }


@app.get("/calculate/add/{a}/{b}")
def add_numbers(a: int, b: int):
    """덧셈 계산 엔드포인트"""
    return {
        "a": a,
        "b": b,
        "result": a + b,
        "operation": "addition"
    }


# 서버 실행용
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# 🧪 파이썬 TDD (Test-Driven Development) 가이드

## TDD란?

**TDD (Test-Driven Development)**는 테스트 주도 개발 방법론으로, 다음 3단계를 반복합니다:

1. **🔴 Red**: 실패하는 테스트를 먼저 작성
2. **🟢 Green**: 테스트를 통과시키는 최소한의 코드 작성
3. **🔵 Refactor**: 코드를 개선하고 리팩토링

## TDD의 장점

- ✅ **명확한 요구사항**: 테스트가 곧 명세서 역할
- ✅ **안전한 리팩토링**: 테스트가 회귀 버그를 방지
- ✅ **더 나은 설계**: 테스트하기 쉬운 코드 = 좋은 설계
- ✅ **자신감**: 변경 시 테스트로 검증 가능

## 파이썬 TDD 도구

### 1. pytest (권장)

```bash
pip install pytest pytest-asyncio httpx
```

**기본 사용법:**
```python
# test_example.py
def test_add():
    assert add(2, 3) == 5
```

**실행:**
```bash
pytest test_example.py -v
```

### 2. unittest (표준 라이브러리)

```python
import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
```

## TDD 실전 예제

### 예제 1: 간단한 계산기 함수

#### Step 1: Red - 실패하는 테스트 작성

```python
# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

**실행 결과:** ❌ `ModuleNotFoundError: No module named 'calculator'`

#### Step 2: Green - 최소한의 코드 작성

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b
```

**실행 결과:** ✅ 모든 테스트 통과!

#### Step 3: Refactor - 코드 개선

```python
# calculator.py (개선된 버전)
from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """두 숫자를 더합니다."""
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """두 숫자를 뺍니다."""
    return a - b

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """두 숫자를 곱합니다."""
    return a * b

def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """두 숫자를 나눕니다.
    
    Args:
        a: 피제수
        b: 제수
        
    Returns:
        나눗셈 결과
        
    Raises:
        ValueError: 제수가 0일 때
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b
```

### 예제 2: FastAPI 엔드포인트 TDD

#### Step 1: Red - 테스트 작성

```python
# test_api.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """루트 엔드포인트 테스트"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, FastAPI!",
        "status": "success"
    }

def test_health_check():
    """헬스 체크 엔드포인트 테스트"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "Python Learning API"
    }

def test_get_user():
    """사용자 조회 엔드포인트 테스트"""
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 1
    assert data["name"] == "User 1"
    assert data["active"] is True

def test_get_items():
    """아이템 목록 조회 테스트"""
    response = client.get("/items?skip=0&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert data["skip"] == 0
    assert data["limit"] == 5
```

#### Step 2: Green - API 구현

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!", "status": "success"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Python Learning API"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": f"User {user_id}",
        "active": True
    }

@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return {
        "items": [],
        "skip": skip,
        "limit": limit
    }
```

#### Step 3: Refactor - 비즈니스 로직 분리

```python
# services/user_service.py
class UserService:
    @staticmethod
    def get_user(user_id: int):
        # 실제 데이터베이스 조회 로직
        return {
            "user_id": user_id,
            "name": f"User {user_id}",
            "active": True
        }

# main.py
from services.user_service import UserService

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return UserService.get_user(user_id)
```

## pytest 고급 기능

### 1. Fixture (픽스처)

```python
import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    """테스트 클라이언트 픽스처"""
    return TestClient(app)

@pytest.fixture
def sample_user():
    """샘플 사용자 데이터"""
    return {"id": 1, "name": "홍길동", "email": "hong@example.com"}

def test_get_user(client, sample_user):
    """픽스처 사용 예제"""
    response = client.get(f"/users/{sample_user['id']}")
    assert response.status_code == 200
```

### 2. Parametrize (매개변수화)

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### 3. Mock (모킹)

```python
from unittest.mock import Mock, patch

def test_external_api_call():
    """외부 API 호출 모킹"""
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"status": "ok"}
        
        result = call_external_api()
        assert result["status"] == "ok"
```

### 4. Async 테스트

```python
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_async_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/async-endpoint")
        assert response.status_code == 200
```

## TDD 모범 사례

### ✅ DO (해야 할 것)

1. **작은 단위로 테스트**: 한 번에 하나의 기능만 테스트
2. **명확한 테스트 이름**: `test_add_two_positive_numbers()` 같은 설명적인 이름
3. **AAA 패턴**: Arrange (준비) → Act (실행) → Assert (검증)
4. **독립적인 테스트**: 각 테스트는 다른 테스트에 의존하지 않아야 함
5. **빠른 실행**: 테스트는 빠르게 실행되어야 함

```python
def test_calculate_total():
    # Arrange (준비)
    items = [10, 20, 30]
    
    # Act (실행)
    total = calculate_total(items)
    
    # Assert (검증)
    assert total == 60
```

### ❌ DON'T (하지 말아야 할 것)

1. **테스트 간 의존성**: 테스트 실행 순서에 의존하지 않기
2. **외부 의존성**: 데이터베이스, API 등은 모킹하기
3. **너무 복잡한 테스트**: 한 테스트에 너무 많은 검증 넣지 않기
4. **테스트 코드 무시**: 테스트 코드도 프로덕션 코드처럼 관리

## TDD 워크플로우

```
1. 요구사항 분석
   ↓
2. 테스트 작성 (Red)
   ↓
3. 테스트 실행 → 실패 확인
   ↓
4. 최소한의 코드 작성 (Green)
   ↓
5. 테스트 실행 → 통과 확인
   ↓
6. 리팩토링 (Refactor)
   ↓
7. 테스트 실행 → 통과 확인
   ↓
8. 다음 기능으로 이동
```

## 실제 프로젝트 적용

### 프로젝트 구조

```
my_project/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   └── api.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_api.py
├── pytest.ini          # pytest 설정
└── requirements.txt
```

### pytest.ini 설정

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
```

## 도전 과제

다음 기능을 TDD로 구현해보세요:

1. **사용자 인증 시스템**
   - 회원가입
   - 로그인
   - 비밀번호 검증

2. **할일 관리 API**
   - 할일 생성
   - 할일 조회
   - 할일 완료 처리
   - 할일 삭제

3. **계산기 확장**
   - 제곱근 계산
   - 거듭제곱 계산
   - 로그 계산

## 참고 자료

- [pytest 공식 문서](https://docs.pytest.org/)
- [FastAPI 테스팅 가이드](https://fastapi.tiangolo.com/tutorial/testing/)
- [Python Testing Best Practices](https://realpython.com/python-testing/)

---

**기억하세요**: TDD는 습관입니다. 처음에는 느릴 수 있지만, 장기적으로 코드 품질과 개발 속도를 크게 향상시킵니다! 🚀

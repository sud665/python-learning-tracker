"""
FastAPI TDD 예제

FastAPI 엔드포인트를 TDD 방식으로 개발하는 예제
"""
import pytest
from fastapi.testclient import TestClient
from fastapi_tdd_app import app

# 테스트 클라이언트 픽스처
@pytest.fixture
def client():
    """테스트 클라이언트 픽스처"""
    return TestClient(app)


class TestRootEndpoint:
    """루트 엔드포인트 테스트"""
    
    def test_read_root(self, client):
        """루트 경로 GET 요청 테스트"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hello, FastAPI!"
        assert data["status"] == "success"


class TestHealthEndpoint:
    """헬스 체크 엔드포인트 테스트"""
    
    def test_health_check(self, client):
        """헬스 체크 테스트"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "Python Learning API"


class TestUserEndpoint:
    """사용자 엔드포인트 테스트"""
    
    def test_get_user(self, client):
        """사용자 조회 테스트"""
        response = client.get("/users/1")
        assert response.status_code == 200
        data = response.json()
        assert data["user_id"] == 1
        assert data["name"] == "User 1"
        assert data["active"] is True
    
    def test_get_user_different_id(self, client):
        """다른 ID의 사용자 조회 테스트"""
        response = client.get("/users/42")
        assert response.status_code == 200
        data = response.json()
        assert data["user_id"] == 42
        assert data["name"] == "User 42"
    
    def test_get_user_invalid_id(self, client):
        """잘못된 사용자 ID 테스트"""
        response = client.get("/users/abc")
        assert response.status_code == 422  # Validation error


class TestItemsEndpoint:
    """아이템 엔드포인트 테스트"""
    
    def test_get_items_default(self, client):
        """기본 파라미터로 아이템 조회 테스트"""
        response = client.get("/items")
        assert response.status_code == 200
        data = response.json()
        assert "items" in data
        assert data["skip"] == 0
        assert data["limit"] == 10
    
    def test_get_items_with_params(self, client):
        """파라미터를 지정한 아이템 조회 테스트"""
        response = client.get("/items?skip=5&limit=20")
        assert response.status_code == 200
        data = response.json()
        assert data["skip"] == 5
        assert data["limit"] == 20


class TestCalculateEndpoint:
    """계산 엔드포인트 테스트"""
    
    def test_add_numbers(self, client):
        """덧셈 계산 테스트"""
        response = client.get("/calculate/add/5/3")
        assert response.status_code == 200
        data = response.json()
        assert data["a"] == 5
        assert data["b"] == 3
        assert data["result"] == 8
        assert data["operation"] == "addition"
    
    def test_add_negative_numbers(self, client):
        """음수 덧셈 테스트"""
        response = client.get("/calculate/add/-5/-3")
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == -8


# Parametrize를 사용한 테스트
@pytest.mark.parametrize("user_id,expected_name", [
    (1, "User 1"),
    (2, "User 2"),
    (100, "User 100"),
])
def test_get_user_parametrized(client, user_id, expected_name):
    """매개변수화된 사용자 조회 테스트"""
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == user_id
    assert data["name"] == expected_name

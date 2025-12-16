"""
Challenge 20: 인증과 보안

TODO: JWT 토큰 기반 인증 시스템을 구현하세요

힌트:
- from fastapi import Depends, HTTPException, status
- from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
- from passlib.context import CryptContext
- from jose import JWTError, jwt
- 환경변수로 SECRET_KEY 관리
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional, List
import os

app = FastAPI(title="Authentication API")

# 보안 설정
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 비밀번호 해싱
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 토큰 스킴
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
bearer_scheme = HTTPBearer()

# Pydantic 모델
class User(BaseModel):
    """
    TODO: 사용자 모델을 정의하세요
    - username: str
    - email: str
    - full_name: Optional[str]
    - disabled: bool = False
    - roles: List[str] = []
    """
    pass

class UserInDB(User):
    """
    TODO: DB에 저장되는 사용자 모델을 정의하세요
    User를 상속받고 hashed_password 필드 추가
    """
    pass

class UserCreate(BaseModel):
    """
    TODO: 사용자 생성 모델을 정의하세요
    - username: str
    - email: str
    - password: str
    - full_name: Optional[str]
    """
    pass

class Token(BaseModel):
    """토큰 응답 모델"""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """토큰 데이터 모델"""
    username: Optional[str] = None

# 임시 사용자 데이터베이스
fake_users_db = {
    "admin": {
        "username": "admin",
        "email": "admin@example.com",
        "full_name": "Admin User",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
        "disabled": False,
        "roles": ["admin", "user"]
    },
    "user": {
        "username": "user", 
        "email": "user@example.com",
        "full_name": "Regular User",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
        "disabled": False,
        "roles": ["user"]
    }
}

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    TODO: 비밀번호를 검증하세요
    
    Args:
        plain_password: 평문 비밀번호
        hashed_password: 해시된 비밀번호
        
    Returns:
        bool: 비밀번호 일치 여부
    """
    pass

def get_password_hash(password: str) -> str:
    """
    TODO: 비밀번호를 해시화하세요
    
    Args:
        password: 평문 비밀번호
        
    Returns:
        str: 해시된 비밀번호
    """
    pass

def get_user(db, username: str):
    """
    TODO: 사용자 정보를 가져오세요
    
    Args:
        db: 사용자 데이터베이스
        username: 사용자명
        
    Returns:
        UserInDB: 사용자 정보 또는 None
    """
    pass

def authenticate_user(db, username: str, password: str):
    """
    TODO: 사용자를 인증하세요
    
    Args:
        db: 사용자 데이터베이스  
        username: 사용자명
        password: 비밀번호
        
    Returns:
        UserInDB: 인증된 사용자 또는 False
    """
    pass

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    TODO: JWT 액세스 토큰을 생성하세요
    
    Args:
        data: 토큰에 포함할 데이터
        expires_delta: 만료 시간
        
    Returns:
        str: JWT 토큰
    """
    pass

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    TODO: 현재 사용자를 가져오세요 (토큰 기반)
    
    Args:
        token: JWT 토큰
        
    Returns:
        UserInDB: 현재 사용자
        
    Raises:
        HTTPException: 인증 실패시
    """
    pass

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """
    TODO: 활성 사용자를 가져오세요
    
    Args:
        current_user: 현재 사용자
        
    Returns:
        User: 활성 사용자
        
    Raises:
        HTTPException: 비활성 사용자인 경우
    """
    pass

def require_role(required_role: str):
    """
    TODO: 특정 역할을 요구하는 의존성 함수를 생성하세요
    
    Args:
        required_role: 필요한 역할
        
    Returns:
        function: 의존성 함수
    """
    def role_checker(current_user: User = Depends(get_current_active_user)):
        pass
    return role_checker

@app.post("/register", response_model=User)
def register_user(user: UserCreate):
    """
    TODO: 새로운 사용자를 등록하세요
    
    Args:
        user: 등록할 사용자 정보
        
    Returns:
        User: 등록된 사용자 정보
        
    Raises:
        HTTPException: 사용자명이 이미 존재하는 경우
    """
    pass

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    TODO: 로그인하여 액세스 토큰을 발급하세요
    
    Args:
        form_data: 로그인 폼 데이터 (username, password)
        
    Returns:
        Token: 액세스 토큰
        
    Raises:
        HTTPException: 인증 실패시
    """
    pass

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """
    TODO: 현재 사용자 정보를 반환하세요
    
    Args:
        current_user: 현재 활성 사용자
        
    Returns:
        User: 현재 사용자 정보
    """
    pass

@app.get("/protected")
async def protected_route(current_user: User = Depends(get_current_active_user)):
    """
    TODO: 보호된 엔드포인트를 구현하세요
    
    Args:
        current_user: 현재 활성 사용자
        
    Returns:
        dict: 보호된 데이터
    """
    pass

@app.get("/admin-only")
async def admin_only_route(current_user: User = Depends(require_role("admin"))):
    """
    TODO: 관리자 전용 엔드포인트를 구현하세요
    
    Args:
        current_user: 관리자 권한을 가진 사용자
        
    Returns:
        dict: 관리자 전용 데이터
    """
    pass

@app.post("/logout")
async def logout(current_user: User = Depends(get_current_active_user)):
    """
    TODO: 로그아웃을 구현하세요 (토큰 무효화)
    
    Args:
        current_user: 현재 사용자
        
    Returns:
        dict: 로그아웃 메시지
    """
    pass

@app.get("/users")
async def list_users(
    current_user: User = Depends(require_role("admin")),
    skip: int = 0,
    limit: int = 100
):
    """
    TODO: 사용자 목록을 반환하세요 (관리자만 접근 가능)
    
    Args:
        current_user: 관리자 사용자
        skip: 건너뛸 개수
        limit: 반환할 최대 개수
        
    Returns:
        List[User]: 사용자 목록
    """
    pass

@app.put("/users/{username}/disable")
async def disable_user(
    username: str,
    current_user: User = Depends(require_role("admin"))
):
    """
    TODO: 사용자를 비활성화하세요
    
    Args:
        username: 비활성화할 사용자명
        current_user: 관리자 사용자
        
    Returns:
        dict: 결과 메시지
    """
    pass

# 서버 실행용
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
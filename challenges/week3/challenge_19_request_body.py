"""
Challenge 19: Request Body & Pydantic Models

TODO: Pydantic 모델과 Request Body 처리를 구현하세요

힌트:
- from pydantic import BaseModel, Field, validator
- from typing import Optional, List
- Field(description="설명", example="예시")
- @validator 데코레이터로 커스텀 유효성 검사
"""

from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional, List, Dict
from datetime import datetime, date
from enum import Enum

app = FastAPI(title="Request Body API")

# Enum 정의
class UserRole(str, Enum):
    """사용자 역할"""
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class PostStatus(str, Enum):
    """게시글 상태"""
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"

# Pydantic 모델 정의
class Address(BaseModel):
    """
    TODO: 주소 모델을 정의하세요
    - street: str = Field(description="도로명")
    - city: str = Field(description="도시")
    - state: str = Field(description="주/도")
    - zip_code: str = Field(description="우편번호", regex=r"^\d{5}$")
    - country: str = Field(default="Korea", description="국가")
    """
    pass

class UserCreate(BaseModel):
    """
    TODO: 사용자 생성 모델을 정의하세요
    - username: str (3~20자, 알파벳+숫자+underscore만)
    - email: EmailStr
    - password: str (8자 이상)
    - full_name: str
    - age: Optional[int] (18 이상)
    - role: UserRole (기본값: USER)
    - address: Optional[Address]
    - interests: List[str] (기본값: 빈 리스트)
    
    유효성 검사:
    - username은 알파벳, 숫자, underscore만 허용
    - password는 최소 8자 이상
    - age는 18 이상이어야 함
    """
    pass
    
    @validator('username')
    def validate_username(cls, v):
        """사용자명 유효성 검사"""
        pass
    
    @validator('password')
    def validate_password(cls, v):
        """비밀번호 유효성 검사"""
        pass
    
    @validator('age')
    def validate_age(cls, v):
        """나이 유효성 검사"""
        pass

class PostCreate(BaseModel):
    """
    TODO: 게시글 생성 모델을 정의하세요
    - title: str (5~200자)
    - content: str (10자 이상)
    - summary: Optional[str] (최대 500자)
    - tags: List[str] (기본값: 빈 리스트)
    - status: PostStatus (기본값: DRAFT)
    - publish_date: Optional[date]
    - metadata: Optional[Dict[str, any]]
    """
    pass
    
    @validator('title')
    def validate_title(cls, v):
        """제목 유효성 검사"""
        pass
    
    @validator('content')
    def validate_content(cls, v):
        """내용 유효성 검사"""
        pass

class UserResponse(BaseModel):
    """사용자 응답 모델"""
    id: int
    username: str
    email: str
    full_name: str
    role: UserRole
    created_at: datetime
    is_active: bool = True

# 임시 저장소
users_db: List[Dict] = []
posts_db: List[Dict] = []
next_user_id = 1
next_post_id = 1

@app.post("/users/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    """
    TODO: 새로운 사용자를 생성하세요
    
    Args:
        user (UserCreate): 생성할 사용자 정보
        
    Returns:
        UserResponse: 생성된 사용자 정보
        
    Raises:
        HTTPException: 중복된 사용자명이나 이메일인 경우
    """
    pass

@app.post("/posts/")
def create_post(post: PostCreate, author_id: int = Body(..., description="작성자 ID")):
    """
    TODO: 새로운 게시글을 생성하세요
    
    Args:
        post (PostCreate): 생성할 게시글 정보
        author_id (int): 작성자 ID
        
    Returns:
        dict: 생성된 게시글 정보
    """
    pass

@app.put("/users/{user_id}")
def update_user(user_id: int, user_update: Dict):
    """
    TODO: 사용자 정보를 업데이트하세요
    부분 업데이트를 지원해야 합니다
    
    Args:
        user_id (int): 업데이트할 사용자 ID
        user_update (Dict): 업데이트할 필드들
        
    Returns:
        dict: 업데이트된 사용자 정보
    """
    pass

@app.post("/users/bulk")
def create_users_bulk(users: List[UserCreate]):
    """
    TODO: 여러 사용자를 한번에 생성하세요
    
    Args:
        users (List[UserCreate]): 생성할 사용자 목록
        
    Returns:
        dict: {"created": 생성된_사용자_수, "users": 생성된_사용자_목록}
    """
    pass

@app.post("/posts/{post_id}/comments")
def add_comment(
    post_id: int,
    comment: Dict = Body(..., description="댓글 내용"),
    author_id: int = Body(..., description="작성자 ID")
):
    """
    TODO: 게시글에 댓글을 추가하세요
    
    comment 형식:
    {
        "content": "댓글 내용",
        "parent_id": null  // 대댓글인 경우 부모 댓글 ID
    }
    
    Args:
        post_id (int): 게시글 ID
        comment (Dict): 댓글 정보
        author_id (int): 작성자 ID
        
    Returns:
        dict: 추가된 댓글 정보
    """
    pass

@app.post("/users/{user_id}/profile")
def update_user_profile(
    user_id: int,
    profile: Dict = Body(..., description="프로필 정보"),
    preferences: Optional[Dict] = Body(None, description="사용자 환경설정")
):
    """
    TODO: 사용자 프로필을 업데이트하세요
    
    Args:
        user_id (int): 사용자 ID
        profile (Dict): 프로필 정보
        preferences (Dict, optional): 환경설정
        
    Returns:
        dict: 업데이트된 프로필 정보
    """
    pass

@app.post("/validate/email")
def validate_email(data: Dict = Body(..., embed=True)):
    """
    TODO: 이메일 유효성을 검사하세요
    
    Args:
        data: {"email": "test@example.com"}
        
    Returns:
        dict: {"email": email, "is_valid": bool, "suggestions": []}
    """
    pass

@app.post("/calculate")
def calculate(
    operation: str = Body(..., description="연산 종류"),
    operands: List[float] = Body(..., description="피연산자들"),
    options: Optional[Dict] = Body(None, description="추가 옵션")
):
    """
    TODO: 다양한 수학 연산을 수행하세요
    
    지원 연산: add, subtract, multiply, divide, average, max, min
    
    Args:
        operation (str): 연산 종류
        operands (List[float]): 피연산자들
        options (Dict, optional): 추가 옵션
        
    Returns:
        dict: 연산 결과
    """
    pass

# 서버 실행용
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
"""
Challenge 21: Final Project - 블로그 API

TODO: 지금까지 배운 모든 내용을 활용하여 완전한 블로그 API를 구현하세요

힌트:
- 사용자 인증 (JWT)
- CRUD 작업 (게시글, 댓글)
- 검색 및 필터링
- 페이징
- 파일 업로드 (선택사항)
- API 문서화

이 프로젝트는 모든 이전 챌린지의 통합입니다.
"""

from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime
import uuid
import os

app = FastAPI(
    title="Blog API - Final Project",
    description="FastAPI 학습의 최종 프로젝트: 완전한 블로그 API",
    version="1.0.0"
)

# 인증 설정
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

# Pydantic 모델들
class UserBase(BaseModel):
    """사용자 기본 모델"""
    username: str = Field(..., min_length=3, max_length=20)
    email: str = Field(..., regex=r'^[^@]+@[^@]+\.[^@]+$')
    full_name: Optional[str] = None
    bio: Optional[str] = Field(None, max_length=500)

class UserCreate(UserBase):
    """
    TODO: 사용자 생성 모델을 정의하세요
    UserBase를 상속받고 password 필드 추가
    """
    pass

class UserResponse(UserBase):
    """
    TODO: 사용자 응답 모델을 정의하세요
    UserBase를 상속받고 추가 필드들:
    - id: int
    - created_at: datetime
    - is_active: bool
    - posts_count: int
    """
    pass

class PostBase(BaseModel):
    """게시글 기본 모델"""
    title: str = Field(..., min_length=5, max_length=200)
    content: str = Field(..., min_length=10)
    summary: Optional[str] = Field(None, max_length=500)
    tags: List[str] = Field(default_factory=list)
    is_published: bool = False

class PostCreate(PostBase):
    """
    TODO: 게시글 생성 모델을 정의하세요
    PostBase를 그대로 사용
    """
    pass

class PostUpdate(BaseModel):
    """
    TODO: 게시글 업데이트 모델을 정의하세요
    모든 필드를 Optional로
    """
    pass

class PostResponse(PostBase):
    """
    TODO: 게시글 응답 모델을 정의하세요
    PostBase를 상속받고 추가 필드들:
    - id: int
    - author_id: int
    - author_username: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - views_count: int
    - likes_count: int
    """
    pass

class CommentBase(BaseModel):
    """댓글 기본 모델"""
    content: str = Field(..., min_length=1, max_length=1000)

class CommentCreate(CommentBase):
    """
    TODO: 댓글 생성 모델을 정의하세요
    CommentBase를 상속받고 parent_id 추가 (대댓글용)
    """
    pass

class CommentResponse(CommentBase):
    """
    TODO: 댓글 응답 모델을 정의하세요
    CommentBase를 상속받고 추가 필드들:
    - id: int
    - post_id: int
    - author_id: int
    - author_username: str
    - parent_id: Optional[int]
    - created_at: datetime
    - replies: List[CommentResponse] = []
    """
    pass

# 임시 데이터베이스
users_db: Dict[str, dict] = {}
posts_db: List[dict] = []
comments_db: List[dict] = []
next_user_id = 1
next_post_id = 1
next_comment_id = 1

# 의존성 함수들
async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    TODO: 현재 사용자를 가져오는 함수를 구현하세요
    토큰을 검증하고 사용자 정보를 반환
    """
    pass

async def get_current_active_user(current_user: dict = Depends(get_current_user)):
    """
    TODO: 활성 사용자를 확인하는 함수를 구현하세요
    """
    pass

# 인증 엔드포인트
@app.post("/auth/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    """
    TODO: 사용자 등록을 구현하세요
    
    Args:
        user: 등록할 사용자 정보
        
    Returns:
        UserResponse: 등록된 사용자 정보
        
    Raises:
        HTTPException: 중복된 사용자명이나 이메일
    """
    pass

@app.post("/auth/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    TODO: 로그인을 구현하세요
    
    Args:
        form_data: 로그인 폼 데이터
        
    Returns:
        dict: {"access_token": token, "token_type": "bearer"}
    """
    pass

# 사용자 엔드포인트
@app.get("/users/me", response_model=UserResponse)
async def get_my_profile(current_user: dict = Depends(get_current_active_user)):
    """
    TODO: 현재 사용자 프로필을 반환하세요
    """
    pass

@app.put("/users/me", response_model=UserResponse)
async def update_my_profile(
    user_update: UserBase,
    current_user: dict = Depends(get_current_active_user)
):
    """
    TODO: 현재 사용자 프로필을 업데이트하세요
    """
    pass

# 게시글 엔드포인트
@app.post("/posts/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(
    post: PostCreate,
    current_user: dict = Depends(get_current_active_user)
):
    """
    TODO: 새 게시글을 생성하세요
    
    Args:
        post: 생성할 게시글 정보
        current_user: 현재 사용자
        
    Returns:
        PostResponse: 생성된 게시글
    """
    pass

@app.get("/posts/", response_model=List[PostResponse])
async def get_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = None,
    tags: Optional[List[str]] = Query(None),
    author: Optional[str] = None,
    published_only: bool = True
):
    """
    TODO: 게시글 목록을 가져오세요 (검색, 필터링, 페이징 포함)
    
    Args:
        skip: 건너뛸 개수
        limit: 반환할 최대 개수
        search: 제목/내용 검색어
        tags: 태그 필터
        author: 작성자 필터
        published_only: 발행된 게시글만 표시
        
    Returns:
        List[PostResponse]: 게시글 목록
    """
    pass

@app.get("/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int):
    """
    TODO: 특정 게시글을 가져오세요 (조회수 증가 포함)
    
    Args:
        post_id: 게시글 ID
        
    Returns:
        PostResponse: 게시글 정보
    """
    pass

@app.put("/posts/{post_id}", response_model=PostResponse)
async def update_post(
    post_id: int,
    post_update: PostUpdate,
    current_user: dict = Depends(get_current_active_user)
):
    """
    TODO: 게시글을 업데이트하세요 (작성자만 가능)
    
    Args:
        post_id: 게시글 ID
        post_update: 업데이트할 내용
        current_user: 현재 사용자
        
    Returns:
        PostResponse: 업데이트된 게시글
    """
    pass

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: int,
    current_user: dict = Depends(get_current_active_user)
):
    """
    TODO: 게시글을 삭제하세요 (작성자만 가능)
    """
    pass

# 댓글 엔드포인트
@app.post("/posts/{post_id}/comments/", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def create_comment(
    post_id: int,
    comment: CommentCreate,
    current_user: dict = Depends(get_current_active_user)
):
    """
    TODO: 댓글을 생성하세요
    
    Args:
        post_id: 게시글 ID
        comment: 댓글 내용
        current_user: 현재 사용자
        
    Returns:
        CommentResponse: 생성된 댓글
    """
    pass

@app.get("/posts/{post_id}/comments/", response_model=List[CommentResponse])
async def get_comments(post_id: int):
    """
    TODO: 게시글의 댓글 목록을 가져오세요 (계층 구조 포함)
    
    Args:
        post_id: 게시글 ID
        
    Returns:
        List[CommentResponse]: 댓글 목록
    """
    pass

# 좋아요 기능
@app.post("/posts/{post_id}/like")
async def like_post(
    post_id: int,
    current_user: dict = Depends(get_current_active_user)
):
    """
    TODO: 게시글 좋아요/취소를 구현하세요
    
    Args:
        post_id: 게시글 ID
        current_user: 현재 사용자
        
    Returns:
        dict: {"liked": bool, "likes_count": int}
    """
    pass

# 통계 엔드포인트
@app.get("/stats")
async def get_stats():
    """
    TODO: 블로그 전체 통계를 반환하세요
    
    Returns:
        dict: {
            "total_users": int,
            "total_posts": int,
            "total_comments": int,
            "published_posts": int
        }
    """
    pass

# 태그 엔드포인트
@app.get("/tags")
async def get_tags():
    """
    TODO: 모든 태그와 사용 횟수를 반환하세요
    
    Returns:
        List[dict]: [{"name": str, "count": int}, ...]
    """
    pass

# 파일 업로드 (보너스)
@app.post("/upload/image")
async def upload_image(
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_active_user)
):
    """
    TODO: 이미지 업로드를 구현하세요 (선택사항)
    
    Args:
        file: 업로드할 파일
        current_user: 현재 사용자
        
    Returns:
        dict: {"filename": str, "url": str}
    """
    pass

# 서버 실행용
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
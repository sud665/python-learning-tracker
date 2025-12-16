"""
Database configuration for FastAPI Learning
"""

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Database URL 설정
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://student:password123@localhost:5432/fastapi_learning"
)

# SQLAlchemy 엔진 생성
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # 연결 확인
    echo=True  # SQL 쿼리 로깅 (개발용)
)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 생성
Base = declarative_base()

# 메타데이터
metadata = MetaData()

def get_db():
    """
    DB 세션 의존성 주입용 함수
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """
    모든 테이블 생성
    """
    Base.metadata.create_all(bind=engine)

def drop_tables():
    """
    모든 테이블 삭제 (테스트용)
    """
    Base.metadata.drop_all(bind=engine)

def check_connection():
    """
    DB 연결 확인
    """
    try:
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False
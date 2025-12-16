-- FastAPI Learning Database 초기화 스크립트

-- 데이터베이스 생성 (이미 존재하므로 생략)
-- CREATE DATABASE fastapi_learning;

-- 확장 기능 설치
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 기본 테이블 생성은 SQLAlchemy가 처리하므로 여기서는 필요시 추가 설정만
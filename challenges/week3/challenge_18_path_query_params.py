"""
Challenge 18: Path & Query Parameters

TODO: 다양한 Parameter 처리 방식을 구현하세요

힌트:
- Path Parameters: {user_id}, {category}
- Query Parameters: ?page=1&size=10
- from fastapi import Path, Query
- 유효성 검사: ge=1 (greater equal), le=100 (less equal)
"""

from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional, List
from enum import Enum

app = FastAPI(title="Parameters API")

# Enum 정의
class CategoryEnum(str, Enum):
    """
    TODO: 카테고리 Enum을 정의하세요
    - ELECTRONICS = "electronics"  
    - CLOTHING = "clothing"
    - BOOKS = "books"
    - HOME = "home"
    """
    pass

class SortOrder(str, Enum):
    """정렬 순서"""
    ASC = "asc"
    DESC = "desc"

# 샘플 데이터
fake_products = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 999.99, "rating": 4.5},
    {"id": 2, "name": "T-Shirt", "category": "clothing", "price": 29.99, "rating": 4.2},
    {"id": 3, "name": "Python Book", "category": "books", "price": 49.99, "rating": 4.8},
    {"id": 4, "name": "Coffee Mug", "category": "home", "price": 15.99, "rating": 4.0},
    {"id": 5, "name": "Smartphone", "category": "electronics", "price": 699.99, "rating": 4.3},
]

@app.get("/products/{product_id}")
def get_product(
    product_id: int = Path(..., description="상품 ID", ge=1, le=1000)
):
    """
    TODO: Path Parameter 유효성 검사와 함께 상품을 반환하세요
    
    Args:
        product_id: 상품 ID (1~1000 범위)
        
    Returns:
        dict: 상품 정보
        
    Raises:
        HTTPException: 상품을 찾을 수 없는 경우
    """
    pass

@app.get("/categories/{category}/products")
def get_products_by_category(
    category: CategoryEnum,
    page: int = Query(1, description="페이지 번호", ge=1),
    size: int = Query(10, description="페이지 크기", ge=1, le=100),
    sort_by: str = Query("name", description="정렬 기준"),
    sort_order: SortOrder = Query(SortOrder.ASC, description="정렬 순서")
):
    """
    TODO: 카테고리별 상품 목록을 페이징과 정렬과 함께 반환하세요
    
    Args:
        category: 상품 카테고리 (Enum)
        page: 페이지 번호 (1 이상)
        size: 페이지 크기 (1~100)
        sort_by: 정렬 기준 (name, price, rating)
        sort_order: 정렬 순서 (asc, desc)
        
    Returns:
        dict: 페이징된 상품 목록과 메타데이터
    """
    pass

@app.get("/search")
def search_products(
    q: str = Query(..., description="검색어", min_length=1, max_length=100),
    min_price: Optional[float] = Query(None, description="최소 가격", ge=0),
    max_price: Optional[float] = Query(None, description="최대 가격", ge=0),
    min_rating: Optional[float] = Query(None, description="최소 평점", ge=0, le=5),
    categories: Optional[List[CategoryEnum]] = Query(None, description="카테고리 필터")
):
    """
    TODO: 다양한 필터로 상품을 검색하세요
    
    Args:
        q: 검색어 (필수, 1~100자)
        min_price: 최소 가격 (선택)
        max_price: 최대 가격 (선택)
        min_rating: 최소 평점 (선택, 0~5)
        categories: 카테고리 목록 (선택)
        
    Returns:
        dict: 검색 결과와 필터 정보
    """
    pass

@app.get("/users/{user_id}/orders/{order_id}")
def get_user_order(
    user_id: int = Path(..., description="사용자 ID", ge=1),
    order_id: int = Path(..., description="주문 ID", ge=1),
    include_items: bool = Query(False, description="상품 정보 포함 여부")
):
    """
    TODO: 사용자의 특정 주문 정보를 반환하세요
    
    Args:
        user_id: 사용자 ID
        order_id: 주문 ID  
        include_items: 주문 상품 정보 포함 여부
        
    Returns:
        dict: 주문 정보
    """
    pass

@app.get("/analytics/products")
def get_product_analytics(
    start_date: Optional[str] = Query(None, description="시작 날짜 (YYYY-MM-DD)"),
    end_date: Optional[str] = Query(None, description="종료 날짜 (YYYY-MM-DD)"),
    category: Optional[CategoryEnum] = Query(None, description="카테고리 필터"),
    metric: str = Query("sales", description="분석 지표")
):
    """
    TODO: 상품 분석 데이터를 반환하세요
    
    Args:
        start_date: 분석 시작 날짜
        end_date: 분석 종료 날짜
        category: 카테고리 필터
        metric: 분석 지표 (sales, views, revenue)
        
    Returns:
        dict: 분석 결과
    """
    pass

@app.get("/products/{product_id}/reviews/{review_id}")
def get_product_review(
    product_id: int = Path(..., ge=1, description="상품 ID"),
    review_id: int = Path(..., ge=1, description="리뷰 ID"),
    include_replies: bool = Query(False, description="답글 포함 여부"),
    format: str = Query("json", description="응답 형식")
):
    """
    TODO: 상품의 특정 리뷰를 반환하세요
    
    Args:
        product_id: 상품 ID
        review_id: 리뷰 ID
        include_replies: 답글 포함 여부
        format: 응답 형식 (json, xml)
        
    Returns:
        dict: 리뷰 정보
    """
    pass

@app.get("/reports/{year}/{month}")
def get_monthly_report(
    year: int = Path(..., description="년도", ge=2020, le=2030),
    month: int = Path(..., description="월", ge=1, le=12),
    detail_level: str = Query("summary", description="상세 수준"),
    export_format: str = Query("json", description="내보내기 형식")
):
    """
    TODO: 월별 리포트를 반환하세요
    
    Args:
        year: 년도 (2020~2030)
        month: 월 (1~12)
        detail_level: 상세 수준 (summary, detailed, full)
        export_format: 내보내기 형식 (json, csv, pdf)
        
    Returns:
        dict: 월별 리포트
    """
    pass

# 서버 실행용
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
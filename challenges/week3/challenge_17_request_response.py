"""
Challenge 17: 요청/응답 처리

TODO: 다양한 HTTP 메서드와 요청/응답 처리를 구현하세요

힌트:
- @app.post(), @app.put(), @app.delete() 데코레이터
- from fastapi import FastAPI, HTTPException
- from pydantic import BaseModel
- 상태 코드: status.HTTP_201_CREATED, status.HTTP_404_NOT_FOUND
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import datetime

app = FastAPI(title="Request/Response API")

# Pydantic 모델 정의
class Item(BaseModel):
    """
    TODO: 아이템 데이터 모델을 정의하세요
    - id: Optional[int] = None
    - name: str
    - description: Optional[str] = None
    - price: float
    - is_available: bool = True
    """
    pass

class ItemCreate(BaseModel):
    """
    TODO: 아이템 생성용 모델을 정의하세요 (id 제외)
    """
    pass

class ItemUpdate(BaseModel):
    """
    TODO: 아이템 업데이트용 모델을 정의하세요 (모든 필드 Optional)
    """
    pass

# 임시 데이터베이스 (메모리)
fake_items_db: List[Item] = []
next_id = 1

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    """
    TODO: 새로운 아이템을 생성하세요
    
    Args:
        item (ItemCreate): 생성할 아이템 데이터
        
    Returns:
        Item: 생성된 아이템 (ID 포함)
    """
    pass

@app.get("/items/", response_model=List[Item])
def get_items(skip: int = 0, limit: int = 100):
    """
    TODO: 아이템 목록을 반환하세요
    
    Args:
        skip (int): 건너뛸 개수
        limit (int): 반환할 최대 개수
        
    Returns:
        List[Item]: 아이템 목록
    """
    pass

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """
    TODO: 특정 아이템을 반환하세요
    아이템이 없으면 404 에러를 발생시키세요
    
    Args:
        item_id (int): 아이템 ID
        
    Returns:
        Item: 아이템 데이터
        
    Raises:
        HTTPException: 아이템을 찾을 수 없는 경우
    """
    pass

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: ItemUpdate):
    """
    TODO: 아이템을 업데이트하세요
    
    Args:
        item_id (int): 업데이트할 아이템 ID
        item_update (ItemUpdate): 업데이트 데이터
        
    Returns:
        Item: 업데이트된 아이템
        
    Raises:
        HTTPException: 아이템을 찾을 수 없는 경우
    """
    pass

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    """
    TODO: 아이템을 삭제하세요
    
    Args:
        item_id (int): 삭제할 아이템 ID
        
    Raises:
        HTTPException: 아이템을 찾을 수 없는 경우
    """
    pass

@app.get("/items/search/", response_model=List[Item])
def search_items(q: Optional[str] = None, min_price: Optional[float] = None, max_price: Optional[float] = None):
    """
    TODO: 아이템을 검색하세요
    - q: 이름에 포함된 문자열로 검색
    - min_price: 최소 가격 필터
    - max_price: 최대 가격 필터
    
    Args:
        q (str, optional): 검색 쿼리
        min_price (float, optional): 최소 가격
        max_price (float, optional): 최대 가격
        
    Returns:
        List[Item]: 검색된 아이템 목록
    """
    pass

@app.post("/items/{item_id}/toggle")
def toggle_item_availability(item_id: int):
    """
    TODO: 아이템의 가용성을 토글하세요
    
    Args:
        item_id (int): 토글할 아이템 ID
        
    Returns:
        dict: {"message": "Item availability toggled", "item": item}
        
    Raises:
        HTTPException: 아이템을 찾을 수 없는 경우
    """
    pass

@app.get("/stats")
def get_stats():
    """
    TODO: 아이템 통계를 반환하세요
    
    Returns:
        dict: {
            "total_items": 전체 아이템 수,
            "available_items": 사용 가능한 아이템 수,
            "average_price": 평균 가격,
            "timestamp": 현재 시간
        }
    """
    pass

# 서버 실행용
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
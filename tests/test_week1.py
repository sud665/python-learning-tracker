"""
Week 1 테스트

pytest를 사용한 자동 테스트 코드
"""

import pytest
import sys
import os

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Solutions를 테스트용으로 import
try:
    from solutions.week1.challenge_01_variables import create_variables, check_types, convert_types
    from solutions.week1.challenge_02_functions import greet, calculate_area, get_max_min, create_profile
except ImportError:
    pytest.skip("Solution files not found", allow_module_level=True)

class TestChallenge01Variables:
    """Challenge 01: 변수와 타입 테스트"""
    
    def test_create_variables(self):
        """변수 생성 테스트"""
        result = create_variables()
        
        assert isinstance(result, dict)
        assert "name" in result
        assert "age" in result
        assert "height" in result
        assert "is_student" in result
        
        assert isinstance(result["name"], str)
        assert isinstance(result["age"], int)
        assert isinstance(result["height"], float)
        assert isinstance(result["is_student"], bool)
    
    def test_check_types(self):
        """타입 확인 테스트"""
        assert check_types(123) == "int"
        assert check_types("hello") == "str"
        assert check_types(3.14) == "float"
        assert check_types(True) == "bool"
        assert check_types([1, 2, 3]) == "list"
        assert check_types({"key": "value"}) == "dict"
    
    def test_convert_types(self):
        """타입 변환 테스트"""
        result = convert_types()
        
        assert isinstance(result, tuple)
        assert len(result) == 4
        
        int_val, str_val, float_val, bool_val = result
        
        assert int_val == 123
        assert isinstance(int_val, int)
        
        assert str_val == "456"
        assert isinstance(str_val, str)
        
        assert float_val == 3.14
        assert isinstance(float_val, float)
        
        assert bool_val is False
        assert isinstance(bool_val, bool)

class TestChallenge02Functions:
    """Challenge 02: 함수 테스트"""
    
    def test_greet(self):
        """인사말 함수 테스트"""
        result = greet("김철수")
        assert result == "안녕하세요, 김철수님!"
        
        result = greet("이영희")
        assert result == "안녕하세요, 이영희님!"
    
    def test_calculate_area(self):
        """넓이 계산 테스트"""
        # 정사각형 (기본값 사용)
        assert calculate_area(5) == 5
        
        # 직사각형
        assert calculate_area(5, 3) == 15
        assert calculate_area(10, 2) == 20
        
        # 소수점 테스트
        assert calculate_area(2.5, 4) == 10.0
    
    def test_get_max_min(self):
        """최대값/최소값 테스트"""
        result = get_max_min(1, 5, 3, 9, 2)
        assert result == (9, 1)
        
        result = get_max_min(10)
        assert result == (10, 10)
        
        result = get_max_min(-5, -1, -10)
        assert result == (-1, -10)
    
    def test_create_profile(self):
        """프로필 생성 테스트"""
        result = create_profile(name="홍길동", age=25, city="서울")
        
        assert isinstance(result, dict)
        assert result["name"] == "홍길동"
        assert result["age"] == 25
        assert result["city"] == "서울"
        
        # 빈 프로필
        result = create_profile()
        assert isinstance(result, dict)

# 추가 테스트를 위한 더미 클래스들
class TestChallengeTemplate:
    """템플릿 테스트 클래스 - 다른 챌린지용"""
    
    def test_placeholder(self):
        """placeholder 테스트"""
        # 다른 챌린지들이 추가되면 여기에 테스트 추가
        pass

if __name__ == "__main__":
    # 직접 실행 시 pytest 실행
    pytest.main([__file__, "-v"])
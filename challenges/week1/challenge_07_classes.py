"""
Challenge 07: 클래스

TODO: 다음 클래스들을 완성하세요

힌트:
- class ClassName:
- __init__(self, ...): 생성자
- self.attribute: 인스턴스 변수
- def method(self, ...): 인스턴스 메서드
"""

class Calculator:
    """간단한 계산기 클래스"""
    
    def __init__(self):
        """
        TODO: 계산기 초기화
        - result: 현재 결과값 (초기값 0)
        """
        pass
    
    def add(self, value):
        """
        TODO: 현재 결과에 값을 더하기
        
        Args:
            value (float): 더할 값
            
        Returns:
            float: 현재 결과값
        """
        pass
    
    def subtract(self, value):
        """
        TODO: 현재 결과에서 값을 빼기
        
        Args:
            value (float): 뺄 값
            
        Returns:
            float: 현재 결과값
        """
        pass
    
    def multiply(self, value):
        """
        TODO: 현재 결과에 값을 곱하기
        
        Args:
            value (float): 곱할 값
            
        Returns:
            float: 현재 결과값
        """
        pass
    
    def get_result(self):
        """
        TODO: 현재 결과값 반환
        
        Returns:
            float: 현재 결과값
        """
        pass
    
    def reset(self):
        """
        TODO: 결과값을 0으로 초기화
        """
        pass

class BankAccount:
    """은행 계좌 클래스"""
    
    def __init__(self, account_number, owner, initial_balance=0):
        """
        TODO: 계좌 초기화
        
        Args:
            account_number (str): 계좌번호
            owner (str): 계좌 소유자
            initial_balance (float): 초기 잔액 (기본값: 0)
        """
        pass
    
    def deposit(self, amount):
        """
        TODO: 입금
        
        Args:
            amount (float): 입금액 (양수여야 함)
            
        Returns:
            bool: 입금 성공 여부
        """
        pass
    
    def withdraw(self, amount):
        """
        TODO: 출금
        잔액이 부족하면 실패
        
        Args:
            amount (float): 출금액 (양수여야 함)
            
        Returns:
            bool: 출금 성공 여부
        """
        pass
    
    def get_balance(self):
        """
        TODO: 잔액 조회
        
        Returns:
            float: 현재 잔액
        """
        pass
    
    def get_account_info(self):
        """
        TODO: 계좌 정보 반환
        
        Returns:
            dict: {"account_number": ..., "owner": ..., "balance": ...}
        """
        pass

class Student:
    """학생 클래스"""
    
    def __init__(self, name, student_id):
        """
        TODO: 학생 초기화
        
        Args:
            name (str): 학생 이름
            student_id (str): 학번
        """
        pass
    
    def add_grade(self, subject, score):
        """
        TODO: 과목 성적 추가
        
        Args:
            subject (str): 과목명
            score (float): 점수
        """
        pass
    
    def get_average(self):
        """
        TODO: 전체 평균 계산
        
        Returns:
            float: 평균 점수 (소수점 2자리까지)
        """
        pass
    
    def get_grade_report(self):
        """
        TODO: 성적표 생성
        
        Returns:
            dict: {"name": ..., "student_id": ..., "grades": {...}, "average": ...}
        """
        pass

# 자동 테스트용 (수정 금지)
if __name__ == "__main__":
    try:
        # Calculator 테스트
        calc = Calculator()
        calc.add(10)
        calc.subtract(3)
        calc.multiply(2)
        print("Calculator result:", calc.get_result())
        
        # BankAccount 테스트
        account = BankAccount("123-456", "홍길동", 1000)
        account.deposit(500)
        account.withdraw(300)
        print("Account info:", account.get_account_info())
        
        # Student 테스트
        student = Student("김철수", "2024001")
        student.add_grade("수학", 90)
        student.add_grade("영어", 85)
        student.add_grade("과학", 92)
        print("Grade report:", student.get_grade_report())
        
    except Exception as e:
        print(f"오류 발생: {e}")
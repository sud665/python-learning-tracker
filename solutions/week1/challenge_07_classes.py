"""
Challenge 07: 클래스 - 솔루션

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
        self.result = 0
    
    def add(self, value):
        """
        TODO: 현재 결과에 값을 더하기
        
        Args:
            value (float): 더할 값
            
        Returns:
            float: 현재 결과값
        """
        self.result += value
        return self.result
    
    def subtract(self, value):
        """
        TODO: 현재 결과에서 값을 빼기
        
        Args:
            value (float): 뺄 값
            
        Returns:
            float: 현재 결과값
        """
        self.result -= value
        return self.result
    
    def multiply(self, value):
        """
        TODO: 현재 결과에 값을 곱하기
        
        Args:
            value (float): 곱할 값
            
        Returns:
            float: 현재 결과값
        """
        self.result *= value
        return self.result
    
    def get_result(self):
        """
        TODO: 현재 결과값 반환
        
        Returns:
            float: 현재 결과값
        """
        return self.result
    
    def reset(self):
        """
        TODO: 결과값을 0으로 초기화
        """
        self.result = 0

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
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
    
    def deposit(self, amount):
        """
        TODO: 입금
        
        Args:
            amount (float): 입금액 (양수여야 함)
            
        Returns:
            bool: 입금 성공 여부
        """
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """
        TODO: 출금
        잔액이 부족하면 실패
        
        Args:
            amount (float): 출금액 (양수여야 함)
            
        Returns:
            bool: 출금 성공 여부
        """
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        """
        TODO: 잔액 조회
        
        Returns:
            float: 현재 잔액
        """
        return self.balance
    
    def get_account_info(self):
        """
        TODO: 계좌 정보 반환
        
        Returns:
            dict: {"account_number": ..., "owner": ..., "balance": ...}
        """
        return {
            "account_number": self.account_number,
            "owner": self.owner,
            "balance": self.balance
        }

class Student:
    """학생 클래스"""
    
    def __init__(self, name, student_id):
        """
        TODO: 학생 초기화
        
        Args:
            name (str): 학생 이름
            student_id (str): 학번
        """
        self.name = name
        self.student_id = student_id
        self.grades = {}
    
    def add_grade(self, subject, score):
        """
        TODO: 과목 성적 추가
        
        Args:
            subject (str): 과목명
            score (float): 점수
        """
        self.grades[subject] = score
    
    def get_average(self):
        """
        TODO: 전체 평균 계산
        
        Returns:
            float: 평균 점수 (소수점 2자리까지)
        """
        if not self.grades:
            return 0.0
        
        average = sum(self.grades.values()) / len(self.grades)
        return round(average, 2)
    
    def get_grade_report(self):
        """
        TODO: 성적표 생성
        
        Returns:
            dict: {"name": ..., "student_id": ..., "grades": {...}, "average": ...}
        """
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grades": self.grades.copy(),
            "average": self.get_average()
        }

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
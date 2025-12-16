"""
코드 검증 모듈

사용자가 작성한 챌린지 코드를 자동으로 테스트하고 검증합니다.
"""

import importlib.util
import sys
import os
import traceback
import pytest
from typing import Dict, List, Tuple, Any
from .progress import ProgressTracker

class ChallengeValidator:
    def __init__(self, progress_tracker: ProgressTracker = None):
        self.progress_tracker = progress_tracker or ProgressTracker()
        self.test_results = {}
    
    def validate_challenge(self, challenge_id: str) -> Dict[str, Any]:
        """
        특정 챌린지를 검증합니다.
        
        Args:
            challenge_id: 챌린지 ID (예: "challenge_01_variables")
            
        Returns:
            검증 결과 딕셔너리
        """
        try:
            # 챌린지 파일 경로 찾기
            week = self._get_week_from_challenge_id(challenge_id)
            challenge_path = f"challenges/week{week}/{challenge_id}.py"
            solution_path = f"solutions/week{week}/{challenge_id}.py"
            
            if not os.path.exists(challenge_path):
                return {
                    "success": False,
                    "error": f"챌린지 파일을 찾을 수 없습니다: {challenge_path}",
                    "score": 0,
                    "details": []
                }
            
            # 사용자 코드 로드
            user_module = self._load_module(challenge_path, f"user_{challenge_id}")
            
            # 솔루션 코드 로드 (비교용)
            solution_module = None
            if os.path.exists(solution_path):
                solution_module = self._load_module(solution_path, f"solution_{challenge_id}")
            
            # 테스트 실행
            test_results = self._run_tests(challenge_id, user_module, solution_module)
            
            # 점수 계산
            score = self._calculate_score(test_results)
            
            # 진행상황 업데이트
            if score >= 70:  # 70점 이상이면 완료로 표시
                self.progress_tracker.mark_completed(challenge_id, score)
            else:
                self.progress_tracker.mark_failed(challenge_id, score)
            
            return {
                "success": True,
                "score": score,
                "details": test_results,
                "passed": score >= 70
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"검증 중 오류 발생: {str(e)}",
                "traceback": traceback.format_exc(),
                "score": 0
            }
    
    def _get_week_from_challenge_id(self, challenge_id: str) -> int:
        """챌린지 ID에서 주차를 추출합니다."""
        challenge_num = int(challenge_id.split('_')[1])
        if challenge_num <= 10:
            return 1
        elif challenge_num <= 15:
            return 2
        else:
            return 3
    
    def _load_module(self, file_path: str, module_name: str):
        """Python 모듈을 동적으로 로드합니다."""
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        
        # 모듈을 sys.modules에 추가하여 import 문제 방지
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        return module
    
    def _run_tests(self, challenge_id: str, user_module, solution_module) -> List[Dict]:
        """특정 챌린지에 대한 테스트를 실행합니다."""
        test_results = []
        
        # 챌린지별 테스트 케이스 정의
        test_cases = self._get_test_cases(challenge_id)
        
        for test_case in test_cases:
            result = self._run_single_test(test_case, user_module, solution_module)
            test_results.append(result)
        
        return test_results
    
    def _get_test_cases(self, challenge_id: str) -> List[Dict]:
        """챌린지별 테스트 케이스를 반환합니다."""
        test_cases = {
            "challenge_01_variables": [
                {
                    "name": "create_variables",
                    "description": "변수 생성 테스트",
                    "function": "create_variables",
                    "args": [],
                    "expected_type": dict,
                    "required_keys": ["name", "age", "height", "is_student"]
                },
                {
                    "name": "check_types", 
                    "description": "타입 확인 테스트",
                    "function": "check_types",
                    "test_data": [
                        (123, "int"),
                        ("hello", "str"), 
                        (3.14, "float"),
                        (True, "bool")
                    ]
                },
                {
                    "name": "convert_types",
                    "description": "타입 변환 테스트",
                    "function": "convert_types",
                    "args": [],
                    "expected": (123, "456", 3.14, False)
                }
            ],
            "challenge_02_functions": [
                {
                    "name": "greet",
                    "description": "인사말 함수 테스트",
                    "function": "greet",
                    "test_data": [
                        (("김철수",), "안녕하세요, 김철수님!")
                    ]
                },
                {
                    "name": "calculate_area",
                    "description": "넓이 계산 테스트",
                    "function": "calculate_area", 
                    "test_data": [
                        ((5,), 5),
                        ((5, 3), 15)
                    ]
                }
            ]
        }
        
        return test_cases.get(challenge_id, [])
    
    def _run_single_test(self, test_case: Dict, user_module, solution_module) -> Dict:
        """단일 테스트 케이스를 실행합니다."""
        try:
            function_name = test_case["function"]
            
            if not hasattr(user_module, function_name):
                return {
                    "name": test_case["name"],
                    "description": test_case["description"],
                    "passed": False,
                    "error": f"함수 '{function_name}'를 찾을 수 없습니다.",
                    "score": 0
                }
            
            user_function = getattr(user_module, function_name)
            
            # 테스트 데이터가 있는 경우
            if "test_data" in test_case:
                passed_tests = 0
                total_tests = len(test_case["test_data"])
                
                for args, expected in test_case["test_data"]:
                    try:
                        if isinstance(args, tuple):
                            result = user_function(*args)
                        else:
                            result = user_function(args)
                        
                        if result == expected:
                            passed_tests += 1
                    except Exception as e:
                        pass  # 테스트 실패
                
                score = (passed_tests / total_tests) * 100
                return {
                    "name": test_case["name"],
                    "description": test_case["description"],
                    "passed": passed_tests == total_tests,
                    "score": score,
                    "details": f"{passed_tests}/{total_tests} 테스트 통과"
                }
            
            # 단일 테스트인 경우
            elif "args" in test_case:
                try:
                    result = user_function(*test_case["args"])
                    
                    # 타입 검사
                    if "expected_type" in test_case:
                        if not isinstance(result, test_case["expected_type"]):
                            return {
                                "name": test_case["name"],
                                "description": test_case["description"],
                                "passed": False,
                                "error": f"반환 타입이 {test_case['expected_type']}이어야 합니다.",
                                "score": 0
                            }
                    
                    # 필수 키 검사 (딕셔너리인 경우)
                    if "required_keys" in test_case and isinstance(result, dict):
                        missing_keys = set(test_case["required_keys"]) - set(result.keys())
                        if missing_keys:
                            return {
                                "name": test_case["name"],
                                "description": test_case["description"],
                                "passed": False,
                                "error": f"필수 키가 누락되었습니다: {missing_keys}",
                                "score": 50
                            }
                    
                    # 정확한 값 검사
                    if "expected" in test_case:
                        if result != test_case["expected"]:
                            return {
                                "name": test_case["name"],
                                "description": test_case["description"],
                                "passed": False,
                                "error": f"예상값: {test_case['expected']}, 실제값: {result}",
                                "score": 50
                            }
                    
                    return {
                        "name": test_case["name"],
                        "description": test_case["description"],
                        "passed": True,
                        "score": 100
                    }
                    
                except Exception as e:
                    return {
                        "name": test_case["name"],
                        "description": test_case["description"],
                        "passed": False,
                        "error": f"실행 중 오류: {str(e)}",
                        "score": 0
                    }
            
        except Exception as e:
            return {
                "name": test_case.get("name", "Unknown"),
                "description": test_case.get("description", ""),
                "passed": False,
                "error": f"테스트 실행 중 오류: {str(e)}",
                "score": 0
            }
    
    def _calculate_score(self, test_results: List[Dict]) -> int:
        """테스트 결과에서 점수를 계산합니다."""
        if not test_results:
            return 0
        
        total_score = sum(result.get("score", 0) for result in test_results)
        return int(total_score / len(test_results))
    
    def validate_all_challenges(self, week: int = None) -> Dict[str, Any]:
        """모든 챌린지 또는 특정 주차의 챌린지를 검증합니다."""
        challenges = self._get_challenge_list(week)
        results = {}
        
        for challenge_id in challenges:
            results[challenge_id] = self.validate_challenge(challenge_id)
        
        return results
    
    def _get_challenge_list(self, week: int = None) -> List[str]:
        """챌린지 목록을 반환합니다."""
        challenges = []
        
        if week is None or week == 1:
            for i in range(1, 11):
                challenge_names = [
                    "variables", "functions", "conditions", "loops", "lists",
                    "dicts", "classes", "modules", "files", "exceptions"
                ]
                challenges.append(f"challenge_{i:02d}_{challenge_names[i-1]}")
        
        if week is None or week == 2:
            challenge_names = ["comprehension", "lambda", "decorators", "context_manager", "type_hints"]
            for i, name in enumerate(challenge_names, 11):
                challenges.append(f"challenge_{i:02d}_{name}")
        
        if week is None or week == 3:
            challenge_names = ["fastapi_basics", "request_response", "path_query_params", "request_body", "authentication", "final_project"]
            for i, name in enumerate(challenge_names, 16):
                challenges.append(f"challenge_{i:02d}_{name}")
        
        return challenges
    
    def get_validation_summary(self) -> Dict[str, Any]:
        """검증 결과 요약을 반환합니다."""
        return {
            "total_challenges": len(self.test_results),
            "passed_challenges": sum(1 for r in self.test_results.values() if r.get("passed", False)),
            "average_score": sum(r.get("score", 0) for r in self.test_results.values()) / max(len(self.test_results), 1),
            "progress": self.progress_tracker.get_progress_summary()
        }
"""
진행상황 추적 모듈

사용자의 챌린지 완료 상황을 JSON 파일에 저장하고 관리합니다.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class ProgressTracker:
    def __init__(self, data_file: str = "data/progress.json"):
        self.data_file = data_file
        self.progress_data = self._load_progress()
    
    def _load_progress(self) -> Dict:
        """진행상황 데이터를 로드합니다."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        
        # 기본 구조 반환
        return {
            "completed_challenges": [],
            "challenge_scores": {},
            "completion_times": {},
            "total_score": 0,
            "last_updated": None
        }
    
    def _save_progress(self) -> None:
        """진행상황 데이터를 저장합니다."""
        self.progress_data["last_updated"] = datetime.now().isoformat()
        
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress_data, f, indent=2, ensure_ascii=False)
    
    def mark_completed(self, challenge_id: str, score: int = 100) -> None:
        """챌린지를 완료로 표시합니다."""
        if challenge_id not in self.progress_data["completed_challenges"]:
            self.progress_data["completed_challenges"].append(challenge_id)
        
        self.progress_data["challenge_scores"][challenge_id] = score
        self.progress_data["completion_times"][challenge_id] = datetime.now().isoformat()
        
        self._update_total_score()
        self._save_progress()
    
    def mark_failed(self, challenge_id: str, score: int = 0) -> None:
        """챌린지를 실패로 표시합니다."""
        if challenge_id in self.progress_data["completed_challenges"]:
            self.progress_data["completed_challenges"].remove(challenge_id)
        
        self.progress_data["challenge_scores"][challenge_id] = score
        self._update_total_score()
        self._save_progress()
    
    def _update_total_score(self) -> None:
        """전체 점수를 업데이트합니다."""
        self.progress_data["total_score"] = sum(self.progress_data["challenge_scores"].values())
    
    def is_completed(self, challenge_id: str) -> bool:
        """챌린지가 완료되었는지 확인합니다."""
        return challenge_id in self.progress_data["completed_challenges"]
    
    def get_score(self, challenge_id: str) -> int:
        """특정 챌린지의 점수를 반환합니다."""
        return self.progress_data["challenge_scores"].get(challenge_id, 0)
    
    def get_completion_time(self, challenge_id: str) -> Optional[str]:
        """특정 챌린지의 완료 시간을 반환합니다."""
        return self.progress_data["completion_times"].get(challenge_id)
    
    def get_completed_challenges(self) -> List[str]:
        """완료된 챌린지 목록을 반환합니다."""
        return self.progress_data["completed_challenges"].copy()
    
    def get_total_score(self) -> int:
        """전체 점수를 반환합니다."""
        return self.progress_data["total_score"]
    
    def get_progress_summary(self) -> Dict:
        """진행상황 요약을 반환합니다."""
        total_challenges = 21  # Week1: 10개 + Week2: 5개 + Week3: 6개
        completed_count = len(self.progress_data["completed_challenges"])
        
        return {
            "total_challenges": total_challenges,
            "completed_challenges": completed_count,
            "completion_rate": (completed_count / total_challenges) * 100,
            "total_score": self.progress_data["total_score"],
            "average_score": self.progress_data["total_score"] / max(completed_count, 1),
            "last_updated": self.progress_data["last_updated"]
        }
    
    def get_week_progress(self, week: int) -> Dict:
        """특정 주차의 진행상황을 반환합니다."""
        if week == 1:
            challenges = [f"challenge_{i:02d}_*" for i in range(1, 11)]
        elif week == 2:
            challenges = [f"challenge_{i:02d}_*" for i in range(11, 16)]
        elif week == 3:
            challenges = [f"challenge_{i:02d}_*" for i in range(16, 22)]
        else:
            return {}
        
        week_completed = [c for c in self.progress_data["completed_challenges"] 
                         if any(c.startswith(ch.split('_')[0] + '_' + ch.split('_')[1]) 
                               for ch in challenges)]
        
        week_scores = {k: v for k, v in self.progress_data["challenge_scores"].items()
                      if any(k.startswith(ch.split('_')[0] + '_' + ch.split('_')[1]) 
                            for ch in challenges)}
        
        return {
            "week": week,
            "completed_challenges": len(week_completed),
            "total_challenges": len(challenges),
            "completion_rate": (len(week_completed) / len(challenges)) * 100,
            "scores": week_scores,
            "average_score": sum(week_scores.values()) / max(len(week_scores), 1)
        }
    
    def reset_progress(self) -> None:
        """전체 진행상황을 리셋합니다."""
        self.progress_data = {
            "completed_challenges": [],
            "challenge_scores": {},
            "completion_times": {},
            "total_score": 0,
            "last_updated": None
        }
        self._save_progress()
    
    def export_progress(self, filename: str) -> None:
        """진행상황을 다른 파일로 내보냅니다."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.progress_data, f, indent=2, ensure_ascii=False)
#!/usr/bin/env python3
"""
Python Learning Tracker - 메인 CLI 엔트리포인트

사용법:
    python main.py list                    # 모든 챌린지 목록
    python main.py list --week 1           # Week 1 챌린지만
    python main.py check 01                # 특정 챌린지 테스트
    python main.py check all               # 전체 테스트
    python main.py check all --week 1      # Week 1만 테스트
    python main.py progress                # 진행상황 보기
    python main.py hint 01                 # 힌트 보기
    python main.py solution 01             # 정답 보기
    python main.py reset                   # 진행상황 리셋
    python main.py export progress.json    # 진행상황 내보내기
"""

import click
import sys
import os

# 현재 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tracker.cli import CLIInterface
from rich.console import Console

console = Console()

@click.group()
@click.version_option("1.0.0", prog_name="Python Learning Tracker")
def cli():
    """
    🐍 Python Learning Tracker
    
    Python 학습을 위한 인터랙티브 챌린지 도구입니다.
    """
    pass

@cli.command()
@click.option('--week', type=int, help='특정 주차만 표시 (1 또는 2)')
def list(week):
    """모든 챌린지 목록을 표시합니다."""
    interface = CLIInterface()
    interface.list_challenges(week)

@cli.command()
@click.argument('challenge', required=True)
@click.option('--week', type=int, help='전체 테스트 시 특정 주차만 (1 또는 2)')
def check(challenge, week):
    """
    챌린지를 검증합니다.
    
    CHALLENGE: 챌린지 번호 (예: 01) 또는 'all'
    """
    interface = CLIInterface()
    
    if challenge.lower() == 'all':
        interface.check_all_challenges(week)
    else:
        # 챌린지 번호를 전체 ID로 변환
        challenge_id = _convert_to_challenge_id(challenge)
        if challenge_id:
            interface.check_challenge(challenge_id)
        else:
            console.print("[red]❌ 잘못된 챌린지 번호입니다. 01-21 사이의 번호를 입력하세요.[/red]")

@cli.command()
def progress():
    """현재 학습 진행상황을 표시합니다."""
    interface = CLIInterface()
    interface.show_progress()

@cli.command()
@click.argument('challenge_num', required=True)
def hint(challenge_num):
    """
    챌린지의 힌트를 표시합니다.
    
    CHALLENGE_NUM: 챌린지 번호 (예: 01)
    """
    challenge_id = _convert_to_challenge_id(challenge_num)
    if challenge_id:
        interface = CLIInterface()
        interface.show_hint(challenge_id)
    else:
        console.print("[red]❌ 잘못된 챌린지 번호입니다. 01-21 사이의 번호를 입력하세요.[/red]")

@cli.command()
@click.argument('challenge_num', required=True)
def solution(challenge_num):
    """
    챌린지의 정답을 표시합니다.
    
    CHALLENGE_NUM: 챌린지 번호 (예: 01)
    """
    challenge_id = _convert_to_challenge_id(challenge_num)
    if challenge_id:
        interface = CLIInterface()
        interface.show_solution(challenge_id)
    else:
        console.print("[red]❌ 잘못된 챌린지 번호입니다. 01-21 사이의 번호를 입력하세요.[/red]")

@cli.command()
def reset():
    """모든 진행상황을 리셋합니다."""
    interface = CLIInterface()
    interface.reset_progress()

@cli.command()
@click.argument('filename', required=True)
def export(filename):
    """
    진행상황을 파일로 내보냅니다.
    
    FILENAME: 저장할 파일명 (예: progress.json)
    """
    interface = CLIInterface()
    interface.export_progress(filename)

@cli.command()
def test():
    """pytest를 사용하여 모든 테스트를 실행합니다."""
    console.print("[bold yellow]🧪 pytest 테스트 실행 중...[/bold yellow]")
    
    try:
        import pytest
        exit_code = pytest.main([
            "tests/",
            "-v",
            "--tb=short",
            "--color=yes"
        ])
        
        if exit_code == 0:
            console.print("[green]✅ 모든 테스트가 통과했습니다![/green]")
        else:
            console.print("[red]❌ 일부 테스트가 실패했습니다.[/red]")
            
    except ImportError:
        console.print("[red]❌ pytest가 설치되지 않았습니다. 'pip install pytest'를 실행하세요.[/red]")

def _convert_to_challenge_id(challenge_num: str) -> str:
    """
    챌린지 번호를 전체 챌린지 ID로 변환합니다.
    
    Args:
        challenge_num: 챌린지 번호 (예: "01", "1", "21")
        
    Returns:
        전체 챌린지 ID 또는 None
    """
    try:
        num = int(challenge_num)
        if not (1 <= num <= 21):
            return None
        
        # 챌린지명 매핑
        challenge_names = {
            1: "variables", 2: "functions", 3: "conditions", 4: "loops", 5: "lists",
            6: "dicts", 7: "classes", 8: "modules", 9: "files", 10: "exceptions",
            11: "comprehension", 12: "lambda", 13: "decorators", 14: "context_manager", 15: "type_hints",
            16: "fastapi_basics", 17: "request_response", 18: "path_query_params", 
            19: "request_body", 20: "authentication", 21: "final_project"
        }
        
        return f"challenge_{num:02d}_{challenge_names[num]}"
        
    except ValueError:
        return None

@cli.command()
def demo():
    """데모용 간단한 챌린지 실행"""
    console.print("[bold green]🚀 Python Learning Tracker 데모[/bold green]\n")
    
    console.print("환영합니다! 이것은 Python 학습을 위한 인터랙티브 도구입니다.\n")
    
    console.print("사용 가능한 명령어:")
    console.print("• [cyan]python main.py list[/cyan] - 모든 챌린지 목록")
    console.print("• [cyan]python main.py check 01[/cyan] - 첫 번째 챌린지 테스트")
    console.print("• [cyan]python main.py progress[/cyan] - 진행상황 확인")
    console.print("• [cyan]python main.py hint 01[/cyan] - 힌트 보기")
    console.print("• [cyan]python main.py solution 01[/cyan] - 정답 보기")
    
    console.print("\n[yellow]💡 팁: 'python main.py --help' 명령어로 더 많은 옵션을 확인하세요![/yellow]")

if __name__ == '__main__':
    # 기본 도움말 표시
    if len(sys.argv) == 1:
        console.print("[bold blue]🐍 Python Learning Tracker[/bold blue]\n")
        console.print("사용법: python main.py [COMMAND] [OPTIONS]\n")
        console.print("명령어 목록을 보려면: [cyan]python main.py --help[/cyan]")
        console.print("데모를 보려면: [cyan]python main.py demo[/cyan]")
        sys.exit(0)
    
    cli()
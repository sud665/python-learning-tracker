"""
CLI 인터페이스 모듈

rich 라이브러리를 사용하여 예쁜 명령줄 인터페이스를 제공합니다.
"""

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.text import Text
from rich.syntax import Syntax
from rich.markdown import Markdown
import os
from typing import Optional

from .progress import ProgressTracker
from .validator import ChallengeValidator

console = Console()

class CLIInterface:
    def __init__(self):
        self.progress_tracker = ProgressTracker()
        self.validator = ChallengeValidator(self.progress_tracker)
    
    def list_challenges(self, week: Optional[int] = None):
        """모든 챌린지 목록을 출력합니다."""
        console.print("\n[bold blue]📚 Python 학습 트래커 - 챌린지 목록[/bold blue]\n")
        
        challenges_info = {
            1: [
                ("challenge_01_variables", "변수와 타입"),
                ("challenge_02_functions", "함수"),
                ("challenge_03_conditions", "조건문"),
                ("challenge_04_loops", "반복문"),
                ("challenge_05_lists", "리스트"),
                ("challenge_06_dicts", "딕셔너리"),
                ("challenge_07_classes", "클래스"),
                ("challenge_08_modules", "모듈"),
                ("challenge_09_files", "파일 처리"),
                ("challenge_10_exceptions", "예외 처리")
            ],
            2: [
                ("challenge_11_comprehension", "리스트 컴프리헨션"),
                ("challenge_12_lambda", "람다 함수"),
                ("challenge_13_decorators", "데코레이터"),
                ("challenge_14_context_manager", "컨텍스트 매니저"),
                ("challenge_15_type_hints", "타입 힌트")
            ],
            3: [
                ("challenge_16_fastapi_basics", "FastAPI 기초"),
                ("challenge_17_request_response", "요청/응답 처리"),
                ("challenge_18_path_query_params", "Path & Query Parameters"),
                ("challenge_19_request_body", "Request Body & Pydantic"),
                ("challenge_20_authentication", "인증과 보안"),
                ("challenge_21_final_project", "최종 프로젝트 (블로그 API)")
            ]
        }
        
        weeks_to_show = [week] if week else [1, 2, 3]
        
        for week_num in weeks_to_show:
            table = Table(title=f"Week {week_num} 챌린지")
            table.add_column("번호", justify="center", style="cyan")
            table.add_column("챌린지 ID", style="yellow")
            table.add_column("제목", style="green")
            table.add_column("상태", justify="center")
            table.add_column("점수", justify="center")
            
            for i, (challenge_id, title) in enumerate(challenges_info[week_num], 1):
                if self.progress_tracker.is_completed(challenge_id):
                    status = "[green]✅ 완료[/green]"
                    score = str(self.progress_tracker.get_score(challenge_id))
                else:
                    status = "[red]❌ 미완료[/red]"
                    score = "-"
                
                table.add_row(
                    str(i),
                    challenge_id,
                    title,
                    status,
                    score
                )
            
            console.print(table)
            console.print()
    
    def show_progress(self):
        """전체 진행상황을 출력합니다."""
        summary = self.progress_tracker.get_progress_summary()
        
        console.print("\n[bold blue]📊 학습 진행상황[/bold blue]\n")
        
        # 전체 진행률
        progress_text = f"전체 진행률: {summary['completed_challenges']}/{summary['total_challenges']} ({summary['completion_rate']:.1f}%)"
        progress_bar = Progress(
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=40),
            TextColumn("[progress.percentage]{task.percentage:>3.1f}%"),
        )
        
        with progress_bar:
            task = progress_bar.add_task(progress_text, total=100)
            progress_bar.update(task, completed=summary['completion_rate'])
        
        # 상세 정보 테이블
        info_table = Table(title="상세 정보")
        info_table.add_column("항목", style="cyan")
        info_table.add_column("값", style="yellow")
        
        info_table.add_row("완료한 챌린지", str(summary['completed_challenges']))
        info_table.add_row("전체 챌린지", str(summary['total_challenges']))
        info_table.add_row("총 점수", str(summary['total_score']))
        info_table.add_row("평균 점수", f"{summary['average_score']:.1f}")
        info_table.add_row("마지막 업데이트", summary['last_updated'] or "없음")
        
        console.print(info_table)
        
        # 주차별 진행상황
        console.print("\n[bold green]📈 주차별 진행상황[/bold green]\n")
        
        for week in [1, 2, 3]:
            week_progress = self.progress_tracker.get_week_progress(week)
            
            week_table = Table(title=f"Week {week}")
            week_table.add_column("항목", style="cyan")
            week_table.add_column("값", style="yellow")
            
            week_table.add_row("완료한 챌린지", f"{week_progress['completed_challenges']}/{week_progress['total_challenges']}")
            week_table.add_row("완료율", f"{week_progress['completion_rate']:.1f}%")
            week_table.add_row("평균 점수", f"{week_progress['average_score']:.1f}")
            
            console.print(week_table)
        
        console.print()
    
    def check_challenge(self, challenge_id: str):
        """특정 챌린지를 검증합니다."""
        console.print(f"\n[bold yellow]🔍 {challenge_id} 검증 중...[/bold yellow]\n")
        
        with console.status("[bold green]테스트 실행 중...") as status:
            result = self.validator.validate_challenge(challenge_id)
        
        if not result["success"]:
            console.print(Panel(
                f"[red]❌ 검증 실패[/red]\n\n{result['error']}",
                title="오류",
                border_style="red"
            ))
            return
        
        # 결과 출력
        if result["passed"]:
            console.print(Panel(
                f"[green]✅ 테스트 통과![/green]\n\n점수: {result['score']}/100",
                title=f"🎉 {challenge_id} 완료!",
                border_style="green"
            ))
        else:
            console.print(Panel(
                f"[red]❌ 테스트 실패[/red]\n\n점수: {result['score']}/100\n\n계속 노력하세요!",
                title=f"😞 {challenge_id} 미완료",
                border_style="red"
            ))
        
        # 상세 결과
        if result["details"]:
            console.print("\n[bold]📋 상세 테스트 결과:[/bold]\n")
            
            detail_table = Table()
            detail_table.add_column("테스트", style="cyan")
            detail_table.add_column("설명", style="white")
            detail_table.add_column("결과", justify="center")
            detail_table.add_column("점수", justify="center")
            detail_table.add_column("오류/세부사항", style="red")
            
            for detail in result["details"]:
                status_icon = "✅" if detail["passed"] else "❌"
                status_text = "[green]통과[/green]" if detail["passed"] else "[red]실패[/red]"
                error_text = detail.get("error", detail.get("details", ""))
                
                detail_table.add_row(
                    detail["name"],
                    detail["description"],
                    status_icon + " " + status_text,
                    str(detail["score"]),
                    error_text
                )
            
            console.print(detail_table)
            console.print()
    
    def check_all_challenges(self, week: Optional[int] = None):
        """모든 챌린지를 검증합니다."""
        week_text = f"Week {week}" if week else "전체"
        console.print(f"\n[bold yellow]🔍 {week_text} 챌린지 검증 중...[/bold yellow]\n")
        
        results = self.validator.validate_all_challenges(week)
        
        # 결과 테이블
        result_table = Table(title=f"{week_text} 검증 결과")
        result_table.add_column("챌린지 ID", style="cyan")
        result_table.add_column("상태", justify="center")
        result_table.add_column("점수", justify="center")
        result_table.add_column("비고")
        
        total_score = 0
        passed_count = 0
        
        for challenge_id, result in results.items():
            if result["success"]:
                status = "✅ 통과" if result["passed"] else "❌ 실패"
                score = result["score"]
                note = ""
                if result["passed"]:
                    passed_count += 1
            else:
                status = "🚫 오류"
                score = 0
                note = "실행 오류"
            
            total_score += score
            
            result_table.add_row(
                challenge_id,
                status,
                str(score),
                note
            )
        
        console.print(result_table)
        
        # 요약 정보
        total_challenges = len(results)
        average_score = total_score / total_challenges if total_challenges > 0 else 0
        
        summary_text = f"""
총 챌린지: {total_challenges}
통과한 챌린지: {passed_count}
통과율: {(passed_count / total_challenges * 100):.1f}%
총 점수: {total_score}
평균 점수: {average_score:.1f}
        """.strip()
        
        console.print(Panel(
            summary_text,
            title="📊 검증 요약",
            border_style="blue"
        ))
        console.print()
    
    def show_hint(self, challenge_id: str):
        """챌린지의 힌트를 보여줍니다."""
        week = self._get_week_from_challenge_id(challenge_id)
        challenge_path = f"challenges/week{week}/{challenge_id}.py"
        
        if not os.path.exists(challenge_path):
            console.print(f"[red]❌ 챌린지 파일을 찾을 수 없습니다: {challenge_path}[/red]")
            return
        
        try:
            with open(challenge_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 힌트 섹션 추출
            lines = content.split('\n')
            hint_start = -1
            hint_end = -1
            
            for i, line in enumerate(lines):
                if line.strip().startswith('힌트:'):
                    hint_start = i
                elif hint_start != -1 and line.strip().startswith('"""') and i > hint_start:
                    hint_end = i
                    break
            
            if hint_start != -1:
                hint_lines = lines[hint_start:hint_end] if hint_end != -1 else lines[hint_start:]
                hint_text = '\n'.join(hint_lines)
                
                console.print(Panel(
                    hint_text,
                    title=f"💡 {challenge_id} 힌트",
                    border_style="yellow"
                ))
            else:
                console.print(f"[yellow]💡 {challenge_id}에 대한 힌트를 찾을 수 없습니다.[/yellow]")
                
        except Exception as e:
            console.print(f"[red]❌ 힌트를 읽는 중 오류 발생: {str(e)}[/red]")
    
    def show_solution(self, challenge_id: str):
        """챌린지의 정답을 보여줍니다."""
        week = self._get_week_from_challenge_id(challenge_id)
        solution_path = f"solutions/week{week}/{challenge_id}.py"
        
        if not os.path.exists(solution_path):
            console.print(f"[red]❌ 정답 파일을 찾을 수 없습니다: {solution_path}[/red]")
            return
        
        try:
            with open(solution_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            syntax = Syntax(content, "python", theme="monokai", line_numbers=True)
            
            console.print(Panel(
                syntax,
                title=f"📝 {challenge_id} 정답",
                border_style="green"
            ))
            
        except Exception as e:
            console.print(f"[red]❌ 정답을 읽는 중 오류 발생: {str(e)}[/red]")
    
    def _get_week_from_challenge_id(self, challenge_id: str) -> int:
        """챌린지 ID에서 주차를 추출합니다."""
        challenge_num = int(challenge_id.split('_')[1])
        if challenge_num <= 10:
            return 1
        elif challenge_num <= 15:
            return 2
        else:
            return 3
    
    def reset_progress(self):
        """진행상황을 리셋합니다."""
        if click.confirm("정말로 모든 진행상황을 리셋하시겠습니까?"):
            self.progress_tracker.reset_progress()
            console.print("[green]✅ 진행상황이 리셋되었습니다.[/green]")
        else:
            console.print("[yellow]취소되었습니다.[/yellow]")
    
    def export_progress(self, filename: str):
        """진행상황을 파일로 내보냅니다."""
        try:
            self.progress_tracker.export_progress(filename)
            console.print(f"[green]✅ 진행상황이 {filename}에 저장되었습니다.[/green]")
        except Exception as e:
            console.print(f"[red]❌ 저장 중 오류 발생: {str(e)}[/red]")
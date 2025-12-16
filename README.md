# 🐍 Python Learning Tracker

Python 학습을 위한 인터랙티브 챌린지 도구입니다. 21개의 챌린지를 통해 Python 기초부터 웹 개발까지 단계별로 학습할 수 있습니다.

## ✨ 주요 기능

- 📚 **21개의 구조화된 챌린지**: 기초부터 웹 개발까지
- 🔍 **자동 코드 검증**: pytest 기반 테스트 시스템
- 📊 **진행상황 추적**: JSON 기반 진행률 관리
- 💡 **힌트 시스템**: 막힐 때 도움말 제공
- 📝 **정답 제공**: 완전한 솔루션 코드 확인
- 🎨 **Rich CLI**: 아름다운 명령줄 인터페이스
- 🌐 **FastAPI 학습**: 실제 웹 API 개발 경험

## 🏗️ 프로젝트 구조

```
python-learning-tracker/
├── challenges/              # 챌린지 파일들
│   ├── week1/              # Week 1: Python 기초 (10개)
│   │   ├── challenge_01_variables.py
│   │   ├── challenge_02_functions.py
│   │   ├── ...
│   │   └── challenge_10_exceptions.py
│   ├── week2/              # Week 2: Python 고급 (5개)
│   │   ├── challenge_11_comprehension.py
│   │   ├── challenge_12_lambda.py
│   │   ├── ...
│   │   └── challenge_15_type_hints.py
│   └── week3/              # Week 3: FastAPI & 웹 개발 (6개)
│       ├── challenge_16_fastapi_basics.py
│       ├── challenge_17_request_response.py
│       ├── ...
│       └── challenge_21_final_project.py
├── solutions/              # 정답 파일들
│   ├── week1/
│   ├── week2/
│   └── week3/
├── tests/                  # 테스트 파일들
│   ├── test_week1.py
│   ├── test_week2.py
│   └── test_week3.py
├── tracker/                # 핵심 모듈
│   ├── progress.py         # 진행상황 관리
│   ├── validator.py        # 코드 검증
│   └── cli.py             # CLI 인터페이스
├── week3_api_server/       # FastAPI 서버 환경
│   ├── docker-compose.yml  # PostgreSQL 설정
│   ├── database.py         # DB 연결 설정
│   └── models.py          # 데이터베이스 모델
├── data/                   # 데이터 저장
│   └── progress.json       # 진행상황 데이터
├── main.py                 # CLI 엔트리포인트
├── requirements.txt        # 의존성
└── README.md              # 이 파일
```

## 🚀 시작하기

### 1. 요구사항

- Python 3.7+
- pip

### 2. 설치

```bash
# 저장소 클론 또는 다운로드
cd python-learning-tracker

# 의존성 설치
pip install -r requirements.txt
```

### 3. 기본 사용법

```bash
# 도움말 확인
python main.py --help

# 모든 챌린지 목록 보기
python main.py list

# 특정 주차만 보기
python main.py list --week 1
python main.py list --week 3

# 첫 번째 챌린지 테스트
python main.py check 01

# FastAPI 챌린지 테스트
python main.py check 16

# 전체 챌린지 테스트
python main.py check all

# Week 3만 테스트
python main.py check all --week 3

# 진행상황 확인
python main.py progress

# 힌트 보기
python main.py hint 01
python main.py hint 20

# 정답 보기
python main.py solution 01
python main.py solution 21

# 데모 실행
python main.py demo
```

## 📚 챌린지 목록

### Week 1: Python 기초 (10개)

1. **variables**: 변수와 타입
2. **functions**: 함수 정의와 호출
3. **conditions**: 조건문 (if, elif, else)
4. **loops**: 반복문 (for, while)
5. **lists**: 리스트 조작
6. **dicts**: 딕셔너리 활용
7. **classes**: 클래스와 객체
8. **modules**: 모듈과 패키지
9. **files**: 파일 입출력
10. **exceptions**: 예외 처리

### Week 2: Python 고급 (5개)

11. **comprehension**: 리스트 컴프리헨션
12. **lambda**: 람다 함수와 함수형 프로그래밍
13. **decorators**: 데코레이터
14. **context_manager**: 컨텍스트 매니저
15. **type_hints**: 타입 힌트

### Week 3: FastAPI & 웹 개발 (6개)

16. **fastapi_basics**: FastAPI 기초와 라우팅
17. **request_response**: 요청/응답 처리와 HTTP 메서드
18. **path_query_params**: Path & Query Parameters
19. **request_body**: Request Body & Pydantic Models
20. **authentication**: JWT 인증과 보안
21. **final_project**: 최종 프로젝트 (블로그 API)

## 🎯 학습 방법

1. **챌린지 파일 열기**: `challenges/week1/challenge_01_variables.py` 등
2. **TODO 주석 확인**: 구현해야 할 함수들 파악
3. **힌트 참고**: `python main.py hint 01`
4. **코드 작성**: pass를 실제 코드로 교체
5. **테스트 실행**: `python main.py check 01`
6. **결과 확인**: 점수와 피드백 검토
7. **정답 비교**: 필요시 `python main.py solution 01`

## 🔍 코드 검증 시스템

- **자동 채점**: 각 함수의 정확성을 자동으로 검증
- **점수 시스템**: 100점 만점으로 점수 부여
- **상세 피드백**: 실패한 테스트의 구체적인 오류 메시지
- **진행률 추적**: 완료한 챌린지와 점수를 자동 저장

## 📊 진행상황 추적

```bash
# 전체 진행상황 보기
python main.py progress

# 진행상황 초기화
python main.py reset

# 진행상황 백업
python main.py export my_progress.json
```

진행상황은 `data/progress.json`에 저장됩니다:
- 완료한 챌린지 목록
- 각 챌린지의 점수
- 완료 시간
- 전체 통계

## 🧪 테스트 실행

```bash
# pytest로 전체 테스트 실행
python main.py test

# 또는 직접 pytest 실행
pytest tests/ -v
```

## 💡 팁과 권장사항

1. **순서대로 진행**: Week 1부터 차례로 완료
2. **힌트 활용**: 막힐 때는 힌트를 먼저 확인
3. **정답 비교**: 구현 후 정답과 비교하여 다른 접근 방법 학습
4. **반복 학습**: 낮은 점수를 받은 챌린지는 다시 도전
5. **문서 참고**: Python 공식 문서와 함께 학습

## 🔧 고급 사용법

### 특정 주차만 테스트

```bash
# Week 1만 테스트
python main.py check all --week 1

# Week 2만 테스트
python main.py check all --week 2

# Week 3만 테스트 (FastAPI)
python main.py check all --week 3
```

### FastAPI 서버 실행

Week 3 챌린지 작업 시:

```bash
# PostgreSQL 시작 (Docker 필요)
cd week3_api_server
docker-compose up -d

# FastAPI 서버 실행 
uvicorn challenges.week3.challenge_16_fastapi_basics:app --reload --port 8000

# API 문서 확인
# 브라우저에서 http://localhost:8000/docs 접속
```

### 커스텀 테스트

`tests/` 디렉토리에서 추가 테스트를 작성할 수 있습니다.

### 진행상황 분석

`data/progress.json` 파일을 직접 분석하여 학습 패턴을 파악할 수 있습니다.

## 📈 점수 시스템

- **100점**: 모든 테스트 통과
- **70점 이상**: 챌린지 완료로 인정
- **50-69점**: 부분적 구현
- **0-49점**: 미완성 또는 오류

## 🤝 기여하기

이 프로젝트에 기여하고 싶으시다면:

1. 새로운 챌린지 추가
2. 테스트 케이스 개선
3. 버그 수정
4. 문서 개선

## 📝 라이센스

이 프로젝트는 교육 목적으로 제작되었습니다.

## 🎉 즐거운 Python 학습 되세요!

질문이나 제안사항이 있으시면 언제든지 연락주세요. 화이팅! 🚀
# TDD 실전 예제

이 디렉토리에는 TDD(Test-Driven Development) 방식으로 개발한 예제 코드가 포함되어 있습니다.

## 파일 구조

```
tdd_example/
├── calculator.py          # 계산기 구현 (Step 2: Green)
├── test_calculator.py     # 계산기 테스트 (Step 1: Red)
├── fastapi_tdd_app.py     # FastAPI 앱 구현
├── test_fastapi_tdd.py    # FastAPI 테스트
└── README.md             # 이 파일
```

## 실행 방법

### 1. 계산기 테스트 실행

```bash
# 프로젝트 루트에서
cd examples/tdd_example
pytest test_calculator.py -v
```

### 2. FastAPI 테스트 실행

```bash
pytest test_fastapi_tdd.py -v
```

### 3. FastAPI 서버 실행

```bash
python fastapi_tdd_app.py
# 또는
uvicorn fastapi_tdd_app:app --reload
```

## TDD 워크플로우

### Step 1: Red (테스트 작성)
1. `test_calculator.py` 작성
2. 테스트 실행 → 실패 확인

### Step 2: Green (구현)
1. `calculator.py` 작성
2. 테스트 실행 → 통과 확인

### Step 3: Refactor (개선)
1. 코드 리팩토링
2. 테스트 실행 → 통과 확인

## 학습 포인트

- ✅ 테스트를 먼저 작성하는 습관
- ✅ pytest의 기본 사용법
- ✅ Fixture와 Parametrize 활용
- ✅ FastAPI 테스트 방법
- ✅ TDD 사이클 이해

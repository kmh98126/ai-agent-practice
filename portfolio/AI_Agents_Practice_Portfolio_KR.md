# AI Agents Practice Projects 포트폴리오 (KR)

작성일: 2026-02-23  
저장소 기준 경로: `/workspace`

---

## 1) 프로젝트 한눈에 보기

**AI Agents Practice Projects**는 AI 에이전트 설계/구현 역량을 실전 형태로 훈련하기 위한 **18개의 독립 프로젝트 모음**입니다.  
한 가지 프레임워크만 다루는 튜토리얼이 아니라, 실제 서비스 개발에서 자주 마주치는 문제를 다양한 스택으로 풀어보도록 구성되어 있습니다.

- 멀티 에이전트 아키텍처 설계
- 상태(State) 기반 워크플로우 구현
- 도구(Tool) 통합 및 자동 실행 루프
- Human-in-the-loop 상호작용
- Guardrail(입력/출력 안전장치) 적용
- API/웹앱/음성 인터페이스까지 포함한 실행 환경

> 근거: `README.md` (Overview, Learning Objectives, Projects 섹션)

---

## 2) 문제 정의와 프로젝트 목표

### 문제 정의
AI 에이전트 학습 자료는 보통 한 가지 프레임워크 중심으로 편중되어 있고, 실제 운영 관점(라우팅, 테스트, 배포, 안전성)을 한 번에 연습하기 어렵습니다.

### 목표
이 저장소는 아래 학습 갭을 메우는 것을 목표로 합니다.

1. **프레임워크 비교 학습**: LangGraph / CrewAI / Google ADK / OpenAI Agents SDK / AutoGen
2. **아키텍처 패턴 체득**: Supervisor, Handoff, Parallel, Stateful routing
3. **실서비스형 산출물 구현**: Streamlit 앱, FastAPI API, 음성 파이프라인
4. **품질 관리 내재화**: 테스트, 점수 기반 재작성 루프, 가드레일

---

## 3) 저장소 구조와 설계 철학

### 구조적 특징
- 각 디렉터리는 독립 실행 가능한 프로젝트 단위
- 공통 규칙: `uv` 기반 의존성 관리, `.env` 기반 시크릿 분리
- 특정 프레임워크 개념을 명확히 보여주기 위한 “작게 쪼갠 예제” + “실전형 응용 예제” 동시 제공

### 루트 프로젝트 구성 (18개)
1. `hello-langgraph`
2. `tutor-agent`
3. `multi-agent-architectures`
4. `youtube-thumbnail-maker`
5. `workflow-architectures`
6. `email-refiner-agent`
7. `workflow-testing`
8. `content-pipeline-agent`
9. `job-hunter-agent`
10. `news-reader-agent`
11. `a2a`
12. `financial-analyst`
13. `youtube-shorts-maker`
14. `chatgpt-clone`
15. `customer-support-agent`
16. `deployment`
17. `deep-research-clone`
18. `my-first-agent`

> 근거: `README.md` (Projects, Project Structure)

---

## 4) 기술 스택 상세

### 공통 기반
- Language: **Python**
- Package Manager: **uv**
- Environment: `.env` (API 키 분리)

### 프레임워크별 핵심 역량

#### A. LangGraph 계열
- StateGraph 중심의 상태 기반 플로우 설계
- Conditional routing / parallel send / checkpoint persistence
- 대표 프로젝트: `hello-langgraph`, `tutor-agent`, `youtube-thumbnail-maker`, `workflow-testing`

#### B. CrewAI 계열
- 역할 기반 에이전트 + 태스크 체인
- YAML 설정(agents/tasks) 분리로 유지보수성 확보
- 점수 기반 품질 게이팅(재작성 루프)
- 대표 프로젝트: `content-pipeline-agent`, `job-hunter-agent`, `news-reader-agent`

#### C. Google ADK 계열
- Sub-agent tool composition
- ParallelAgent 기반 병렬 처리
- Structured output과 아티팩트 생성
- 대표 프로젝트: `youtube-shorts-maker`, `financial-analyst`, `a2a`

#### D. OpenAI Agents SDK 계열
- Handoff, Guardrails, Session 관리
- Streamlit UI + 실시간 응답 처리
- 음성 파이프라인 포함
- 대표 프로젝트: `chatgpt-clone`, `customer-support-agent`, `deployment`

#### E. AutoGen 계열
- 팀 기반 리서치 협업 패턴
- 계획/조사/종료 조건이 있는 멀티 에이전트 리서치 루프
- 대표 프로젝트: `deep-research-clone`

---

## 5) 핵심 구현 패턴 (디테일)

### 5-1. Human-in-the-loop 개선 루프
- 사용자 피드백을 단순 입력값이 아니라 **워크플로우 제어 신호**로 활용
- 예: 시 생성 결과를 피드백 받고 개선안 재생성
- 가치: 생성형 결과물의 품질 튜닝에 실무적으로 유용

관련 프로젝트:
- `hello-langgraph`
- `youtube-thumbnail-maker`

### 5-2. 라우터 기반 멀티 에이전트
- 분류 노드가 사용자 상태를 판단하고 전문 에이전트에 위임
- 예: 교육 수준 분류 → teacher/feynman/quiz 분기
- 가치: 복잡한 도메인에서 응답 품질과 책임 분리를 동시에 달성

관련 프로젝트:
- `tutor-agent`
- `multi-agent-architectures`
- `customer-support-agent`

### 5-3. 병렬 처리 + 집계 패턴
- 여러 후보 산출물을 동시에 생성하고, 집계/선별 단계로 연결
- 예: 썸네일 다중 후보 생성, 문서 청크 병렬 요약
- 가치: 처리 시간 단축 + 다양성 확보

관련 프로젝트:
- `youtube-thumbnail-maker`
- `workflow-architectures`
- `youtube-shorts-maker`

### 5-4. 품질 게이팅 자동 재시도
- 스코어 기준 미달 시 자동 재작성 루프
- 품질을 운영 규칙으로 강제
- 가치: “한 번 생성 후 끝”이 아닌 지속 개선형 생성 파이프라인

관련 프로젝트:
- `content-pipeline-agent`

### 5-5. 가드레일/안전성 내장
- 입력/출력에 필터를 적용해 위험 응답을 차단
- 가치: 실제 서비스 적용 시 필수인 안전성 기준 확보

관련 프로젝트:
- `customer-support-agent`

---

## 6) 대표 프로젝트 10선 요약

| 프로젝트 | 해결하려는 문제 | 핵심 흐름 | 기술 포인트 |
|---|---|---|---|
| hello-langgraph | LangGraph 입문 | 대화 + 피드백 루프 | interrupt, checkpoint |
| tutor-agent | 맞춤형 학습 지원 | 분류 → 전문가 에이전트 라우팅 | conditional edges |
| multi-agent-architectures | 다국어 고객 지원 | supervisor가 언어별 에이전트에 위임 | AgentTool 패턴 |
| youtube-thumbnail-maker | 영상 기반 썸네일 자동화 | 추출/요약 → 병렬 후보 생성 → 피드백 선택 | Send 패턴, 외부툴 연계 |
| workflow-testing | 에이전트 품질 검증 | E2E + 노드 단위 + 평가 기반 테스트 | 테스트 전략 표준화 |
| content-pipeline-agent | 마케팅 콘텐츠 자동 제작 | 조사 → 생성 → 점수평가 → 재작성 | CrewAI Flow, scoring gate |
| job-hunter-agent | 구직 지원 자동화 | 매칭/선택/이력서/기업조사/면접준비 | YAML config, 다단계 체인 |
| customer-support-agent | 음성 고객 지원 | triage → 전문 에이전트 handoff | VoicePipeline, guardrails |
| chatgpt-clone | 범용 AI 어시스턴트 UI | 멀티도구 + 스트리밍 응답 | Streamlit, MCP 통합 |
| deployment | 운영 가능한 API 제공 | 대화 생성/메시지/스트리밍 API | FastAPI, SSE, 배포 설정 |

---

## 7) 아키텍처 관점의 데이터 흐름

### A. 상태 기반 라우팅형 (예: tutor-agent)
1. 사용자 메시지 입력
2. 분류 에이전트가 학습자 레벨 판정
3. 적절한 전문 에이전트로 분기
4. 결과를 상태에 축적하고 최종 응답 반환

핵심 포인트:
- 분류 결과가 단순 라벨이 아니라 **다음 노드를 결정하는 라우팅 키** 역할

### B. 품질 평가 루프형 (예: content-pipeline-agent)
1. 리서치 데이터 수집
2. 콘텐츠 초안 생성
3. SEO/바이럴 점수 평가
4. 점수 기준 미달 시 재작성
5. 통과 시 최종 산출물 확정

핵심 포인트:
- 자동 재시도 조건을 파이프라인 규칙으로 내장

### C. 음성 인터페이스형 (예: customer-support-agent)
1. 음성 입력 수집
2. 텍스트 변환 및 의도 분석
3. triage 에이전트가 전문 영역 판단
4. 담당 에이전트가 해결 응답 생성
5. 출력 가드레일 검증 후 음성 응답

핵심 포인트:
- 사용자 경험(voice) + 안정성(guardrail) + 확장성(handoff) 동시 확보

---

## 8) 실행, 테스트, 배포 관점의 완성도

### 실행
- 각 프로젝트 디렉터리에서 `uv sync` 후 실행
- Streamlit 앱: `uv run streamlit run main.py`
- Python 앱: `uv run python main.py`

### 테스트
- `workflow-testing`에서 E2E, 노드 단위, 평가 기반 테스트 패턴 제공
- “워크플로우도 테스트 대상”이라는 관점을 명확히 제시

### 배포
- `deployment` 프로젝트에서 FastAPI + SSE 제공
- `railway.json`으로 클라우드 배포 시작점 제공

---

## 9) 프로젝트 강점 (포트폴리오 강조 포인트)

1. **프레임워크 다변화 역량**
   - 단일 툴 종속이 아니라 상황별 프레임워크 선택 능력 입증

2. **아키텍처 패턴 이해도**
   - Supervisor, Handoff, Parallel, Routing, Human-in-the-loop를 코드로 구현

3. **실서비스형 인터페이스 경험**
   - Streamlit 웹앱, VoicePipeline, FastAPI API 제공

4. **품질/안전성 내재화**
   - 점수 기반 재작성, Guardrail, 테스트 전략 확보

5. **확장 가능한 구조**
   - 프로젝트 분리 구조 + YAML 기반 설정 관리로 유지보수 용이

---

## 10) 개선 로드맵 (향후 확장 제안)

1. **공통 관찰성(Observability) 계층 추가**
   - 공통 로깅 스키마, trace ID, latency 메트릭 통합

2. **통합 벤치마크 대시보드**
   - 프로젝트별 응답 품질/비용/지연시간 비교 자동화

3. **CI 파이프라인 강화**
   - PR 단위 에이전트 회귀 테스트 및 품질 게이트

4. **공통 도구 인터페이스 표준화**
   - 프로젝트 간 Tool 스펙 통합으로 재사용성 향상

5. **배포 템플릿 다변화**
   - Railway 외 Docker/Kubernetes 예시 확장

---

## 11) 면접/발표용 한 줄 요약

“이 저장소는 18개 독립 실습을 통해 AI 에이전트의 핵심 패턴(라우팅, 병렬화, 상태관리, 안전성, 배포)을 프레임워크별로 비교 구현한 실전형 포트폴리오입니다.”

---

## 12) 참고한 주요 파일

- `README.md`
- `hello-langgraph/README.md`
- `tutor-agent/README.md`
- `multi-agent-architectures/README.md`
- `youtube-thumbnail-maker/README.md`
- `content-pipeline-agent/README.md`
- `job-hunter-agent/README.md`
- `customer-support-agent/README.md`
- `workflow-testing/README.md`
- `deployment/README.md`
- `a2a/README.md`
- 각 프로젝트 `pyproject.toml`


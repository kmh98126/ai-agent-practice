# AI Agents Practice Projects - Portfolio

---

## 프로젝트 개요

**프로젝트명:** AI Agents Practice Projects  
**개발 기간:** 2025  
**개발 인원:** 1인 (개인 프로젝트)  
**저장소:** GitHub  

> 다양한 AI Agent 프레임워크와 아키텍처 패턴을 실습하며, 총 18개의 독립적인 AI Agent 프로젝트를 설계하고 구현한 종합 실습 저장소입니다. LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, AutoGen 등 주요 프레임워크를 활용하여 멀티 에이전트 시스템, 워크플로우 자동화, 음성 기반 AI, 콘텐츠 생성 파이프라인 등 실무에 가까운 AI Agent 시스템을 구축했습니다.

---

## 기술 스택

### 언어 및 런타임

| 항목 | 기술 |
|------|------|
| **주 언어** | Python 3.13+ |
| **패키지 매니저** | uv (Modern Python Package Manager) |
| **의존성 관리** | pyproject.toml |

### AI Agent 프레임워크

| 프레임워크 | 용도 | 사용 프로젝트 수 |
|------------|------|:-----------------:|
| **LangGraph** | 상태 기반 워크플로우, 그래프 오케스트레이션 | 7개 |
| **CrewAI** | 역할 기반 멀티 에이전트 시스템 | 3개 |
| **Google ADK** | 서브 에이전트, 병렬 실행 | 3개 |
| **OpenAI Agents SDK** | 핸드오프, 가드레일, 음성 처리 | 3개 |
| **AutoGen** | 멀티 에이전트 연구 시스템 | 1개 |

### 웹 프레임워크 및 UI

| 기술 | 용도 |
|------|------|
| **Streamlit** | 대화형 웹 인터페이스 (ChatGPT Clone, Customer Support) |
| **FastAPI** | RESTful API 서버, SSE 스트리밍 |

### 데이터베이스 및 저장소

| 기술 | 용도 |
|------|------|
| **SQLite** | 세션 관리, 체크포인트, 대화 기록 저장 |
| **OpenAI Vector Store** | 파일 검색용 벡터 저장소 |

### 외부 API 및 서비스

| 서비스 | 용도 |
|--------|------|
| **OpenAI API** | GPT 모델, Whisper(음성), DALL-E(이미지) |
| **Firecrawl API** | 웹 스크래핑 및 검색 |
| **Google Cloud Platform** | ADK 프로젝트 인프라 |
| **yfinance** | 주식 시장 데이터 조회 |
| **MCP Servers** | Model Context Protocol (Yahoo Finance, Time, Context7) |

### 배포

| 기술 | 용도 |
|------|------|
| **Railway** | 클라우드 배포 (NIXPACKS 빌더) |
| **uvicorn** | ASGI 서버 |

### 테스트

| 기술 | 용도 |
|------|------|
| **pytest** | 유닛 테스트, 통합 테스트 |
| **LLM 기반 평가** | AI 응답 품질 자동 평가 |

### 핵심 라이브러리

| 라이브러리 | 용도 |
|-----------|------|
| **Pydantic** | 데이터 검증 및 구조화된 출력 |
| **LangChain** | LLM 체인 및 도구 통합 |
| **python-dotenv** | 환경 변수 관리 |
| **sounddevice** | 음성 입출력 처리 |
| **numpy** | 수치 연산 |

---

## 프로젝트 아키텍처 및 설계 패턴

### 적용한 아키텍처 패턴 요약

| 패턴 | 설명 | 적용 프로젝트 |
|------|------|--------------|
| **StateGraph** | 상태 기반 워크플로우 관리, 조건부 라우팅 | LangGraph 전체 |
| **Supervisor** | 중앙 관리자가 전문 에이전트에게 작업 라우팅 | multi-agent-architectures |
| **Send (병렬 처리)** | 동적 디스패치로 병렬 실행 후 결과 집계 | workflow-architectures, youtube-thumbnail-maker |
| **Human-in-the-Loop** | interrupt()로 사용자 피드백 요청 및 반복 개선 | hello-langgraph, youtube-thumbnail-maker |
| **Agent Chain** | 순차적 에이전트 실행 및 출력 전달 | job-hunter-agent, content-pipeline-agent |
| **ParallelAgent** | 서브 에이전트 동시 실행 | youtube-shorts-maker, financial-analyst |
| **Flow (CrewAI)** | @start, @listen, @router 데코레이터 기반 흐름 제어 | content-pipeline-agent |
| **Handoff** | 에이전트 간 컨텍스트 유지 전환 | customer-support-agent |
| **Guardrails** | 입출력 필터링으로 안전성 보장 | customer-support-agent |
| **A2A Protocol** | JSON-RPC 기반 에이전트 간 통신 | a2a |

### 상태 관리 전략

- **MessagesState**: 대화 기록 추적
- **TypedDict**: 타입 안전한 상태 구조 정의
- **Annotated List**: 병렬 처리 결과 자동 병합
- **SQLite Checkpoint**: 워크플로우 상태 영속화 및 복원

---

## 프로젝트 상세 설명

---

### 1. Hello LangGraph

> LangGraph의 기본 개념을 학습하기 위한 입문 프로젝트

**프레임워크:** LangGraph  
**핵심 기능:**
- 간단한 대화형 에이전트 구현
- 시(Poetry) 생성 후 사용자 피드백을 받아 수정하는 Human-in-the-Loop 패턴
- SQLite 기반 대화 상태 영속화 (메모리 체크포인트)

**기술적 포인트:**
- `interrupt()` 함수를 활용한 사용자 개입 패턴
- `SqliteSaver`를 통한 상태 저장/복원
- LangGraph의 StateGraph 기본 구조 이해

**배운 점:**
- LangGraph의 노드-엣지 기반 그래프 구조
- 상태 기반 워크플로우의 기본 원리
- 체크포인트를 활용한 상태 영속화

---

### 2. Tutor Agent (교육 튜터 에이전트)

> 학습자의 수준에 맞는 개인화된 교육을 제공하는 4-에이전트 시스템

**프레임워크:** LangGraph  
**핵심 기능:**
- **Classification Agent**: 학습자 질문 분석 및 수준 분류
- **Teacher Agent**: 단계별 개념 설명 및 교육
- **Feynman Agent**: 파인만 기법으로 복잡한 개념을 쉽게 설명
- **Quiz Agent**: 퀴즈 생성 및 평가 피드백 제공
- 웹 검색 도구 통합으로 최신 정보 제공

**아키텍처:**

```
사용자 질문 → Classification Agent → 수준 판별
                                        ├→ Teacher Agent (기본 설명)
                                        ├→ Feynman Agent (쉬운 설명)
                                        └→ Quiz Agent (퀴즈 평가)
```

**기술적 포인트:**
- 조건부 라우팅(Conditional Edge)으로 학습자 수준에 따른 에이전트 자동 선택
- 도구(Tools) 통합을 통한 웹 검색 기능
- 구조화된 상태 관리로 대화 컨텍스트 유지

---

### 3. Multi-Agent Architectures (다중 에이전트 아키텍처)

> Supervisor 패턴을 활용한 다국어 고객 지원 시스템

**프레임워크:** LangGraph  
**핵심 기능:**
- 중앙 Supervisor가 사용자 언어를 판별하여 적절한 에이전트로 라우팅
- 한국어/스페인어/그리스어 전용 에이전트
- AgentTool 패턴으로 에이전트를 도구로 활용

**아키텍처:**

```
사용자 입력 → Supervisor Agent
               ├→ Korean Agent (한국어 응답)
               ├→ Spanish Agent (스페인어 응답)
               └→ Greek Agent (그리스어 응답)
```

**기술적 포인트:**
- Supervisor 패턴: 중앙 관리자가 작업을 분배하는 멀티 에이전트 구조
- AgentTool: 에이전트 자체를 도구로 래핑하여 유연한 조합 가능
- 언어별 전문 에이전트 분리로 각 도메인의 품질 향상

---

### 4. YouTube Thumbnail Maker (유튜브 썸네일 생성기)

> 동영상에서 자동으로 썸네일 후보를 생성하고 사용자가 선택하는 워크플로우

**프레임워크:** LangGraph  
**핵심 기능:**
- 동영상 → 오디오 추출 → 음성 인식 → 요약 → 썸네일 생성의 전체 파이프라인
- Send 패턴으로 복수의 썸네일 후보를 병렬 생성
- 사용자 피드백 기반 최종 선택 (Human-in-the-Loop)

**아키텍처:**

```
Video Input → ffmpeg(Audio) → Whisper(Transcription) → GPT(Summary)
                                                          ↓
                                                   [Send Pattern]
                                              ├→ DALL-E (Thumbnail 1)
                                              ├→ DALL-E (Thumbnail 2)
                                              └→ DALL-E (Thumbnail 3)
                                                          ↓
                                              User Selection (interrupt)
```

**기술적 포인트:**
- LangGraph의 Send 패턴을 활용한 동적 병렬 처리
- ffmpeg, Whisper, DALL-E 등 다양한 외부 도구 통합
- 멀티미디어 처리 파이프라인 설계

---

### 5. Workflow Architectures (워크플로우 아키텍처)

> 문서 분할 및 병렬 요약을 통한 대용량 문서 처리 최적화

**프레임워크:** LangGraph  
**핵심 기능:**
- 대용량 문서를 청크로 분할
- 각 청크를 병렬로 요약 (Send 패턴)
- 요약 결과를 집계하여 최종 종합 요약 생성

**기술적 포인트:**
- Map-Reduce 패턴의 AI 에이전트 버전
- 동적 워커 생성을 통한 확장 가능한 병렬 처리
- Annotated List를 활용한 결과 자동 병합

---

### 6. Email Refiner Agent (이메일 처리 에이전트)

> 이메일을 자동으로 분류하고 우선순위를 매기며 응답을 생성하는 시스템

**프레임워크:** LangGraph  
**핵심 기능:**
- 이메일 분류: 스팸 / 일반 / 긴급
- 우선순위 점수 매기기 (1~10)
- 자동 응답 초안 작성
- 부가 기능: 여행 어드바이저 에이전트 (날씨, 환율, 관광지 정보)

**아키텍처:**

```
이메일 입력 → Classification (스팸/일반/긴급)
               → Priority Scoring (1~10)
               → Response Drafting (자동 응답 생성)
```

**기술적 포인트:**
- Pydantic 모델을 활용한 구조화된 출력
- 순차적 워크플로우 설계
- 세션 기반 상태 영속화

---

### 7. Workflow Testing (워크플로우 테스트)

> LangGraph 워크플로우에 대한 체계적인 테스트 전략 실습

**프레임워크:** LangGraph + pytest  
**핵심 기능:**
- End-to-End 그래프 테스트
- 개별 노드 단위 테스트
- LLM 기반 응답 품질 자동 평가
- 부분 실행 테스트 (특정 지점부터 실행)

**테스트 코드 예시:**

```python
@pytest.mark.parametrize(
    "email, expected_category, min_score, max_score",
    [
        ("this is urgent!", "urgent", 8, 10),
        ("i wanna talk to you", "normal", 4, 7),
        ("i have an offer for you", "spam", 1, 3),
    ],
)
def test_full_graph(email, expected_category, min_score, max_score):
    result = graph.invoke({"email": email})
    assert result["category"] == expected_category
    assert min_score <= result["priority_score"] <= max_score
```

**기술적 포인트:**
- AI 시스템의 테스트 전략 수립
- 매개변수화된 테스트로 다양한 시나리오 검증
- LLM 출력의 품질을 LLM으로 평가하는 메타 평가 패턴

---

### 8. Content Pipeline Agent (콘텐츠 생성 파이프라인)

> SEO 및 바이럴 점수를 기반으로 콘텐츠를 자동 생성하고 최적화하는 시스템

**프레임워크:** CrewAI Flow  
**핵심 기능:**
- 리서치 → 콘텐츠 생성 → 점수 평가 → 리라이팅의 반복 루프
- 블로그, 트윗, LinkedIn 포스트 자동 생성
- SEO 점수 및 바이럴 점수 평가
- 점수 7 미만 시 자동 리라이팅 트리거

**아키텍처:**

```
Research → Content Generation → Score Evaluation
                                    ↓
                              score >= 7 → 완료
                              score < 7  → Rewrite → 재평가 (루프)
```

**기술적 포인트:**
- CrewAI Flow의 `@start`, `@listen`, `@router` 데코레이터 활용
- 품질 기반 조건부 루프 설계
- 두 개의 독립 Crew (SEO Crew + Virality Crew) 조합

---

### 9. Job Hunter Agent (취업 지원 에이전트)

> 이력서 기반 맞춤형 채용 검색 및 면접 준비를 자동화하는 5-에이전트 체인

**프레임워크:** CrewAI  
**핵심 기능:**
- **검색 에이전트**: 채용 공고 수집
- **매칭 에이전트**: 이력서와 공고 매칭 (1~5 점수)
- **선택 에이전트**: 최적 공고 선정
- **이력서 최적화 에이전트**: 선정된 공고에 맞게 이력서 최적화
- **기업 분석 에이전트**: 기업 정보 조사 및 면접 준비

**아키텍처:**

```
Job Search → Resume Matching (1~5점) → Job Selection
→ Resume Optimization → Company Research → Interview Prep
```

**기술적 포인트:**
- YAML 설정 파일로 에이전트/태스크 관리 (`agents.yaml`, `tasks.yaml`)
- Knowledge Source를 통한 이력서 정보 활용
- 5단계 순차 에이전트 체인의 데이터 흐름 설계

---

### 10. News Reader Agent (뉴스 리더 에이전트)

> 뉴스를 자동 수집하고 다단계 요약을 생성하는 큐레이션 시스템

**프레임워크:** CrewAI  
**핵심 기능:**
- 3단계 프로세스: 수집 → 요약 → 큐레이션
- 웹 검색/스크래핑으로 뉴스 수집
- 다단계 요약: 트윗 / 이그제큐티브 요약 / 상세 요약
- 신뢰도 및 관련성 점수 필터링

**기술적 포인트:**
- 웹 스크래핑 도구(Firecrawl) 통합
- 다단계 요약 전략 설계
- 점수 기반 콘텐츠 필터링

---

### 11. A2A - Agent-to-Agent Communication (에이전트 간 통신)

> 서로 다른 프레임워크의 에이전트가 통신하는 A2A 프로토콜 구현

**프레임워크:** Google ADK + LangGraph + FastAPI  
**핵심 기능:**
- LangGraph 에이전트와 Google ADK 에이전트 간 통신
- Agent Card JSON을 통한 에이전트 디스커버리
- JSON-RPC 프로토콜 기반 메시지 교환
- 원격 에이전트를 서브 에이전트로 활용

**아키텍처:**

```
User-Facing Agent
  ├→ Local LangGraph Agent
  └→ Remote ADK Agent (FastAPI Server)
       └→ Agent Card (.well-known/agent-card.json)
       └→ JSON-RPC Message Handler
```

**기술적 포인트:**
- A2A(Agent-to-Agent) 프로토콜 표준 구현
- 이기종 프레임워크 간 상호 운용성
- FastAPI 기반 에이전트 서버 설계

---

### 12. Financial Analyst (금융 분석 시스템)

> 주식 데이터, 재무제표, 뉴스를 병렬 분석하여 투자 리포트를 생성하는 시스템

**프레임워크:** Google ADK  
**핵심 기능:**
- 메인 에이전트가 3개의 서브 에이전트를 병렬 실행
  - **Data Agent**: yfinance를 통한 주식 데이터 조회
  - **Financial Agent**: 재무 분석
  - **News Agent**: 관련 뉴스 수집 및 분석
- 종합 투자 어드바이스 리포트 자동 생성

**아키텍처:**

```
Main Agent (Financial Advisor)
  ├→ Data Sub-Agent (yfinance)     ─┐
  ├→ Financial Sub-Agent            ├→ 종합 리포트 생성
  └→ News Sub-Agent (Web Search)   ─┘
         [ParallelAgent - 병렬 실행]
```

**기술적 포인트:**
- Google ADK의 ParallelAgent를 활용한 병렬 서브 에이전트 실행
- 실시간 주식 데이터 API(yfinance) 통합
- 구조화된 투자 리포트 출력

---

### 13. YouTube Shorts Maker (유튜브 쇼츠 자동 생성기)

> 주제만 입력하면 콘텐츠 기획부터 영상 조립까지 자동화하는 시스템

**프레임워크:** Google ADK  
**핵심 기능:**
- 콘텐츠 기획: 장면(Scene) 목록 자동 생성
- 에셋 생성: 이미지와 음성을 병렬로 생성
- 영상 조립: 장면별 에셋을 결합하여 최종 영상 생성
- 입력 필터링 콜백으로 부적절한 요청 차단

**아키텍처:**

```
주제 입력 → Content Planner (Scene List)
             → [ParallelAgent]
               ├→ Image Generator (각 장면 이미지)
               └→ Voice Generator (각 장면 나레이션)
             → Video Assembler (최종 영상)
```

**기술적 포인트:**
- Pydantic 구조화된 출력 (Scene 리스트)
- 콜백 기반 입력 필터링
- 멀티미디어 에셋 병렬 생성 및 조립

---

### 14. ChatGPT Clone (ChatGPT 클론)

> 다양한 도구와 MCP 서버를 통합한 다기능 대화형 AI 어시스턴트

**프레임워크:** OpenAI Agents SDK + Streamlit  
**핵심 기능:**
- **웹 검색**: 실시간 정보 검색
- **파일 검색**: Vector Store 기반 문서 검색
- **이미지 생성**: DALL-E를 통한 이미지 생성
- **코드 실행**: 코드 인터프리터
- **MCP 서버 통합**: Yahoo Finance, Time, Context7
- 스트리밍 응답 지원
- 파일 업로드 (텍스트/이미지)

**기술적 포인트:**
- Model Context Protocol (MCP) 서버 통합
- OpenAI Vector Store를 활용한 파일 검색
- Streamlit 기반 실시간 스트리밍 UI
- 다중 도구의 동적 선택 및 실행

---

### 15. Customer Support Agent (고객 지원 에이전트)

> 음성 기반 고객 지원 시스템 - 자동 분류, 라우팅, 가드레일 적용

**프레임워크:** OpenAI Agents SDK + Streamlit  
**핵심 기능:**
- **Triage Agent**: 문의 분류 및 전문 에이전트로 라우팅
- **Account Agent**: 계정 관련 문의 처리
- **Billing Agent**: 결제/청구 문의 처리
- **Order Agent**: 주문 관련 문의 처리
- **Technical Agent**: 기술 지원 문의 처리
- VoicePipeline으로 음성 입출력
- Input/Output Guardrails로 안전성 보장

**아키텍처:**

```
음성 입력 → VoicePipeline → Triage Agent
                              ├→ Account Agent  ──┐
                              ├→ Billing Agent   ──┤→ Handoff
                              ├→ Order Agent     ──┤   (컨텍스트 유지)
                              └→ Technical Agent ──┘
                                         ↓
                              Output Guardrails → 음성 출력
```

**기술적 포인트:**
- OpenAI VoicePipeline을 활용한 음성 기반 상호작용
- Handoff 메커니즘으로 에이전트 간 컨텍스트 유지 전환
- Input Guardrails: 주제 외 요청 필터링
- Output Guardrails: 응답 정확성 및 안전성 검증

---

### 16. Deployment (API 배포)

> AI 에이전트를 RESTful API로 배포하는 실전 예제

**프레임워크:** FastAPI + OpenAI Agents SDK  
**핵심 기능:**
- 대화 생성 및 관리 API
- 동기/비동기 메시지 처리
- Server-Sent Events (SSE) 스트리밍 응답
- Railway 클라우드 배포 설정

**API 엔드포인트:**

| Method | Endpoint | 설명 |
|--------|----------|------|
| `GET` | `/` | 헬스 체크 |
| `POST` | `/conversations` | 대화 생성 |
| `POST` | `/conversations/{id}/message` | 메시지 전송 (동기) |
| `POST` | `/conversations/{id}/message-stream` | 메시지 전송 (스트리밍) |
| `POST` | `/conversations/{id}/message-stream-all` | 전체 이벤트 스트리밍 |

**기술적 포인트:**
- FastAPI의 비동기 처리와 SSE 스트리밍
- OpenAI Conversations API 통합
- Railway를 통한 클라우드 배포 자동화

---

### 17. Deep Research Clone (딥 리서치 팀)

> 멀티 에이전트 팀이 협업하여 심층 리서치를 수행하고 보고서를 생성하는 시스템

**프레임워크:** AutoGen  
**핵심 기능:**
- SelectorGroupChat으로 에이전트 팀 구성
- 리서치 플래너 → 리서치 에이전트 → 종료 조건 체크
- 웹 검색 통합
- 자동 보고서 생성

**기술적 포인트:**
- AutoGen의 SelectorGroupChat 패턴
- 에이전트 간 역할 분배 및 협업
- 종료 조건 설정을 통한 자동 완료

---

### 18. My First Agent (첫 에이전트)

> OpenAI API를 직접 사용하여 기본적인 에이전트를 구현하는 입문 튜토리얼

**프레임워크:** OpenAI API (직접 사용)  
**핵심 기능:**
- Function Calling 패턴 학습
- 날씨 조회 도구 구현 예제
- 에이전트의 기본 구조 이해

**기술적 포인트:**
- OpenAI API의 Function Calling 메커니즘
- 도구 정의 및 실행 루프
- 에이전트 기본 아키텍처 학습

---

## 프로젝트 구조

```
ai-agents-practice/
│
├── README.md                          # 프로젝트 문서
├── .gitignore                         # Git 제외 파일 설정
│
├── [LangGraph 기반]
│   ├── hello-langgraph/               # LangGraph 입문
│   ├── tutor-agent/                   # 교육 튜터 에이전트
│   ├── multi-agent-architectures/     # Supervisor 패턴
│   ├── youtube-thumbnail-maker/       # 유튜브 썸네일 생성기
│   ├── workflow-architectures/        # 병렬 처리 패턴
│   ├── email-refiner-agent/           # 이메일 처리 에이전트
│   └── workflow-testing/              # 워크플로우 테스트
│
├── [CrewAI 기반]
│   ├── content-pipeline-agent/        # 콘텐츠 생성 파이프라인
│   ├── job-hunter-agent/              # 취업 지원 에이전트
│   └── news-reader-agent/             # 뉴스 리더
│
├── [Google ADK 기반]
│   ├── a2a/                           # Agent-to-Agent 통신
│   ├── financial-analyst/             # 금융 분석 시스템
│   └── youtube-shorts-maker/          # 유튜브 쇼츠 생성기
│
├── [OpenAI Agents SDK 기반]
│   ├── chatgpt-clone/                 # ChatGPT 클론
│   ├── customer-support-agent/        # 고객 지원 에이전트
│   └── deployment/                    # API 배포 예제
│
├── [AutoGen 기반]
│   └── deep-research-clone/           # 딥 리서치 팀
│
└── [기타]
    └── my-first-agent/                # 첫 에이전트 (입문)
```

---

## 학습 성과 및 역량

### AI Agent 설계 역량

- **멀티 에이전트 아키텍처 설계**: Supervisor, Chain, Parallel, Handoff 등 다양한 에이전트 조합 패턴 구현 경험
- **상태 기반 워크플로우**: StateGraph를 활용한 복잡한 비즈니스 로직의 그래프 기반 모델링
- **도구 통합 설계**: 외부 API, 데이터베이스, 멀티미디어 도구를 에이전트에 연결하는 설계 능력

### 프레임워크 활용 역량

- **LangGraph**: 상태 관리, 조건부 라우팅, 병렬 처리, Human-in-the-Loop, 체크포인트
- **CrewAI**: 역할 기반 에이전트, 태스크 체인, Flow 기반 워크플로우, YAML 설정
- **Google ADK**: 서브 에이전트, ParallelAgent, 구조화된 출력, 콜백
- **OpenAI Agents SDK**: Handoff, Guardrails, VoicePipeline, MCP 통합, 세션 관리

### 소프트웨어 엔지니어링 역량

- **테스트 전략**: pytest를 활용한 단위/통합 테스트, LLM 기반 자동 평가
- **API 설계**: RESTful API, SSE 스트리밍, 대화 관리
- **배포**: Railway 클라우드 배포, FastAPI + uvicorn 프로덕션 서버
- **데이터 모델링**: Pydantic을 활용한 타입 안전 데이터 구조 설계
- **보안**: 가드레일 패턴, 환경 변수 관리, 입출력 필터링

### 문제 해결 경험

| 도메인 | 해결한 문제 | 적용 프로젝트 |
|--------|------------|--------------|
| 교육 | 학습자 수준별 맞춤 교육 자동화 | Tutor Agent |
| 콘텐츠 | 품질 기준 미달 시 자동 리라이팅 루프 | Content Pipeline |
| 취업 | 이력서 기반 채용 매칭 및 면접 준비 자동화 | Job Hunter |
| 금융 | 주식 데이터 병렬 수집 및 투자 리포트 생성 | Financial Analyst |
| 고객 지원 | 음성 기반 자동 분류 및 전문 에이전트 라우팅 | Customer Support |
| 미디어 | 동영상 → 썸네일/쇼츠 자동 생성 파이프라인 | YouTube Thumbnail/Shorts |
| 커뮤니케이션 | 이기종 에이전트 간 A2A 프로토콜 통신 | A2A |
| 배포 | AI 에이전트의 프로덕션 API 서비스화 | Deployment |

---

## 향후 계획

- 프로덕션 레벨의 에이전트 시스템 배포 및 모니터링 구축
- RAG (Retrieval-Augmented Generation) 고도화
- 에이전트 메모리 시스템 심화 (장기/단기 기억)
- 에이전트 평가 및 벤치마킹 체계 수립
- 실제 비즈니스 도메인 적용 프로젝트 진행

---

## 연락처

- **GitHub**: [GitHub 프로필 링크]
- **Email**: [이메일 주소]
- **LinkedIn**: [LinkedIn 프로필 링크]

---

> 이 문서는 PDF 변환을 위한 Markdown 포맷으로 작성되었습니다.
> 권장 변환 도구: [Pandoc](https://pandoc.org/), [md-to-pdf](https://www.npmjs.com/package/md-to-pdf), [Typora](https://typora.io/), VS Code의 Markdown PDF 확장

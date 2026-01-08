# AI Agent 완전 학습 가이드

이 문서는 AI Agent의 기본 개념부터 Multi-Agent 시스템까지 단계별로 학습할 수 있도록 구성되었습니다. 각 개념은 실제 프로젝트 예시와 함께 설명됩니다.

---

## 📚 목차

1. [AI Agent 기본 개념](#1-ai-agent-기본-개념)
2. [Function Calling - Agent의 핵심](#2-function-calling---agent의-핵심)
3. [State Management - 상태 관리](#3-state-management---상태-관리)
4. [Single Agent 구현](#4-single-agent-구현)
5. [Multi-Agent 아키텍처](#5-multi-agent-아키텍처)
6. [프레임워크별 상세 가이드](#6-프레임워크별-상세-가이드)
7. [고급 패턴](#7-고급-패턴)

---

## 1. AI Agent 기본 개념

### 1.1 Agent란?

**Agent**는 사용자의 목표를 달성하기 위해 자율적으로 행동하는 AI 시스템입니다. 단순한 챗봇과 달리:

- **도구(Tools) 사용**: 외부 API 호출, 데이터베이스 쿼리, 계산 등
- **상태 관리**: 대화 맥락과 정보 유지
- **의사결정**: 상황에 따라 적절한 행동 선택
- **자율성**: 사용자 개입 없이 여러 단계 작업 수행

### 1.2 Agent의 기본 구조

```
사용자 입력 → LLM (의사결정) → 도구 실행 → 결과 반영 → 응답 생성
                    ↑                                    ↓
                    └─────────── 상태 업데이트 ───────────┘
```

### 1.3 프로젝트 예시: `my-first-agent`

가장 기본적인 Agent 구현 예시입니다.

**코드 구조:**
```python
# 1. 도구 정의
def get_weather(city):
    return "33 degrees celsius."

# 2. 도구를 LLM에 등록
TOOLS = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "도시의 날씨를 가져옵니다.",
        "parameters": {...}
    }
}]

# 3. Agent 루프
def call_ai():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=TOOLS,  # 도구 제공
    )
    
    # 도구 호출이 있으면 실행
    if response.tool_calls:
        # 도구 실행 → 결과를 messages에 추가 → 다시 LLM 호출
        process_ai_response(response)
```

**학습 포인트:**
- Function Calling이 어떻게 작동하는지
- 도구 실행 후 LLM에 결과를 어떻게 전달하는지
- 메시지 히스토리를 어떻게 관리하는지

---

## 2. Function Calling - Agent의 핵심

### 2.1 Function Calling이란?

LLM이 직접 함수를 호출할 수 있게 하는 메커니즘입니다. LLM이:
1. 사용자 요청 분석
2. 필요한 도구 선택
3. 도구 호출 파라미터 생성
4. 도구 실행 결과를 받아 최종 응답 생성

### 2.2 작동 방식

```
1. 사용자: "마드리드 날씨 알려줘"
2. LLM: "get_weather 도구가 필요하다" 
   → {"name": "get_weather", "arguments": {"city": "Madrid"}}
3. 시스템: get_weather("Madrid") 실행 → "25°C, 맑음"
4. LLM: "마드리드는 현재 25°C이고 맑습니다."
```

### 2.3 프로젝트 예시 비교

#### `my-first-agent` (수동 구현)
```python
# 도구 호출을 직접 처리
if message.tool_calls:
    for tool_call in message.tool_calls:
        function_to_run = FUNCTION_MAP.get(function_name)
        result = function_to_run(**arguments)
        # 결과를 messages에 추가
```

#### `hello-langgraph` (프레임워크 사용)
```python
from langgraph.prebuilt import ToolNode

# ToolNode가 자동으로 도구 실행
tool_node = ToolNode(tools=[get_human_feedback])

# 그래프에 자동 연결
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
```

**차이점:**
- 수동 구현: 더 많은 제어, 더 많은 코드
- 프레임워크: 자동화, 코드 간소화

---

## 3. State Management - 상태 관리

### 3.1 State가 필요한 이유

Agent는 여러 단계의 대화와 작업을 수행하므로, **이전 맥락을 기억**해야 합니다.

### 3.2 State의 구성 요소

1. **메시지 히스토리**: 대화 내용
2. **작업 상태**: 현재 진행 중인 작업 정보
3. **컨텍스트**: 사용자 정보, 환경 설정 등
4. **중간 결과**: 각 단계에서 생성된 데이터

### 3.3 프로젝트 예시

#### `hello-langgraph` - MessagesState
```python
class State(MessagesState):
    pass  # 기본 메시지 히스토리만 사용

# 메시지 자동 관리
def chatbot(state: State):
    response = llm.invoke(state['messages'])
    return {"messages": [response]}  # 새 메시지 추가
```

#### `tutor-agent` - 커스텀 State
```python
class TutorState(MessagesState):
    current_agent: str  # 현재 활성 에이전트 추적

# 라우팅에 사용
def router_check(state: TutorState):
    current_agent = state.get("current_agent", "classification_agent")
    return current_agent
```

#### `content-pipeline-agent` - 복잡한 State (CrewAI Flow)
```python
class ContentPipelineState(BaseModel):
    # 입력
    content_type: str
    topic: str
    
    # 내부 상태
    research: str
    score: Score | None
    
    # 생성된 콘텐츠
    blog_post: BlogPost | None
    tweet: Tweet | None
```

### 3.4 State Persistence (상태 저장)

**`hello-langgraph` - SQLite Checkpoint:**
```python
from langgraph.checkpoint.sqlite import SqliteSaver

conn = sqlite3.connect("memory.db")
memory = SqliteSaver(conn)

graph = graph_builder.compile(checkpointer=memory)
# 대화 세션 자동 저장 및 복원 가능
```

---

## 4. Single Agent 구현

### 4.1 기본 Single Agent

**예시: `hello-langgraph`**

```python
# 1. 그래프 생성
graph_builder = StateGraph(State)

# 2. 노드 추가 (LLM Agent)
graph_builder.add_node("chatbot", chatbot)

# 3. 도구 노드 추가
graph_builder.add_node("tools", tool_node)

# 4. 엣지 연결
graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", tools_condition)  # 도구 필요시 분기
graph_builder.add_edge("tools", "chatbot")  # 도구 실행 후 다시 chatbot으로
graph_builder.add_edge("chatbot", END)

# 5. 컴파일
graph = graph_builder.compile()
```

**실행 흐름:**
```
START → chatbot → [도구 필요?] 
                  ├─ Yes → tools → chatbot → END
                  └─ No → END
```

### 4.2 도구 통합 패턴

#### 패턴 1: ToolNode 사용 (LangGraph)
```python
from langgraph.prebuilt import ToolNode, tools_condition

tool_node = ToolNode(tools=[get_weather, web_search])

# 조건부 라우팅
graph_builder.add_conditional_edges(
    "chatbot", 
    tools_condition  # tool_calls가 있으면 "tools"로, 없으면 END로
)
```

#### 패턴 2: Agent에 도구 직접 바인딩 (OpenAI Agents SDK)
```python
from agents import Agent, WebSearchTool, FileSearchTool

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    tools=[
        WebSearchTool(),
        FileSearchTool(),
    ]
)
```

### 4.3 Human-in-the-Loop 패턴

**예시: `hello-langgraph` - interrupt 사용**

```python
from langgraph.types import interrupt

@tool
def get_human_feedback(poem: str):
    response = interrupt({"poem": poem})  # 실행 중단, 사용자 입력 대기
    return response["feedback"]
```

**사용 시나리오:**
- 중요한 결정 전 사용자 확인
- 생성된 콘텐츠 피드백 수집
- 작업 승인 요청

---

## 5. Multi-Agent 아키텍처

### 5.1 Multi-Agent가 필요한 이유

**Single Agent의 한계:**
- 복잡한 작업을 하나의 Agent가 처리하기 어려움
- 전문성이 필요한 작업에 대해 범용 Agent는 부적합
- 병렬 처리 불가 (순차 실행만 가능)

**Multi-Agent의 장점:**
- 각 Agent가 특화된 역할 담당
- 병렬 처리 가능
- 모듈화와 확장성

### 5.2 Multi-Agent 아키텍처 패턴

#### 패턴 1: Supervisor Pattern (감독자 패턴)

**예시: `multi-agent-architectures`**

```python
# 감독자 Agent
def supervisor(state):
    llm_with_tools = llm.bind_tools(tools=[korean_agent_tool, spanish_agent_tool])
    result = llm_with_tools.invoke(state["messages"])
    return {"messages": [result]}

# 서브 에이전트를 도구로 변환
def make_agent_tool(tool_name, system_prompt):
    @tool(name=tool_name)
    def agent_tool(state):
        result = agent.invoke(state)  # 서브 에이전트 실행
        return result["messages"][-1].content
    return agent_tool

# 그래프 구조
graph_builder.add_node("supervisor", supervisor)
graph_builder.add_node("tools", ToolNode(tools=[...]))

graph_builder.add_edge(START, "supervisor")
graph_builder.add_conditional_edges("supervisor", tools_condition)
graph_builder.add_edge("tools", "supervisor")
```

**실행 흐름:**
```
사용자 입력
    ↓
Supervisor (언어 감지 및 라우팅)
    ↓
[한국어?] → korean_agent_tool 실행
[스페인어?] → spanish_agent_tool 실행
    ↓
결과를 Supervisor에 반환
    ↓
최종 응답
```

**실제 사용:**
- `customer-support-agent`: Triage Agent가 4개의 전문 에이전트로 라우팅
- `tutor-agent`: Classification Agent가 학습자 스타일에 따라 Teacher/Feynman/Quiz Agent로 라우팅

#### 패턴 2: Chain Pattern (체인 패턴)

**예시: `job-hunter-agent` (CrewAI)**

```python
@CrewBase
class JobHunterCrew:
    @agent
    def job_search_agent(self):
        return Agent(...)  # 1단계: 채용 공고 검색
    
    @agent
    def job_matching_agent(self):
        return Agent(...)  # 2단계: 이력서 매칭
    
    @task
    def job_extraction_task(self):
        return Task(
            agent=self.job_search_agent(),
            output_pydantic=JobList,
        )
    
    @task
    def job_matching_task(self):
        return Task(
            agent=self.job_matching_agent(),
            context=[self.job_extraction_task()],  # 이전 태스크 결과 사용
        )
    
    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,  # 순차 실행
        )
```

**실행 흐름:**
```
Job Search Agent → Job Matching Agent → Resume Optimization Agent 
    → Company Research Agent → Interview Prep Agent
```

**실제 사용:**
- `job-hunter-agent`: 5단계 순차 파이프라인
- `news-reader-agent`: 수집 → 요약 → 큐레이션

#### 패턴 3: Parallel Pattern (병렬 패턴)

**예시: `financial-analyst` (Google ADK)**

```python
financial_advisor = Agent(
    name="FinancialAdvisor",
    tools=[
        AgentTool(agent=data_analyst),      # 병렬 실행
        AgentTool(agent=financial_analyst), # 병렬 실행
        AgentTool(agent=news_analyst),      # 병렬 실행
    ],
)
```

**실행 흐름:**
```
Financial Advisor (메인)
    ├─→ Data Analyst (회사 기본 정보 수집)
    ├─→ Financial Analyst (재무제표 분석)
    └─→ News Analyst (뉴스 분석)
    
    모든 결과 수집 후 종합 분석
```

**예시: `workflow-architectures` (LangGraph Send 패턴)**

```python
def dispatch_summarizers(state: State):
    chunks = state["document"].split("\n\n")
    # 여러 청크를 병렬로 처리
    return [
        Send("summarize_p", {"paragraph": chunk, "index": i})
        for i, chunk in enumerate(chunks)
    ]

# 여러 인스턴스가 동시에 실행됨
graph_builder.add_conditional_edges(
    START,
    dispatch_summarizers,  # 여러 작업 생성
    ["summarize_p"],       # 병렬 실행
)
```

#### 패턴 4: Hybrid Pattern (하이브리드 패턴)

**예시: `customer-support-agent` (OpenAI Agents SDK)**

```python
# 1단계: Triage (Supervisor)
triage_agent = Agent(
    name="Triage Agent",
    handoffs=[  # Handoff 메커니즘 사용
        make_handoff(technical_agent),
        make_handoff(billing_agent),
        make_handoff(account_agent),
        make_handoff(order_agent),
    ],
)

# 2단계: 전문화된 Agent들이 각각 도구 사용
technical_agent = Agent(
    tools=[run_diagnostic_check, provide_troubleshooting_steps],
)
```

**Handoff 메커니즘:**
```python
@handoff
def make_handoff(agent):
    return handoff(
        agent=agent,
        on_handoff=handle_handoff,  # 전환 시 콜백
        input_type=HandoffData,     # 구조화된 전환 데이터
    )
```

### 5.3 Agent 간 통신 방법

#### 방법 1: State 공유 (LangGraph)
```python
class State(MessagesState):
    data_analyst_result: str
    financial_analyst_result: str

# Agent A가 결과를 State에 저장
# Agent B가 State에서 읽어서 사용
```

#### 방법 2: AgentTool (Google ADK)
```python
# 서브 에이전트를 도구로 사용
main_agent = Agent(
    tools=[
        AgentTool(agent=sub_agent),  # 서브 에이전트 호출
    ],
)
```

#### 방법 3: Handoff (OpenAI Agents SDK)
```python
# Agent A가 Agent B로 명시적으로 전환
triage_agent.handoffs = [make_handoff(technical_agent)]
```

#### 방법 4: Task Context (CrewAI)
```python
@task
def task_b(self):
    return Task(
        context=[self.task_a()],  # 이전 태스크 결과 자동 전달
    )
```

---

## 6. 프레임워크별 상세 가이드

### 6.1 LangGraph

**특징:**
- State 기반 워크플로우 관리
- 그래프 구조로 복잡한 로직 표현
- Human-in-the-loop 지원
- Checkpoint로 상태 저장/복원

#### 기본 구조

```python
from langgraph.graph import StateGraph, START, END

# 1. State 정의
class MyState(MessagesState):
    custom_field: str

# 2. 노드 함수 정의
def my_node(state: MyState):
    # 상태 읽기
    messages = state["messages"]
    
    # LLM 호출
    response = llm.invoke(messages)
    
    # 상태 업데이트
    return {"messages": [response]}

# 3. 그래프 빌드
graph_builder = StateGraph(MyState)
graph_builder.add_node("my_node", my_node)
graph_builder.add_edge(START, "my_node")
graph_builder.add_edge("my_node", END)

# 4. 컴파일 및 실행
graph = graph_builder.compile()
result = graph.invoke({"messages": [HumanMessage("Hello")]})
```

#### 프로젝트 예시

**`hello-langgraph`** - 기본 구조 학습
- 단순한 대화 Agent
- ToolNode 사용
- Interrupt 패턴

**`tutor-agent`** - 라우팅 패턴
- 조건부 라우팅 (conditional_edges)
- State에 current_agent 저장
- Agent 간 전환

**`workflow-architectures`** - 병렬 처리
- Send 패턴으로 여러 작업 동시 실행
- State 병합 (Annotated[list, add])

**`multi-agent-architectures`** - Supervisor 패턴
- 감독자가 서브 에이전트를 도구로 사용
- AgentTool 패턴 구현

### 6.2 CrewAI

**특징:**
- Role-based Agent 설계
- Task 중심 워크플로우
- YAML 설정 지원
- Knowledge Source 활용

#### 기본 구조

```python
from crewai import Agent, Task, Crew

# 1. Agent 정의 (역할 기반)
researcher = Agent(
    role="Researcher",
    goal="Research and gather information",
    backstory="You are an expert researcher...",
    tools=[web_search_tool],
)

writer = Agent(
    role="Writer",
    goal="Write compelling content",
    backstory="You are a professional writer...",
)

# 2. Task 정의
research_task = Task(
    description="Research the topic: {topic}",
    agent=researcher,
    expected_output="A research report",
)

writing_task = Task(
    description="Write an article based on: {research}",
    agent=writer,
    context=[research_task],  # 이전 태스크 결과 사용
    expected_output="A complete article",
)

# 3. Crew 생성 및 실행
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True,
)

result = crew.kickoff(inputs={"topic": "AI Agents"})
```

#### YAML 설정 (CrewBase 패턴)

```python
# config/agents.yaml
job_search_agent:
  role: Senior Job Market Research Specialist
  goal: Find and extract job listings
  backstory: You are an expert at finding jobs...
  
# main.py
@CrewBase
class JobHunterCrew:
    @agent
    def job_search_agent(self):
        return Agent(
            config=self.agents_config["job_search_agent"],  # YAML에서 로드
            tools=[web_search_tool],
        )
```

#### 프로젝트 예시

**`job-hunter-agent`** - Task Chain
- 5개 Agent가 순차적으로 작업
- Knowledge Source (이력서 파일) 사용
- Pydantic 모델로 구조화된 출력

**`content-pipeline-agent`** - CrewAI Flow
- Flow 패턴으로 복잡한 워크플로우 관리
- 조건부 라우팅 (@router)
- 반복 개선 (점수 체크 후 재생성)

**`news-reader-agent`** - 3단계 파이프라인
- 수집 → 요약 → 큐레이션
- 각 단계에서 필터링 및 점수 평가

### 6.3 Google ADK (Agent Development Kit)

**특징:**
- 서브 에이전트를 도구로 사용
- Structured Output (Pydantic)
- ParallelAgent로 병렬 실행
- Artifact 저장 기능

#### 기본 구조

```python
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

# 1. 서브 에이전트 정의
data_analyst = Agent(
    name="DataAnalyst",
    model=MODEL,
    tools=[get_company_info, get_stock_price],
    output_key="data_analyst_result",  # State에 저장될 키
)

# 2. 메인 에이전트가 서브 에이전트를 도구로 사용
main_agent = Agent(
    name="MainAgent",
    model=MODEL,
    tools=[
        AgentTool(agent=data_analyst),  # 서브 에이전트를 도구로
    ],
)

# 3. 실행
result = Runner.run(main_agent, "Analyze AAPL stock")
```

#### ParallelAgent 패턴

```python
from google.adk.agents.parallel_agent import ParallelAgent

# 여러 서브 에이전트를 병렬 실행
parallel_agent = ParallelAgent(
    agents=[image_generator_agent, voice_generator_agent],
)

main_agent = Agent(
    tools=[AgentTool(agent=parallel_agent)],
)
```

#### Structured Output

```python
from pydantic import BaseModel

class Scene(BaseModel):
    title: str
    narration: str
    duration: int

# 에이전트가 구조화된 출력 생성
agent = Agent(
    model=MODEL,
    response_format=Scene,  # Pydantic 모델 지정
)
```

#### 프로젝트 예시

**`financial-analyst`** - Multi-Agent 협업
- 3개 서브 에이전트가 병렬 실행
- 결과를 State에 저장 후 종합
- 리포트를 Artifact로 저장

**`youtube-shorts-maker`** - 복잡한 파이프라인
- Content Planner → Asset Generator → Video Assembler
- ParallelAgent로 이미지/음성 동시 생성
- Callback으로 입력 필터링

### 6.4 OpenAI Agents SDK

**특징:**
- Handoff 메커니즘
- Guardrails (입력/출력 필터링)
- VoicePipeline (음성 처리)
- Session 관리

#### 기본 구조

```python
from agents import Agent, Runner, SQLiteSession

# 1. Agent 정의
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    tools=[WebSearchTool(), FileSearchTool()],
)

# 2. Session 생성
session = SQLiteSession("conversation-id", "db.sqlite")

# 3. 실행
result = Runner.run(
    agent,
    "What's the weather in Seoul?",
    session=session,
)
```

#### Handoff 메커니즘

```python
from agents import handoff

def make_handoff(agent):
    return handoff(
        agent=agent,
        on_handoff=handle_handoff,  # 전환 시 콜백
        input_type=HandoffData,     # 구조화된 데이터
    )

triage_agent = Agent(
    handoffs=[
        make_handoff(technical_agent),
        make_handoff(billing_agent),
    ],
)
```

#### Guardrails

```python
from agents import input_guardrail, output_guardrail

@input_guardrail
async def validate_input(wrapper, agent, input):
    # 입력 검증
    if is_off_topic(input):
        return GuardrailFunctionOutput(
            tripwire_triggered=True,
            output_info="Off-topic request",
        )
    return GuardrailFunctionOutput(tripwire_triggered=False)

agent = Agent(
    input_guardrails=[validate_input],
)
```

#### VoicePipeline

```python
from agents.voice import VoiceWorkflowBase

class CustomWorkflow(VoiceWorkflowBase):
    async def run(self, transcription):
        result = Runner.run_streamed(agent, transcription)
        async for chunk in VoiceWorkflowHelper.stream_text_from(result):
            yield chunk  # 음성으로 변환하여 스트리밍
```

#### 프로젝트 예시

**`customer-support-agent`** - 완전한 지원 시스템
- Triage Agent로 라우팅
- 4개 전문 에이전트 (Account, Billing, Order, Technical)
- Input Guardrail로 오프토픽 필터링
- Output Guardrail로 기술적 정확성 검증
- VoicePipeline으로 음성 입출력

**`chatgpt-clone`** - 종합 어시스턴트
- 여러 도구 통합 (Web, File, Image, Code)
- MCP 서버 통합
- 스트리밍 응답
- Session으로 대화 히스토리 관리

---

## 7. 고급 패턴

### 7.1 Human-in-the-Loop

**언제 사용:**
- 중요한 결정 전 확인 필요
- 생성된 콘텐츠 피드백 수집
- 작업 승인 요청

**구현 방법:**

**LangGraph - interrupt 사용**
```python
from langgraph.types import interrupt

@tool
def get_approval(action: str):
    response = interrupt({"action": action})
    return response["approved"]
```

**실제 예시: `hello-langgraph`**
- 시 생성 후 사용자 피드백 수집
- 피드백 반영하여 재생성

### 7.2 조건부 라우팅 (Conditional Routing)

**언제 사용:**
- 입력에 따라 다른 처리 경로 선택
- 상태에 따른 분기 처리

**구현 방법:**

**LangGraph - conditional_edges**
```python
def route_function(state):
    if condition1:
        return "path1"
    elif condition2:
        return "path2"
    else:
        return "path3"

graph_builder.add_conditional_edges(
    "node",
    route_function,
    {
        "path1": "node1",
        "path2": "node2",
        "path3": "node3",
    }
)
```

**실제 예시:**
- `tutor-agent`: 학습자 스타일에 따라 Teacher/Feynman/Quiz Agent 선택
- `content-pipeline-agent`: 콘텐츠 타입에 따라 Blog/Tweet/LinkedIn 생성

### 7.3 병렬 처리 (Parallel Processing)

**언제 사용:**
- 독립적인 작업을 동시에 수행
- 성능 최적화

**구현 방법:**

**LangGraph - Send 패턴**
```python
from langgraph.types import Send

def dispatch_workers(state):
    return [
        Send("worker", {"task": task})
        for task in state["tasks"]
    ]

graph_builder.add_conditional_edges(
    START,
    dispatch_workers,
    ["worker"],  # 여러 인스턴스 병렬 실행
)
```

**Google ADK - ParallelAgent**
```python
from google.adk.agents.parallel_agent import ParallelAgent

parallel_agent = ParallelAgent(
    agents=[agent1, agent2, agent3],
)
```

**실제 예시:**
- `workflow-architectures`: 문서를 청크로 나눠 병렬 요약
- `financial-analyst`: 3개 서브 에이전트 병렬 실행
- `youtube-shorts-maker`: 이미지와 음성 동시 생성

### 7.4 반복 개선 (Iterative Refinement)

**언제 사용:**
- 품질 기준을 만족할 때까지 반복
- 점수 기반 품질 검증

**구현 방법:**

**CrewAI Flow - Router와 Listen**
```python
@router(check_score)
def score_router(self):
    if self.state.score >= 7:
        return "check_passed"
    else:
        return "remake"  # 재생성으로 돌아감

@listen("remake")
def remake_content(self):
    # 콘텐츠 재생성
    ...
```

**실제 예시: `content-pipeline-agent`**
- 콘텐츠 생성 → 점수 평가 → 7점 미만이면 재생성 → 반복

### 7.5 구조화된 출력 (Structured Output)

**언제 사용:**
- 일관된 형식의 출력 필요
- 파싱이 쉬운 구조 필요

**구현 방법:**

**Pydantic 모델 사용**
```python
from pydantic import BaseModel

class JobListing(BaseModel):
    title: str
    company: str
    location: str
    salary: float

# Google ADK
agent = Agent(response_format=JobListing)

# CrewAI
task = Task(output_pydantic=JobListing)
```

**실제 예시:**
- `job-hunter-agent`: JobList, RankedJobList 등 구조화된 모델
- `youtube-shorts-maker`: Scene 리스트 구조화
- `content-pipeline-agent`: BlogPost, Tweet 등

### 7.6 Knowledge Source 활용

**언제 사용:**
- 외부 문서나 데이터를 Agent가 참조해야 할 때
- 지식 베이스 통합

**구현 방법:**

**CrewAI - Knowledge Source**
```python
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

resume_knowledge = TextFileKnowledgeSource(
    file_paths=["resume.txt"],
)

agent = Agent(
    knowledge_sources=[resume_knowledge],
)
```

**실제 예시: `job-hunter-agent`**
- 이력서 파일을 Knowledge Source로 제공
- Agent가 이력서 내용을 참조하여 채용 공고 매칭

### 7.7 Guardrails (안전장치)

**언제 사용:**
- 부적절한 입력 필터링
- 출력 검증
- 비즈니스 규칙 적용

**구현 방법:**

**OpenAI Agents SDK**
```python
@input_guardrail
async def validate_input(wrapper, agent, input):
    if is_off_topic(input):
        return GuardrailFunctionOutput(tripwire_triggered=True)
    return GuardrailFunctionOutput(tripwire_triggered=False)

@output_guardrail
async def validate_output(wrapper, agent, output):
    if contains_inaccurate_info(output):
        return GuardrailFunctionOutput(tripwire_triggered=True)
    return GuardrailFunctionOutput(tripwire_triggered=False)
```

**실제 예시: `customer-support-agent`**
- Input Guardrail: 오프토픽 요청 필터링
- Output Guardrail (Technical): 기술적 정확성 검증

### 7.8 Callback과 인터셉션

**언제 사용:**
- 요청/응답 전처리/후처리
- 로깅 및 모니터링
- 입력 필터링

**구현 방법:**

**Google ADK - Callback**
```python
def before_model_callback(callback_context, llm_request):
    # LLM 호출 전에 인터셉트
    last_message = llm_request.contents[-1]
    if "hummus" in last_message.text:
        # 특정 키워드 감지 시 차단
        return LlmResponse(content="Sorry I can't help with that.")
    return None  # 정상 진행

agent = Agent(
    before_model_callback=before_model_callback,
)
```

**실제 예시: `youtube-shorts-maker`**
- 특정 키워드("hummus") 감지 시 요청 차단

---

## 8. 프로젝트별 학습 경로 추천

### 초급자 경로

1. **`my-first-agent`** - Function Calling 기본 이해
2. **`hello-langgraph`** - LangGraph 기본, Human-in-the-Loop
3. **`chatgpt-clone`** - 단일 Agent + 다양한 도구

### 중급자 경로

4. **`tutor-agent`** - Multi-Agent 라우팅 (LangGraph)
5. **`multi-agent-architectures`** - Supervisor 패턴 (LangGraph)
6. **`job-hunter-agent`** - Task Chain (CrewAI)
7. **`customer-support-agent`** - Handoff 메커니즘 (OpenAI Agents SDK)

### 고급자 경로

8. **`financial-analyst`** - 병렬 Multi-Agent (Google ADK)
9. **`content-pipeline-agent`** - 복잡한 워크플로우 (CrewAI Flow)
10. **`workflow-architectures`** - 병렬 처리 (LangGraph Send)
11. **`youtube-shorts-maker`** - 복잡한 파이프라인 (Google ADK)

---

## 9. 핵심 개념 정리

### 9.1 Agent의 4가지 핵심 요소

1. **LLM (Language Model)**: 의사결정과 추론
2. **Tools (도구)**: 외부 세계와 상호작용
3. **State (상태)**: 맥락과 정보 유지
4. **Orchestration (조율)**: 워크플로우 관리

### 9.2 Multi-Agent 선택 가이드

| 상황 | 추천 패턴 | 프레임워크 | 예시 프로젝트 |
|------|----------|-----------|--------------|
| 단순 순차 작업 | Chain | CrewAI | `job-hunter-agent` |
| 입력에 따른 분기 | Supervisor | LangGraph | `tutor-agent` |
| 독립 작업 병렬 실행 | Parallel | LangGraph/ADK | `financial-analyst` |
| Agent 간 전환 필요 | Handoff | OpenAI SDK | `customer-support-agent` |
| 복잡한 조건부 로직 | Flow | CrewAI Flow | `content-pipeline-agent` |

### 9.3 프레임워크 선택 가이드

**LangGraph를 선택하세요:**
- State 기반 복잡한 워크플로우
- Human-in-the-Loop 필요
- 그래프 구조로 로직 표현
- Checkpoint로 상태 저장 필요

**CrewAI를 선택하세요:**
- Role-based Agent 설계
- Task 중심 워크플로우
- YAML 설정 선호
- Knowledge Source 활용

**Google ADK를 선택하세요:**
- 서브 에이전트를 도구로 사용
- Structured Output 중요
- 병렬 실행 필요
- Artifact 저장 필요

**OpenAI Agents SDK를 선택하세요:**
- Handoff 메커니즘 필요
- Guardrails 중요
- Voice 지원 필요
- 프로덕션 배포

---

## 10. 실전 팁

### 10.1 디버깅

- **State 확인**: 각 단계에서 State 내용 로깅
- **도구 호출 추적**: 어떤 도구가 언제 호출되는지 확인
- **에러 핸들링**: 도구 실행 실패 시 대체 경로 제공

### 10.2 성능 최적화

- **병렬 처리**: 독립적인 작업은 병렬 실행
- **캐싱**: 동일한 요청 결과 캐싱
- **점진적 실행**: 큰 작업을 작은 단위로 분할

### 10.3 비용 관리

- **모델 선택**: 단순 작업에는 더 작은 모델 사용
- **도구 호출 최소화**: 불필요한 도구 호출 방지
- **토큰 관리**: State 크기 관리, 오래된 메시지 제거

### 10.4 확장성

- **모듈화**: Agent와 도구를 재사용 가능하게 설계
- **설정 외부화**: YAML이나 환경 변수 사용
- **플러그인 구조**: 새로운 도구나 Agent 쉽게 추가 가능하게

---

## 결론

이 가이드를 통해:
1. ✅ AI Agent의 기본 개념 이해
2. ✅ Function Calling과 State Management 이해
3. ✅ Single Agent 구현 방법 학습
4. ✅ Multi-Agent 아키텍처 패턴 이해
5. ✅ 각 프레임워크의 특징과 사용법 학습
6. ✅ 고급 패턴과 실제 활용 방법 학습

**다음 단계:**
1. 각 프로젝트의 코드를 직접 실행해보기
2. 작은 프로젝트부터 시작하여 점진적으로 복잡도 증가
3. 자신의 문제에 맞는 패턴 선택 및 적용
4. 커뮤니티와 지식 공유

행운을 빕니다! 🚀

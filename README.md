[🇰🇷 한국어](README.md) | [🇺🇸 영어](README_en.md)

# AI Bot 🤖

**Google Gemini와 Perplexity의 강력한 기능을 Mattermost로 연결하는 지능형 어시스턴트.**

## 🚀 What is it?

AI Bot은 최첨단 LLM(Large Language Models)을 팀의 커뮤니케이션 허브인 Mattermost와 즉시 연동시켜주는 Python 기반 CLI 도구입니다. 복잡한 설정 없이 질문 하나로 생성형
AI의 답변과 실시간 검색 결과를 팀원들과 공유하세요.

## ✨ Key Features

- **Dual Intelligence**: 창의적이고 빠른 **Google Gemini**와 실시간 정보 검색에 강한 **Perplexity Pro**를 자유롭게 전환하며 사용 가능.
- **Seamless Integration**: Markdown이 적용된 깔끔한 포맷으로 Mattermost 채널에 답변 자동 전송.
- **Developer Ready**: 간편한 CLI 인터페이스로 스크립트 및 워크플로우 자동화에 최적화.

## 🛠 Quick Start

### 1. Prerequisites

필요한 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

### 2. Configuration

`.env` 파일에 API 키를 설정하세요.

```properties
GEMINI_API_KEY=your_gemini_key
PPLX_API_KEY=your_perplexity_key
MATTERMOST_WEBHOOK_URL=your_webhook_url
```

### 3. Usage

원하는 모델을 선택하여 바로 실행해보세요.

**Perplexity로 실시간 정보 검색 (Sonar Pro)**

```bash
python ai_bot.py --prompt "2024년 생성형 AI 기술 트렌드 요약해줘" --model perplexity
```

**Gemini로 창의적인 답변 및 코딩 (Default)**

```bash
python ai_bot.py --prompt "Python 데코레이터 패턴 예제 코드 작성해줘"
```

---
Built for speed and simplicity. 

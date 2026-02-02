import os
import argparse
import requests
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Jenkins Credentials에서 주입받을 환경변수
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PPLX_API_KEY = os.getenv("PPLX_API_KEY")
MATTERMOST_WEBHOOK_URL = os.getenv("MATTERMOST_WEBHOOK_URL")


def ask_gemini(prompt):
    """Google Gemini Pro에게 질문"""
    try:
        client = genai.Client()
        response = client.models.generate_content(model="gemini-3-flash-preview", contents=prompt)
        return response.text
    except Exception as e:
        return f"Gemini API 오류: {str(e)}"


def ask_perplexity(prompt):
    """Perplexity Sonar Pro에게 질문 (최신 정보 검색)"""
    try:
        url = "https://api.perplexity.ai/chat/completions"
        payload = {
            "model": "sonar-pro",  # 또는 sonar-reasoning-pro
            "messages": [
                {
                    "role": "system",
                    "content": "1. 데이터를 생성하기 위해 사용된 자료에 링크가 있다면, 링크는 맨 마지막에 따로 제공해주세요. 2. 생성 결과는 항상 Markdown 형식으로 제공해주세요. 3. 내용은 이해하기 쉽게, 어려운 용어는 풀어서 설명해주세요.",
                },
                {"role": "user", "content": prompt},
            ],
        }
        headers = {"Authorization": f"Bearer {PPLX_API_KEY}", "Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # HTTP 에러 체크
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Perplexity API 오류: {str(e)}"


def send_mattermost(message, bot_name="AI Assistant"):
    """Mattermost로 메시지 전송"""
    headers = {"Content-Type": "application/json"}
    payload = {
        "text": message,
        "username": bot_name,
        "icon_url": "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",  # 원하는 아이콘 URL
    }

    try:
        response = requests.post(MATTERMOST_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
        if response.status_code != 200:
            print(f"메시지 전송 실패: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Mattermost 전송 중 에러 발생: {str(e)}")


if __name__ == "__main__":
    # 인자 파싱
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True, help="질문 내용")
    parser.add_argument("--model", default="gemini", help="사용할 모델 (gemini/perplexity)")
    args = parser.parse_args()

    print(f"Processing: [{args.model}] {args.prompt}")

    # 모델 선택 및 호출
    if args.model.lower() == "perplexity":
        answer = ask_perplexity(args.prompt)
        source_emoji = "🧠"  # Perplexity 상징 (검색/지식)
        model_name = "Perplexity Pro"
    else:
        answer = ask_gemini(args.prompt)
        source_emoji = "✨"  # Gemini 상징
        model_name = "Gemini Pro"

    # Mattermost 메시지 포맷팅 (Markdown 활용)
    # > 인용구로 질문을 표시하고, 답변을 아래에 배치
    formatted_message = f"""
### {source_emoji} {model_name}

---

{answer}
    """

    send_mattermost(formatted_message, bot_name=model_name)
    print(answer)
    print("Done.")

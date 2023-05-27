from typing import Dict
import requests
import os

class ChatgptController():

    @classmethod
    def reduce_content(cls, context: str) -> str:
        response: Dict[str] = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {os.getenv('OPENAI_API')}"},
            json={"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": f"{context} 라는 내용을 [Title]과 [Context] 순으로 한칸 뛰운다음 잘 정리해서 알려줘"}]},
        )

        return response.json()["choices"][0]["message"]["content"]
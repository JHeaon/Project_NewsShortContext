## Python-Vanilla-NewsShortContext

해당 프로젝트는 telegram, chatgpt에서 제공하는 api와 selenium을 이용하여, kbs에서 제공하는 뉴스 내용을 chatgpt을 통해 정리후
telegram으로 해당 내용을 보내주는 프로젝트 입니다. 


## Quick Start

- python version : 3.11.3
- .env

```
py -3.11 -m venv env
source env/Scripts/Activate
pip install -r requirements.txt
```

해당 main.py 을 사용하기 위해선 .env 파일에 다음과 같이 api_key가 정리되어 있어야 합니다. 
```
OPENAI_API=[openai 에서 제공하는 api_key]
HTTP_API=[telegram_bot 에서 제공하는 api_key]
CHAT_ID=[telegram에서 사용할 챗 id]
```

## Stack

- Python 3.11.3 version
- telegram_api
- chatgpt_api
- selenium 4.9.1 version


## History

- youtube kbs 채널에서 제공하는 newsdata을 이용하여 텔레그램 메세지로 전송하는 기능 개발 (23.05.27) <br>


## Reference

- 
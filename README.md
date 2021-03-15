# Realw Newbie bot

![python](https://img.shields.io/pypi/pyversions/discord.py.svg)

[![RAID Join](https://discord.com/api/guilds/678572912797679617/widget.png?style=banner2)](https://discord.gg/raidkr)

[FiveM 리얼월드 서버팩의 데이터베이스 기반으로 제작하였습니다.](https://github.com/fivem-realw/RWServer)

배포하더라도, 출처는 꼭 밝혀주세요! (해당 Github 주소 첨부 필수)

기초적인 틀만 짰습니다. 알아서 수정해서 사용하시면 됩니다.

## **Setting**

[Python 다운로드하려면 여기를 클릭해주세요.](https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe)

Linux/macOS
```
python3 -m pip install -U discord.py
python3 -m pip install -U pymysql
```
Windows
```
py -3 -m pip install -U discord.py
py -3 -m pip install -U pymysql
```

## Database Config

- config.json을 꼭 수정해주세요.

  - 자신의 데이터베이스 설정대로 수정해주세요. (기본값에 맞춰 미리 설정하였습니다)

  - **테이블 이름**은 **리얼월드 서버팩** `vrp_newbie` 스크립트에 맞춰 `vrp_newbie_bonus`로 하였습니다. (다르다면 수정해주세요)

## Bot Config

- config.json을 꼭 수정해주세요.

  - 자신이 사용할 봇 토큰을 입력해주세요.

    - 토큰 없이 실행 시, 오류 메시지가 띄워지며, 토큰을 생성하는 방법 창이 열립니다.

     - [봇 생성 또는 토큰 불러오기](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)


- 자신이 뉴비인증 채널로 쓰고싶은 채널의 ID를 작성해주세요.

  - 채널 ID가 어디있는지 모른다면, [이곳을 눌러 확인하세요.](https://support.discord.com/hc/ko/articles/206346498-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%84%9C%EB%B2%84-%EB%A9%94%EC%8B%9C%EC%A7%80-ID%EB%8A%94-%EC%96%B4%EB%94%94%EC%84%9C-%ED%99%95%EC%9D%B8%ED%95%98%EB%82%98%EC%9A%94-) 공식 디스코드 링크


- 뉴비인증 후 지급할 역할의 ID를 적어주세요.

 - 역할 ID가 어디있는지 모른다면, [이곳을 눌러 확인하세요.](https://www.youtube.com/watch?v=Xme4lBvrCN8) 유튜브 링크

## Other

MySQL 관련 오류는 알아서 고쳐주세요.


**모듈 설치 중 에러 발생 시**

Linux/macOS
```bash
py -3 -m pip install -U wheel
```
Windows
```c
python -m pip install -U wheel
```

Made by daekwon#0001 (Discord)

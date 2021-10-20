# Realw Newbie bot (2021.09.01. 정상 작동 확인됨.)
[FiveM 리얼월드 서버팩의 데이터베이스 기반으로 제작하였습니다.](https://github.com/fivem-realw/RWServer)

해당 레파지토리는 **2021.01.27**에 게시되었습니다.

2차 배포 시 출처는 꼭 밝혀주세요. (해당 주소 첨부)

## **Setting**

**3.9 버전** 이하로 다운로드해주세요.

[[Python 다운로드하기!]](https://wikidocs.net/8)

위 사항을 모두 완료 후, setup.bat 을 실행해주세요.

## Database Config

- config.json을 꼭 수정해주세요.

  - 자신의 데이터베이스 설정대로 수정해주세요. (기본값에 맞춰 미리 설정하였습니다)

  - **테이블 이름**은 **리얼월드 서버팩** `vrp_newbie` 스크립트에 맞춰 `vrp_newbie_bonus`로 하였습니다.

    - **모두 config.json에서 수정하실 수 있습니다.**

## Bot Config

- config.json을 꼭 수정해주세요.

  - 자신이 사용할 봇 토큰을 입력해주세요.

    - 토큰 없이 실행 시, 오류 메시지가 띄워지며, 토큰을 생성하는 방법이 나옵니다.

     - [[봇 생성 또는 토큰 불러오기]](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)


- 자신이 뉴비인증 채널로 쓰고싶은 채널의 ID를 작성해주세요.

  - 채널 ID가 어디있는지 모른다면, [[이곳을 눌러 확인하세요.]](https://support.discord.com/hc/ko/articles/206346498-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%84%9C%EB%B2%84-%EB%A9%94%EC%8B%9C%EC%A7%80-ID%EB%8A%94-%EC%96%B4%EB%94%94%EC%84%9C-%ED%99%95%EC%9D%B8%ED%95%98%EB%82%98%EC%9A%94-) - 공식 디스코드 링크


- 뉴비인증 후 지급할 역할의 ID를 적어주세요.

 - 역할 ID가 어디있는지 모른다면, [[이곳을 눌러 확인하세요.]](https://www.youtube.com/watch?v=Xme4lBvrCN8) - 유튜브 링크

- 봇에게 들어가 있는 역할에 `역할 관리하기` 권한을 추가해주세요.

- **봇의 역할**을 지급하려는 역할보다 `높게` 설정하셔야 합니다.

## Other


**setup.bat 에러 발생 시**

Linux/macOS
```bash
py -3 -m pip install -U wheel
```
Windows
```c
python -m pip install -U wheel
```

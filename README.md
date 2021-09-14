# flask_boilerplate
- flask 프로젝트를 위한 기본적인 셋팅을 도와줍니다.
- 현재 db가 SQLite로 설정되어 있습니다. 다른 RDBMS를 쓰고 싶으시다면 

# 실행 순서
## 0. 준비물
- git이 설치되어있어야 한다.

## 1. 폴더 만들기
- 빈 폴더를 생성한다.(예: mkdir project)
## 2. git clone, checkout
1. 방금 생성한 폴더에 들어간다.(cd project)
2. 해당 위치에 git clone한다. (git clone https://github.com/gon2gon2/flask_boilerplate .)
3. 윈도우 유저는 run.bat을, 리눅스 유저는 run.sh를 실행시킵니다.(run.bat  / sh run.sh)

## 3. 내 프로젝트로 이름 바꾸기
- project_name 폴더명
- project_name/views/models.py 의 3번 라인 from ~~~ import db
- config.py의 5번 라인 '~~~.db'
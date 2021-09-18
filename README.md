# flask_boilerplate
- flask 프로젝트를 위한 기본적인 셋팅을 도와줍니다.
- 현재 db가 SQLite로 설정되어 있습니다. 다른 RDBMS를 쓰고 싶으시다면 알잘딱깔센
- 처음 하시는 분들은 가이드 영상을 보면서 따라해주세요.

# 실행 방법, 순서
### 준비물
- git
- editor(vscode, pycharm, ...)
---
## 초기 설정
### 1. 폴더 만들기
    - 예: "mkdir project"
### 2. 방금 생성한 폴더에 들어간다.
    - 예: "cd project"
### 3. 해당 위치에 git clone한다. (맨 뒤의 점까지)
    - "git clone https://github.com/gon2gon2/flask_boilerplate ."
    - 리눅스인 경우: git checkout linux 도 실행.
### 4. 내 프로젝트로 이름 바꾸기
    - project_name/views/models.py 의 3번 라인 "from ~~~ import db"
    - 현재 디렉토리의 project_name 폴더명을 내 프로젝트 이름으로 변경 (예: library)
    - config.py의 5번 라인 '~~~.db'
### 5. 가상환경과 db 생성
    - Windows
        1. pip install virtualenv
        2. virtualenv venv
        3. activate
        4. pip install -r requirements.txt
        5. db
        6. run
    - Linux
        1. pip3 install virtualenv
        2. virtualenv venv
        3. source venv/bin/activate
        4. pip3 install -r requirements.txt
        5. sh ./db.sh
        6. sh ./run.sh
---
## 초기 설정 이후
<b>1.db.cmd 혹은 db.sh 파일 내용을 수정해주세요.</b>
- 3번 라인의 "flask db init"을 삭제 혹은 주석처리 해주세요.

<b>2. (중요)초기 설정 이후 개발 할 때 순서</b>
1. 가상환경 활성화
2. run 파일 실행
3. db가 바뀌었다면 db 파일 실행(아래 3번 참조)

<b>3. models.py가 변경 되었어요.</b>
- 윈도우: db.cmd를 실행시키세요.
- 리눅스: db.sh를 실행시키세요.

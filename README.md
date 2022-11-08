# 📝 Sprint 3-2
### 오늘의 키워드
- Web Server Gateway Interface (WSGI)
  - 중간 역할을 맡고 있는 middleware
  - 서버나 게이트웨이를 애플리케이션이나 프레임워크와 이어줌
  - Flask 와 같은 마이크로 프레임워크를 서버로 연결해 외부에서 접속할 수 있도록 도와주는 역할
  - Heroku
    - 클라우드 플랫폼을 제공하는 서비스
    ```
    $ heroku login
    $ heroku apps #heroku 등록된 app 리스트 확인
    $ heroku create my_app
    $ heroku apps:info --app my_app #app 상세정보 확인
    ```
    - 배포를 위해서는 flask_app, requirements.txt, Procfile 존재해야함
    - pip freeze > requirements.txt
    - Procfile 내용 web: gunicorn --workers=2 'flask_app:create_app()' -> create_app()은 app=flask(__name__) 들어가 있는 부분
    - 'flask_app:app'
   - Metabase 대시보드
    - docker에서 이미지 받아와서 container 실행 : docker run -p 3000:3000 --name metabase_test metabase/metabase
    - 127.0.0.1:3000 실행 확인
    - winpty docker container exec -it metabase_test bash로 리눅스 경로 확인
    - 대시보드 생성 원하는 db 데이터 원하는 경로에 복사하여 이미지 생성
    - docker cp ./chinook.db metabase_test:/app
    - 아래 첨부와 같이 복사한 경로 및 대시보드 생성 이름 설정 후 마무리
    
    ![image](https://user-images.githubusercontent.com/48580158/200589206-3b5203c5-765b-469b-a916-f0cafbd27d67.png)

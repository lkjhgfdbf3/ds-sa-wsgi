# π Sprint 3-2
### μ€λμ ν€μλ
- Web Server Gateway Interface (WSGI)
  - μ€κ° μ­ν μ λ§‘κ³  μλ middleware
  - μλ²λ κ²μ΄νΈμ¨μ΄λ₯Ό μ νλ¦¬μΌμ΄μμ΄λ νλ μμν¬μ μ΄μ΄μ€
  - Flask μ κ°μ λ§μ΄ν¬λ‘ νλ μμν¬λ₯Ό μλ²λ‘ μ°κ²°ν΄ μΈλΆμμ μ μν  μ μλλ‘ λμμ£Όλ μ­ν 
  - Heroku
    - ν΄λΌμ°λ νλ«νΌμ μ κ³΅νλ μλΉμ€
    ```
    $ heroku login
    $ heroku apps #heroku λ±λ‘λ app λ¦¬μ€νΈ νμΈ
    $ heroku create my_app
    $ heroku apps:info --app my_app #app μμΈμ λ³΄ νμΈ
    ```
    - λ°°ν¬λ₯Ό μν΄μλ flask_app, requirements.txt, Procfile μ‘΄μ¬ν΄μΌν¨
    - pip freeze > requirements.txt
    - Procfile λ΄μ© web: gunicorn --workers=2 'flask_app:create_app()' -> create_app()μ app=flask(__name__) λ€μ΄κ° μλ λΆλΆ
    - 'flask_app:app'
   - Metabase λμλ³΄λ
    - dockerμμ μ΄λ―Έμ§ λ°μμμ container μ€ν : docker run -p 3000:3000 --name metabase_test metabase/metabase
    - 127.0.0.1:3000 μ€ν νμΈ
    - winpty docker container exec -it metabase_test bashλ‘ λ¦¬λμ€ κ²½λ‘ νμΈ
    - λμλ³΄λ μμ± μνλ db λ°μ΄ν° μνλ κ²½λ‘μ λ³΅μ¬νμ¬ μ΄λ―Έμ§ μμ±
    - docker cp ./chinook.db metabase_test:/app
    - μλ μ²¨λΆμ κ°μ΄ λ³΅μ¬ν κ²½λ‘ λ° λμλ³΄λ μμ± μ΄λ¦ μ€μ  ν λ§λ¬΄λ¦¬
    
    ![image](https://user-images.githubusercontent.com/48580158/200589206-3b5203c5-765b-469b-a916-f0cafbd27d67.png)

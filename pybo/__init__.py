# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 10:26:40 2025

@author: KIMMINJI
"""
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def create_app():        
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models
    
    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # 필터
    from .filter import format_datetime, markdown_to_html
    app.jinja_env.filters['datetime'] = format_datetime
    
    # markdown
    app.jinja_env.filters['markdown'] = markdown_to_html  

    
    return app


'''
#====== 2트 ====================
def create_app():           # 애플리케이션 팩토리(플라스크 내부에서 정의된 함수) => 절대 수정 불가능
    app = Flask(__name__)
    
    @app.route('/')
    def hello_pybo():
        return 'Hello Pybo'
    
    return app

#====== 1트 ====================
app = Flask(__name__)

@app.route('/')
def hello_pybo():
    return 'Hello Pybo'

#=> C:\project\myproject\pybo.py
'''

'''
app = Flask(__name__)
=> Flask 클래스로 만든 객체 

플라스크는 app 객체를 사용해 여러 가지 설정을 진행
  app 객체를 전역으로 사용
  프로젝트 규모가 커질수록 순환 참조(circular import) 오류가
  발생할 확률이 높아진다.
 
 순환 참조(circular import)
 => A 모듈이 B 모듈을 참조하고
 => B 모듈이 다시 A 모듈을 참조하는 경우
 
플라스크 공식 홈페이지에서는 
"애플리케이션 팩토리(application factory)를 사용하라"
팩토리 : 디자인패턴 (코드)
'''
#=> C:\project\myproject\pybo.py => pybo 폴더에 옮기고 => __init__.py 로 변경
# -*- coding: utf-8 -*-
'''
@app.route('/')
http://127.0.0.1:5000/

@app.route('/login')
http://127.0.0.1:5000/login

* 반드시 '/' 뒤에 동일하게 작성하기.
'''

'''
블루프린트
플라스크의 블루프린트를 이용하면 라우팅 함수를 체계적으로 관리할 수 있다. 
=> 플라스크에서 URL과 함수의 매핑을 관리하기 위해 사용하는 도구(클래스)

(myproject) c:\projects\myproject\pybo> mkdir views
(myproject) c:\projects\myproject\pybo/views> main_
'''

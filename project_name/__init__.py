from flask import Flask, request, render_template, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = "쉿, 비밀이야"
    
    
    ## 자기가 만든 bp들을 app에 등록합니다.
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    ## ORM을 위한 init 과정입니다.
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app
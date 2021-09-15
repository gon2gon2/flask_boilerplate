from flask import Blueprint, request, session, render_template

from project_name import db
from ..models import Test, User

from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def home():
    
    now = datetime.now()
    history = Test(now)
    db.session.add(history)
    db.session.commit()
    
    return render_template('mainpage.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')
    
    id = request.form['id']
    pw = request.form['pw']
    user = User(user_id=id, pw=pw)
    db.session.add(user)
    db.session.commit()
    return render_template('signup.html')
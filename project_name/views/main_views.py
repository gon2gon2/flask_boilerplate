from flask import Blueprint, render_template

from project_name import db
from ..models import Test

from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def home():
    
    now = datetime.now()
    history = Test(now)
    db.session.add(history)
    db.session.commit()
    
    return render_template('mainpage.html')
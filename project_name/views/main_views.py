from flask import Blueprint, request, session, render_template

from project_name import db
from ..models import History

from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def home():
    
    now = datetime.now()
    history = History(now)
    db.session.add(history)
    db.session.commit()
    
    return render_template('mainpage.html')
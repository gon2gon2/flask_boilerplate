from flask import Blueprint, request, session, render_template

from project_name import db


bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def home():
    return render_template('mainpage.html')
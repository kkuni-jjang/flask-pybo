# -*- coding: utf-8 -*-
from flask import Blueprint, render_template,  url_for, current_app
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

'''
@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list = question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html', question=question)


@bp.route('/detail/<int:question_id>/')
def detail(question_id): 
    question = Question.query.get_or_404(question_id)   
    return render_template('question/question_detail.html', question=question)
'''
@bp.route('/')
def index():
    current_app.logger.info("INFO 레벨로 출력")
'''
'main'
    => Blueprint의 별칭
    
__name__
    => main_views
    
url_prefix='/'
    => localhost:5000/
    
ex) url_prefix='/main'
    => localhost:5000/main
'''





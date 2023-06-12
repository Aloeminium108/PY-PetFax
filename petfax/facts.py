from flask import ( Blueprint, redirect, render_template, request ) 
from . import models

bp = Blueprint('facts', __name__, url_prefix="/facts")

@bp.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'GET':
    results = models.Fact.query.all()

    return render_template('facts/index.html', facts=results)
  
  if request.method == 'POST':
    submitter = request.form['submitter']
    fact = request.form['fact']

    new_fact = models.Fact(submitter=submitter, fact=fact)
    models.db.session.add(new_fact)
    models.db.session.commit()

    return redirect('/facts')


  
  
@bp.route('/new', methods=['GET'])
def new():
  return render_template('facts/new.html')
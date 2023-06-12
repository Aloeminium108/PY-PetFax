from flask import ( Blueprint, redirect, render_template, request ) 

bp = Blueprint('facts', __name__, url_prefix="/facts")

@bp.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'GET':
    return render_template('facts/index.html')
  if request.method == 'POST':
    print(request.form)
    return redirect('/facts')


  
  
@bp.route('/new', methods=['GET'])
def new():
  return render_template('facts/new.html')
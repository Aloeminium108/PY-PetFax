from flask import ( Blueprint, redirect, render_template, request ) 

bp = Blueprint('facts', __name__, url_prefix="/facts")
  
@bp.route('/new', methods=['POST', 'GET'])
def fact_form():
  if request.method == 'GET':
    return render_template('fact_form.html')
  if request.method == 'POST':
    print(request.form['submitter'])
    return redirect('/pets')
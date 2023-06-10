from flask import ( Blueprint, render_template ) 
import json

bp = Blueprint('pet', __name__, url_prefix="/pets")

pets = json.load(open('pets.json'))

@bp.route('/')
def index():
  return render_template('index.html', pets=enumerate(pets))
  
@bp.route('/<pet_id>')
def show_pet(pet_id: int):
  return render_template('pet_show.html', pet=pets[int(pet_id)])
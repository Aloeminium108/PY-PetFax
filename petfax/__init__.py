from flask import Flask 
from flask_migrate import Migrate

def create_app():

  app = Flask(__name__, template_folder='../templates')

  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/petfax'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  from . import models
  models.db.init_app(app)
  migrate = Migrate(app, models.db)

  from . import pet
  app.register_blueprint(pet.bp)

  from . import facts
  app.register_blueprint(facts.bp)

  @app.route('/')
  def hello(): 
    return 'Hello, PetFax!'

  return app

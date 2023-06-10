from flask import Flask 

def create_app():

  app = Flask(__name__, template_folder='../templates')

  from . import pet
  app.register_blueprint(pet.bp)

  from . import facts
  app.register_blueprint(facts.bp)

  @app.route('/')
  def hello(): 
    return 'Hello, PetFax!'

  return app

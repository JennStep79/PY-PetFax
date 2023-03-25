# imports
from flask import Flask

# application factory function
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, PetFax!'

    # register blueprints
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)


    return app
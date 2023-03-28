# imports
from flask import Flask
from flask_migrate import Migrate


# application factory function
def create_app():
    app = Flask(__name__)

    # db config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4425@localhost:5432/petfax'
    app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def index():
        return 'Hello, PetFax!'

    # register blueprints
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)


    return app
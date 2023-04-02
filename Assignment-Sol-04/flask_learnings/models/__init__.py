from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db  =  SQLAlchemy()             #It have its own init_app .

def init_app(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    return app
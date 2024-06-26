from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from redis import Redis
from flask_migrate import Migrate
from config import Config  

db = SQLAlchemy()
jwt = JWTManager()
redis_client = Redis.from_url(Config.REDIS_URL)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate = Migrate(app, db)

    from app import routes, auth
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)

    return app

from app import models

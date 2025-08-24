from flask import Flask
from .models import db
from .routes.main import main_bp
from .routes.auth import auth_bp
from .routes.questions import q_bp
from .routes.profile import profile_bp

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="change-me",
        SQLALCHEMY_DATABASE_URI="sqlite:///studentoverflow.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(q_bp, url_prefix="/q")
    app.register_blueprint(profile_bp, url_prefix="/u")

    with app.app_context():
        db.create_all()

    return app
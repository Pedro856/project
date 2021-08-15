from flask import Flask, render_template, flash
from flask.blueprints import Blueprint
from flask_sqlalchemy import SQLAlchemy
from models import User
from flask_login import LoginManager, login_manager, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)
main = Blueprint('main', __name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
from app import main as main_blueprint
app.register_blueprint(main_blueprint)

@app.route('/')
def index():
    return render_template('bora.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
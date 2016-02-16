from flask import Flask

app = Flask(__name__)

app.config["DATABASE"] = 'database.db'
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "like I'd tell you"
app.config["USERNAME"] = "root"
app.config["PASSWORD"] = "demo"

from app import views, models


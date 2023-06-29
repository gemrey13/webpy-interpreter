from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173", "methods": ["GET", "POST", "PUT", "DELETE"]}})
db = SQLAlchemy(app)

class Code_Input(db.Model):
    id = db.Column('code_id', db.Integer, primary_key=True)
    content = db.Column(db.String(600), nullable=False)
    input_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return self.content

    def __init__(self, content):
        self.content = content
        utc_now = datetime.utcnow()
        ph = timedelta(hours=8)
        self.input_time = utc_now + ph


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'Hello World'



if __name__ == '__main__':
    app.run(debug=True)
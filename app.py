from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@localhost:5432/monsters_api"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Monsters(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    nature = db.Column(db.String())
    ability = db.Column(db.String())
    attack = db.Column(db.String())

    def __init__(self, name, nature, ability, attack):
        self.name = name
        self.nature = nature
        self.ability = ability
        self.attack = attack


@app.route("/")
def home():
    return {"ayy": "yyo"}


if __name__ == "__main__":
    app.run(debug=True)

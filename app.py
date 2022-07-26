from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:Urawizardsn0w*@localhost:5432/Monster"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Monsters(db.Model):
    __tablename__ = "Monster"

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

    def __repr__(self):
        return f"<Monster {self.name}"


@app.route("/")
def home():
    return {"ayy": "yyo"}


if __name__ == "__main__":
    app.run(debug=True)

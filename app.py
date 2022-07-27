from lzma import MODE_FAST
from re import L
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import db_conn

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://postgres:{db_conn.db_password}@localhost:5432/{db_conn.db_name}"
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


@app.route("/monsters", methods=["POST", "GET"])
def handle_monsters():
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            new_monster = Monsters(
                name=data["name"],
                nature=data["nature"],
                ability=data["ability"],
                attack=data["attack"],
            )
            db.session.add(new_monster)
            db.session.commit()
            return {"message": f" The monster {new_monster.name} has been creatd."}
        else:
            return {"error": "There was an issue creating the monster."}

    elif request.method == "GET":
        monster = Monsters.query.all()
        results = [
            {
                "name": monster.name,
                "nature": monster.nature,
                "ability": monster.ability,
                "attack": monster.attack,
            }
            for monster in Monsters
        ]

        return {"count": len(results), "monsters": results}


@app.route("/monsters/<monster_id>", methods=["GET", "PUT", "DELETE"])
def monster_handler(monster_id):
    monster = Monsters.query.get_or_404(monster_id)

    if request.method == "GET":
        response = {
            "name": monster.name,
            "nature": monster.nature,
            "ability": monster.ability,
            "attack": monster.attack,
        }
        return {"message": "success", "monster": response}

    elif request.method == "PUT":
        data = request.get_json()
        monster.name = data["name"]
        monster.nature = data["nature"]
        monster.ability = data["ability"]
        monster.attack = data["attack"]

        db.session.add(monster)
        db.session.commit()

        return {"message": f"the monster {monster.name} has been updated"}

    elif request.method == "DELETE":
        db.session.delete(car)
        db.session.commit()

        return {"message": f"Monster {monster.name} has been deleted."}


if __name__ == "__main__":
    app.run(debug=True)

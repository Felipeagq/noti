from flask import Blueprint, jsonify
from flask import request
from models.modelos import Notifications
from models.modelos import db


add = Blueprint("add",__name__)

@add.route("/add", methods=["POST"])
def add_route():
    if request.method == "POST":
        json_ = request.get_json()
        id = json_.get("id")
        id_traslado = json_.get("id_traslado")
        date = json_.get("date")
        noti = Notifications(id=id, id_traslado=id_traslado, date=date)
        db.session.add(noti)
        db.session.commit()
        return json_
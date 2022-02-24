from flask import Blueprint, jsonify
from flask import request
from models.modelos import Notifications
from models.modelos import db


read = Blueprint("read",__name__)

@read.route("/read")
def read_route():
    noti = Notifications.query.all()
    notificaciones = []
    for notis in noti:
        agregar = [noti.id, noti.id_traslado, noti.date]
        notificaciones.append(agregar)
        return jsonify({"msg":"ok",
        "notificaciones":notificaciones})
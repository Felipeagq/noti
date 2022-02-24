from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_crontab import Crontab
from dotenv import load_dotenv
from datetime import datetime
#from models import model
#from routes.add_route import add
#from routes.read_route import read

load_dotenv()

app = Flask(__name__)
crontab = Crontab(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


# Creación del modelo de la tabla
class Notifications(db.Model):
    __tablename__ = "NOTIFICATIONS"
    id = db.Column(db.Integer, primary_key=True)
    id_traslado = db.Column(db.Integer)
    date = db.Column(db.Text(10))



## CREAMOS BASE DE DATOS ##
if not os.path.exists("database.db"):
    db.create_all()
    print("-- Base de datos creada --")
else:
    print("-- Base de datos existe --")

#app.register_blueprint(add, url_prefix="/api")
#app.register_blueprint(read, url_prefix="/api")

@app.route("/api/v1/add", methods=["POST"])
def add_route():
    if request.method == "POST":
        json_ = request.get_json()
        id = json_.get("id")
        id_traslado = json_.get("id_traslado")
        date = json_.get("date")
        noti = Notifications(id_traslado=id_traslado, date=date)
        db.session.add(noti)
        db.session.commit()
        print("agregado")
        return json_
    else:
        return jsonify({"msg":"bad method"})


@app.route("/api/v1/read")
def read_route():
    noti = Notifications.query.all()
    notificaciones = []
    for notis in noti:
        agregar = [notis.id,notis.id_traslado, notis.date]
        notificaciones.append(agregar)
        return jsonify({"msg":"ok",
        "notificaciones":notificaciones})

@app.route("/")
def hello_check():
    return jsonify({"version":"v0.0.1",
    "msg":"ok"})


@crontab.job(minute="*")
def do_notification():
    noti = Notifications.query.all()
    ahora = datetime.now()
    ahora_str = f"{ahora.hour}:{ahora.minute}"
    for notis in noti:
        if notis.date == ahora_str:
            print("ENVIO DE NOTIFICACIONES")



if "__main__" == __name__:
    app.run(debug=True,host="0.0.0.0",port=5000)
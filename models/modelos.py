from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
# Creación del modelo de la tabla
class Notifications(db.Model):
    __tablename__ = "NOTIFICATIONS"
    id = db.Column(db.Integer, primary_key=True)
    id_traslado = db.Column(db.Integer)
    date = db.Column(db.Text(10))
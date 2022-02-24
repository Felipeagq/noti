from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


def model(app:Flask) -> None:
    # Creación del Objeto db
    db = SQLAlchemy(app)


    ## CREAMOS BASE DE DATOS ##
    if not os.path.exists("database.db"):
        db.create_all()
        print("-- Base de datos creada --")
    else:
        print("-- Base de datos existe --")

    

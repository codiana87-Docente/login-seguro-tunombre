# app.py  ->  Archivo principal: crea la app y REGISTRA los blueprints
import os
from flask import Flask
from bp_auth import auth_bp
from bp_main import main_bp
from bp_perfil import profile_bp
 
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "clave-secreta-de-clase")   
 
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(profile_bp)
 
if __name__ == "__main__":
    app.run(debug=True)
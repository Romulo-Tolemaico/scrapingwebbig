from flask import Blueprint, jsonify
from models.attModel import AttModel

main = Blueprint('att_blueprint', __name__)

@main.route('/save/<id>')
def guardarInformacion(id):
    try:
        AttModel.guardar_informacion(id)
        return jsonify({'message': 'Información guardada correctamente'}), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

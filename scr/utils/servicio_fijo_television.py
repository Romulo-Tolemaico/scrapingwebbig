import json
import re
import requests
from database import db
import utils.fecha as fec
import utils.convertidor as conv

class Servicio_Fijo_Television():
    @staticmethod
    def almacenar():
        try:
            website = "https://tarifas.att.gob.bo/index.php/tarifaspizarra/tarifasTvcable"
            resultado = requests.get(website)
            content = resultado.text
            match = re.search(r'var\s+dataJSONArray\s*=\s*JSON\.parse\(\'(.*?)\'\);', content)
            if match:
                json_data = match.group(1)
                data = json.loads(json_data)
                conn = db.get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM sf_television;")
                conn.commit()
                for servicio in data:
                    cursor.execute("""
                        INSERT INTO sf_television (
                            nombre_comercial, razon_social, departamento, nombre_tarifa_plan,
                            costo_instalacion, precio_mensual, cantidad_canales_digitales,
                            cantidad_canales_analogicos, denominacion_tecnologia, tipo_pago,
                            tarifa_punto_adicional, observaciones, fecha_create
                        ) VALUES (
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                        )
                    """, (
                        servicio.get('NOMBRE_COMERCIAL', ''),
                        servicio.get('RAZON_SOCIAL', ''),
                        servicio.get('DEPARTAMENTO', ''),
                        servicio.get('NOMBRE_TARIFA_PLAN', ''),
                        conv.numeroFlotante(servicio.get('COSTO_INSTALACION', "0")),
                        conv.numeroFlotante(servicio.get('PRECIO_MENSUAL', "0")),
                        conv.numeroEntero(servicio.get('CANTIDAD_CANALES_DIGITALES', "0")),
                        conv.numeroEntero(servicio.get('CANTIDAD_CANALES_ANALOGICOS', "0")),
                        servicio.get('DENOMINACION_TECNOLOGIA', ''),
                        servicio.get('TIPO_PAGO', ''),
                        conv.numeroFlotante(servicio.get('TARIFA_PUNTO_ADICIONAL', "0")),
                        servicio.get('OBSERVACIONES', None),
                        fec.generar_fecha_aleatoria()
                    ))
                    conn.commit()
        except requests.RequestException as ex:
            print("Error durante la solicitud HTTP:", ex)
        finally:
            conn.close()


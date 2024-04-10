import json
import re
import requests
from database import db
import utils.fecha as fec
import utils.convertidor as conv

class Servicio_Fijo_Internet():
    @staticmethod
    def almacenar():
        try:
            website = "https://tarifas.att.gob.bo/index.php/tarifaspizarra/tarifasInternetFijo"
            resultado = requests.get(website)
            content = resultado.text
            match = re.search(r'var\s+dataJSONArray\s*=\s*JSON\.parse\(\'(.*?)\'\);', content)
            if match:
                json_data = match.group(1)
                data = json.loads(json_data)
                conn = db.get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM sf_internet;")
                conn.commit()
                for servicio in data:
                    cursor.execute("""
                        INSERT INTO sf_internet (
                            razon_social, nombre_comercial, costo_instalacion, 
                            tipo_pago, otros_beneficios, nombre_tarifa_plan, ancho_banda_bajada, precio_mensual, 
                            ancho_banda_subida, denominacion_tecnologia,departamento, fecha_create
                        ) VALUES (
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                        )
                    """, (
                        servicio.get('RAZON_SOCIAL', ''),
                        servicio.get('NOMBRE_COMERCIAL', ''),
                        conv.numeroFlotante(servicio.get('COSTO_INSTALACION', "0")),
                        servicio.get('TIPO_PAGO', ''),
                        servicio.get('OTROS_BENEFICIOS', None),
                        servicio.get('NOMBRE_TARIFA_PLAN', ''),
                        conv.numeroEntero(servicio.get('ANCHO_BANDA_BAJADA', "0")),
                        conv.numeroFlotante(servicio.get('PRECIO_MENSUAL', "0")),
                        conv.numeroEntero(servicio.get('ANCHO_BANDA_SUBIDA', "0")),
                        servicio.get('DENOMINACION_TECNOLOGIA', ''),
                        servicio.get('DEPARTAMENTO', ''),
                        fec.generar_fecha_aleatoria()
                    ))
                    conn.commit()
        except requests.RequestException as ex:
            print("Error durante la solicitud HTTP:", ex)
        finally:
            conn.close()


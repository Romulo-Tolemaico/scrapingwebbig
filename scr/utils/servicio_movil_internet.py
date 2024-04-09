import json
import re
import requests
from database import db
import utils.fecha as fec

class Servicio_Movil_Internet():
    @staticmethod
    def almacenar():
        conn = db.get_connection()
        try:
            print("Iniciando almacenamiento de datos...")
            website = "https://tarifas.att.gob.bo/index.php/tarifaspizarra/tarifasInternetMovil"
            resultado = requests.get(website)
            print("Solicitud HTTP completada con éxito.")
            content = resultado.text
            match = re.search(r'var\s+dataJSONArray\s*=\s*JSON\.parse\(\'(.*?)\'\);', content)
            if match:
                json_data = match.group(1)
                data = json.loads(json_data)
                print("Datos JSON cargados exitosamente.")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM sm_internet;")
                conn.commit()
                for servicio in data:
                    cursor.execute("""
                        INSERT INTO sm_internet (nombre, precio, modalidad_pago, fecha_create, operador, tipo_conexion, mb, minutos, vigencia, ud_vigencia)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        servicio.get("NOMBRE_TARIFA_PLAN", ""),
                        float(servicio.get("PRECIO_MENSUAL", 0)),
                        servicio.get("TIPO_PAGO", ""),
                        fec.generar_fecha_aleatoria(),  
                        servicio.get("RAZON_SOCIAL", ""),
                        servicio.get("DENOMINACION_TECNOLOGIA", ""),
                        int(float(servicio.get("MB_DISPONIBLES", 0) or 0)),
                        int(float(servicio.get("MINUTOS_COMBOS", 0) or 0)), 
                        int(float(servicio.get("VIGENCIA_BOLSA", 0) or 0)),  
                        servicio.get("UNIDAD_VIGENCIA_BOLSA", ""),  
                    ))
                    print("Datos insertados correctamente en la tabla.")
                    conn.commit()
        except requests.RequestException as ex:
            print("Error durante la solicitud HTTP:", ex)
        except Exception as ex:
            print("Error inesperado:", ex)
        finally:
            conn.close()



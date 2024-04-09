import json
import re
import requests
from database import db
import utils.fecha as fec
import utils.convertidor as conv

class Servicio_Movil_Prepago():
    @staticmethod
    def almacenar():
        conn = db.get_connection()
        try:
            website = "https://tarifas.att.gob.bo/index.php/tarifaspizarra/tarifasServicioMovilPrepago"
            resultado = requests.get(website)
            content = resultado.text
            match = re.search(r'var\s+dataJSONArray\s*=\s*JSON\.parse\(\'(.*?)\'\);', content)
            if match:
                json_data = match.group(1)
                data = json.loads(json_data)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM sm_prepago;")
                conn.commit()
                for servicio in data:
                    cursor.execute("""
                        INSERT INTO sm_prepago (
                            nombre_comercial, precio_mensual, nombre_tarifa_plan,
                            tarifa_normal, tarifa_reducida, tarifa_super_reducida, sms_libres,
                            tarifa_sms_adicional, mb_disponibles, precio_mb_adicional,
                            fecha_create
                        ) VALUES (
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                        )
                    """, (
                        servicio.get("NOMBRE_COMERCIAL", ""),
                        conv.numeroFlotante(servicio.get("PRECIO_MENSUAL", "0")),
                        servicio.get("NOMBRE_TARIFA_PLAN", ""),
                        conv.numeroFlotante(servicio.get("TARIFA_NORMAL", "0")),
                        conv.numeroFlotante(servicio.get("TARIFA_REDUCIDA", "0")),
                        conv.numeroFlotante(servicio.get("TARIFA_SUPER_REDUCIDA", "0")),
                        conv.numeroEntero(servicio.get("SMS_LIBRES", 0)),
                        conv.numeroFlotante(servicio.get("TARIFA_SMS_ADICIONAL", "0")),
                        conv.numeroEntero(servicio.get("MB_DISPONIBLES", 0)),
                        conv.numeroFlotante(servicio.get("PRECIO_MB_ADICIONAL", "0")),
                        fec.generar_fecha_aleatoria()
                    ))
                    conn.commit()
        except requests.RequestException as ex:
            print("Error durante la solicitud HTTP:", ex)
        finally:
            conn.close()


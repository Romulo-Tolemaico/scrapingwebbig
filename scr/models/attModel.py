from utils.servicio_movil_internet import Servicio_Movil_Internet
from utils.servicio_movil_prepago import Servicio_Movil_Prepago
from utils.servicio_fijo_internet import Servicio_Fijo_Internet
from utils.servicio_fijo_television import Servicio_Fijo_Television
class AttModel():
    @classmethod
    def guardar_informacion(self,id):
        try:
            id = int(id)
            if id == 1:
                Servicio_Movil_Internet.almacenar()
            elif id == 2:
                Servicio_Movil_Prepago.almacenar()
            elif id == 3:
                Servicio_Fijo_Internet.almacenar()
            elif id == 4:
                Servicio_Fijo_Television.almacenar()
            else:
                print("Error")
        except Exception as ex:
            raise Exception(ex)

import random as rd

def numeroFlotante(dato):
    dato = str(dato).replace(',', '.')
    try:
        return float(dato)
    except ValueError as ex:
        return rd.uniform(1,500)
    
def numeroEntero(dato):
    try:
        return int(dato)
    except ValueError:
        return rd.randint(1,500)

def numeroFlotante(dato):
    dato = str(dato).replace(',', '.')
    try:
        return float(dato)
    except ValueError as ex:
        return 0.0
    
def numeroEntero(dato):
    try:
        return int(dato)
    except ValueError:
        return 0

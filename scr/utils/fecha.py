import random
from datetime import datetime, timedelta

def generar_fecha_aleatoria():
    inicio = datetime(2021, 1, 1)
    fin = datetime(2023, 12, 31)
    diferencia = fin - inicio
    dias_aleatorios = random.randint(0, diferencia.days)
    fecha_aleatoria = inicio + timedelta(days=dias_aleatorios)

    return fecha_aleatoria


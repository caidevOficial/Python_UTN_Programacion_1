from datetime import datetime

def test_sort(callback, *args, **kwargs):
    inicio = datetime.now()
    lista = callback(*args)
    fin = datetime.now()

    # Calcular la diferencia
    diferencia = fin - inicio
    # Obtener minutos, segundos y milisegundos
    minutos = diferencia.seconds // 60
    segundos = diferencia.seconds % 60
    milisegundos = diferencia.microseconds // 1000
    print(f'\n{kwargs.get('sort_name')}: ', lista[:20])
    print(f"{kwargs.get('sort_name')}: {minutos} minutos, {segundos} segundos, {milisegundos} milisegundos")
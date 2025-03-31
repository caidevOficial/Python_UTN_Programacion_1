movimientos = {
    "movimientos": 0
}

def torre_de_hanoi(mov: dict, cant_discos: int, nombre_torre_origen: str, 
                   nombre_torre_destino: str, nombre_torre_aux: str) -> None:
    
    texto =\
f"""
        ------------------------------
        Origen: {nombre_torre_origen}
        Disco en Origen: {cant_discos}
        Destino: {nombre_torre_destino}
        AUX: {nombre_torre_aux}
        -------------------------
"""
    print(texto)
    
    if cant_discos == 1:
        print(f'Se movio el disco 1 desde {nombre_torre_origen} a {nombre_torre_destino}')
        mov['movimientos'] += 1
    else:
        torre_de_hanoi(mov, cant_discos - 1, nombre_torre_origen, nombre_torre_aux, nombre_torre_destino)
        mov['movimientos'] += 1
        print(f'Se movio el disco {cant_discos} desde {nombre_torre_origen} a {nombre_torre_destino}')
        torre_de_hanoi(mov, cant_discos - 1, nombre_torre_aux, nombre_torre_destino, nombre_torre_origen)
        mov['movimientos'] += 1

torre_de_hanoi(movimientos, 7, "Torre 1", "Torre 2", "Torreón 3")
print(f'Movimientos: {movimientos["movimientos"]}')
def reconocer_cadena(cadena,alfabeto,edo_actual,edos_aceptores,tabla_transicion):
    for car in cadena:
        fila=tabla_transicion[edo_actual]
        indice=alfabeto.index(car)
        edo_actual=fila[indice]

    if edo_actual in edos_aceptores:
        return True
    else:
        return False
def reconocer_cadena(cadena,alfabeto,edo_actual,edos_aceptores,tabla_transicion):

    for car in cadena:
        fila=tabla_transicion[edo_actual]
        indice=alfabeto.index(car)
        if isinstance(fila[indice],str):
            edo_actual=fila[indice]
        else:
            edo_actual=fila[indice][0]

    if edo_actual in edos_aceptores:
        return True
    else:
        return False
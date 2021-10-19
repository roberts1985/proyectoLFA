'''Este módulo sirve para convertir un Autómata Finito No Determinístico en un Autómata Finito Determinístico'''

def obtener_binario(numero,cantidad_estados):
    n=bin(numero).replace("0b","")
    dif=cantidad_estados-len(n)
    cad="0"*dif

    return cad+n

def obtener_combinaciones_estados(estados):
    cantidad_estados = len(estados)
    potencia=2**cantidad_estados
    lista_combinaciones_estados=[]

    for i in range(1,potencia):
        binario=obtener_binario(i,cantidad_estados)
        indice=0
        combinacion=[]
        for ele in binario:
            if ele!='0':
                estado=estados[indice]
                combinacion.append(estado)
            indice+=1
        lista_combinaciones_estados.append(tuple(combinacion))

    return lista_combinaciones_estados

def recorre_recursivo_tablaAFD(lista,tablaAFD_final,tabla_AFD):
    for e in lista:
        if e not in tablaAFD_final and e!=():
            tablaAFD_final[e]=tabla_AFD[e]
            recorre_recursivo_tablaAFD(tabla_AFD[e],tablaAFD_final,tabla_AFD)

def obtener_AFD(edo_inicial,lista_combinaciones_estados,alfabeto,tabla_transiciones_afn):
    tabla_AFD={}

    for estado in lista_combinaciones_estados:
        fila=crear_fila_tablaAFD(estado,alfabeto,tabla_transiciones_afn)
        tabla_AFD[tuple(estado)]=fila

    tablaAFD_final={}
    tablaAFD_final[tuple(edo_inicial)]=tabla_AFD[tuple(edo_inicial)]
    recorre_recursivo_tablaAFD(tabla_AFD[tuple(edo_inicial)],tablaAFD_final,tabla_AFD)

    return tablaAFD_final

def crear_fila_tablaAFD(estado,alfabeto,tabla_transiciones_afn):
    fila=[]

    for a in alfabeto:
        col=[]
        indice=alfabeto.index(a)
        for e in estado:
            elemento=tabla_transiciones_afn[e][indice]
            if elemento != ('',) and elemento!='':
                col.extend(list(elemento))
        c=list(set(col))
        c.sort()
        fila.append(tuple(c))

    return fila

def devolver_estados_aceptoresAFD(claves,estados_aceptores):
    con=set()
    for edo in estados_aceptores:
        for c in claves:
            if edo in c:
                con.add(c)
                
    return con

def mapear_AFD(tablaAFD,edo_inicial,edos_aceptores):
    dicc_aux={}
    dicc_aux2={}
    con=0
    for clave in tablaAFD.keys():
        cadena="C"+str(con)
        dicc_aux2[clave]=cadena
        dicc_aux[clave]=tuple(cadena.split(" "))
        con+=1

    tablaAFD_mapeada = mapear(tablaAFD,dicc_aux,dicc_aux2)

    estados_aceptores=[]
    for e in edos_aceptores:
        estados_aceptores.append(dicc_aux2[e])

    return tablaAFD_mapeada, dicc_aux2[edo_inicial], estados_aceptores

def mapear(tablaAFD,dicc_aux,dicc_aux2):
    tablaAFD_mapeada_graficador = {}

    for clave, valor in tablaAFD.items():
        lista = []
        for v in valor:
            if v != ():
                lista.append(dicc_aux[v])
            else:
                lista.append(tuple())
        tablaAFD_mapeada_graficador[dicc_aux2[clave]] = lista

    return tablaAFD_mapeada_graficador

def convertir_AFN_a_AFD(estados,alfabeto,estado_inicial,estados_aceptores,tabla_transiciones):
    edo_inicial = estado_inicial.split(" ")
    alfabeto.sort()
    tabla_transiciones_afn = tabla_transiciones
    lista_combinaciones_estados = obtener_combinaciones_estados(estados)
    resultado = obtener_AFD(edo_inicial,lista_combinaciones_estados,alfabeto,tabla_transiciones_afn)
    edos_aceptores = devolver_estados_aceptoresAFD(resultado.keys(), estados_aceptores)
    tablaAFD, edo_inicial, edos_aceptores = mapear_AFD(resultado, tuple(edo_inicial),edos_aceptores)

    #return tablaAFD_graficador, tablaAFD_reconocedor, alfabeto, edo_inicial, edos_aceptores
    return tablaAFD, list(tablaAFD.keys()),alfabeto, edo_inicial, edos_aceptores
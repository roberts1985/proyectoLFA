from os import system

def archivo_graphviz(alfabeto, estados, edo_inicial, edos_aceptores, tabla_transicion,archivodot): #Cambiar nombre a original archivo_graphviz
    ccomas = 1
    Lista=[]
    num_edos_aceptores = len(edos_aceptores)
    archivopng=str(archivodot).replace(".dot",".png")
    archivo = open(archivodot, "w")
    archivo.write("digraph g{\nrankdir=\"LR\";\nsize=\"5,7;\"")
    archivo.write("\nnode [shape = point, color=white, fontcolor=white]; start;")
    archivo.write(
        "\nnode [shape = doublecircle, color=black, fontcolor=black] ")  # Empezamos a listar los estados de aceptacion
    for i in edos_aceptores:
        archivo.write(str(i))
        if ccomas < num_edos_aceptores:  # Esto es solo para que después del último estado no se imprima una coma de más
            archivo.write(",")
            ccomas += 1;
    archivo.write("\nnode [shape = circle];start->")  # Esta línea y la siguiente ponen en el archivo el estado inicial
    archivo.write(str(edo_inicial))
    archivo.write("\n")
    for clave, valor in tabla_transicion.items():  # Recorremos toda la tabla de transición para mandarla al archivo
        ind = 0
        ind2=0
        for i in alfabeto:
            Lista=valor[ind]     #Almacenamos cada elemento de la tupla en una lista
            for j in range (len(Lista)):
                if Lista[ind2]!=() and Lista[ind2]!='':
                    archivo.write(str(clave))
                    archivo.write("->")
                    archivo.write(str(Lista[ind2]))

                    archivo.write("[label=\" ")
                    archivo.write(str(i))
                    archivo.write(" \"];\n")
                    ind2+=1
            ind += 1
            ind2=0
    archivo.write("\n}")
    archivo.close()
    archivodot=str(archivodot).replace(' ','\ ')
    archivopng=str(archivopng).replace(' ','\ ')
    print("Construyendo imagen en: "+archivopng)
    generar_imagen="dot -Tpng "+archivodot+" > "+archivopng
    system(generar_imagen)
'''Este archivo es de prueba, primero importamos el paquete automatas y sus módulos y'''
from Pythomatas import *

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def imprimir_mensaje(tipo):
     root = tk.Tk()
     root.withdraw()
     if tipo==1:
         messagebox.showinfo(message="¡Elige un nombre para tu AFN!", title="Atención")
     else:
         messagebox.showinfo(message="¡Elige un nombre para tu AFD!", title="Atención")
     root.destroy()

def select_save_path(): #Creo que esto se va a dibuja_automata_graphviz
    root = tk.Tk()
    root.withdraw()
    path =  filedialog.asksaveasfile(mode='a',title="Guardar archivo DOT", defaultextension=".dot",filetypes=(("DOT files", "*.dot"),)).name
    root.destroy()
    return (path)

def menu():
    print("1.- AFD")
    print("2.- AFN")
    print("3.- Salir")
    opcion=input("Escribe una opción: ")

    return opcion

def obtener_datos_afn():
    '''Esta función sirve para obtener los datos (estados, alfabeto, edo. inicial, edos. aceptores,
    tabla de transiciones) del AFN (Autómata Finito No determinístico) que se convertirá en AFD.
    Devuelve una tupla de 5 elementos:
        pos 0 de la tupla, es una lista que contiene los estados del AFN
        pos 1 de la tupla, es una lista que contiene el alfabeto del AFN
        pos 2 de la tupla, es una cadena que contiene el estado inicial del AFN
        pos 3 de la tupla, es una lista que contiene los estados aceptores del AFN
        pos 4 de la tupla, es un diccionario que contiene la tabla de transiciones del AFN'''
    estados = input("Introduce los estados (separados por espacios): ").split(" ")
    alfabeto = input("Introduce el alfabeto (separados por espacios): ").split(" ")
    estado_inicial = input("Introduce el estado inicial: ")
    estados_aceptores=input("Introduce el/los estado(s) aceptor(es) (separados por espacios): ").split(" ")
    tabla={}

    for edo in estados:
        fila=[]
        for a in alfabeto:
            col=input(f"Introduce la transición de {edo} con {a} (separa con espacios si hay más de un edo. por transición): ").split(" ")
            fila.append(tuple(set(col)))
        tabla[edo]=fila

    return estados,alfabeto,estado_inicial,estados_aceptores,tabla

def obtener_datos_afd():
    '''
    Devuelve una tupla de 5 elementos:
        pos 0 de la tupla, es una lista que contiene los estados del AFN
        pos 1 de la tupla, es una lista que contiene el alfabeto del AFN
        pos 2 de la tupla, es una cadena que contiene el estado inicial del AFN
        pos 3 de la tupla, es una lista que contiene los estados aceptores del AFN
        pos 4 de la tupla, es un diccionario que contiene la tabla de transiciones del AFN'''
    estados = input("Introduce los estados (separados por espacios): ").split(" ")
    alfabeto = input("Introduce el alfabeto (separados por espacios): ").split(" ")
    estado_inicial = input("Introduce el estado inicial: ")
    estados_aceptores=input("Introduce el/los estado(s) aceptor(es) (separados por espacios): ").split(" ")
    tabla={}

    for edo in estados:
        fila=[]
        for a in alfabeto:
            col=input(f"Introduce la transición de {edo} con {a}: ")
            fila.append(col)
        tabla[edo]=fila

    return estados,alfabeto,estado_inicial,estados_aceptores,tabla

if __name__=="__main__":
    ban=True
    while ban:
        opc=int(menu())
        if opc==1:
            estados, alfabeto, estado_inicial, estados_aceptores, tabla = obtener_datos_afd()
            imprimir_mensaje(2)
            archivodot = select_save_path()

            print("archivodot")
            print(archivodot)

            dibuja_automata_graphviz.archivo_graphviz(alfabeto, estados, estado_inicial, estados_aceptores, tabla, archivodot)
            cadena = input("Escribe la cadena a analizar: ")
            res=reconocedor.reconocer_cadena(cadena, alfabeto, estado_inicial, estados_aceptores, tabla)
            if res==True:
                print("Cadena aceptada...")
            else:
                print("Cadena no aceptada...")
        elif opc==2:
            estados,alfabeto,estado_inicial,estados_aceptores,tabla=obtener_datos_afn()
            imprimir_mensaje(1)
            archivodot=select_save_path()
            dibuja_automata_graphviz.archivo_graphviz(alfabeto, estados, estado_inicial, estados_aceptores, tabla,archivodot)
            tablaAFD, estadosAFD, alfabeto, edo_inicial, edos_aceptores = AFN_a_AFD.convertir_AFN_a_AFD(estados, alfabeto, estado_inicial,
                                                                                   estados_aceptores, tabla)
            imprimir_mensaje(2)
            archivodot=select_save_path()
            dibuja_automata_graphviz.archivo_graphviz(alfabeto, estadosAFD, edo_inicial, edos_aceptores, tablaAFD,archivodot)
            cadena = input("Escribe la cadena a analizar: ")
            res=reconocedor.reconocer_cadena(cadena, alfabeto, edo_inicial, edos_aceptores, tablaAFD)
            if res==True:
                print("Cadena aceptada...")
            else:
                print("Cadena no aceptada...")
        elif opc==3:
            ban=False
        else:
            print("Opción incorrecta...")

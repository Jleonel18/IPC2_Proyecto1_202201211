import xml.etree.ElementTree as ET
from lista_enlazada.lista_datos import lista_datos
from lista_enlazada.dato import dato

lista = lista_datos

def leerXML():

    print('')
    print('')
    print('Escriba el nombre y extension del archivo')
    ruta = input()



    tree  = ET.parse(ruta)
    root = tree.getroot()            
        
    for i in root.findall('senal'):

        contador = 0
        validar_tiempo_senal(i.get('t'))
        validar_amplitud_senal(i.get('A'))
        tiempo_dato = 0
        amplitud_dato = 0
        dato_binario = 0

        for j in i.findall('dato'):

            if validar_tiempo_dato(j.get('t'),i.get('t')) == True:
                tiempo_dato = j.get('t')
            if validar_amplitud_dato(j.get('A'),i.get('A')) == True:
                amplitud_dato = j.get('A')

            if int(j.text) !=0:
                dato_binario = 1
            else:
                dato_binario = 0
            
            nuevo = dato(int(j.text),int(tiempo_dato),int(amplitud_dato),i.text,dato_binario)
            lista.agregar_ultimo(nuevo)
            contador +=1
            
        if contador < int(i.get('t'))*int(i.get('A')):
            while contador < int(i.get('t'))*int(i.get('A')):
                print('Faltaba aqui una linea')
                contador+=1
                

def validar_tiempo_senal(tiempo):
    if int(tiempo) > 0 and int(tiempo)<=3600:
        return True
    else:
        return False

def validar_amplitud_senal(amplitud):
    if int(amplitud) > 0 and int(amplitud)<=130:
        return True
    else:
        return False

def validar_tiempo_dato(tiempo_dato,tiempo_senal):
    if int(tiempo_dato) > int(tiempo_senal):
        return False
    else:
        return True

def validar_amplitud_dato(amplitud_dato, amplitud_senal):
    if int(amplitud_dato) > int(amplitud_senal):
        return False
    else:
        return True


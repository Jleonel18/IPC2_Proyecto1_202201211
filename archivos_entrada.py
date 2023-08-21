import xml.etree.ElementTree as ET
from lista_enlazada.lista_datos import lista_datos
from lista_enlazada.lista_senal import lista_senal
from lista_enlazada.dato import dato
from lista_enlazada.senal import senal

class archivos_entrada():

    def __init__(self):
        self.archivo = ''

    lista = lista_datos()
    lista_senal = lista_senal()

    def leerXML(self):

        tree  = ET.parse(self.archivo)
        root = tree.getroot()            
            
        for i in root.findall('senal'):

            contador = 0
            self.validar_tiempo_senal(i.get('t'))
            self.validar_amplitud_senal(i.get('A'))
            tiempo_dato = 0
            amplitud_dato = 0
            dato_binario = 0

            for j in i.findall('dato'):

                if (self.validar_tiempo_dato(j.get('t'),i.get('t')) == True) and (self.validar_amplitud_dato(j.get('A'),i.get('A')) == True):
                    tiempo_dato = j.get('t')
                    amplitud_dato = j.get('A')

                    if int(j.text) != 0:
                        dato_binario = 1
                    else:
                        dato_binario = 0
                
                    nuevo = dato(int(j.text),int(tiempo_dato),int(amplitud_dato),i.get('nombre'),dato_binario)
                    self.lista.agregar_ultimo(nuevo)
                contador +=1
                
            if contador < int(i.get('t'))*int(i.get('A')):
                while contador < int(i.get('t'))*int(i.get('A')):
                    nuevo = dato(0,int(tiempo_dato),int(amplitud_dato),i.get('nombre'),0)
                    self.lista.agregar_ultimo(nuevo)
                    contador+=1
            nueva_senal = senal(i.get('nombre'),int(i.get('t')),int(i.get('A')))
            self.lista_senal.agregar_ultimo(nueva_senal)
        
        self.lista.recorrido()
        print('=============================')
        self.lista_senal.recorrido()

    def cargarXML(self):
        print('')
        print('')
        print('Escriba el nombre del archvio:')
        self.archivo = input()          

    def validar_tiempo_senal(self,tiempo):
        if int(tiempo) > 0 and int(tiempo)<=3600:
            return True
        else:
            return False

    def validar_amplitud_senal(self,amplitud):
        if int(amplitud) > 0 and int(amplitud)<=130:
            return True
        else:
            return False

    def validar_tiempo_dato(self,tiempo_dato,tiempo_senal):
        if int(tiempo_dato) > int(tiempo_senal):
            return False
        else:
            return True

    def validar_amplitud_dato(self,amplitud_dato, amplitud_senal):
        if int(amplitud_dato) > int(amplitud_senal):
            return False
        else:
            return True


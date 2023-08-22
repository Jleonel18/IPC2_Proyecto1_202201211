import xml.etree.ElementTree as ET
from lista_enlazada.lista_datos import lista_datos
from lista_enlazada.lista_senal import lista_senal
from lista_enlazada.dato import dato
from lista_enlazada.senal import senal

class archivos_entrada():

    def __init__(self):
        self.archivo = ''

    lista_senales = lista_senal()


    def leerXML(self):



        tree  = ET.parse(self.archivo)
        root = tree.getroot()            
            
        for i in root.findall('senal'):

            lista = lista_datos()

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
                    print("Los datos ingresados son:",int(j.text),int(tiempo_dato),int(amplitud_dato),i.get('nombre'),dato_binario)
                    nuevo = dato(int(j.text),int(tiempo_dato),int(amplitud_dato),i.get('nombre'),dato_binario)
                    lista.agregar_ultimo(nuevo)
                contador +=1
                
            """if contador < int(i.get('t'))*int(i.get('A')):
                while contador < int(i.get('t'))*int(i.get('A')):
                    nuevo = dato(0,int(tiempo_dato),int(amplitud_dato),i.get('nombre'),0)
                    lista.agregar_ultimo(nuevo)
                    contador+=1"""
                
            valor_t = i.get('t')
            valor_a = i.get('A')
            coordenadas_existen = set((dato.get('t'),dato.get('A')) for dato in i.findall('dato'))

            for cont1 in range(1,int(valor_t)+1):
                for cont2 in range(1,int(valor_a)+1):
                    coordenada = (str(cont1),str(cont2))
                    if coordenada not in coordenadas_existen:
                        print("senal:",i.get('nombre'))
                        print("Falta un dato en tiempo:",str(cont1),"y amplitud:",str(cont2))
                        nuevo_dato = dato(0,int(cont1),int(cont2),i.get('nombre'),0)
                        lista.agregar_ultimo(nuevo_dato)

            nueva_senal = senal(i.get('nombre'),int(i.get('t')),int(i.get('A')),lista)
            self.lista_senales.agregar_ultimo(nueva_senal)

        print('=============================')
        self.lista_senales.recorrido()

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
    
    def seleccionar_senal(self):
        print("")
        print("")
        print("Escriba el nombre se la senal que desea imprimir grafica")
        senal_seleccionada = input()
        if(self.lista_senales.buscar_senal(senal_seleccionada) != ""):
            print("")
            print("")
            print("Seleccione 1 si desea graficar la matriz normal")
            print("Seleccione 2 si desea graficar la matriz binaria")
            print("Seleccione 3 si desea graficar la matriz reducida")
            seleccion_matriz = input()

            print("")
            print("")

            if seleccion_matriz == "1":
                self.lista_senales.grafica_lista_normal(senal_seleccionada)
            elif seleccion_matriz == "2":
                self.lista_senales.grafica_lista_binaria(senal_seleccionada)
            elif seleccion_matriz == "3":
                pass
            else: 
                print("Opcion no valida")
        else:
            print("No existe una senal con ese nombre")


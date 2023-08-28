from lista_enlazada.nodo_senal import nodo_senal
from lista_enlazada.grupo import grupo
from lista_enlazada.lista_matriz_suma import lista_matriz_suma
from lista_enlazada.matriz_suma import matriz_suma
import xml.etree.ElementTree as ET

class lista_senal():

    def __init__(self):
        self.primero = None
        self.size = 0

    def vacia(self):
        return self.primero == None
    
    def agregar_ultimo(self, dato):
        new_nodo = nodo_senal(dato)
        if self.size == 0 or(new_nodo.senal.tiempo, new_nodo.senal.amplitud) < (self.primero.senal.tiempo, self.primero.senal.amplitud):

            new_nodo.siguiente = self.primero
            self.primero = new_nodo
        
        else:
            aux = self.primero
            while aux.siguiente is not None and (aux.siguiente.senal.tiempo, aux.siguiente.senal.amplitud) <= (new_nodo.senal.tiempo, new_nodo.senal.amplitud):
                aux = aux.siguiente
            new_nodo.siguiente = aux.siguiente
            aux.siguiente = new_nodo
        self.size+=1
    
    def recorrido(self):
        aux = self.primero
        while aux != None:
            print("senal:",aux.senal.senal,"tiempo:",aux.senal.tiempo,"amplitud:",aux.senal.amplitud,
                "\ndatos:")
            aux.senal.lista_datos.recorrido()
            aux = aux.siguiente
            print("=========================================")

    def buscar_nombre_senal(self,nombre_senal):
        aux = self.primero
        bandera = False
        while aux != None:
            if aux.senal.senal == nombre_senal:
                bandera = True
                break
            aux = aux.siguiente

        return bandera

    def buscar_senal(self,senal_buscada):
        aux = self.primero
        bandera = False
        while aux != None:
            if(aux.senal.senal == senal_buscada):
                bandera = True
                break
            aux = aux.siguiente

        if bandera == True:
            return aux.senal
        else:
            return ""
    
    def verificar_tamano(self):
        return self.size
    
    def grafica_lista_normal(self,nombre_senal):
        actual = self.primero
            
        while actual != None:
            if actual.senal.senal == nombre_senal:
                
                actual.senal.lista_datos.generar_grafica(actual.senal.senal, str(actual.senal.tiempo), str(actual.senal.amplitud))
                break
            actual = actual.siguiente

    def grafica_lista_binaria(self,nombre_senal):
        actual = self.primero

        while actual != None:
            if actual.senal.senal == nombre_senal:
                actual.senal.lista_datos.generar_grafica_binaria(actual.senal.senal,str(actual.senal.tiempo), str(actual.senal.amplitud))
                break
            actual = actual.siguiente
    
    def eliminar_senal(self,nombre_senal):
        nodoActual = self.primero
        nodoAnterior = None

        while (nodoActual != None) and (nodoActual.senal.senal != nombre_senal):
            nodoAnterior = nodoActual
            nodoActual = nodoActual.siguiente

        if nodoActual is None:
            return
        
        if nodoAnterior is None:
            self.primero = self.primero.siguiente
        else:
            nodoAnterior.siguiente = nodoActual.siguiente
        
        self.size-=1
    
    def calcular_patrones(self,nombre_senal,suma):
        actual = self.primero
        
        while actual != None:
            if actual.senal.senal == nombre_senal:
                actual.senal.lista_patrones =  actual.senal.lista_datos.devolver_patrones_por_tiempo(actual.senal.lista_patrones)

                lista_patrones_temporal = actual.senal.lista_patrones
                grupos_sin_analizar = lista_patrones_temporal.encontrar_coincidencias()

                buffer = ""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito == "-" and buffer!="":
                        cadena_grupo = actual.senal.lista_datos.devolver_cadena_del_grupo(buffer)
                        actual.senal.lista_grupos.insertar_dato(grupo = grupo(buffer,cadena_grupo,actual.senal.lista_grupos.get_size()))
                        self.sumar_lista(actual.senal.lista_datos,actual.senal.amplitud,buffer,actual.senal.lista_grupos.get_size(),suma)
                        buffer=""
                    else:
                        buffer=""
                #actual.senal.lista_grupos.recorrer_e_imprimir_lista()

                return
            
            actual = actual.siguiente
        print("no se encontro la senal")

    def sumar_lista(self, lista_datos, amplitud, grupo,cantidad_grupo,lista):
        suma_datos = 0
        contador = 0
        string_resultado = ""
        tiempo_sin_comas = grupo.replace(",","")
        for i in range(1, int(amplitud)+1):
            for datos_leidos in lista_datos:
                
                if str(datos_leidos.dato.tiempo) in grupo and int(datos_leidos.dato.amplitud) == i:
                    suma_datos = suma_datos + int(datos_leidos.dato.dato)
                    contador += 1
                    if contador == len(tiempo_sin_comas):
                        string_resultado+=str(suma_datos)+","
                        lista.insertar_dato(matriz_suma(datos_leidos.dato.tiempo,datos_leidos.dato.amplitud,suma_datos,cantidad_grupo))

            contador = 0
            suma_datos = 0
    
    def lista_temporal(self,lista,nombre):
        aux = self.primero
        while aux != None:
            if aux.senal.senal == nombre:
                aux.senal.lista_matriz_suma = lista
                return
            aux = aux.siguiente

    def crear_xml(self,nombre_archivo):
        senales_reducidas =  ET.Element("Senales-reducidas")
        aux = self.primero

        while aux != None:
            senal_reducida = ET.SubElement(senales_reducidas,"senal",nombre_archivo=f'{aux.senal.senal}',A=f'{aux.senal.amplitud}')
            almacen = aux.senal.lista_grupos

            for al in almacen:
                grupo = ET.SubElement(senal_reducida,"grupo",grupo=f'{al.grupo.veces_ingresada}')
                tiempo = ET.SubElement(grupo,"tiempos")
                tiempo.text = al.grupo.el_grupo

                datos_grupal = ET.SubElement(grupo,"datosGrupo")
                datos_grupos = aux.senal.lista_matriz_suma

                for i in datos_grupos:
                    if i.dato.grupo == al.grupo.veces_ingresada:
                        dato = ET.SubElement(datos_grupal,"dato",A=f"{i.dato.amplitud}")
                        dato.text = str(i.dato.valor)

            aux = aux.siguiente
        
        self.ordenar_xml(senales_reducidas)
        tree = ET.ElementTree(senales_reducidas)
        print("XML Finalizado!")
        tree.write(f"{nombre_archivo}.xml", encoding="utf-8", xml_declaration=True)


    def ordenar_xml(self,elemento):

        indentado ="    "
        fila = [(0,elemento)]

        while fila:
            nivel, elemento = fila.pop(0)
            children = [(nivel + 1, child) for child in list(elemento)]
            if children:
                elemento.text = '\n'+indentado*(nivel+1)
            
            if fila:
                elemento.tail = '\n' + indentado[0][0]
            else:
                elemento.tail = '\n' + indentado*(nivel-1)
            fila[0:0] = children


    def eliminar_todo(self):
        while self.primero:
            aux = self.primero
            self.primero = self.primero.siguiente
            del aux
            

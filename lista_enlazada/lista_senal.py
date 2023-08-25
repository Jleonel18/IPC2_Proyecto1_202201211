from lista_enlazada.nodo_senal import nodo_senal
from lista_enlazada.grupo import grupo

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
    
    def calcular_patrones(self,nombre_senal):
        actual = self.primero
        
        while actual != None:
            if actual.senal.senal == nombre_senal:
                actual.senal.lista_patrones =  actual.senal.lista_datos.devolver_patrones_por_tiempo(actual.senal.lista_patrones)
                actual.senal.lista_patrones.recorrer_e_imprimir_lista()

                lista_patrones_temporal = actual.senal.lista_patrones
                grupos_sin_analizar = lista_patrones_temporal.encontrar_coincidencias()

                buffer = ""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito == "-" and buffer!="":
                        cadena_grupo = actual.senal.lista_datos.devolver_cadena_del_grupo(buffer)
                        actual.senal.lista_grupos.insertar_dato(grupo = grupo(buffer,cadena_grupo))
                        buffer=""
                    else:
                        buffer=""
                actual.senal.lista_grupos.recorrer_e_imprimir_lista()

                return
            
            actual = actual.siguiente
        print("no se encontro la senal")
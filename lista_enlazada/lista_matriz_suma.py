from lista_enlazada.nodo_matriz_suma import nodo_matriz_suma

class lista_matriz_suma:

    def __init__(self):
        self.primero = None
        self.size = 0

    def insertar_dato(self,dato):
        
        if self.primero == None:
            self.primero = nodo_matriz_suma(dato = dato)
            return
        actual = self.primero
        
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_matriz_suma(dato = dato)
    
    def recorrer_e_imprimir_lista(self):
        print("--------------------------")
        actual = self.primero
        while actual != None:
            print("El tiempo de la matriz sumada es:",actual.dato.tiempo,"valor:",actual.dato.valor,"grupo:",actual.dato.grupo)
            actual = actual.siguiente
        print("--------------------------")

    def __iter__(self):
        self.actual = self.primero
        return self
    
    def __next__(self):
        if self.actual is not None:
            valor_actual = self.actual
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration


from lista_enlazada.nodo import nodo

class lista_siemple_enlazada():

    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None
    
    def agregar_ultimo(self,dato):
        if self.vacia() == True:
            self.primero = self.ultimo = nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo(dato)

    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux  = aux.siguiente


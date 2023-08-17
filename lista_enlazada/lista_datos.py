from lista_enlazada.nodo_dato import nodo_dato

class lista_datos:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    
    def vacia(self):
        return self.primero == None
    
    def agregar_ultimo(self,dato):
        if self.vacia() == True:
            self.primero = self.ultimo = nodo_dato(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo_dato(dato)
        self.size+=1

    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux  = aux.siguiente

    def eliminar_ultimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        
        aux.siguiente = None
        self.ultimo = aux

    def verificar_tamano(self):
        return self.size


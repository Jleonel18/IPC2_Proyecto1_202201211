from lista_enlazada.nodo_senal import nodo_senal

class lista_senal():

    def __init__(self):
        self.primero = None
        self.ultimo = None
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
            print("senal:",aux.senal.senal,"tiempo:",aux.senal.tiempo,"amplitud:",aux.senal.amplitud)
            aux = aux.siguiente

    def eliminar_ultimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente

        aux.siguiente = None
        self.ultimo = aux
    
    def verificar_tamano(self):
        return self.size
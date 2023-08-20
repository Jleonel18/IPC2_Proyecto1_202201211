from lista_enlazada.nodo_dato import nodo_dato

class lista_datos:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    
    def vacia(self):
        return self.primero == None
    
    def agregar_ultimo(self,dato):
        new_nodo = nodo_dato(dato)
        if self.size == 0 or(new_nodo.dato.tiempo, new_nodo.dato.amplitud) < (self.primero.dato.tiempo, self.primero.dato.amplitud):
            
            new_nodo.siguiente = self.primero
            self.primero = new_nodo

        else:
            aux = self.primero
            while aux.siguiente is not None and (aux.siguiente.dato.tiempo, aux.siguiente.dato.amplitud) <=(new_nodo.dato.tiempo, new_nodo.dato.amplitud):
                aux = aux.siguiente
            new_nodo.siguiente = aux.siguiente
            aux.siguiente = new_nodo
        self.size+=1


    def recorrido(self):
        aux = self.primero
        while aux != None:
            print("dato:",aux.dato.dato,"tiempo:",aux.dato.tiempo,"amplitud:",aux.dato.amplitud)
            aux  = aux.siguiente

    def eliminar_ultimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        
        aux.siguiente = None
        self.ultimo = aux

    def verificar_tamano(self):
        return self.size


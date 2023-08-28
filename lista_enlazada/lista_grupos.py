from lista_enlazada.nodo_grupo import nodo_grupo

class lista_grupos:
    def __init__(self):
        self.primero = None
        self.contador_grupos = 0

    def insertar_dato(self,grupo):
        
        if self.primero is None:
            self.primero = nodo_grupo(grupo = grupo)
            self.contador_grupos+=1
            return 
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_grupo(grupo = grupo)
        self.contador_grupos+=1

    def recorrer_e_imprimir_lista(self):
        print("=====================")
        actual = self.primero
        while actual != None:
            print("Grupo:",actual.grupo.el_grupo,"cadena_grupo:",actual.grupo.cadena_grupo)
            actual = actual.siguiente
        print("==============")

    def get_size(self):
        return self.contador_grupos
    
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
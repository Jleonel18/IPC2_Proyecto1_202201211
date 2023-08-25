from lista_enlazada.nodo_patron import nodo_patron

class lista_patrones:
    def __init__(self):
        self.primero = None
        self.contador_patrones = 0

    def insertar_dato(self,patron):
        
        if self.primero is None:
            self.primero = nodo_patron(patron = patron)
            self.contador_patrones+=1
            return 
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_patron(patron = patron)
        self.contador_patrones+=1

    def recorrer_e_imprimir_lista(self):
        print("=====================")
        actual = self.primero
        while actual != None:
            print("nivel:",actual.patron.nivel,"cadena_patron:",actual.patron.cadena_patron)
            actual = actual.siguiente
        print("==============")
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
            print("grupo_patron:",actual.patron.grupo_patron,"cadena_patron:",actual.patron.cadena_patron)
            actual = actual.siguiente
        print("==============")

    def eliminar(self,grupo_patron):
        actual = self.primero
        anterior = None
        while actual and actual.patron.grupo_patron != grupo_patron:
            anterior = actual
            actual = actual.siguiente
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None
    
    def encontrar_coincidencias(self):
        print("")
        print("")
        print("")
        resultado = ""

        while self.primero:
            actual = self.primero
            temp_string = ""
            temp_grupo_patron = ""
            while actual:
                if actual.patron.cadena_patron == self.primero.patron.cadena_patron:
                    temp_grupo_patron += str(actual.patron.grupo_patron)+","
                actual = actual.siguiente
            buffer = ""

            for digito in temp_grupo_patron:
                if digito.isdigit():
                    buffer +=digito
                else:
                    if buffer !="":
                        self.eliminar(int(buffer))
                    else:
                        buffer = ""
            resultado += temp_grupo_patron+"--"
        return resultado

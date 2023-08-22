from lista_enlazada.nodo_dato import nodo_dato
import os

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
            print("dato:",aux.dato.dato,"tiempo:",aux.dato.tiempo,"amplitud:",aux.dato.amplitud,"senal",aux.dato.senal,"binario",aux.dato.binario)
            aux  = aux.siguiente

    def eliminar_ultimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        
        aux.siguiente = None
        self.ultimo = aux

    def verificar_tamano(self):
        return self.size
    
    def generar_grafica(self,nombre_senal,tiempo,amplitud):
        
        f = open('bb.dot','w')
        # configuraciones del grafo
        text ="""
            digraph G {"tiempos="""+tiempo+"""","amplitudes="""+amplitud+""""->" """+nombre_senal+ """" bgcolor="#3990C4" style="filled"
            subgraph cluster1 {fillcolor="blue:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.dato.tiempo #iniciaria en 1
        fila_iniciada=False
        while actual != None:
            # Si mi fila actual es diferente a la que viene
            if  sentinela_de_filas!=actual.dato.tiempo:
                #print(sentinela_de_filas,actual.celda.nivel,"hola")
                sentinela_de_filas=actual.dato.tiempo
                fila_iniciada=False
                # Cerramos la fila
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                #Abrimos la fila
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.dato.dato)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.dato.dato)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o Grafica.png')
        print("terminado")

    def generar_grafica_binaria(self,nombre_senal,tiempo,amplitud):
        
        f = open('bb.dot','w')
        # configuraciones del grafo
        text ="""
            digraph G {"tiempos="""+tiempo+"""","amplitudes="""+amplitud+""""->" """+nombre_senal+ """" bgcolor="#3990C4" style="filled"
            subgraph cluster1 {fillcolor="blue:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.dato.tiempo #iniciaria en 1
        fila_iniciada=False
        while actual != None:
            # Si mi fila actual es diferente a la que viene
            if  sentinela_de_filas!=actual.dato.tiempo:
                #print(sentinela_de_filas,actual.celda.nivel,"hola")
                sentinela_de_filas=actual.dato.tiempo
                fila_iniciada=False
                # Cerramos la fila
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                #Abrimos la fila
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.dato.binario)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.dato.binario)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o Grafica.png')
        print("terminado")

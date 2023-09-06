from lista_enlazada.nodo_matriz_suma import nodo_matriz_suma
import os

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
        
    def generar_grafica(self,nombre,tiempo,amplitud):
        f = open('bb.dot','w')

        text ="""
            digraph G {"Amplitud="""+amplitud+""""->" """+nombre+ """" bgcolor="#3990C4" style="filled"
            subgraph cluster1 {fillcolor="yellow" style="filled"
            node [ fillcolor="blue" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:yellow" gradientangle="315">\n"""
        aux = self.primero
        sentinela_de_filas=aux.dato.grupo
        fila_iniciada=False
        
        text+="""<TR><TD border="3"  bgcolor="yellow" gradientangle="315">"""+"Grupo="+str(aux.dato.grupo)+" t="+str(aux.dato.tiempo)+"""</TD>\n"""
        while aux != None:

            
            if sentinela_de_filas!=aux.dato.grupo:
                
                sentinela_de_filas=aux.dato.grupo
                
                fila_iniciada=False

                text+="""</TR>\n""" 
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+"Grupo="+str(aux.dato.grupo)+" t="+str(aux.dato.tiempo)+"""</TD>\n"""
            if fila_iniciada==False:
                fila_iniciada=True

                
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(aux.dato.valor)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(aux.dato.valor)+"""</TD>\n"""
            aux = aux.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f"dot -Tpng bb.dot -o matriz-reducida.png")
        print("----->Grafica reducida generada con éxito!")



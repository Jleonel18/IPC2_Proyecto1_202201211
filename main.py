import archivos_entrada as archivos_entrada
#from lista_enlazada.lista_simple_enlazada import lista_siemple_enlazada
#lista = lista_siemple_enlazada()

def menuPrincipal():
    print('')
    print('Menu principal:')
    print('    1. Cargar archivo')
    print('    2. Procesar archivo')
    print('    3. Escribir archivo de salida')
    print('    4. Mostrar datos del estudiante')
    print('    5. Generar gráfica')
    print('    6. Inicializar sistema')
    print('    7. Salida')
    
    """
    lista.agregar_ultimo(12)
    lista.agregar_ultimo(2)
    lista.agregar_ultimo(25)
    lista.agregar_ultimo(30)
    """   

    #lista.recorrido()

    opcion = input()
    if opcion == '1':
        archivos_entrada.leerXML()
        menuPrincipal()
        print('')    
    elif opcion == '2':
        menuPrincipal()
    elif opcion == '3':
        menuPrincipal()
    elif opcion == '4':
        mostrarDatos()
        menuPrincipal()
    elif opcion == '5':
        menuPrincipal()
    elif opcion == '6':
        menuPrincipal()
    elif opcion == '7':
        print('Feliz dia :)')
    else:
        print('Elija una opcion valida')
        menuPrincipal()


def mostrarDatos():
    print('')
    print('Los datos del estudiante son:')
    print('> José Leonel López Ajvix')
    print('> 202201211')
    print('> Introducción a la programacion y computacion seccion D')
    print('> Ingenieria en Ciencias y Sistemas')
    print('> 4to Semestre')

menuPrincipal()
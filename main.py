from archivos_entrada import archivos_entrada

archivos_entrada = archivos_entrada()

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

    opcion = input()
    if opcion == '1':
        archivos_entrada.cargarXML()
        menuPrincipal()
        print('')    
    elif opcion == '2':
        archivos_entrada.leerXML()
        menuPrincipal()
    elif opcion == '3':
        archivos_entrada.escribir_nombre_archivo()
        menuPrincipal()
    elif opcion == '4':
        mostrarDatos()
        menuPrincipal()
    elif opcion == '5':
        archivos_entrada.seleccionar_senal()
        menuPrincipal()
    elif opcion == '6':
        archivos_entrada.limpiar_todo()
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
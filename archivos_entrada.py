import xml.etree.ElementTree as ET

def leerXML():

    tree  = ET.parse('archivo.xml')
    root = tree.getroot()
    try:            
        
        for i in root.findall('senal'):

            contador = 0
            validar_tiempo_senal(i.get('t'))
            validar_amplitud_senal(i.get('A'))

            for j in i.findall('dato'):

                validar_tiempo_dato(j.get('t'),i.get('t'))
                validar_amplitud_dato(j.get('A'),i.get('A'))
                contador +=1
            
            if contador < int(i.get('t'))*int(i.get('A')):
                while contador < int(i.get('t'))*int(i.get('A')):
                    print('Faltaba aqui una linea')
                    contador+=1
                
    except Exception as err:
        print(err)

def validar_tiempo_senal(tiempo):
    if int(tiempo) > 0 and int(tiempo)<=3600:
        print('El tiempo es',tiempo)
    else:
        print('La dimension de tiempo no es correcta')

def validar_amplitud_senal(amplitud):
    if int(amplitud) > 0 and int(amplitud)<=130:
        print('La amplitud es',amplitud)
    else:
        print('La amplitud no es correcta')

def validar_tiempo_dato(tiempo_dato,tiempo_senal):
    if int(tiempo_dato) > int(tiempo_senal):
        print('El tiempo del dato es mayor al tiempo de la senal')
    else:
        print('El tiempo del dato es',tiempo_dato)

def validar_amplitud_dato(amplitud_dato, amplitud_senal):
    if int(amplitud_dato) > int(amplitud_senal):
        print('La amplitud del dato es mayor a la amplitud de la senal')
    else:
        print('La amplitud del dato es',amplitud_dato)


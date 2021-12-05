#Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero 
#tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la 
#línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla 
#informando de ello.
def ent():
    n = int(input('Introduce un número entero entre 1 y 10: '))
    m = int(input('Introduce otro número entero entre 1 y 10: '))
    file = 'tabla-' + str(n) + '.txt'
    try: 
        f = open(file, 'r')
    except FileNotFoundError:
        print('No existe el fichero con la tabla del ', n)
    else:
        lines = f.readlines()
        print(lines[m - 1])
ent()
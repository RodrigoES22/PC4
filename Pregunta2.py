#Escribir una función que pida un número entero entre 1 y 10, lea el fichero 
#tabla-n.txt con la tabla de multiplicar de ese número, done n es el número 
#introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar 
#un mensaje por pantalla informando de ello.
def ent():
    n = int(input('Introduce un número entero entre 1 y 10: '))
    file_name = 'tabla-' + str(n) + '.txt'
    try: 
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('No existe el fichero con la tabla del', n)
    else:
        print(f.read())
ent()
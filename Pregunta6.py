#Escriba una expresión regular que encuente los nombres de archivos txt en la cadena:
# - Nombre de archivo txt siempre inicia al principio de la cadena
# - Siempre comienzan con una secuencia de 2 o 3 vocales mayúsculas o minúsculas 
# (a e i o u).
# - Archivo siempre termina con ".txt" .
from modulo import datos
import re
path = './src/re/short_tweets.csv'
analisis_sentimientos = datos.read_pandas(path,780,782)
regex = r"^[aeiouAEIOU]{2,3}[A-Za-z]+.txt"
for tweet in analisis_sentimientos:
    print(tweet)
    print(re.findall(regex, tweet))
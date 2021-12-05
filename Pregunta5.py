#Escriba una expresión regular para cada caso:
#todos los usuarios que sigan el siguente patron. User_mentions:9
#encuentre los numero de likes: likes: 5
#que permita encontrar el numero de retweets. number of retweets: 4
from modulo import datos
import re
s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
print(re.findall(r"User_mentions:\d", s))
print(re.findall(r"likes: \d", s))
print(re.findall(r"number of retweets: \d", s))
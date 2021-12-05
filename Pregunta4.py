#Escriba una expresión regular que encuentre todas las coincidencias que sigan el 
#siguiente patrón. Ej. @robot3!
from modulo import datos
import re
s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
print(re.findall(r"@robot\d\W", s))
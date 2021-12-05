#Escriba una expresión regular que valide una lista de correos electrónicos
# Primera parte:
# Caracteres en mayuscula y minúscula
# Números
# Caracteres especiales: !, #, %, &, *, $, .
# Debe contener @
# Dominio:
# Puede ser cualquier conjunto de caracteres
# Solo puede terminar con .com
# ENTRADA:
# ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
# SALIDA:
# The email n.john.smith@gmail.com is a valid email
# The email 87victory@hotmail.com is a valid email
# The email !#mary-=@msca.net is invalid
import re
regex = r".+@.+com$"
emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    if re.match(regex, example):
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))   
import re

def comprueba(dni):
    print(dni)
    letras_dni=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    if re.match("[0-9]{8}[a-z]",dni,re.IGNORECASE):
        letra=dni[8]
        num=int(dni[:8])
        #print(letras_dni)
        print(num)
        #print(num % 23)
        print(letra,letras_dni[num%23])
        if  letra.upper() == letras_dni[num % 23]:
            return "ok"
        else:
            return "no ok"

if __name__ == '__main__':
    print(comprueba(input("Escribe un NIF: ")))
from tercero import *
import re

a=input("¿Quieres ver la lista (s/n)? ")
expr=re.compile("[sn]",re.I)
if (expr.fullmatch(a)):
   if (a=="s"):
     lista()
else:
    print("No has escrito ni s ni n")

dni=input("Escribe tu dni")
expr=re.compile("[0-9]{8}[a-z]",re.I)
if (expr.fullmatch(dni)):
    print(f"El dni {dni} es correcto")
else:
    print(f"{dni} no es un dni correcto")
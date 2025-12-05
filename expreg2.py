import re

try:
   a,b=int(input("Escribe un número: ")),int(input("Escribe otro número mayor que el primero: "))
   if (a>=b):
       raise Exception("Error:",f"{a} no puede ser mayor o igual que {b}")
   nombre=input("Escribe tu nombre completo: ")
   expr = re.compile("[a-záéíóú ]+",re.I)
   if (expr.fullmatch(nombre) is None):
       raise Exception("Error:", "El nombre solo debe contener letras")

   for i in range(a,b):
        print(f"{i}=>{nombre}")
   
except Exception as e:
    print(e)
else:
    print("Cuando no hay excepciones")
finally:
    print("Siempre")
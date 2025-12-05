'''
Docstring for ejercicio3-3
https://docs.python.org/3/library/datetime.html#datetime.date.strptime
https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
'''
from datetime import datetime

def validar_entero():
    n = int(input("¿Número? "))
    if n <= 0:
        raise ValueError("El número debe ser mayor que 0.")
    return n

def validar_fecha():
    actual = datetime.now().year
    fecha_str = input("¿Fecha de nacimiento (dd/mm/yyyy)? ")
    fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
    if fecha.year < 1900 or fecha.year > actual:
        raise ValueError(f"Año debe estar entre 1900 y {actual}.")
    return fecha_str 

def validar_nombre():
    nombre=input("¿Nombre? ").strip()
    if len(nombre)==0:
        raise "El nombre no puede estar vacío"
    else:
        return nombre

def pedir(validar):
    while True:
        try:
          return validar()
        except ValueError as e:
            print("Error:", e)
        except KeyboardInterrupt:
            print("\nInterrumpido por el usuario")
        

def main():
    personas = {}
    cantidad = pedir(validar_entero)

    for i in range(cantidad):
        print(f"\nPersona {i+1}:")
        nombre = pedir(validar_nombre)
        fecha = pedir(validar_fecha)
        personas[nombre] = fecha
        print(personas)

    print("\nListado de personas:")
    for nombre, fecha in personas.items():
        print(f"{nombre}: {fecha}")

    print("\nBuscar una persona:")
    buscar = pedir(validar_nombre)

    if buscar in personas:
        print(f"{buscar} Fecha de nacimiento: {personas[buscar]}.")
    else:
        print(f"{buscar} no está registrado.")

if __name__=="__main__":
    main()
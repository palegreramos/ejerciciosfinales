'''
Docstring for ejercicio3-2
https://www.w3schools.com/python/python_ref_functions.asp
https://www.w3schools.com/python/ref_func_sum.asp
'''
import sys
import statistics
clase = {}
try:
    nums=int(input("¿Cuántos alumnos hay en la clase? "))
    for i in range(nums):
        alumno = input(f'Alumno {i+1} ¿Nombre? ')
        nota = float(input(f'¿Nota de {alumno}? '))
        clase[alumno]=nota
        print(clase)

    for k,v in clase.items():
        print(f"Alumno {k} = {v:.2f}")

    print("\nClaves de diccionario:", clase.keys())
    print ("\nValores de diccionario:", clase.values())
    print(1 in clase.values())
    print ("\nElementos de diccionario:", clase.items())

    print(f"\n{'Alumno'!r:>10}:{'Nota'!r:*>10}")
    for nombre, nota in clase.items():
        print(f"{nombre!r:>10}:{nota:10.2f}")


    media = sum(clase.values()) / len(clase)
    print(f"\nMedia de la clase es: {media:.2f}")

    print(f"{statistics.mean(clase.values()):.2f}")

    print(f"\nNota más alta: {max(clase.values()):.2f}. Nota más baja: {min(clase.values()):.2f}")

    nombre=input("Nombre del alumno a buscar: ")
    if nombre in clase:
        print(f"El alumno {nombre} sí está en la clase")
        nota=clase[nombre]
        if nota>media:
            print(f"{nota} es mayor a la media {media:.2f}")
        else:
            print(f"{nota} no es mayor a la media {media:.2f}")
    else:
        print(f"El alumno {nombre} no está")
except ValueError as e:
    print(f"ValueError: '{e}'") 
except KeyboardInterrupt:
    print("\nTerminado por el usuario")
except:
    print("Unexpected error:", sys.exc_info()[1])
    print(sys.exc_info())     

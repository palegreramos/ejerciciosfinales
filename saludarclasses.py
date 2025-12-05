class Saludar():
    def __init__(self):
        print("¿Cómo se llama?",end=" ")
        nombre = input()
        print(f"Me alegro de conocerle, {nombre}")
      
def main():
    mi_app = Saludar()
    return 0

# Mediante el atributo __name__ tenemos acceso al nombre de un
# un módulo. Python utiliza este atributo cuando se ejecuta
# un programa para conocer si el módulo es ejecutado de forma
# independiente (en ese caso __name__ = '__main__') o es 
# importado:

if __name__ == '__main__':
    main()
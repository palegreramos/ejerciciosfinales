class Validar:

    @staticmethod
    def validar_sueldo(self):
        n = int(input("¿Sueldo? "))
        if n <= 0:
            raise ValueError("El sueldo debe ser mayor que 0.")
        return n
   
    @staticmethod
    def validar_nombre(self):
        nombre = input("¿Nombre? ").strip()
        if len(nombre) == 0:
            raise ValueError("El nombre no puede estar vacío") 
        return nombre

    @staticmethod
    def pedir(self, validar):
        while True:
            try:
                return validar()
            except ValueError as e:
                print("Error:", e)
            except KeyboardInterrupt:
                print("\nInterrumpido por el usuario")
                break

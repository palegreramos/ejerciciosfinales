class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"Nombre empleado: {self.nombre} Sueldo: {self.sueldo}"

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print(f"{self.nombre} debe pagar impuestos.")
        else:
            print(f"{self.nombre} no debe pagar impuestos.")
            

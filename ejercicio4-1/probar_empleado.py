from empleado import *
from validar_entrada import Validar



nombre = Validar.pedir(Validar.validar_nombre)
sueldo = Validar.pedir(Validar.validar_sueldo)


empleado1 = Empleado(nombre,sueldo)
print(empleado1)
empleado1.pagar_impuestos()
from empleado import *
from validar_entrada import *


v=Validar()

nombre = v.pedir(v.validar_nombre)
sueldo = v.pedir(v.validar_sueldo)


empleado1 = Empleado(nombre,sueldo)
print(empleado1)
empleado1.pagar_impuestos()
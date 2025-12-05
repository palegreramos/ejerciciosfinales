import re
nombre=input("Escribe tu nombre: ")

prog = re.compile("^[a-z]+$")
result = prog.match(nombre)
print(result)

prog1 = re.compile("^[a-z]+$",re.I)
result1 = prog1.match(nombre)
print(result1)

prog2 = re.compile("^[a-z]+$",re.IGNORECASE)
result2 = prog2.search(nombre)
print(result2)

prog3 = re.compile("[a-z]+",re.I)
result3 = prog3.fullmatch(nombre)
print(result3)

variable="""<h1>Hola</h1>
<ul>
<li>hola</li>
</ul>
"""
frasecani="hola colega, cómo estás colega"

print(frasecani.replace("c","k"))
expr=re.compile("[aeiou]")

if (expr.match(frasecani[-1])):
    print(f"{frasecani.replace('c','k')}hhhhh")

print(f"{frasecani[5:11]}")
#diccionarios
lenguajes = {'C':1972,'Python':1991,'Java':1996}
print(lenguajes)
print(lenguajes['Python'])
#itera por las claves
for lenguaje in lenguajes:
    print(lenguaje,lenguajes[lenguaje])
for lenguaje in lenguajes.keys(): #igual que la anterior
    print(lenguaje,lenguajes[lenguaje])
for año in lenguajes.values():
    print(año)

for lenguaje, año in lenguajes.items():
    print(lenguaje,año)

print('Python' in lenguajes)
lenguajes['Pascal']=1977
del lenguajes['Java']
print(lenguajes)
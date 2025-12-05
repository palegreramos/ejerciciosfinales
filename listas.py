from math import sqrt

lista=[]
n=input("número: ")
while n != "-1":
    lista.append(n)
    print(",".join(lista))
    n=input("número: ")

print(lista)
lista.reverse()
print(lista)
print("---".join(map(str,lista)))
print(lista)
result = list(map(float, lista) )
print(result)
result2=list(map(sqrt,result))
print(result2)
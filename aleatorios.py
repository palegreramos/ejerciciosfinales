from random import randrange,choice


for i in range(10):
    a=randrange(1,20)
    print(a)
nums=[1,2,3,4]
print(f"Número elegido de: {','.join(map(str,nums))}")
print(choice(nums))
lista=["una","dos","tres","cuatro"]
print(f"Palabra elegida de {','.join(lista)}")
print(choice(lista))
input("Pulsa Enter para terminar....")
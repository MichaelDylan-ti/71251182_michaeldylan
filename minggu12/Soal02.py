lista = input("Lista = ").split(',')
listb = input("Lista = ").split(',')

lista = [x.strip() for x in lista]
listb = [x.strip() for x in listb]

kamus = dict()
for i in range(len(lista)):
    kamus[lista[i]] = listb[i]

print(kamus)
lista = []
for i in range(6):
    lista.append(i + 1)
print(lista)
if 3 in lista:
    lista.remove(3)
else:
    print('Elemento não encontrado na lista!')
if 6 in lista:
    lista.remove(6)
else:
    print('Elemento não encontrado na lista!')
print(lista)
print('Tamanho da lista:',len(lista))
ultimo = len(lista) - 1
lista[ultimo] = 6
print(lista)

import random

valor = []
dado = [0,0,0,0,0,0]

for contadorA in range(100):
    for contadorB in range(6):
        valor.append(random.randint(1,6))
        
print(valor)

for contadorC in range(len(valor)):
    if 1 == valor[contadorC]:
        dado[0] += 1
    if 2 == valor[contadorC]:
        dado[1] += 1
    if 3 == valor[contadorC]:
        dado[2] += 1
    if 4 == valor[contadorC]:
        dado[3] += 1
    if 5 == valor[contadorC]:
        dado[4] += 1
    if 6 == valor[contadorC]:
        dado[5] += 1
for contadorD in range(len(dado)):
    print('Quantidade de números', contadorD + 1,'=',dado[contadorD])


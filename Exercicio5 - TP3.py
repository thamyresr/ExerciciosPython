nomes = []
alturas = []
registro = [] 
sair = False
contador = 0

def calcularMedia():
    alturaTotal = 0
    for contador in range(len(alturas)):
        alturaTotal = alturaTotal + alturas[contador]  
    media = float(alturaTotal/len(alturas))
    return media 


def calcularMaiorAltura():
    mediaTotal = calcularMedia()
    for contador in range (len(alturas)):
        if alturas[contador] > mediaTotal:
            print ('Aluno com altura acima da média: ',nomes[contador], '\nAltura do aluno:', alturas[contador])

while not sair: 
    nome = input("Digite seu nome: ")
    if nome == "sair":
        break
    else:
        nomes.append(nome)
    altura = float(input("Digite a sua altura: "))    
    alturas.append(altura)       


calcularMaiorAltura()

vetor = []
tamanhoVetor = int(input('Informe o tamanho do vetor:'))
contador = 0

for i in range(tamanhoVetor):
    numeros = (int(input('Digite um número:')))
    vetor.append(numeros)
    
for i in range(len(vetor)):
    if vetor[i] == 0:
        contador = contador + 1
        
print('Quantidade de números zero:',contador)
        
vetor = []
ativa = True
while ativa:
    frase = str(input('Digite uma frase:'))
    if frase != 'sair':        
        vetor.append(frase)
    else:
        ativa = False
        
for contador in range(len(vetor)):
    if 'eu' in vetor[contador].split(' '):
        print(vetor[contador])
    
        
    


        
        

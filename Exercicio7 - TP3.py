lista = []
ativa = True

def mostrarLista(lista):
    print('\n-----Lista-----')
    for contador in range(len(lista)):
        print(lista[contador])
    print('---------------\n')

def incluirElemento(lista):
    lista.append(input('\nDigite um valor:\n'))

def removerElemento(lista):
    numero = input('\nDigite o valor a ser removido:\n')
    if numero in lista:
        lista.remove(numero)
        print(numero,'Removido com sucesso!\n')
    else:
        print('\nElemento não encontrado na lista!\n')

def apagarLista(lista):
    lista.clear()
    print('\nA lista foi completamente removida.\n')
    
def menu():
    while ativa:
        print('1 - Mostrar elemento(s) da lista')
        print('2 - Incluir elemento na lista')
        print('3 - Remover elemento da lista')
        print('4 - Apagar todos os elementos da lista')
        print('5 - Sair')
        operacao = input('\nDigite a opção desejada:\n')
        if '1' == operacao:
            mostrarLista(lista)
        elif '2' == operacao:
            incluirElemento(lista)
        elif '3' == operacao:
            removerElemento(lista)
        elif '4' == operacao:
            apagarLista(lista)
        elif '5' == operacao:
            print('\nOperação finalizada')
            break        
        else:
            print('\nOperação inválida!!!')
            
menu()


import os

def cadastrar(lista, nomeTitular, tipo, valor):
    t = len(lista)
    if t == 0:
        codigo = 12000
    else:
        codigo = lista[t-1][1] + 1
    conta = ([nomeTitular, codigo, tipo,valor])
    lista.append(conta)
    print('\nConta cadastrada com sucesso!')
    print(f'O número da sua conta {conta[2]} é {codigo}.\n')
    return lista


def buscaIndice(lista, numeroConta):
    indice = 0
    for c in lista:
        if c[1] == numeroConta:
            break
        indice +=1
    else:
        indice = -100
    return indice


def sacar(lista, numeroConta, valor):
    i = buscaIndice(lista, numeroConta)
    if i < 0:
         print('\nConta não encontrada. Por favor, verifique os dados da sua conta.')
         return
    else:
        if lista[i][1] == numeroConta:
            anterior = lista[i][3]
            if lista[i][3] >= valor:
                lista[i][3] -= valor
                print('\nSaque realizado com sucesso!\n')
                print(f'Saldo anterior: R${anterior}')
                print(f'Saldo atual: R${lista[i][3]}')
            else:
                print('Saldo insuficiente!')
        else:
            print('Conta não encontrada. Por favor, verifique os dados da sua conta.')
        return lista

def depositar(lista, numeroConta, valor):
    i = buscaIndice(lista, numeroConta)
    if i < 0:
         print('\nConta não encontrada. Por favor, verifique os dados da sua conta.')
         return
    else:
        if lista[i][1] == numeroConta:
            lista[i][3] += valor
            print('\nDeposito realizado com sucesso!')
        else:
            print('\nERRO. Por favor, verifique os dados da sua conta!')
        return lista
    

def buscarConta(lista, numeroConta):
    for dado in lista:
        if dado[1] == numeroConta:
            print(f'TITULAR DA CONTA: {dado[0]}')
            print(f'NÚMERO DA CONTA: {dado[1]}')
            print(f'TIPO: {dado[2]}')
            print(f'SALDO: R${dado[3]}')
            return
    return print(' - Nenhuma conta encontrada com os dados informados!')


def buscarNome(lista, nometitular):
    for dado in lista:
        if dado[0] == nometitular:
            print(f'TITULAR DA CONTA: {dado[0]}')
            print(f'NÚMERO DA CONTA: {dado[1]}')
            print(f'TIPO: {dado[2]}')
            print(f'SALDO: R${dado[3]}')
            return
    return print(' - Nenhuma conta encontrada com os dados informados!')


def excluir(lista, numeroConta):
    lista2 = []
    i = buscaIndice(lista, numeroConta)  
    saldo = lista[i][3] 
    if saldo > 0:
        print(f'\nA conta não pode ser exluída pois ainda contém um saldo de R${saldo}!')
        print('Faça a retirada dos fundos ou transfira para outra conta e tente novamente!\n')
        return
    else:
        for p in lista: 
            if p[1] != numeroConta:
                lista2.append(p)

        print(f'\nConta excluída com sucesso! \n')  
    return lista2


def imprimir(lista):
    print('======= CONTAS ========')
    for p in lista:
            print('')
            print(f'TITULAR DA CONTA: {p[0]}')
            print(f'NÚMERO DA CONTA: {p[1]}')
            print(f'TIPO: {p[2]}')
            print(f'SALDO: R${p[3]}')
            print('=======================')
    return lista


def editar(lista, numeroconta, nomeTitular, tipo):
    indice= buscaIndice(lista, numeroconta)
    if indice <  0:
        print('\nERRO. Conta não encontrada, tente novamente!\n')
        return
    else:
        i = 0
        for p in lista:
            if p[1] == numeroconta: 
                break
            i += 1              
        lista[i][0] = nomeTitular
        lista[i][2] = tipo
        print('\nDados alterados com sucesso!\n')
        return lista


def transferencia(lista, conta_origem, conta_destino, valor):
    origem = buscaIndice(lista, conta_origem)
    destino = buscaIndice(lista, conta_destino)
    
    if origem < 0 and destino < 0:
        print('\nERRO. Conta de ORIGEM e conta de DESTINO não encontradas!\n')
        return
    elif origem < 0:
        print('\nERRO. Conta de ORIGEM não encontrada!\n')
        return
    elif destino < 0:
        print('\nERRO. Conta de DESTINO não encontrada!\n')
        return
    elif origem  == destino:
        print('\nERRO! A conta de ORIGEM não pode ser igual a conta de DESTINO!\n')
        return
    
    elif origem >= 0 and destino >=0:
        if lista[origem][3] >= valor:
            lista[origem][3] -= valor
            lista[destino][3] += valor
        else:
            return print('\nERRO. Saldo insuficiente!\n')
        return print('\nTransferencia realizada com sucesso!\n')


def mostrarSaldo(lista, numeroConta):
    i = buscaIndice(lista, numeroConta)
    saldo = lista[i][3]
    print(f'DISPONÍVEL PARA SAQUE: R${saldo}')
    return 

def mostrarConta(lista, numeroConta):
    i = buscaIndice(lista, numeroConta)
    nome = lista[i][0]
    numero = lista[i][1]
    print('NOME DO TITULAR: ',nome)
    print('NÚMERO DA CONTA: ',numero)
    return



import funcionalidades as funcoes
import os

contas = [
    ["lau", 12000, "Corrente", 9000],
    ["Anderson", 12001, "Poupança", 4000],
    ["Marcos", 12002, "Corrente", 1300],
    ["João", 12003, "Poupança", 2000],
]

while True:
    os.system("cls")
    print("===== SISTEMA BANCÁRIO =====")
    print(f"""
1 - CADASTRAR NOVA CONTA
2 - SACAR
3 - DEPOSITAR
4 - BUSCAR
5 - EXCLUIR 
6 - EDITAR CONTA
7 - TRANSFERIR DINHEIRO
0 - SAIR 
""" )
    op = input("QUAL OPERAÇÃO DESEJA REALIZAR? ")

    if op == "0":
        os.system("cls")
        print("===== SISTEMA ENCERRADO =====")
        break

    elif op == "1":
        os.system("cls")
        print("===== CADASTRO DE CONTA =====\n")
        nomeTitular = input("NOME DO TITULAR: ")
        if nomeTitular == '':
            print('\nERRO. O nome do titular da conta não pode estar vazio!\n')
            os.system('pause')
        else:
            tipo = input("QUAL O TIPO DE CONTA? \n 1 - POUPANÇA \n 2 - CORRENTE \n >> ")
            if tipo != "1" and tipo != "2":
                print("Opcão inválida!")
                os.system("pause")
            else:
                if tipo == "1":
                    tipo = "Poupança"
                elif tipo == "2":
                    tipo = "Corrente"

                try:
                    saldo = float(input("\nSALDO INICIAL: "))
                except ValueError:
                    print("\nERRO. O valor inserido não é um número, Tente novamente!\n")
                    os.system("pause")
                    continue
                
                if saldo < 0:
                    print("\nERRO. O saldo inicial não pode ser menor que 0!\n")
                    os.system("pause")
                else:
                    funcoes.cadastrar(contas, nomeTitular, tipo, saldo)
                    os.system("pause")

    elif op == "2":
        os.system("cls")
        print("===== SACAR DINHEIRO =====\n")
        try:
            numeroConta = int(input("NÚMERO DA CONTA: "))
            funcoes.mostrarSaldo(contas, numeroConta)
            valor = float(input("\nVALOR DO SAQUE: "))
        except ValueError:
            print("\nERRO. O valor inserido não é um número, Tente novamente!\n")
            os.system("pause")
            continue

        print(f"\nCONFIRMA QUE DESEJA RETIRAR R${valor} ?")
        confirma = input("\n 1 - SIM \n 2 - NÃO \n >> ")

        if confirma != "1" and confirma != "2":
            print("Opcão inválida!")
            os.system("pause")
        else:
            if confirma == "1":
                funcoes.sacar(contas, numeroConta, valor)
                print("")
                os.system("pause")
            elif confirma == "2":
                print("\nOperação cancelada!\n")
                os.system("pause")


    elif op == "3":
        os.system("cls")
        print("===== DEPOSITO =====\n")
        nome = input("NOME DO DEPOSITANTE: ")  
        try:
            numeroConta = int(input("NÚMERO DA CONTA: "))
        except ValueError:
            print('\nERRO. O valor inserido não é um número, Tente novamente!\n')
            os.system('pause')
            continue

        indice = funcoes.buscaIndice(contas, numeroConta)
        if indice < 0:
            print("\nErro. Conta inexistente!")
            os.system("pause")

        else:
            try:  
                valor = float(input("\nVALOR DO DEPOSITO: "))
                os.system("cls")
                print("===== DEPOSITO =====\n")
                funcoes.mostrarConta(contas, numeroConta)
                print(f"\nCONFIRMA QUE DESEJA DEPOSITAR R${valor} NESTA CONTA?")
                confirma = input("\n 1 - SIM \n 2 - NÃO \n >> ")

                if confirma != "1" and confirma != "2":
                    print("Opcão inválida!")
                    os.system("pause")
                else:
                    if confirma == "1":
                        funcoes.depositar(contas, numeroConta,valor)
                        print("")
                        os.system("pause")
                    elif confirma == "2":
                        print("\nOperação cancelada!\n")
                        os.system("pause")
            except ValueError:
                print("\nERRO. O valor inserido não é um número, Tente novamente!\n")
                os.system("pause")
                continue

            
    elif op == "4":
        os.system("cls")
        print("===== BUSCAR CONTA =====\n")
        busca = input("QUAL TIPO DE BUSCA DESEJA REALIZAR? \n\n 1 - PELO NOME \n 2 - PELO NÚMERO DA CONTA \n >>  ")
        if busca != "1" and busca != "2":
            print("Opcão inválida!")
            os.system("pause")
        else:
            if busca == "1":
                os.system("cls")
                print("===== BUSCAR CONTA =====\n")
                nomeTitular = input("NOME DO TITULAR DA CONTA: ")
                print("\nResultados da busca: \n")
                funcoes.buscarNome(contas, nomeTitular)
                print("")
                os.system("pause")

            if busca == "2":
                try:
                    os.system("cls")
                    print("===== BUSCAR CONTA =====\n")
                    numeroConta = int(input("NÚMERO DA CONTA: "))
                except ValueError:
                    print("\nERRO. O valor inserido não é um número, Tente novamente!\n")
                    os.system("pause")
                    continue

                print("\nResultados da busca: \n")
                funcoes.buscarConta(contas, numeroConta)
                print("")
                os.system("pause")

    elif op == "5":
        os.system("cls")
        print("===== EXCLUSÃO DE CONTA =====\n")
        funcoes.imprimir(contas)
        try:
            numeroConta = int(input("\nNÚMERO DA CONTA QUE DESEJA EXCLUIR: "))
        except ValueError:
            print("\nERRO. O valor inserido não é um número, Tente novamente!\n")
            os.system("pause")
            continue

        indice = funcoes.buscaIndice(contas, numeroConta)
        if indice < 0:
            print("\nErro. Conta inexistente!")
            os.system("pause")
        else:
            while True:
                os.system("cls")
                print("===== EXCLUSÃO DE CONTA =====\n")
                funcoes.mostrarConta(contas, numeroConta)
                confirma = input(f"\nTEM CERTEZA QUE DESEJA EXLUIR ESTA CONTA? (S / N)")
                if confirma == "S" or confirma == "s":
                    contas = funcoes.excluir(contas, numeroConta)
                    os.system("pause")
                    break

                elif confirma == "N" or confirma == "n":
                    print("\nExclusão de conta cancelada!\n")
                    os.system("pause")
                    break
                else:
                    print("\nERRRO. Comando inválido!\n")
                    tentarNovamente = input("Pressione ENTER para tentar novamente! ")
                os.system("cls")

    elif op == "6":
        os.system("cls")
        print("===== EDITAR DADOS BANCÁRIOS =====\n")
        funcoes.imprimir(contas)
        try:
            numeroConta = int(input("\nNÚMERO DA CONTA QUE DESEJA EDITAR: "))
        except ValueError:
            print("\nERRO. O valor inserido não é um número, Tente novamente!\n")
            os.system("pause")
            continue
        
        os.system('cls')
        print("===== EDITAR DADOS BANCÁRIOS =====\n")
        nomeTitular = input("NOVO NOME DE TITULAR: ")
        tipo = input("NOVO TIPO DE CONTA: \n 1 - POUPANÇA \n 2 - CORRENTE \n >> ")
        if tipo != "1" and tipo != "2":
            print("Opcão inválida!")
            os.system("pause")
        else:
            if tipo == "1":
                tipo = "Poupança"
            elif tipo == "2":
                tipo == "Corrente"
            funcoes.editar(contas, numeroConta, nomeTitular, tipo)
            os.system("pause")

    elif op == "7":
        os.system("cls")
        print("===== TRANSFERÊNCIA BANCÁRIA =====\n")
        try:
            conta_origem = int(input("CONTA DE ORIGEM: "))
            conta_destino = int(input("CONTA DE DESTINO: "))
            valor = float(input("VALOR DA TRANSFERÊNCIA: "))
        except ValueError:
            print("\nERRO. O valor inserido não é um número, Tente novamente!\n")
            os.system("pause")
            continue

        os.system("cls")
        print("===== TRANSFERÊNCIA BANCÁRIA =====\n")
        print(f"CONFIRMA QUE DESEJA TRANSFERIR R${valor} PARA A CONTA {conta_destino}?")
        confirma = input("\n 1 - SIM \n 2 - NÃO \n >> ")

        if confirma != "1" and confirma != "2":
            print("Opcão inválida!")
            os.system("pause")
        else:
            if confirma == "1":
                funcoes.transferencia(contas, conta_origem, conta_destino, valor)
                os.system("pause")

            elif confirma == "2":
                print("\nOperação cancelada!\n")
                os.system("pause")
    else:
        print("\nComando inválido!")
        os.system("pause")

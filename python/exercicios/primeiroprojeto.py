nome1 = 0
valorentrou = 0 
nome2 = 0
valorentrou = 0
opcao = 0

while opcao !=5:
    
    print()
    print("===== CONTROLE FINANCEIRO =====")
    print()

    print("1 - ADICIONAR RECEITAS ")
    print("2 - ADICIONAR DESPESAS ")
    print("3 - CONSULTAR SALDO ")
    print("4 - LISTAR MOVIMENTACOES")
    print("5 - SAIR")
    print()

    opcao = int(input("ESCOLHA UMA OPCAO: "))

    if opcao == 1:
        print('OPCAO 1 - ADICIONAR RECEITA')
        nome1 = input("DESCRICAO: ")
        valorentrou = float(input("VALOR: "))
        if valorentrou < 0:
            print("VALOR INVALIDA! TENTE NOVAMENTE")
    
    
    elif opcao == 2:
        print("opcao 2 - ADICIONAR DESPESAS ")
        nome2 = input("DESCRICAO: ")
        valorsaiu = float(input("VALOR: "))
        if valorsaiu < 0:
            print("VALOR INVALIDO! TENTE NOVAMENTE")

        


    elif opcao == 3:
        print("OPCAO 3 - CONSULTAR SALDO")   
        print(F"TOTAL RECEITAL: {valorentrou + 1}")
        print(f"TOTAL DESPESAS: {valorentrou - valorsaiu:.2f}")

    elif opcao == 4:
        print("OPCAO - 4 LISTAR MOVIMENTACOES")
        print("RECEITAS:")
        print(nome1)
        print(valorentrou)
        print("DESPESAS:")
        print(nome2)
        print(valorsaiu)
    elif opcao == 5:
        print("PROGRAMA ENCERRADO")





        










    

    

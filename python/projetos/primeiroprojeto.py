#controle financeiro pessoal====python


receita = []
despesas = []
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

        if valorentrou <= 0:
            print("VALOR INVALIDA!")
        else:
            receita.append([nome1, valorentrou])
            print("RECEITA CADASTRADA!")

        
    
    elif opcao == 2:
        print("opcao 2 - ADICIONAR DESPESAS ")
        nome2 = input("DESCRICAO: ")
        valorsaiu = float(input("VALOR: "))

        if valorsaiu <= 0:
            print("VALOR INVALIDO! ")
        else:
            despesas.append([nome1, valorsaiu])   

        


    elif opcao == 3:
        total_receitas = 0
        total_despesas = 0

        for item in receita:
            total_receitas += item[1]

        for  item in despesas:
            total_despesas += item[1]

            saldo = total_receitas - total_despesas

        print("===== CONSULTAR SALDO =====")   
        print(f"TOTAL RECEITAS: {total_receitas:.2f} ")
        print(f"TOTAL DESPESAS: {total_despesas:.2f}")
        print(f"SALDO: {saldo:.2f} ")

    elif opcao == 4:
        print("===== RECEITAS =====")
        print(f"TOTAL RECEITAS: {total_receitas:.2f}")
        print(f"TOTAL DESPESAS: {total_despesas:.2f}")
        print(f"SALDO ATUAL: {saldo:.2f}")
    elif opcao == 5:
        print("PROGRAMA ENCERRADO!")
    else:
        print("OPCAO INVALIDA! TENTE NOVAMENTE.")





        










    

    

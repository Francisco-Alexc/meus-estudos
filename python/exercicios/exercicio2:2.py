
#Problema "lanchonete" (adaptado de URI 1038)
#Uma lanchonete possui vários produtos. Cada produto possui um código
#e um preço. Você deve fazer um programa para ler o código e a
#quantidade comprada de um produto (suponha um código válido), e daí
#informar qual o valor a ser pago, com duas casas decimais, conforme
#tabela de produtos ao lado.

#produto = int(input("digite o codigo do produto: "))
#quantidade = int(input("digite a quantidade: "))


#if produto == 1:
#    preco = 5.00
#elif produto == 2:
#    preco = 3.50
#elif produto == 3:
#    preco = 4.80
#elif produto == 4:
#    preco = 8.90
#elif produto == 5:
#    preco = 7.32

#print(f"valor a pagar: R${preco * quantidade:.2f}")

#================================================================================

#Problema "multiplos" (adaptado de URI 1044)
#Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. Os
#números podem ser digitados em qualquer ordem.

#a = int(input("digite numeros inteiros: "))
#b = int(input("digite numeros inteiros: "))

#if a > b:
#    if a % b == 0:
#        print("sao multiplos.")
#    else:
#        print("nao sao multiplos.")
#else:
#    if b % a == 0:
#        print("sao multiplos.")
#    else:
#        print("nao sao multiplos.")


#================================================================


#Problema "aumento" (adaptado de URI 1048)
#Uma empresa vai conceder um aumento percentual de
#salário aos seus funcionários dependendo de quanto
#cada pessoa ganha, conforme tabela ao lado. Fazer um
#programa para ler o salário de uma pessoa, daí mostrar
#qual o novo salário desta pessoa depois do aumento,
#quanto foi o aumento e qual foi a porcentagem de
#aumento.

#Salário atual Aumento
#Até R$ 1000.00 20%
#Acima de R$ 1000.00
#até R$ 3000.00 15%
#Acima de R$ 3000.00
#até R$ 8000.00 10%
#Acima de R$ 8000.00 5% 


#salario = float(input("digite o salario da pessoa: "))

#if salario <= 1000:
#    porecentagem = 20
#elif salario <= 3000:
#    porecentagem = 15
#elif salario <= 8000:
#    porecentagem = 10
#else:
#    porecentagem = 5

#aumento = salario * porecentagem / 100
#novo_salario = salario + aumento

#print(f"novo salario = R$ {novo_salario:.2f}")
#print(f"aumento = R$ {aumento:.2f}")
#print(f"porcentagem = {porecentagem}%")

#==========================================================================================================





#Problema "tempo_de_jogo" (adaptado de URI 1046)
#Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo
#pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24
#horas. 

#hora1 = int(input("hora inicial: ")) 
#hora2 = int(input("hora final: "))

#if hora2 > hora1:
#    duracao = (24 - hora2) + hora1
#elif hora2 < hora1:
#    duracao = (24 - hora1) + hora2
#else:
#    duracao = 24

#print(f"o jogo durou {duracao} hora(s)")

#=========================================================================================

#valor_x = float(input("digite o valor de X: "))
#valor_y = float(input("digite o valor de Y: "))

#if valor_x > 0 and valor_y > 0:
#    print("Q1")
#elif valor_x < 0 and valor_y > 0:
#    print("Q2")
#elif valor_x < 0 and valor_y < 0:
#    print("Q3")
#elif valor_x > 0 and valor_y < 0:
#    print("Q4")
#elif valor_x == 0 and valor_y == 0:
#    print("Origem")
#elif valor_x == 0:
#    print("Eixo Y")
#elif valor_y == 0:
#    print("Eixo X")

#============================================================================================
x = (input("digite o primeiro numero: "))


while x != 0:
    input("outro numero:")

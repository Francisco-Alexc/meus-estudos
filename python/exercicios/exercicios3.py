# Fazer um programa que lê um valor inteiro N e depois N números inteiros. Ao final, mostra a soma dos N números lidos

numero = int(input("digite um numero: "))

soma = 0 

while numero != 0:
    soma = soma+numero
    numero = int(input("digite outro numero:"))

print(soma)
print("fim da execucao.")

#=======================================================================================================================

# Problema "media_idades"
# Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
# indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
# e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
# mostrar a mensagem "IMPOSSIVEL CALCULAR". 

idade = int(input("digite as idades: "))
soma = 0
cont = 0

while idade >= 0:
    soma = soma + idade
    cont = cont + 1
    idade = int(input("digite as idades: "))
    
if cont == 0:
    print("impossivel calcular.")
else:
    media = soma / cont
    print(f"media: {media:.2f}")

#===========================================================================================

# estrutura "para/for"

N = int(input("quantos numeros serao digitados ? "))
soma = 0

for i in range(1, N + 1):
    x = int(input("digite um numero: "))
    soma = soma + x
print("soma=", soma)

#=============================================================================================================

# Problema "tabuada"
# Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10, conforme exemplo. 

N = int(input("deseja a tabuada de qual valor ? "))

for i in range(1, 11):
    soma = N * i
    print(f"{N} x {i} = {soma}")

#============================================================================================================

# Problema "soma_impares" (adaptado de URI 1071)
# Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números
# impares entre eles

# forma1 - dois pedidos, duas entradas ⤵️

x = int(input('digite o primeiro numero: '))
y = int(input('digite o segundo numero: '))

# forma2 - um pedido, dua entradas⤵️

x = int(input('digite dois numeros:\n'))
y = int(input())

if x > y:
    troca = x
    x = y
    y = troca

soma = 0

for i in range (x + 1, y):
    if i % 2 != 0:
        soma = soma + i
print(f"SOMA DOS IMPARES = {soma}")

#==============================================================================================================================================

# repetindo ENQUANTO a resposta for "s" ⤵️

c = float(input("digite a temperatura em celsius: ")) 
f = 9.0 * c / 5.0 + 32.0

print(f"equivalente em fahrenheit: {f:3.1f}")
resp = input("deseja repetir? (s/n)? ")

while resp == "s":
    c = float(input("digite a temperatura em celsius: "))
    f = 9.0 * c / 5.0 + 32.0

    print(f"equivalente em fahrenheit: {f:3.1f}")
    resp =  input("deseja repetir (s/n ? )")


# repetindo ATE a resposta se diferente de "s"⤵️

while True:
    c = float(input("digite a temperatura em celsius: ")) 
    f = 9.0 * c / 5.0 + 32.0
   
    print(f"equivalente em fahrenheit: {f:.1f}")

    resp = input("deseja repetir (s/n) ? ")
    if resp != "s":
        break


#========================================================================================================

# Problema "senha_fixa" (adaptado de URI 1114)
# Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
# senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
# for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
# encerrado. Considere que a senha correta é o valor 2002. 

senha = int(input("digite a sua senha: "))
while senha != 2002:
    senha = int(input("senha invalida! tente novamente: ")) 
print("acesso permitido!")

#===========================================================================

# Problema "quadrante" (adaptado de URI 1115)
# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no
# sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O
# algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem
# escrever mensagem alguma). 

print("digite os valores das coordenadas X e Y:")
x = int(input("x: "))
y = int(input("y: "))

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("Quadrante Q1")
    elif x < 0 and y > 0:
        print("Quadrante Q2")
    elif x < 0 and y < 0:
        print("Quadrante Q3")
    else:
        print("quadrante Q4") 

    print("digite os valores das coordenadas X e Y:")
    x = int(input("x: "))
    y = int(input("y: "))
print("fim.")

#==========================================================================================================

# Problema "validacao_de_nota" (adaptado de URI 1117)
# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a
# média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
# intervalo [0,10]). Cada nota deve ser validada separadamente. 

nota1 = float(input("digite a primeira nota: "))

while nota1 <0 or nota1 >10:
    print("valor invalido! digite novamente.")
    nota1 = float(input())

nota2 = float(input("digite a segunda nota: "))

while nota2 <0 or nota2 >10:
    print("valor invalido! digite novamente.")
    nota2 = float(input())

media = (nota1 + nota2) / 2
print("media: ", media)

#===================================================================================================================================

# Problema "combustivel" (adaptado de URI 1134)
# Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
# Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma:
# 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a
# 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o
# código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem
# como as quantidades de cada combustível. 

alcool = 0
gasolina = 0
diesel = 0
codigo = int(input("INFORME UM CODIGO (1, 2, 3) OU 4 PARA PARAR: "))

while codigo != 4:
    if codigo == 1:
        alcool = alcool + 1
    elif codigo == 2:
        gasolina = gasolina + 1
    elif codigo == 3:
        diesel = diesel + 1
    codigo = int(input("INFORME UM CODIGO (1, 2, 3) OU 4 PARA PARAR: "))

print("MUITO OBRIGADO.")
print("alcool: ", alcool)
print("gasolina: ", gasolina)
print("diesel: ", diesel)

#==================================================================================================================================

# Problema "pares_consecutivos" (adaptado de URI 1159)
# O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X
# for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X
#  se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação:
# 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a
# soma de 12+14+16+18+20

x = int(input("digite um numero inteiro: "))

while x != 0:
    if x % 2 != 0:
        x = x + 1
    soma = (5 * x) + 20
    print("soma = ", soma)
    x = int(input("digite um numero inteiro: "))

#===========================================================================================================================================


# Problema "dentro_fora" (adaptado de URI 1072)
# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo,
# conforme exemplo 

n = int(input("quantos numeros voce vai digitar? "))
dentro = 0
fora = 0

for i in range(0, n):
    x = int(input("digite um numero: "))
    if x >= 10 and x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print(f"{dentro} DENTRO")
print(f"{fora} FORA")

#==================================================================================================================================



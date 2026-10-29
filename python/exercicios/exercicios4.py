#Problema "negativos"
#Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
#e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos.

n = int(input("QUANTOS NUMEROs VOCE VAI DIGITAR (max.10) ?"))
vet = [0] * n

for i in range(n):
   vet[i] = float(input("DIGITE UM NUMERO: "))

print("NUMEROS NEGATIVOS:")

for i in range(n):
   if vet[i] <0:
       print(vet[i])

#===============================================================================================================================

# Problema "soma_vetor"
# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
# - Imprimir todos os elementos do vetor
# - Mostrar na tela a soma e a média dos elementos do vetor  

n = int(input("QUANTOS NUMEROS VOCE VAI DIGITAR? (max.10) "))
vet = [0] * n

for i in range(n):
    print("DIGITE UM NUMERO: ", end="")
    vet[i] = float(input())

print()
print("VALORES = ", end="")

for i in range(0, n):
    print(f"{vet[i]:3}", end=" ")

print()

soma = 0
for i in range(0, n):
    soma += vet[i]

print(f"SOMA = {soma:.2f}")
media = soma / n
print(f"MEDIA = {media:.2f}")

#=======================================================================================================================

#Problema "alturas"
# Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
# tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
# bem como os nomes dessas pessoas caso houver. 

pessoa = int(input("QUANTAS PESSOAS SERAO DIGITADAS? "))
nome = [""] * pessoa
idade = [0] * pessoa
altura = [0.0] * pessoa

for i in range(pessoa):
    print("DADOS DA ", i+1, "PESSOA:")
    nome[i] = input("NOME: ")
    idade [i] = int(input("IDADE: "))
    altura [i] = float(input("ALTURA: "))

soma = 0
for i in range(pessoa):
    soma += altura[i]

media = soma / pessoa
print(f"ALTURA MEDIA: {media:.2f}")

cont = 0

for i in range(pessoa):
    if idade[i] < 16:
        cont += 1

porcent = cont * 100 / pessoa
print(f"PESSOAS COM MENOS DE 16 ANOS: {porcent:.1f}%")

for i in range(pessoa):
    if idade[i] < 16:
        print(nome[i])

#===========================================================================================================================

# Problema "numeros_pares"
# Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
# tela todos os números pares, e também a quantidade de números pares. 




n = int(input("QUANTOS NUMEROS VOCE VAI DIGITAR ? "))
vet = [0] * n

for i in range(n):
    vet[i] = int(input("DIGITE UM NUMERO: "))

qtepares = 0
print()
print("NUMEROS PARES: ")

for i in range(n):
    if vet[i] % 2 == 0:
        print(vet[i], end=" ")
        qtepares += 1 
print()
print("QUANTIDADE DE PARES = ", qtepares)

#============================================================================================================================

# Problema "maior_posicao"
# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
# o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
# considerando a primeira posição como 0 (zero).

n = int(input("QUANTOS NUMEROS VOCE VAI DIGITAR?" ))
vet = [0.0] * n

for i in range(n):
    vet[i] = float(input("DIGITE UM NUMERO: "))

maior = vet[0]
posicao = 0
for i in range(1, n):
    if vet[i] > maior:
        maior = vet[i]
        posicao = i
print()
print(f"MAIOR VALOR: {maior:.2f}")
print(f"POSICAO DO MAIOR VALOR = {posicao}")

#=============================================================================================================================

# Problema "soma_vetores"
# Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
# terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
# o vetor C gerado. 

valor = int(input("QUANTOS VALORES VAI TER CADA VETOR? "))
vetorA = [0] * valor
vetorB = [0] * valor
vetorC = [0] * valor

for i in range(valor):
    vetorA[i] = int(input("DIGITE OS VALORES DO VETOR A: "))
print()
for i in range(valor):
    vetorB[i] = int(input("DIGITE OS VALORES DO VETOR B: "))

for i in range(valor):
    vetorC[i] = vetorA[i] + vetorB[i]

print("VETOR RESULTANTE: ")

for i in range(valor):
    print(vetorC[i])

#============================================================================================================================

# Problema "abaixo_da_media"
# Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
# mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos
# os elementos do vetor que estejam abaixo da média, com uma casa decimal cada

elemento = int(input("QUANTOS ELEMENTOS VAI TER VETOR ? "))
vet = [0] * elemento

for i in range(elemento):
    vet[i] = float(input("DIGITE UM NUMERO: "))

soma = 0

for i in range(elemento):
    soma += vet[i]

media = soma /elemento
print()

print(f"MEDIA DO VETOR = {media:.3f}")
print('ELEMENTOS ABAIXO DA MEDIA: ')
for i in range(elemento):
    if vet[i] < media:
        print(f"{vet[i]:.1}")

#===========================================================================================================================

# Problema "media_pares "
# Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média
# aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for
# digitado, mostrar a mensagem "NENHUM NUMERO PAR"

n = int(input("QUANTOS ELEMENTOS VAI TER O VETOR ?"))
vetor = [0] * n

for i in range(n):
    vetor[i] = float(input("DIGITE UM NUMERO: "))

soma = 0
contpares = 0

for i in range(n):
    if vetor[i] % 2 ==0:
        soma += vetor[i]
        contpares += 1

if contpares == 0:
    print("NENHUM NUMERO PAR")
else:
    media = soma / contpares
    print(f"MEDIA DO PARES = {media:.1f}")

#=============================================================================================================================================

# Problema "mais_velho"
# Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
# devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
# da pessoa mais velha.

pessoas = int(input("QUANTAS PESSOAS VOCE VAI DIGITAR? "))
vetnome = [0] * pessoas
idadevet = [0] * pessoas

for i in range(pessoas):
    print("DADOS DA", i+1, "PESSOA: ")
    vetnome[i] = input("NOME: ")
    idadevet[i] = int(input("IDADE: "))

maioridade = idadevet[0]
posmaior = 0
for i in range(pessoas):
    if idadevet[i] > maioridade:
        maioridade = idadevet[i]
        posmaior = i

print("PESSOA MAIS VELHA = ", vetnome[posmaior])

#=========================================================================================================

# Problema "aprovados"
# Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
# no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir
# os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou
# igual a 6.0 (seis). 


n = int(input("QUANTOS ALUNOS SERAO DIGITADOS ? "))

vetnome = [""] * n
nota1 = [0.0] * n
nota2 = [0.0] * n


for i in range(n):
    print("DIGITE NOME, PRIMEIRA E SEGUNDA NOTA DO" , i+1, "ALUNO: ")
    vetnome[i] = input()
    nota1[i] = float(input())
    nota2[i] = float(input())

print("ALUNOS APROVADOS: ")

for i in range(n):
    media = (nota1[i] + nota2[i]) / 2
    if media >= 6:
        print(vetnome[i])

#========================================================================================================================

# Problema "dados_pessoas"
# Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
# que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
# de homens

pessoas = int(input("QUANTAS PESSOAS SERAO DIGITADA? "))
altura = [0.0] * pessoas
genero = [""] * pessoas

for i in range(pessoas):
    altura[i] = float(input(f"ALTURA DA {i+1} PESSOA: "))
    genero[i] = input(f"GENERO DA {i+1} PESSOA (F ou M): ").upper()

maioralt = altura[0]
menoralt = altura[0]

for i in range(pessoas):
    if altura[i] > maioralt:
        maioralt = altura[i]
    if altura[i] < menoralt:
        menoralt = altura[i]

print("MAIOR ALTURA =",maioralt)
print("MENOR ALTURA =",menoralt)

soma = 0
contf = 0

for i in range(pessoas):
    if genero[i] == "F":
        soma += altura[i]
        contf += 1

if contf == 0:
    print("IMPOSSIVEL CALCULAR A ALTURA MEDIA DAS MULHERES.")
else: 
    media = soma / contf
    print(f"MEDIA DAS ALTURAS DAS MULHERES {media:.2f}")

contm = pessoas - contf
print("NUMEROS DE HOMENS = ",contm)

#=============================================================================================================

# Problema "comerciante"
# Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. Para isto,
# mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de compra e preço de
# venda das mesmas. Fazer um programa que leia tais dados e determine e escreva quantas mercadorias
# proporcionaram:
#  lucro < 10%
#  10% ≤ lucro ≤ 20%
#  lucro > 20%
# Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como
# o lucro total

prod = int(input("SERAO DIGITADOS QUANTOS PRODUTOS? "))
nome = [""] * prod
compra = [0.0] * prod
venda = [0.0] * prod

for i in range(prod):
    print("produto", i+1, ":")
    nome[i] = input("nome: ")
    compra[i] = float(input("preco de compra: "))
    venda[i] = float(input("preco de venda: "))

abaixo = 0
entre = 0
acima = 0

for i in range(prod):
    lucro = venda[i] - compra[i]
    porcentlucro = lucro * 100 / compra[i]
    if porcentlucro <10:
        abaixo += 1
    else:
        if porcentlucro <= 20:
            entre += 1
        else:
            acima += 1

totalcompra = 0
totalvenda = 0

for i in range(prod):
    totalcompra += compra[i]
    totalvenda += venda[i]

lucro = totalvenda - totalcompra

print("RELATORIO:")
print("LUCRO ABAIXO DE 10%: ",abaixo )
print("LUCRO ENTRE 10% E 20%: ",entre)
print("LUCRO ACIMA DE 20%: ", acima)
print(f"VALOR TOTAL DE COMPRA: {totalcompra:.2f}")
print(f"VALOR TOTAL DE VENDA: {totalvenda:.2f}")
print(f"LUCRO TOTAL: {lucro:.2f}")

# Problema "diagonal_negativos"
# Fazer um programa para ler um número inteiro N (máximo = 10) e uma matriz quadrada de ordem N
# contendo números inteiros. Em seguida, mostrar a diagonal principal e a quantidade de valores
# negativos da matriz. 

n =  int(input("QUAL A ORDEM DA MATRIZ? "))
matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        print("ELEMENTO[", i, ",", j, "]: ", end= "")
        valor = int(input()) 
        linha.append(valor)
    matriz.append(linha)

print("DIAGONAL PRINCIPAL:")

for i in range(n):
    print(matriz[i][i], end=" ")

print()
cont = 0

for i in range(n):
    for j in range(n):
        if matriz[i][j] < 0:
            cont += 1

print("QUANTIDADE DE NEGATIVOS =", cont)

#===================================================================================================================

# Problema "soma_linhas"
# Fazer um programa para ler dois números inteiros M e N (máximo = 10). Em seguida, ler uma matriz
# de M linhas e N colunas contendo números reais. Gerar um vetor de modo que cada elemento do vetor
# seja a soma dos elementos da linha correspondente da matriz. Mostrar o vetor gerado. 

linha = int(input('QUAL A QUANTIDADE DE LINHAS DA MATRIZ? '))
coluna = int(input('QUAL A QUANTIDADE DE COLUNAS DA MATRIZ? '))

mat = []
vet = []
for i in range(linha):
    print("DIGITE OS ELEMENTOS DA", i +1, "A LINHA: ")
    mat.append([])
    for j in range(coluna):
        mat[i].append(float(input()))

for i in range(linha):
    vet.append (0) 
    for j in range(coluna):
        vet[i] += mat[i][j]

print("VETOR GERADO:")
for i in range(linha):
    print(f"{vet[i]:.1f}")
    
#=================================================================================================================

# Problema "negativos_matriz"
# Ler dois números M e N (máximo = 10), e depois ler uma matriz MxN de números inteiros, conforme
# exemplo. Em seguida, mostrar na tela somente os números negativos da matriz. 

m = int(input('QUAL A QUANTIDADE DE LINHAS DA MATRIZ? '))
n = int(input('QUAL A QUANTIDADE DE COLUNAS DA MATRIZ? '))

mat = []

for i in range(m):
    mat.append([])
    for j in range(n):
        valor = int(input(f"ELEMENTO[{i},{j}]: "))
        mat[i].append(valor)
print()
print("VALORES NEGATIVOS: ")

for i in range(m):
    for j in range(n):
        if mat[i][j] < 0:
            print(mat[i][j])

#===========================================================================================================================================

# Problema "cada_linha"
# Ler um inteiro N e uma matriz quadrada de ordem N (máximo = 10). Mostrar qual o maior elemento
# de cada linha. Suponha não haver empates.

n = int(input("QUAL A ORDEM DA MATRIZ? "))
matriz = []

for i in range(n):
    matriz.append([])
    for j in range(n):
        valor = float(input(f"ELEMENTO[{i},{j}]: "))
        matriz[i].append(valor)

print('MAIOR DE CADA LINHA: ')

for i in range(n):
    maior = matriz [i][0]
    for j in range(n):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    print(maior)        

#======================================================================================================================

# Problema "soma_matrizes"
# Fazer um programa para ler duas matrizes de números inteiros A e B, contendo de M linhas e N colunas
# cada (M e N máximo = 10). Depois, gerar uma terceira matriz C onde cada elemento desta é a soma
# dos elementos correspondentes das matrizes originais. Imprimir na tela a matriz gerada. 

n = int(input("QUANTAS LINHAS VAI TER CADA MATRIZ ? "))
m = int(input("QUANTAS COLUNAS VAI TER CADA MATRIZ ? "))
A = []
B = []
C = []

print("DIGITE OS VALORES DA MATRIZ A: ")

for i in range(n):
    A.append([])
    for j in range(m):
        valor = int(input(f"ELEMENTO[{i},{j}]: "))
        A[i].append(valor)

print("DIGITE OS VALORES DA MATRIZ B: ")

for i in range(n):
    B.append([])
    for j in range(m):
        valor = int(input(f"ELEMENTO[{i},{j}]: "))
        B[i].append(valor)

for i in range(n):
    C.append([])
    for j in range(m):
        C[i].append(A[i][j] + B[i][j])

print("MATRIZ SOMA: ")

for i in range(n):
    for j in range(m):
        print(C[i][j], end=" ")

    print()

#======================================================================================================================

# Problema "acima_diagonal"
# Ler um inteiro N (máximo = 10) e uma matriz quadrada de ordem N
# contendo números inteiros. Mostrar a soma dos elementos acima da
# diagonal principal. Um exemplo de números acima da diagonal
# principal é mostrado ao lado (no caso as células com fundo cinza).

m = int(input("QUAL A ORDEM DA MATRIZ? "))
matriz = []

for i in range(m):
    matriz.append([])
    for j in range(m):
        valor = int(input(f"ELEMENTO[{i},{j}]: "))
        matriz[i].append(valor)

soma = 0

for i in range(m):
    for j in range(m):
        if j > i:
            soma += matriz[i][j]
print()
print(f"SOMA ACIMA DA DIAGONAL PRINCIPAL: {soma}")

#=================================================================================================

# Problema "matriz_geral"
# Ler uma matriz quadrada de ordem N (máximo = 10), contendo números reais. Em seguida, fazer as
# seguintes ações:
# a) calcular e imprimir a soma de todos os elementos positivos da matriz.
# b) fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos os elementos desta linha.
# c) fazer a leitura do índice de uma coluna da matriz e, daí, imprimir todos os elementos desta coluna.
# d) imprimir os elementos da diagonal principal da matriz.
# e) alterar a matriz elevando ao quadrado todos os números negativos da mesma. Em seguida imprimir
# a matriz alterada.


n = int(input("QUAL A ORDEM DA MATRIZ? "))
matriz = []


for i in range(n):
    matriz.append([])
    for j in range(n):
        valor = float(input(f"ELEMENTO[{i},{j}]: "))
        matriz[i].append(valor)

soma = 0

for i in range(n):
    for j in range(n):
        if matriz[i][j] > 0:
            soma += matriz[i][j]

print(f"\nSOMA DOS POSITIVOS: {soma:.1f}")
print()

linha = int(input("ESCOLHA UMA LINHA: "))
print("LINHA ESCOLHIDA:")
for j in range(n):
    print(f"{matriz [linha][j]:.1f}", end=" ")
print()
print()

coluna = int(input("ESCOLHA UMA COLUNA: "))
print("COLUNA ESCOLHIDA: ")
for i in range(n):
    print(f"{matriz [i][coluna]:.1f}", end=" ")
print()
print()

print("DIAGONAL PRINCIPAL: ")
for i in range(n):
    print(f"{matriz[i][i]}", end=" ")
print()

for i in range(n):
    for j in range(n):
        if matriz[i][j] < 0:
            matriz[i][j] = matriz[i][j] * matriz[i][j]

print()
print("MATRIZ ALTERADA: ")

for i in range(n):
    for j in range(n):
        print(f"{matriz[i][j]:.1f}", end=" ")
    print()
 










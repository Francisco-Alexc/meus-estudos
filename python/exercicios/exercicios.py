
#Problema "idades"
#Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
#nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo


nome = input("digite o nome: ")
idade = int(input("digite a idade: "))
nome_2 = input("digite o nome: ")
idade_2 = int(input("digite a idade: "))


media_idade = (idade + idade_2) /2

print("nome: " +str(nome))
print(f"idade: {idade}")
print("nome: "+str(nome_2))
print(f"idade: {idade_2}")
print(f"a idade media de {nome} e {nome_2} e de {media_idade:.1f} anos.")

#=====================================================================



#Problema "soma"
#Fazer um programa para ler dois valores inteiros X e Y, e depois mostrar na tela o valor da soma destes
#números. 

valor_de_x = int(input("digite o valor: "))
valor_de_y = int(input("digite o valor:"))

soma = valor_de_x + valor_de_y

print(f"valor: {valor_de_x}")
print(f"valor: {valor_de_y}")
print(f"soma total: {soma}")

#================================================================

#Problema "troco"
#Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
#O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
#e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
#mostrar o valor do troco a ser devolvido ao cliente. 

preco_unitario = float(input("digite o preco do produto: R$ "))
quantidade = int(input("digite a quantidade: "))
valor_recebido = float(input("digite o valor recebido: R$ "))

total = valor_recebido - (preco_unitario * quantidade)

print(f"preco unitario do produto: R$ {preco_unitario:.2f}")
print(f"quantidade de produto: {quantidade}")
print(f"dinheiro recebido: R$ {valor_recebido:.2f}" )
print(f"troco = R$ {total:.2f}")

#==================================

#Problema "circulo"
#Fazer um programa para ler o valor "r" do raio de um círculo, e depois mostrar o valor da área do
#círculo com três casas decimais. A fórmula da área do círculo é a seguinte: 𝑎𝑟𝑒𝑎 = 𝜋. 𝑟
#ଶ
#. Você pode
#usar o valor de 𝜋 fornecido pela biblioteca da sua linguagem de programação, ou então, se preferir, use
#diretamente o valor 3.14159.

import math

raio = float(input("digite o valor do raio do circulo: "))

area = math.pi * raio ** 2

print(f"valor do circulo: {raio}")
print(f"area: {area:.3f}")

#========================================

#Problema "pagamento"
#Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
#quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
#uma mensagem explicativa, conforme exemplo. 

nome = input("digite o nome: ")
valor_da_hora_trabalhada = float(input("digite o valor da hora: "))
horas_trabalhadas = float(input("digite as horas trabalhadas: "))

soma_horas = valor_da_hora_trabalhada * horas_trabalhadas

print(f"Nome: {nome}")
print(f"valor da hora: {valor_da_hora_trabalhada:.2f}")
print(f"Horas trabalhadas: {horas_trabalhadas:.2f}")
print(f"O pagamento para {nome} deve ser {soma_horas:.2f} ")

#================================================

#Problema "consumo"
#Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
#combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
#médio do carro, com três casas decimais. 

Distancia_percorrida = float(input("distancia percorrida: "))
Combustível_gasto = float(input("consumo gasto: "))

calculo_medio = Distancia_percorrida / Combustível_gasto

print(f"distancia percorrida: {Distancia_percorrida} ")
print(f"combustivel gasto: {Combustível_gasto}")
print(f"consumo medio = {calculo_medio:.3f}")

#=========================================================

#Problema "medidas"
#Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
#com quatro casas decimais):
#a) a área do quadrado que tem lado A
#b) a área do triângulo retângulo que base A e altura B
#c) a área do trapézio que tem bases A e B, e altura C 


medidaA = float(input("digite a medida A: "))
medidaB = float(input("digite a medida B: "))
medidaC = float(input("digite a medida C: "))

calculo_medidaA =  (medidaA * medidaA)
calculo_medidaB = (medidaB + medidaB)
calculo_medidaC = (medidaA + medidaB) * medidaC /2

print(f"Area do quadrado: {calculo_medidaA:.4f}")
print(f"Area do triangulo: {calculo_medidaB:.4f}  ")
print(f"Area do trapezio: {calculo_medidaC:.4f} ")

#====================================================
#Problema "duracao"
#Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
#formato horas:minutos:segundos.  


duracao = int(input("digite a duracao em segundos: "))

horas = duracao // 3600
resto = duracao % 3600

minutos = resto // 60
segundos = resto % 60

print(f"{horas}:{minutos}:{segundos}")





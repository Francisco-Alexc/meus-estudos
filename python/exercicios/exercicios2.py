idade = int(input("digite sua idade: "))


if idade >= 18: 
    tem_ingresso = input("tem ingresso? ")
    if tem_ingresso == "sim":
        print("pode entrar.")
    elif tem_ingresso == "nao":
        print("adquira um ingresso.")
else:
    print("venda proibida para menores.")

#=============================================================


hora = int(input("digite a hora:"))

if hora <12:
    print("bom dia.")

elif hora >= 12  and hora <= 18:
    print("boa tarde.")

else:
    print("boa noite.")    

#==============================================================

#Problema "notas"
#Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
#uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
#ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
#mensagem "REPROVADO", conforme exemplos. 
 
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

nota_final = nota1 + nota2
print(f"Nota final: {nota_final:.1f}")

if nota_final < 60:
    print("REPROVADO.")

#==========================================================================

#Problema "baskara"
#Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
#de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
#conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem.
 
import math

a = float(input("Coeficiente A: "))
b = float(input("Coeficiente B: "))
c = float(input("Coeficiente C: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Esta equacao nao possui raizes reais.")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"x1 = {x1:.4f}")
    print(f"x2 = {x1:.4f}")

#=======================================================

#Problema "menor_de_tres"
#Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
#números lidos. Em caso de empate, mostrar apenas uma vez. 

valor1 = int(input("Primeiros valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))

if valor1 < valor2 and valor1 < valor3:
    menor = valor1
elif valor2 < valor3:
   menor = valor2
else:
    menor = valor3

print(f"menor = {menor}")    

#===========================================================

#Problema "operadora"
#Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
#telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
#ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago. 

plano = int(input("Digite a quantidade de minutos: "))
valor = 50

if plano <=100:
    print(f"valor a pagar: R$ {valor:.2f}")
elif plano >100:
     print(f"valor a pagar: R$ {valor + 2 * (plano - 100):.2f}")

#==================================================================

#Problema "troco_verificado"
#Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
#O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
#e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
#ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
#valor restante conforme exemplo.

preco = float(input("preco unitario: "))
quntidade = int(input("quantidade: "))
dinheiro =  float(input("dinheiro recebido: "))

soma = (quntidade * preco)

if dinheiro < soma:
    falta = soma - dinheiro
    print(f"dinheiro insficiente. faltam  R$ {falta:.2f}")
else:
    troco = dinheiro - soma
    print(f"troco: R$ {troco:.2f}")    

#===========================================================

#Problema "glicose"                                          Classificação    |    Glicose
#Fazer um programa para ler a quantidade de glicose.           Normal         |   Até 100 mg/dl
#no sangue de uma pessoa e depois mostrar na tela a.          Elevado         | Maior que 100 até
#classificação desta glicose de acordo com a tabela de.                       | 140 mg/dl
#referência ao lado.                                           Diabetes       | Maior de 140 mg/dl 

medida = float(input("digite a medida da glicose: "))

if medida <= 100: 
  print("classificacao: normal")
elif medida <= 140:
  print("classificacao: elevado")
else:
  print("classificado: diabetes")

#==========================================================

#Problema "dardo"
#No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
#Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual
#foi a maior. 

distancia1 = float(input("digite a distancias: "))
distancia2 = float(input("digite a distancias: "))
distancia3 = float(input("digite a distancias: "))

if distancia1 > distancia2 and distancia1 > distancia3:
    maior = distancia1
elif distancia2 > distancia3:
    maior = distancia2
else:
  maior = distancia3

  print(f"maior distancia: {maior:.2f}")

#======================================================

#Problema "temperatura"
#Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
#isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
#informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com 

escala = input("voce vai digitar a temperatura em qual escala (C/F) ?")

if escala == "F" or escala == "f":
    fahrenheit = float(input("digite a temperaturae em fahrenheit: "))
    celsius = (5/9) * (fahrenheit - 32)
    print(f"temperatura equivalente em celsius: {celsius:.2f}")
else:
    celsius = float(input("digite a temperatura em ceusius: "))
    fahrenheit = celsius * 9 / 5 + 32    
    print(f"a temperatura eqivalenete em fahrenheit: {fahrenheit:.2f} ")

#======================================================================



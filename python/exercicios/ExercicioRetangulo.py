import math

teclado = input ("digite o produto: ")
preco =  float(input("digite o preco: "))
quantidade = int(input("digite a quantidade: "))
frete = float(input("digite o frete: "))
comprimento_caixa = float(input("digite o comprimento da caixa: "))
largura_caixa = float(input("digite a largura da caixa: "))

area_da_caixa =  (comprimento_caixa * largura_caixa)
diagonal = math.sqrt ( comprimento_caixa **2 + largura_caixa **2 )
preco_final = frete + (preco * quantidade)

print(f"produto: {teclado}")
print(f"preco: R$  {preco:.2f}")
print(f"quantidade: {quantidade}")
print(f"frete: R$  {frete:.2f}")
print(f"area da caixa: {area_da_caixa:.2f}")
print(f"diagonal da caixa: {diagonal:.4f}")
print(f"valor final: R$ {preco_final:.2f} ")
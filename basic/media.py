qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor #* soma dos valores
    qtd = qtd + 1 #* contador da quantidade de valores inseridos
    valor = float(input("Digite um valor: ")) #* entrada de valores

#? caso digite um valor negativo o laco encerra
media = soma / qtd 
print(f"\nTotal da soma: {soma}")
print(f"\nQuantidade de valores digitados: {qtd}")
print(f"\nMedia dos valores: {media}")
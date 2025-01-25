#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Digite o valor do seu produto:'))
desconto = produto * 5 / 100
nvalor = produto - desconto
print('O valor do seu produto é R${:.2f}. O valor do produto com desconto de 5% é de: R${:.2f}.'.format(produto,nvalor))
#Outra forma
produto = float(input('Digite o valor do seu produto:'))
novo = produto - (produto * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(produto,novo))
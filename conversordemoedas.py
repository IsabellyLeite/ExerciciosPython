#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares e Euros ela pode comprar.
#Considerando os valores atuais do dia 25/01/25:
#Dolar: 1 US$ = 5.91
#Euro: 1 € = 6.21
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real/5.91
euro = real/6.21
print('Com {:.2f}R$, você consegue comprar US${:.2f} e €{:.2f}.'.format(real,dolar,euro))
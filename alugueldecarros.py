#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos Km foram percorridos durante o aluguel?'))
dias = int(input('Por quantos dias o carro foi alugado?'))
p = (km * 0.15) + (dias * 60)
print('O valor a pagr é R$ {}'.format(p))
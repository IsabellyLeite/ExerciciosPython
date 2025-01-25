s = float(input('Qual o salário do funcionário? R$'))
ns = s + (s * 15 / 100)
print('O salário de R${:.2f} com o reajuste de mais 15% fica: R${:.2f}.'.format(s,ns))
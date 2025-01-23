#Desenvolva um programa que leia duas notas de um aluno. Calcule e mostre a sua média.
n1 = float(input('Digite sua nota do primeiro semestre:'))
n2 = float(input('Digite sua nota do segundo semestre:'))
m = ((n1 + n2) /2)
print('Sua média é : {:.1f}.'.format(m))
#Outra forma
n1 = float(input('Digite sua nota do primeiro semestre:'))
n2 = float(input('Digite sua nota do segundo semestre:'))
print('Sua média é : {:.1f}.'.format((n1+n2)/2))

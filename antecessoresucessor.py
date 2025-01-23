#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.
n = int(input('Digite um número:'))
a = n - 1
s = n + 1
print('O sucessor deste número é {} e o antecessor é {}.'.format(s,a))
#Outra forma
n = int(input('Digite um número:'))
print('O sucessor deste número é {} e o antecessor é {}.'.format((n+1),(n-1)))
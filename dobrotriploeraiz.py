#Crie um algoritmo que leia um número e mostre o seu dobro , triplo e raiz quadrada.
n = int(input('Digite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro deste número é {}, o triplo é {} e a raiz quabrada é {:.2f}.'.format(d,t,r))
#Outra forma
n = int(input('Digite um número:'))
print('O dobro deste número é {}, o triplo é {} e a raiz quadrada é {:.2f}.'.format((n*2),(n*3),(n**(1/2))))
#Se quiser acrescentar quebras entre as operações basta acrescentar o \n
#O :.2f quer dizer que serão mostradas 2 casas decimais flutuantes. 
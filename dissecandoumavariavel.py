#Faça um programa que leia algo no teclado e mostra na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
algo = input('Escreva algo:')
print('O tipo primitivo desse valor é:', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?' , algo.isnumeric())
print('É alfabetico?' , algo.isalpha())
print('É alfanúmerico?' , algo.isalnum())
print('Está em maiúsculas?' , algo.isupper())
print('Está em minúsculas?' , algo.islower())
print('Está capitalizada?' , algo.istitle())
#Válido lembrar que o "algo" é sempre o objeto, ele possui características e realiza funcionaliadades(atributos e métodos).
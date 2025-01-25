#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
#Sabendo que cada litro de tinta , pinta uma área de 2m quadrados.
largura = float(input('Qual a largura da parede?'))
altura = float(input("Qual a altura da parede?"))
area = largura * altura
tinta = area / 2
print('Sua parede tem dimensões de {} X {} e sua área é {}m².\nQuantidade de tinta necessaria: {}L.'.format(largura,altura,area,tinta))

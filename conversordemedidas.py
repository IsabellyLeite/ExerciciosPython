#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
medida = float(input('Digite uma distância em metros:'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A distância corresponde a:\n{}km.\n{}hm.\n{}dam.\n{:.0f}dm.\n{:.0f}cm.\n{:.0f}mm.'.format(km,hm,dam,dm,cm,mm))
#Outra forma
medida = float(input('Digite uma distância em metros:'))
print('A distancia corresponde a:\n{}km.\n{}hm.\n{}dam.\n{:.0f}dm.\n{:.0f}cm.\n{:.0f}mm.'.format((medida/1000),(medida/100),(medida/10),(medida*10),(medida*100),(medida*1000)))
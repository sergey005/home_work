import math
from decimal import *

while True:
	N =int(input('Введите количество знаков после запятой(0-1000): '))
	if 0<=N<=1000:
		break
	else:
		print('Вы ввели число не входящее в диапазон 0-1000')

precision = 30 #Для того, чтобы последние числа не округлялись 

e=Decimal(0)
getcontext().prec = N+precision # Указываем какая точность 

#Нахождение числа е как сумму ряда
for i in range(N+precision):
	e+=Decimal(1)/math.factorial(i)

print(str(e)[0:N+2])

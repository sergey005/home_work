
'''
Задание:
Вычислить число PI с точностью до N цифр** - 
Введите число, и программа вычисляет число &pi; (пи) с заданной точностью. Установите ограничение, 
тобы не вводить слишком большое значение параметра N.

'''


from decimal import *


while True:
	N =int(input('Введите количество знаков после запятой(0-1000): '))
	if 0<=N<=1000:
		break
	else:
		print('Вы ввели число не входящее в диапазон 0-1000')


precision = 30  #Для того, чтобы последние числа не округлялись 

getcontext().prec = N+precision # Указываем какая точность 

#формула Бэйли-Боруэйна-Плаффа для нахождения числа pi
pi = Decimal(0)
for i in range(N):
	pi+= (Decimal(1)/(16**i))*((Decimal(4)/((8*i)+1))-(Decimal(2)/((8*i)+4))-(Decimal(1)/((8*i)+5))-(Decimal(1)/((8*i)+6)))
	
print(str(pi)[0:N+2])

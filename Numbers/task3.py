'''
Задание:
Числа Фибоначчи** - 
Введите число, и программа вычисляет числа Фибоначчи - либо которые не большое указанного числа, 
либо вычисляет указанное количество чисел Фибоначчи.
'''

N = int(input("Введите количество чисел Фибоначчи: "))


lt = [0,1]
for i in range(2,N):
	lt.append(lt[i-1]+lt[i-2])

print(lt)
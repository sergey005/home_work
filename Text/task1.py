'''
Fizz Buzz** - 
Напишите программу, которая выводит на экран числа от 1 до 100. Но для тех чисел, которые 
делятся на 3, вместо числа выведите “Fizz”. Для тех чисел, которые делятся на 5, 
выведите “Buzz”. А для чисел, которые делятся и на три, и на пять, выведите “FizzBuzz”.
'''

for j in range(1, 101):
	if j%3 == 0 and j%5 == 0:
		print('FizzBuzz')
	elif j%5 == 0 :
		print('Buzz')       
	elif j%3 == 0 :
		print('Fizz')
	else:
		print(j)



'''
Следующее простое число** - 
Программа продолжает находить простые числа до тех пор, пока пользователь не прекратит просить 
программу показать следующее простое число.
'''


num = 2 # Надо с чего то начать 
def prime_number():	
	global num
	while True:
		flag_prime_number = 0 # Флаг для определения простого числа (если равен 2)
		for i in range(1, num+1): 
			if num%i == 0:
				flag_prime_number += 1
		if flag_prime_number == 2:
			result = num
			num += 1
			break
		else:
			num += 1
	return result


while True:

	print(prime_number())
	st = input('Нажми какую-нибудь клавишу для показа следующего простого числа\n'
		'Или "выход" для выхода из программы: ')
	if st.lower() == 'выход':
		break

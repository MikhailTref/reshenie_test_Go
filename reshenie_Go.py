
'''Напишите приложение, которое печатает на экран числа от 1 до 100. При этом вместо чисел, кратных трем, программа должна выводить слово Fizz,
а вместо чисел, кратных пяти — слово Buzz. Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz'''

for i in range(1,100):		#запускаем цикл от 1 до 100
	if (i % 15 == 0):		#проверяем делиться ли число на 15
		print("FizzBuzz")	#число делиться на 15 - выводим слово FizzBuzz
	elif (i % 5 == 0):		#проверяем делиться ли число на 5
		print("Buzz")		#число делиться на 5 - выводим слово Buzz
	elif (i % 3 == 0):		#проверяем делиться ли число на 3
		print("Fizz")		#число делиться на 3 - выводим  слово FizzBuzz
	else:
		print(i)			#выводим текущее число не удовлетворяющее условиям изменения


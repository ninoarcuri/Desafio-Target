def fibonacci(entrada):
	fib1 = 0
	fib2 = 1
	while fib2 < entrada:
			fib1, fib2 = fib2, fib1 + fib2
	return fib2 == entrada

number = input("Digite um número: ")
try:
	entrada = int(number)
	if fibonacci(entrada):
			print(f"O número {entrada} faz parte da sequência de Fibonacci")
	else:
			print(f"O número {entrada} não faz parte da sequência de Fibonacci")
except ValueError:
	print("Por favor, digite um número válido")
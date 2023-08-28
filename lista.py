#1

num1 = int(input("Digite um numero: "))
ant = num1 - 1
suc = num1 + 1
print(f" o numero esolhido foi {num1}, seu antecessor é {ant} e seu sucessor é {suc}")

#2

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
soma = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
print(f" A soma é {soma}, a subtração é {sub}, a multiplicação é {mul}, a divisão é {div}")

#3

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
boole = (num1 > num2 == True and num1 <= num2 == False)
k = num1 > num2
print(f"{k}")

#4

c = int(input("Digite a temperatura local: "))
cal = c + 1.8 + 32
f = cal
print(f"Fahrenheit {f} e Celsius {c}")

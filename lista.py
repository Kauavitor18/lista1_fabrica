#1

num1 = int(input("Digite um numero: "))
ant = num1 - 1
suc = num1 + 1
print(f" o numero esolhido foi {num1}, seu antecessor é {ant} e seu sucessor é {suc}\n")

#2

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
soma = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
print(f" A soma é {soma}, a subtração é {sub}, a multiplicação é {mul}, a divisão é {div}\n")

#3

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
boole = (num1 > num2 == True and num1 <= num2 == False)
k = num1 > num2
print(f"{k}\n")

#4

c = int(input("Digite a temperatura local: "))
cal = c + 1.8 + 32
f = cal
print(f"Fahrenheit {f} e Celsius {c}\n")

idade = int(input("Digite sua idade: "))
if(idade >= 18):
    print("Você tem idadee suficiente")
else:
    print("Não está apto! \n")

#5

vel = int(input("Velocidade do carro: ")
if( vel > 80):
    print("você foi multado")
else:
    print("Nã foi multado")
    

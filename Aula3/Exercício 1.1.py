"""

Número de Fibonacci

Fn = Fn-1
F1 = 1 ; F2 = 1

"""

def Fibonacci(numero):
    if numero == 0:
        return 0
    if numero == 1 or numero == 2:
        return 1
    else:
        return Fibonacci (numero -1) + Fibonacci (numero-2)

x = int(input("Digite um número para calcular"))
res = Fibonacci(x)
y = 0

while Fibonacci(y) <=res:
    print(Fibonacci(y))
    y += 1
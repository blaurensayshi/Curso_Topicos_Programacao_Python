"""

"""

a = float(input("Qual foi a sua frequência nessa matéria? "))
if a < 75:
    print("Reprovado")
else:
    print("Digite sua nota na P1: ")
    p1 = float(input())
    p2 = float(input("Digite sua nota na P2: "))
    media1 = (p1+p2)/2
if a >= 75 and media1 >= 7:
    print("Aprovado")
elif a >= 75 and media1 < 3:
    print("Reprovado")
elif a >= 75 and media1 >= 3 and media1 < 7:
    print("Prova Final")
    pf = float(input("Digite sua nota na PF: "))
    media2 = (media1+pf)/2
if a >=75 and media1>=3 and media1<7 and media2>=5:
    print("Aprovado")
elif a>=75 and media1>=3 and media1<7 and media2<5:
    print("Reprovado")

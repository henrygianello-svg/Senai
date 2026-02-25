nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

while idade > 0 or idade < 120:
    idade = int(input("idade(anos completos - ate 120 anos)"))
    dias_vividos = idade * 365
    print(f"{nome}, você já viveu {dias_vividos} dias")
else: 
    print("idade digitada incorreta")
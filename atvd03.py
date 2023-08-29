velLimite = 80
valPorKM = 7
try:
    velCarro = int(input("Digite a velocidade do carro: "))
except ValueError:
    print("O valor digitado não é um numero.")
    exit()
if (velCarro > velLimite):
    velExcede = velCarro - velLimite
    valTotal = velExcede * valPorKM
    print(f"Seu carro está {velExcede}km acima da velocidade permitida.\nSua multa é no valor de R${valTotal}")
else:
    print("Seu carro está dentro da velocidade permitida.")

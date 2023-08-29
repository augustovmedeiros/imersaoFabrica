try:
    idade = int(input("Digite a idade: "))
except ValueError:
    print("O valor digitado não é um numero.")
    exit()

if (idade >= 18):
    print("Apto a receber uma CNH")
else:
    print("Inapto a receber um CNH")

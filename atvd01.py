try:
    numero = int(input("Digite um numero: "))
except ValueError:
    print("O valor digitado não é um numero.")
    exit()
antecessor = numero-1
sucessor = numero+1
print(f"O numero foi {numero}, seu antecessor é {antecessor} e seu sucessor é {sucessor}")

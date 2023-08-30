def soma(x: int | float, y: int | float):
    '''SOMA
    x: recebe um int ou float
    y: recebe um int ou float
    
    retorna a soma de X e Y'''
    return x + y

def print_subtracao(x: int | float, y: int | float):
    '''printa o resultado da subtração.

    x: recebe um int ou float
    y: recebe um int ou float'''
    print(f"{x - y}")

def soma_sem_parametro():
    '''retorna a soma de valores predefinidos'''
    x = 5
    y = 5
    return x + y
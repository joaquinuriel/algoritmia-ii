# Encontrar todos los primos circulares del 1 al 100
# ej 17 y 71

primos = []

primosCirculares = []

def esPrimo(n):
    # n = int(n)
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def permutar(n):
    n = str(n)
    for i in range(0, len(n)):
        n[i] = n[-i-1]
    return int(n)

print(permutar(123456))
# Encontrar todos los primos circulares del 1 al 100

def esPrimo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def permutar(n):
    return int(str(n)[::-1])

def esPrimoCircular(n):
    if esPrimo(n):
        m = permutar(n)
        return esPrimo(m)
    return False


lista = [
    n for n in range(1, 101) if esPrimoCircular(n)
]

print(*lista)

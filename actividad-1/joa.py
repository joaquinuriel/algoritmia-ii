# Encontrar todos los primos circulares del 1 al 100

def esPrimo(n):
    # por cada divisor de n, 
    # si n es divisible por ese divisor, 
    # n no es primo
    for i in range(2, n):
        if n % i == 0:
            return False
    # si n no es divisible por ninguno de los divisores anteriores,
    # entonces n es primo
    return True

def permutar(n):
    # convertir N a una cadena de texto
    n = str(n)
    # invertir la cadena de texto
    n = n[::-1]
    # devolver N como un entero 
    return int(n)

def esPrimoCircular(n):
    # m es el inverso a N
    m = permutar(n)
    return esPrimo(n) and esPrimo(m)

lista = [
    # cada numero en el rango 1 al 99 si es primo circular
    n for n in range(1, 100) if esPrimoCircular(n)
]

# imprimir los primos circulares
print(*lista)

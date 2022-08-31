# calcular tribonachi al 1000
# guardar 100 numeros no divisibles por los anteriores y no pares

lista = [
  n + lista[-1] + lista[-2] for n in range(1000) if n < 1000
]


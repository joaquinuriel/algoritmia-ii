# Calcular la serie de Tribonacci que empieza 1,1,1,5,9,17,31, suma los tres primeros números  y genera el siguiente (1+1+1)=3, (3+1+1)=5 y así sucesivamente.

# Generar 100 números  de la serie de Tribonacci y luego generar un diccionario con los números no divisibles por la serie de Tribonacci (exceptuando la division por 1) y que no sean pares.

# La clave del diccionario debe estar compuesta por el ultimo numero no divisible menor, por ejemplo: el numero 7 no es divisible por 5 (que pertenece a la serie y además es el valor más cercano al 7 porqye después viene el 9 y es más grande que 7) por lo tanto  7 no es par y con ello debemos agregarlo al diccionario, entonces el diccionario debe componerse por {"5": 7 }.

# El 7 no se debe dividir por numeros mas grandes en la secuencia, por lo tanto solo debe dividirse hasta el 5.

# Generar solo 100 numeros no divisibles y no pares.

# tribo = secuencia
# x = nuevo numero en tribo
# n = n numero no divisible
# i = iteracion en tribonachi


tribonachi = [1, 1, 1]

while len(tribonachi) != 100:
    x = tribonachi[-1] + tribonachi[-2] + tribonachi[-3]
    tribonachi.append(x)

dic = {"": ""}
counter = 1

# print(*tribo)

def va(n):
    for i in tribonachi:
        if i == 1:
            continue
        if n % i == 0:
            return False
        if n < i:
            break
    return True

while len(dic.keys()) <= 100:
    if va(counter):
        key = list(dic.values())[-1]
        dic[key] = counter
    counter += 2
    
for key, val in dic.items():
    print(key, val)
    

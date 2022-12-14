# Calcular la serie de Tribonacci que empieza 1,1,1,5,9,17,31, suma los tres primeros números  y genera el siguiente (1+1+1)=3, (3+1+1)=5 y así sucesivamente.

# Generar 100 números  de la serie de Tribonacci y luego generar un diccionario con los números no divisibles por la serie de Tribonacci (exceptuando la division por 1) y que no sean pares.

# La clave del diccionario debe estar compuesta por el ultimo numero no divisible menor, por ejemplo: el numero 7 no es divisible por 5 (que pertenece a la serie y además es el valor más cercano al 7 porqye después viene el 9 y es más grande que 7) por lo tanto  7 no es par y con ello debemos agregarlo al diccionario, entonces el diccionario debe componerse por {"5": 7 }.

# El 7 no se debe dividir por numeros mas grandes en la secuencia, por lo tanto solo debe dividirse hasta el 5.
# Generar solo 100 numeros no divisibles y no pares.

def initTribonachi():
    serie = [1, 1, 1]
    while len(serie) != 100:
        serie.append(serie[-1] + serie[-2] + serie[-3])
    return serie


def counterIsValid(counter, serie):
    for i in serie:
        if i == 1:
            continue
        if counter % i == 0:
            return False
        if counter < i:
            break
    return True


def main():
    tribonachi = initTribonachi()
    for i in range(100):
      print(i+1, tribonachi[i])

    dict = {"": ""}
    counter = 1

    while len(dict) != 100:
        lastValue = list(dict.values())[-1]
        if counterIsValid(counter, tribonachi):
            dict[lastValue] = counter
        counter += 2

    for key, val in dict.items():
        print(key, val)
        
main()

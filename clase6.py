def cargar_dic(): 
    dic = {}
    flag = True 
    while flag:
        try:
            nombre = input("Ingrese nombre: ")
            if nombre != "*":
                flag = False
            else:
                edad = int(input("Ingrese edad: "))
                dic[nombre] = edad 
        except ValueError:
            print("Error, ingrese un numero")
    return dic

def calcular_promedio(dic):
    try:
        suma = 0
        for edad in dic.values():
            suma += edad
        promedio = suma / len(dic)
        return promedio
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return 0
    # opcion 2
    # return sum(dic.values()) / len(dic)

def main():
    dic = cargar_dic()
    promedio = calcular_promedio(dic)
    print("El promedio de edad es: ", promedio) 
    # opcion 2
    try:
        promedio = calcular_promedio(dic)
    except Exception: # captura cualquier error
        print("Error", Exception)
    else:
        print(f"el promedio es {promedio}")
    finally:
        print("Fin del programa")

# main()

ciudades = {"cordoba": 2000000, "mendoza": 300000}
# para saber la mayor (valor)
mayor = max(list(ciudades.values()))
# para saber el key..?
# mi opcion...
# ciudades devuelve las keys
# el lambda filtra por valor
# filtramos keys por valores
# devuelve la key 
maximoKey = max(ciudades, key = lambda x: ciudades[x])
# la del profe...
# items devuelve [key, value] por cada item
# el parametro x es [key, value]
# de esa x elegimos value con x[1]
# devuelve (key, value)
maximoItem = max(ciudades.items(), key = lambda x: x[1])
# print(maximoKey, maximoItem)

# Ordenar ciudades

# claves_ordenadas = sorted(ciudades, key = lambda x: ciudades[x])
# ciudades_ordenadas = sorted(ciudades.items(), key = lambda x: x[1])

# print(claves_ordenadas)
# print(ciudades_ordenadas)

# FILTRAR CIUDADES

clavesMayoresA500k = list(filter(lambda x: ciudades[x] > 500000, ciudades))
itemsMayoresA500k = dict(filter(lambda x: x[1] > 500000, ciudades.items()))

# print(clavesMayoresA500k)
# print(itemsMayoresA500k)

dobles = list(map(lambda x: 2*x, [0, 1, 2, 3, 4]))
print(dobles)

# map(funcion, lista) -> <map object>
# list(<map object>) -> lista
# el lambda acepta un arg x que representa cada item
# despues del : devuelve 2 * x para cada item

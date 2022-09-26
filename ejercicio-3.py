while True:
    try:
        cadena = input("Ingrese un numero: ")
        int(cadena)
    except ValueError:
        print("Error, ingrese un NUMERO")
    else:
        break

subcadenas = []

# sub = [
#     cadena[i:j+1]
#     for i in range(len(cadena))
#     for j in range(i, len(cadena))
# ]

for i in range(len(cadena)):
    for j in range(i, len(cadena)):
        subcadenas.append(cadena[i:j+1])

divisibles = []

# div = [
#     int(i)  
#     for i in subcadenas  
#     if int(i) % 3 == 0
# ]

for i in subcadenas:
    if int(i) % 3 == 0:
        divisibles.append(int(i))

print(f"Hay {len(divisibles)} subcadenas divisibles por 3")


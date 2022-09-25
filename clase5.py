# Manejo de errores

# int("hola") -> ValueError
# print(5 / 0) -> ZeroDivisionError

try:
    print(5/0)
    # si hay error el try no corre
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
except BaseException: # cualquier error
    print("Otro error:", BaseException)
else: 
    pass 
    # si no hay errores...
finally:
    pass
    # finalmente, haya o no errores

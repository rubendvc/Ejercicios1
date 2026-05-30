#PAR O IMPAR

#ENTRADA

num = int(input("Ingrese un numero: "))

#SALIDA

if num % 2 == 0:
    print(f"El numero {num} es par.")
else:
    print(f"El numero {num} es impar.")    
    
if num < 0:
    print(f"El numero {num} es negativo")
elif num > 0:
    print(f"El numero {num} es positivo")
else:
    print(f"El numero {num} es cero")        
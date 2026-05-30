nota1 = int (input("Ingrese la primera nota: "))
nota2 = int (input("Ingrese la segunda nota: "))
nota3 = int (input("Ingrese la tercera nota: "))

if nota1 < 0 or nota1 > 20:
    print("Error: Las notas deben estar entre 0 y 20.") 
elif nota2 < 0 or nota2 > 20:
    print("Error: Las notas deben estar entre 0 y 20.")
elif nota3 < 0 or nota3 > 20:
    print("Error: Las notas deben estar entre 0 y 20.") 
else:
    promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 11:
    print(f"El alumno esta aprobado con : {promedio: .2f}")
else:
    print(f"El alumno esta desaprobado con : {promedio: .2f}")
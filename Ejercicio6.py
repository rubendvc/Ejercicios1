dia = int(input("Ingrese un numero entre el 1 y el 7: "))

if dia < 1 or dia > 7:
    print("Error: El número debe estar entre 1 y 7.") 

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
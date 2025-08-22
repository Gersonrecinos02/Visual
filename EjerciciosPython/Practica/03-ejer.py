nombre= input("Ingrese su nombre: ")
notaObtenida = int(input("Ingrese su nota obtenida: "))
puntaje = int(input("Ingrese el puntaje maximo (ejemplo 100: )"))

if notaObtenida > 0: 
    porcentaje = (notaObtenida / puntaje) * 100
    print(f"{nombre}, obtuviste un {porcentaje}%")
else:
    print("Datos incorrectos")
# El programa, dado el costo de un producto y la cantidad de dinero entregada 
# por el cliente, calcula el vuelto que hay que entregarle al mismo

def dinero(costo, cantidad):
    if cantidad >= costo:
        vuelto = cantidad - costo
        print(f"El cambio a entregar es: ${vuelto:.2f}")
    else:
        diferencia = costo - cantidad
        print(f"Dinero insuficiente. Faltan: ${diferencia:.2f}")

# Solicitar datos al usuario
costo_producto = float(input("Ingrese el costo del producto: "))
dinero_cliente = float(input("Ingrese la cantidad entregada por el cliente: "))

# Llamar a la función
dinero(costo_producto, dinero_cliente)

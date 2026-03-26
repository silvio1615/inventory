producto = input("Ingrese nombre del producto: ")

cantidad_invalida = True
while cantidad_invalida:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad < 0:
            print("Error: ingrese un valor positivo para la cantidad.")
        else:
            cantidad_invalida = False
    except ValueError:
        print("Error: ingrese un número entero válido.")

precio_invalido = True
while precio_invalido:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("Error: ingrese un valor positivo para el precio.")
        else:
            precio_invalido = False
    except ValueError:
        print("Error: ingrese un número válido.")

costo_total = precio * cantidad
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: ${precio:.2f}")
print(f"Costo total: ${costo_total:.2f}")

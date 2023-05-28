'''Cree un sistema de ventas de supermercado en el cual se pueda agregar productos al carro de compras, las opciones del menú serán:
Agregar productos deberá mostrar un menú con 5 productos y sus precios (creado por usted), cada vez que se seleccione un producto quedará agregado en la lista. Ver canasta, es mostrar todos los productos seleccionados. Ver total, es mostrar el total a pagar por el cliente.'''

carrito = []
productos = [{"nombre":"Pintura Negra","precio":5000},{"nombre":"Pintura Blanca","precio":7000},{"nombre":"Pintura Roja","precio":3000},{"nombre":"Pintura Azul","precio":10000},{"nombre":"Pintura Rosa","precio":6000}]
opcion = 0
total = 0
while opcion != 4:
    while True:
        print("1) Agregar Productos.")
        print("2) Ver carrito de compras.")
        print("3) Ver total a pagar.")
        print("4) SALIR")
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion>0 and opcion < 5:
                break
            else:
                print("Ingrese una opción válida.")
        except:
            print("Ingrese valores numéricos.")

    while opcion == 1:
        print("*"*5, " PRODUCTOS ","*" *5)
        for posicion in range(len(productos)):
            print(f"{posicion+1}) {productos[posicion]['nombre']} -> $ {productos[posicion]['precio']}")
        print("6) Volver al menú principal.")
        try:
            opcionProducto = int(input("¿Que producto desea seleccionar? "))
            if opcionProducto > 0 and opcionProducto < 6:
                opcionProducto -= 1
                print(f"Seleccionaste {productos[opcionProducto]['nombre']}")
                total += productos[opcionProducto]['precio']
                clave = "cantidad"
                if clave in productos[opcionProducto]:
                    for carritoItem in carrito:
                        if productos[opcionProducto]['nombre'] == carritoItem['nombre']:
                            carritoItem['cantidad'] += 1
                else:
                    productos[opcionProducto]['cantidad'] = 1
                    carrito.append(productos[opcionProducto])
            elif opcionProducto == 6:
                break
            else:
                print("Ingrese una opción válida.")
        except:
            print("Ingrese un valor numérico.")
    while opcion == 2:
        print("*"*5," CARRITO DE COMPRAS ","*"*5)
        for producto in carrito:
            print(producto['nombre'], "x",producto['cantidad'])
        break
    while opcion == 3:
        print("$"*5," TOTAL A PAGAR ","$"*5)
        print(f"El total a pagar es : ${total}")
        break
print("Has salido del programa.")
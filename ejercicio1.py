'''Cree 2 listas, en las cuales se guardarán 3 nombres y 3 apellidos (1 lista para nombres y una 1 lista para apellidos). El sistema deberá mostrar de forma ordenada los nombres y apellidos.'''

nombres = []
apellidos = []
numeros = []

for numero in range(10):
    numeros.append(str(numero))

for nombre in range(3):
    while True:
        errorNombre = False
        nombreInput = input("Ingrese un nombre para almacenar: ")
        for nom in nombreInput:
            for n in nom:
                for num in numeros:
                    if n == num:
                        errorNombre = True   
        if len(nombreInput) > 1 and errorNombre == False:
            nombres.append(nombreInput)
            break
        else:
            print("ERROR : Ingrese un nombre válido")

for apellido in range(3):
    while True:
        errorApellido = False
        apellidoInput = input("Ingrese un apellido para almacenar: ")
        for apell in apellidoInput:
            for a in apell:
                for num in numeros:
                    if a == num:
                        errorApellido = True   
        if len(apellidoInput) > 1 and errorApellido == False:
            apellidos.append(apellidoInput)
            break
        else:
            print("ERROR : Ingrese un apellido válido")

nombres.sort()
apellidos.sort()
print(nombres)
print(apellidos)
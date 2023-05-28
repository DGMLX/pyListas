'''Cree una lista para almacenar nombres. El proceso se realiza preguntando si desea seguir ingresando. Si la respuesta es NO, se detiene el proceso. Luego, elimine el nombre con la menor cantidad de caracteres.'''

nombres = []
numeros = []
opcion = 0

for numero in range(10):
    numeros.append(str(numero))

while opcion != 2:
    while True:
        errorNombre = False
        nombreInput = input("Ingrese nombre para almacenar :")
        for nombre in nombreInput:
            for numero in numeros:
                if nombre == numero:
                    errorNombre = True
        if len(nombreInput) > 1 and errorNombre == False:
            nombres.append(nombreInput)
            break
        else:
            print("Nombre inválido.")
    while True:
        try:
            print("1) SI")
            print("2) NO")
            opcion = int(input("¿Desea ingresar otro nombre? "))
            if opcion== 1 or opcion == 2:
                break
            else:
                print("Ingrese una de las opciones. 1 o 2")
        except:
            print("Ingrese un valor numérico.")

print("Has salido del programa.")
nombreMenor = nombres[0]
for posicion in range(len(nombres)):
    if len(nombreMenor) > len(nombres[posicion]):
        nombreMenor = nombres[posicion]
        pos = posicion
print(f"Se ha eliminado el nombre con menos caracteres: {nombreMenor}")
nombres.pop(pos)
print(nombres)


        

#Ejercicio 1
def correo(direccion_correo):
    variable1 = '@'
    for i in direccion_correo:
        if i == variable1:
            return True #La función es verdadera
    else:
        return False #La función es falsa

direccion = input("Ingresa tu dirección de correo electrónico: ")
if correo(direccion): #Si la función es verdadera:
    print("Dirección de correo Valida")
else: #Si no es verdadera:
    print("Dirección de correo Invalida,Por favor Verificar")

print(correo(direccion))

#Ejercicio 2
def numeros(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10 #Nuevo valor de número
    return suma

n = int(input("Ingresa un número: ")) #Solicitar al usuario el ingreso de un número
while n != 0:
    print("Suma =", numeros(n))
    n = int(input("Ingresa un número: "))

#Ejercicio 3
def numeros(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma

sumatoria = 0
n = int(input("Ingresa un número: "))
while n != 0:
    print("Suma de digitos =", numeros(n))
    sumatoria = sumatoria + n  #Asignacion del nuevo valor para la variable sumatoria
    n = int(input("Ingresa un número: "))
print("Suma de los numeros ingresados =", sumatoria)

#Ejercicio 4
def primos(numero):
    if numero % 2 == 0:
        return False #La función es falsa
    else:
        return True #La función es verdadera

n = int(input("Ingresa un número entero: "))
if primos(n): #Si se cumple la condición de que la funcion sea verdadera:
    print("El número ingresado es primo")
else:  #si es falsa:
    print("El número ingresado NO es primo")

#Ejercicio 5
def frequency(numero,digito):
    frecuencia = 0
    while numero != 0:
        digito1 = numero % 10
        if digito1 == digito: #Condición
            frecuencia = frecuencia + 1
        numero = numero // 10 #Nuevo valor para la variable número
    return frecuencia


n = int(input("Ingresa un número entero: ")) #Solicitar al usuario el ingreso de un número entero
digito = int(input("Ingresa un digito: "))
str(n) #Tipo de dato str para poder concatenar
str(digito) #Tipo de dato str para poder concatenar
print("La frecuencia del digito ingresado en el número es de:", frequency(n,digito))

#Ejercicio 6
def factoriall(numero):
    factorial = 1
    for i in range (1,numero+1):
        factorial = factorial * i #Nuevo valor para la variable factorial
    return factorial


cantidad = 0
n = int(input("Ingresa un número para calcular su factorial: "))  #Solicitar al usuario el ingreso de un número
while n != 0:
    print("El factorial del numero ingresado es: ", factoriall(n))
    cantidad = cantidad + 1  #Asignación de un nuevo valor para la variable cantidad
    n = int(input("Ingresa un número para calcular su factorial: "))
print("Se leyeron un total de:" , cantidad,"números")

#Ejercicio 7
def numeros(numero): #Definimos la función numeros
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma


cantidad = 0
mayor = 0
n = int(input("Ingresa un número: "))
mayor_suma = 0
while n != 0:
    if numeros(n) > mayor: #Establecimiento de condiciones
        mayor = numeros(n)
        mayor_suma = n
    if numeros(n) < 10:
        cantidad = cantidad + 1
    n = int(input("Ingresa un número: "))
print("El número ",mayor_suma, " es el que posee una mayor sumatoria de digitos, con un valor de: ",mayor) #Imprimir por pantalla
print("Existen", cantidad, "números, con sumatoria de dígitos menor a 10")

#Ejercicio 8

# Utilizamos funciones ya utilizadas anteriormente

def primos(numero):
    if numero % 2 == 0:
        return False
    else:
        return True

def numeros(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma

def frequency(numero,digito):
    frecuencia = 0
    while numero != 0:
        digito1 = numero % 10
        if digito1 == digito:
            frecuencia = frecuencia + 1
        numero = numero // 10
    return frecuencia

def factoriall(numero):
    factorial = 1
    for i in range (1,numero+1):
        factorial = factorial * i
    return factorial

mayor = 0
n = int(input("Ingresa un número primo, 0 para salir: "))
digito = int(input("Ingresa un dígito,0 para salir: "))
while primos(n):
    print("Sumatoria de digitos: ",numeros(n))
    print("La frecuencia del dígito ingresado en el número es de:", frequency(n, digito))
    if n > mayor:
        mayor = n
    n = int(input("Ingresa un número primo, 0 para salir: "))
    digito = int(input("Ingresa un dígito, 0 para salir: "))
print("El factorial del mayor número ingresado es = ", factoriall(mayor))

#Ejercicio 9
def documento(numero): #Definimos la función documento
    if len(numero) == 10 or len(numero) == 8: #Establecemos una condición para el argumento ingresado
        return True #Funcion Verdadera
    return False #Función Falsa

numero = input("Ingresa el número de tu cédula, sin puntos: ") #Solicitamos al usuario el ingreso de su documento
if documento(numero):
    print("Tu número de cedula es Válido")
else:
    print("Tu número de cedula es Invalido, por favor comprobar datos")

#Ejercicio 10
def ultimapalabra(frase):
    palabra = ""
    letra = ""
    contador = len(frase) - 1
    for i in range(len(frase),-1,-1): # I recorre el rango de la frase al revés
        letra = frase[contador]
        if letra == ' ':
            print("La longitud de la última palabra de la frase ingresada es:",len(palabra))
            break
        else:
            palabra = palabra + letra

        contador = contador - 1


frase = str(input("Ingresa una frase: "))
ultimapalabra(frase)





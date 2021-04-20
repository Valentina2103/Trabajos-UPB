#Ejercicio 1
def primos(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False #Si el número ingresado no es primo, la función será FALSA
    return True #Si el número cumple con la condicion de ser primo, la función será VERDADERA

def numeros(numero):
    suma = 0
    while numero != 0:
        if numero % 2 ==0:
            break #Si el número no es primo, se rompe el ciclo
        else:
            digito = numero % 10
            suma = suma + digito
            numero = numero // 10
    return suma #Se devuelve el valor de suma

def frequency(numero,digito):
    frecuencia = 0
    while numero != 0:
        if numero % 2 == 0:
            break #Si el número no es primo, se rompe el ciclo
        else:
            digito1 = numero % 10
            if digito1 == digito:
                frecuencia = frecuencia + 1
            numero = numero // 10
    return frecuencia #Se devuelve el valor de la frecuencia

def factoriall(numero):
    factorial = 1
    for i in range (1,numero+1):
        factorial = factorial * i
    return factorial #Se devuelve el valor del factorial

mayor = 0
n = int(input("Ingresa un número primo: ")) #Le solicitamos al usuario que ingrese un número impar
digito = int(input("Ingresa un dígito: ")) #Le solicitamos al usuario que ingrese un digito
while primos(n):
    print("Sumatoria de dígitos: ",numeros(n))
    print("La frecuencia del dígito ingresado en el número es de:", frequency(n, digito))
    if n > mayor:
        mayor = n
    n = int(input("Ingresa un número primo: "))
    digito = int(input("Ingresa un dígito: "))
print("El factorial del mayor número ingresado es = ", factoriall(mayor))

#Ejercicio 2
def aumento_numero(x,y):
    for i in range (3): #Se aumenta i en un rango de 3, en las variable ingresadas "x" y "y"
        x = x + 1
        y = y + 1
    return x,y

x=int(input("Ingresa un número para la Coordenada del eje x: ")) #Le pedimos al usuario que ingrese un valor para x
y=int(input("Ingresa un número para la Coordenada del eje y: ")) #le pedimos al usuario que ingrese un valor para y
print(aumento_numero(x,y)) #Llamamos a la función


#Ejercicio 3
def maximo(x,y): #Definición de la función, la cual contiene dos parámetros
    if x > y:
        return x #Si "x" , Es mayor que "y", se devuelve el valor de "x"
    else:
        return y #Si "x" , No mayor que "y", se devuelve el valor de "y"

def minimo(x,y):
    if x < y:
        return x #Si "x" Es menor que "y", se devuelve el valor de "x"
    else:
        return y #Si "x" No menor que "y", se devuelve el valor de "y"


# programa principal

#Solicitamos al usuario el ingreso de los valores de x y y
x = int(input("Ingresa un número para x: "))
y = int(input("Ingresa un número para y: "))
print(maximo(x-3,minimo(x+2,y-5)))

#Ejercicio 4
print(pow(2,2))
print(pow(3,4))

print(divmod(13,2))
print(divmod(25,3))


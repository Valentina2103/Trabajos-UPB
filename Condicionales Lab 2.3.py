#Ejercicio 1
n = int(input("Ingresa un número "))
if n%5 == 0 and n%3 == 0:
    print("El número ingresado es multiplo de 15")
elif n%5 == 0:
    print("El número ingresado es multiplo de 5")
elif n%3 == 0:
    print("El número ingresado es multiplo de 3")
else:
    print("El número ingresado no es multiplo de 3 ni de 5")

#Ejercicio 2
n1 = float(input("Ingresa la nota número 1 "))
n2 = float(input("Ingresa la nota número 2 "))
n3 = float(input("Ingresa la nota número 3 "))
promedio = (n1+n2+n3)/3
if promedio >= 7:
    print("Promovido","Tu promedio es:",promedio)
elif promedio >= 4 and promedio <7:
    print("Regular","Tu promedio es:",promedio)
elif promedio < 4:
    print("Reprobado","Tu promedio es:",promedio)

#Ejercicio 3
n1 = int(input("Ingresa la nota número 1 "))
n2 = int(input("Ingresa la nota número 2 "))
n3 = int(input("Ingresa la nota número 3 "))
promedio = (n1+n2+n3)/3
if promedio >= 7:
    print("Promocionado")
if promedio >= 4 and promedio <7:
    print("Regular")
if promedio < 4:
    print("No habilitado")

#Ejercicio 4
lista = [1,2,3,4,82,31,32,293,3949,123,938,9129]
print(lista[3:6])

lista.insert(2,"Hola")
print(lista[:])
print(lista.index("Hola"))
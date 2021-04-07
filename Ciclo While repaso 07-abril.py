#Ejercicio 1
numero = 0
while numero <= 10:
    print(numero)
    numero = numero +1
#Ejercicio 2
anio = 2010
while anio <= 2012:
    print("Informes del año",anio)
    anio = anio + 1
#Ejercicio 3
numero,suma = 0,0
while numero <= 10:
    suma = numero + suma
    numero = numero + 1
print ("La suma es " + str(suma))

#Ejercicio 4
print ("Introduzca la nota de un estudiante (-1 para salir): ")
contar,total = 0,0
grado = int(input())
while grado != -1:
    total = total + grado
    contar = contar + 1
    print ("Introduzca la nota de un estudiante (-1 para salir): ")
    grado = int(input())
promedio = total/contar
print ("Promedio de notas del grado escolar es: " + str(promedio))

#Ejercicio 5
grado = int(input("nota "))
total,contar = 0,0
while grado != -1:
    total = total + grado
    contar += 1
    grado = int(input("nota "))
else:
    promedio = total / contar
    print ("Promedio de notas del grado escolar: " + str(promedio))

#Escribe y ejecuta el siguiente código utilizando break
while True:
    opcion = input("Elige una fruta para tu desayuno: 1-Manzanas 2-Bananas 3-Nada ")
    if opcion == str(1):
        print("Has seleccionado manzanas")
        break
    elif opcion == str(2):
        print("Has seleccionado bananas")
        break
    elif opcion == str(3):
        print("Has seleccionado nada")
        break
    else:
        print("Debes seleccionar una ocpión (1,2 o 3)")

print("Programa terminado, que disfrutes tu desayuno")

#Break
number = 0
for number in range(10):
    if number == 5:
        break
    print('Number is ' + str(number))
print('Fuera del ciclo')

#Continue
number = 0
for number in range(10):
    if number == 5:
        continue
    print('Number is ' + str(number))
print('Fuera del ciclo')

#pass
number = 0
for number in range(10):
    if number == 5:
        pass
    print('Number is ' + str(number))
print('Fuera del ciclo')


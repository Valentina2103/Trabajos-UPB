#Ejercicio 1
nombre = 'Valentina'
calificativo = str(input("Ingresa un calificativo: "))
print(nombre,calificativo)

#Ejercicio 2
n = int(input("Ingresa un número: "))
cuadrado = str(n * n)
print("El cuadrado de",n,"es:",cuadrado)

#Ejercicio 3
n1 = int(input("Ingresa un número: "))
n2 = int(input("Ingresa un número: "))
suma = str(n1+n2)
print("La suma de los números ingresados es:",suma)

#Ejercicio 4
n1 = int(input("Ingresa un número: "))
n2 = int(input("Ingresa un número: "))
suma = str(n1+n2)
resta = str(n1-n2)
multiplicacion = str(n1*n2)
division = str(n1/n2)
residuo = str(n1%n2)
print("Suma =",suma,"Resta =",resta, "Multiplicación =",multiplicacion,"División =",division, "Residuo =",residuo)

#Ejercicio 5
import math
n = float(input("Ingresa un número que posea parte decimal: "))
decimal,entero = math.modf(n)
print(f"La parte decimal del número ingresado es: {decimal} \nLa parte entera del número ingresado es: {entero}")

#Ejercicio 6
p1 = 0.15;p2 = 0.20;p3 = 0.15;p4 = 0.30;p5 = 0.20
nota1 = 0; nota2 = 0; nota3 = 0; nota4 = 0; nota5 =0
contador = 1

while contador <= 5:

    nota = float(input("Ingrese  el valor de la nota " + str(contador) +  " : "))
    print(nota)

    if contador == 1:
        nota1 = nota * p1
    if contador == 2:
        nota2 = nota * p2
    if contador == 3:
        nota3 = nota * p3
    if contador == 4:
        nota4 = nota * p4
    if contador == 5:
        nota5 = nota * p5

    contador = contador + 1

definitiva = float(nota1  + nota2  + nota3 + nota4  + nota5)

print("SU NOTA DEFINITIVA ES :" + str(definitiva))

#Ejercicio 7
valor_venta = float(input("Ingrese el valor de la venta realizada: "))
iva = valor_venta * 0.19
total = valor_venta + iva
print(f"El valor de su venta fue: {valor_venta} \nEl valor del iva equivale a: {iva} \nEl valor de su venta con iva incluido es de: {total}")

#Ejercicio 8
import math
radio = float(input("Ingresa el valor del radio del ciruculo en metros: "))
area = math.pi * pow(radio,2)
perimetro =  2 * math.pi * radio
print(f"El area del cituclo es: {area} M^2\nEl perimetro del citculo es {perimetro}M^2")

#Ejercicio 9
lado = float(input("Ingresa el valor de un lado del hexagono en centimetros: "))
apotema = float(input ("Ingresa el valor del apotema del hexagono en centimetros: "))
area =  ((lado * 6)* apotema )/2
print(f"El valor del area del hexagono es: {area} cm")

#Ejercicio 10
numero = float(input("Ingresa un número menor a 10: "))
n1 = 0; n2 = 0 ; n3 = 0
contador = 1
while numero <=  10:
    if contador == 1:
        n1 = numero
    if contador == 2:
        n2 = numero
    if contador == 3:
        n3 = numero
        break
    contador = contador + 1
    numero = float(input("Ingresa un número menor a 10: "))

promedio = (n1+n2+n3)/3
print("El promedio de los números ingresados es de:",promedio)

#Ejercicio 11
a = int(input("Ingresa un valor para a: "))
b = int(input("Ingresa un valor para b: "))
print (f"El valor inicial de a es:{a}\nEl valor inicial de b es: {b}")
a2 = b
b2 = a
print (f"El nuevo valor de a es:{a2}\nEl nuevo valo de b es: {b2}")

#Ejercicio 12
import math
gravedad = 9.8
altura = float(input("ingresa la altura en metros, desde la cual el objeto es lanzado: "))
tiempo_caida = math.sqrt((2*altura)/gravedad)
print ("El tiempo que se demora en caer el objeto es de:",tiempo_caida,"segundos")

#Ejercicio 13
velocidad = float(input("Ingresa el valor de la velocidad en m/s): "))
aceleracion = float(input("Igresa el valor de la aceleración en m/s^2: "))
tiempo = aceleracion / velocidad
distacia = (aceleracion * tiempo)/2
print("La distancia total recorrida por el objeto es de: ",distacia)

#Ejercicio 14
aceleracion = float(input("Ingresa el valor de la aceleracion en m/s^2: "))
tiempo = float(input ("ingresa el valor del tiempo en segundos:"))
velocidad = 0 + aceleracion * tiempo
print("la velocidad final es: ",velocidad,"m/s")

#Ejercicio 15
masa = float(input("Ingrea el valor de la masa del objeto en kg: "))
velocidad = float(input("Ingresa el valor de la velocidad del objeto en m/s:"))
energia = (masa * pow(velocidad,2))/2
print("El valor de la energia es de :",energia ,"julios")

#Ejercicio 16
#√((x_2-x_1)²+(y_2-y_1)²)
import math
x1= float(input("Ingresa el valor de x1: "))
y1=float(input("Ingresa el valor de y1: "))
x2=float(input("Ingresa el valor de x2: "))
y2=float(input("Ingresa el valor de y2: " ))
distancia = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("La distancia equivale a:",distancia)

#Ejercicio 17
segundos = float(input("Ingresa la cantidad de segundos que quieres pasar a horas: "))
horas = segundos / 3600
print(f"{segundos}segundos,equivalen a {horas} horas")

#Ejercicio 18
segundos = float(input("Ingresa la cantidad de segundos que quieres pasar a minutos: "))
minutos = segundos / 60
print(f"{segundos} segundos,equivalen a {minutos} minutos")

#Ejercicio 19
segundos=int(input("Ingresa una cantidad de segundos: "))
horas=(int(segundos/3600))
minutos=int((segundos-(horas*3600))/60)
seg=segundos-((horas*3600)+(minutos*60))
print(f"{str(horas)}h:{str(minutos)}m:{str(seg)}s")

#Ejercicio 20
cantidad = int(input("Ingresa la cantidad de dinero que quieres desglosar (pesos colombianos): "))
denominaciones = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
for i in denominaciones:
    if cantidad >= i:
        desglosado = cantidad // i
        print(str(desglosado), "billetes de",str(i),"mil pesos ")
        cantidad = cantidad % i

#Ejercicio 21
numero = input("Ingresa un número de 4 cifras: ")
print("El número ingresado es:",numero)
numero2 = numero[::-1]
print("El número ingresado de manera inversa es:",numero2)

#Ejercicio 22
n = int(input("Ingresa un número entero: "))
if n%2 == 0:
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")

#Ejercicio 23
n = int(input("Ingresa un número: "))
if n < 0 :
    print("El número ingresado es negativo")
elif n == 0:
    print("El número 0 no se considera ni positivo, ni negativo")
else:
    print("El número ingresado es positivo")

#Ejercicio 24
numero =float(input("Ingresa el número: "))
if numero < 0 and numero % 2 == 0 :
    print("El número ingresado es par-negativo")
elif numero < 0 and numero % 2 != 0 :
    print("El número ingresado es impar-negativo")
elif numero > 0 and numero % 2 == 0 :
    print("El número ingresado es par-positivo")
elif numero > 0 and numero % 2 != 0 :
    print("El número ingresado es impar-positivo")

#Ejercicio 25
valor_venta = float(input("Ingresa el valor del producto: "))
iva = valor_venta * 0.19
descuento = valor_venta * 0.05
if valor_venta <= 150.000:
    valor_venta = valor_venta + iva
    print("El valor total a pagar es:",valor_venta)
elif valor_venta > 150.000 :
    valor_venta = valor_venta + iva
    total = valor_venta - descuento
    print(f"El valor total a pagar es: {total}, ya que se realizó un descuento del 5%,que equivale a {descuento},por compras mayores a 150.000")

#Ejercicio 26
n = float(input("Ingresa un número: "))
if n >= 10:
    triple = n * 3
    print("El triple del número ingresado es: ",triple)
else:
    cuartaparte= n/4
    print("La cuarta parte del número ingresado es:", cuartaparte)

#Ejercicio 27
p1 = 0.15;p2 = 0.20;p3 = 0.15;p4 = 0.30;p5 = 0.20
nota1 = 0; nota2 = 0; nota3 = 0; nota4 = 0; nota5 =0
contador = 1

while contador <= 5:

    nota = float(input("Ingrese  el valor de la nota " + str(contador) +  " : "))
    print(nota)

    if contador == 1:
        nota1 = nota * p1
    if contador == 2:
        nota2 = nota * p2
    if contador == 3:
        nota3 = nota * p3
    if contador == 4:
        nota4 = nota * p4
    if contador == 5:
        nota5 = nota * p5

    contador = contador + 1

definitiva = float(nota1  + nota2  + nota3 + nota4  + nota5)

if definitiva < 2:
    print("SU NOTA DEFINITIVA ES :",str(definitiva),"No puedes habilitar")
elif definitiva < 3:
    print("SU NOTA DEFINITIVA ES :", str(definitiva), "Reprobaste")
elif definitiva >= 3:
    print("SU NOTA DEFINITIVA ES :", str(definitiva), "Aprobaste")
elif definitiva > 4.5:
    print("SU NOTA DEFINITIVA ES :", str(definitiva), "Aprobaste con excelente nota FELICITACIONES!!!")

#Ejercicio 28
n1 = float(input("Ingresa un número: "))
n2 = float(input("Ingresa un número: "))
if n1 > n2:
    print("El número mayor es: ",n1)
else:
    print("El número mayor es: ",n2)

#Ejercicio 29
n = float(input("Ingresa un número: "))
decimal = n/100
print("En número ingresado en decimal equivale a:",decimal)

#Ejercicio 30
n1 = float(input("Ingresa un número: "))
n2 = float(input("Ingresa un número: "))
n3 = float(input("Ingresa un número: "))
menor = 0
mayor = 0
#Evaluamos el menor valor
if n1 < n2 and n1 <n3:
    menor = n1
elif n2 < n1 and n2 <n3:
    menor = n2
elif n3 < n2 and n3 <n1:
    menor = n3
    pass
#Evaluamos el mayor valor
if n1 > n2 and n1>n3:
    mayor = n1
elif n2 > n1 and n2>n3:
    mayor = n2
elif n3 > n2 and n3>n2:
    mayor = n3
print("De los números ingresados es menor es: ",menor,"y el mayor es:",mayor)

#Ejercicio 31
n1 = float(input("Ingresa un número: "))
n2 = float(input("Ingresa un número: "))
n3 = float(input("Ingresa un número: "))
sumatoria = n1+n2
if sumatoria > n3:
    print("La sumatoria del primer y segundo valor ingresado, es MAYOR al tercer valor, esta sumatoria equivale a: ",sumatoria)
elif sumatoria == n3:
    print("La sumatoria del primer y segundo valor, ES IGUAL a el tercer valor ingresado")
elif sumatoria < n3:
    print("La sumatoria del primer y segundo valor ingresado, es MENOR al tercer valor, esta sumatoria equivale a: ",sumatoria)

#Ejercicio 32
print("Datos de interes: ")
print("Si viajas más de 1000 km y más de 7 dias tendras un descuento del 15%")
print("La cantidad minima para poder realizar el vuelo es de 20 km por recorrer")
distancia = float(input("Ingresa la cantidad de km que viajaras: "))
dias = int(input("Ingresar la cantidad de dias que viajaras: "))
precio = distancia * 5000
descuento = precio * 0.15
if distancia > 1000 and dias > 7:
    print("Has obtenido un descuento del 15%")
    precio = precio - descuento
    print("El precio de tu viaje equivale a:",precio)
if precio < 100000 or distancia < 20:
    print("La cantidad minima para poder realizar el vuelo es de 20 km por recorrer, verifica los datos ingresados")
else:
    print("El costo para realizar tu viaje equivale a: ",precio)

#Ejercicio 33
year = int(input("Ingresa un año para saber si es biciesto o no: "))
if year % 4 == 0  and year % 100 != 0:
    print("El año ingresado es bisiesto")
elif year % 400 == 0:
    print("El año ingresado es bisiesto")
else:
    print("El año ingresado No es un año bisiesto")

#Ejercicio 34
from math import sqrt
a = int(input("Ingresa un número para a: "))
b = int (input("Ingresa un número para b: "))
c = int (input("Ingresa un número para c: "))
determiante =( b**2)-4*a*c
if determiante > 0:
    x_1 = -b+sqrt(b**2-4*a*c)/(2*a)
    x_2 = -b-sqrt(b**2-4*a*c)/(2*a)
    print(x_1, x_2)
elif determiante == 0:
    x_1 = -b / ("2*a")
    print (x_1)
elif determiante < 0:
    print("La solución de la ecuacion es con números complejos")

#Ejercicio 35
usuario = 'Valentina'
contrasena = '123456'
print("Usuario = Valentina y Contraseña = 123456")
print("INICIO DE SESIÓN")
usuario2 = input("Ingresa tu usuario: ")
contrasena2 = input("Ingresa tu contraseña: ")
if usuario == usuario2 and contrasena == contrasena2:
    print("Has iniciado sesión exitosamente")
else:
    print("Los datos ingresados son incorrectos, Por favor verificar")

#Ejercicio 36
numeros = ["Cero","Uno","Dos","Tres","Cuatro","Cinco","Seis","Siete","Ocho","Nueve","Diez"]
n = int(input ("Ingresa un número del 1 al 10, para saber como se escribe: "))
if n >= 0 and n <= 10:
    print(numeros[n])
else:
    print("Número invalido, Ingresa un número entre el 1 y 10")

#Ejercicio 37
numero = int(input("Ingresa un número entero no mayor a 100.000: "))
contador = 0
while numero > 0:
    if numero < 100000:
        numero = numero // 10
        contador = contador + 1
    else:
        print("poVerificar el número ingresado, este debe ser menor a 100000")
print(f"El número ingresado tiene {contador} digitos")

#Ejercicio 38
n1 = int(input("Ingresa un número entero: "))
n2 = int(input("Ingresa un número entero: "))
n3 = int(input("Ingresa un número entero: "))
if n1 < n2 < n3 :
    print("Los números se estan incrementando")
elif n1 > n2 > n3:
    print("Los números se estan disminuyendo")
else:
    print("Los números no se estan incrementando ni disminuyendo")

#Ejercicio 39
n1 = int(input("Ingresa un número entero: "))
n2 = int(input("Ingresa un número entero: "))
if n1 >= 0 and n1 <= 5:
    if n2 >= 0 and n2 <= 5:
        print("True")
    else:
        print("False")

#Ejercicio 40
dias = ["Invalido","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
n = int(input("Igresa un número de 1 al 7, para saber a que dia de la semana corresponde: "))
if n > 0 and n <= 7:
    print("El número ingresado,equivale a el dia:",dias[n])
else:
    print("Verifica que el número ingresado este entre el 1 y el 7")

#Ejercicio 41
n1 = float(input("Ingresa un número para n1: "))
n2 = float(input("Ingresa un número para n2: "))
n3 = float(input("Ingresa un número para n3: "))
if n1 == n2:
    print("Los números n1 y n2 son iguales")
elif n1 == n3:
    print("Los números n1 y n3 son iguales")
elif n2 == n1:
    print("Los númeroso n2 y n1 son iguales")
elif n2 == n3:
    print("Los números n2 y n3 son iguales")
elif n3 == n1:
    print("Los números n3 y n1 son iguales")
elif n3 == n2:
    print("Los números n3 y n2 son iguales")
else:
    print("n1,n2 Y n3, Son diferentes")

#Ejercicio 42
for i in range(10):
    print(i)

#Ejercicio 43
for i in range(20):
    if i % 2 != 0:
        print(i)

#Ejercicio 44
for i in range(20):
    if i % 2 == 0:
        print(i)

#Ejercicio 45
n = int(input("Ingresa la cantidad de números naturales que deseas imprimir: "))
for i in range(0, n):
    print(i)

#Ejercicio 46
n = int(input("Ingresa un número: "))
for i in range(1, n):
    if i % 2 == 0:
        i = i - (2 * i)
    print(i)

#Ejercicio 47
print("El valor de m tiene que ser MAYOR a el valor de n")
n = int(input("Ingresa un valor para n: "))
m = int(input("Ingresa un valor para m: "))
if n < m:
    for i in range(n, m):
        print(i)
else:
    print("Verificar que el valor de m, sea mayor a el valor de n")

#Ejercicio 48
print("El valor de m tiene que ser MAYOR a el valor de n")
n = int(input("Ingresa un valor para n: "))
m = int(input("Ingresa un valor para m: "))
sumatoria = 0
if n < m:
    for i in range(n, m):
        sumatoria = sumatoria + i
        print(i)
else:
    print("Verificar que el valor de m, sea mayor a el valor de n")
print("La sumatoria de los anteriores números naturales es: ",sumatoria)


#Ejercicio 49
sumatoria = 0
promedio = 0
contador = 1
while True:
    numero = int(input("Ingresa un número: "))
    sumatoria = sumatoria + numero
    contador = contador + 1
    if contador == 11:
        break
promedio = sumatoria / 10
print("La sumatoria de los números ingresados es: ", sumatoria)
print("El promedio de los números ingresados es: ",promedio)


#Ejercicio 50
n = int(input("Ingresa la cantidad de números que deseas trabajar: "))
sumatoria = 0
promedio = 0
contador = 1
while True:
    numero = int(input("Ingresa un número: "))
    sumatoria = sumatoria + numero
    contador = contador + 1
    if contador == n +1 :
        break
promedio = sumatoria / n
print("La sumatoria de los números ingresados es: ", sumatoria)
print("El promedio de los números ingresados es: ",promedio)


#Ejercicio 51
sum_impares,sum_pares = 0,0
contador1,contador2 = 0,0
promedio1,promedio2 = 0,0
cantidad = int(input("Ingresa la cantidad de numeros que deseas trabajar: "))
for i in range (1,cantidad):
    n = int(input("Ingres un número entero: "))
    if n % 2 == 0:
        sum_pares = sum_pares + n
        contador1 = contador1 + 1
        promedio1 = sum_pares // contador1
    elif n % 2 != 0:
        sum_impares = sum_impares + n
        contador2 = contador2 + 1
        promedio2 = sum_impares // contador2
n = int(input("Ingres un número entero: "))
print(f"El promedio de los números pares es {promedio1}\nEl promedio de los números impares es {promedio2}")

#Ejercicio 52
while True:
    n = int(input("Ingrese un número entero positivo: "))
    if n > 0:
        print("El valor ingresado fue: ",n)
        break
    else:
        print("Ingrese un valor valido")

#Ejercicio 53
n = int(input("Ingresa un número, 0 para salir: "))
contador1 = 0
contador2 = 0
while n != 0 :
    if n < 100:
        contador1 = contador1 + 1
    elif n > 100 :
        contador2 = contador2 + 1
    n = int(input("Ingresa un número, 0 para salir: "))
print("La cantidad de números ingresados menores a 100, es: ", contador1)
print("La cantidad de números ingresados mayores a 100, es: ", contador2)

#Ejercicio 54
n = int(input("Ingresa un número, 0 para salir: "))
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
while n != 0 :
    #Positivos y negaticvos
    if n >= 0:
        contador1 = contador1 + 1
    elif n < 0:
        contador2 = contador2 + 1
    #Pares e Impares
    if n % 2 == 0:
        contador3 = contador3 + 1
    elif n % 2 != 0:
        contador4 = contador4 + 1
    #Multiplos de 8
    if n % 8 == 0:
        contador5 = contador5 + 1
    n = int(input("Ingresa un número, 0 para salir: "))
print("La cantidad de números ingresados positivos es de: ", contador1)
print("La cantidad de números ingresados negativos es de: ", contador2)
print("La cantidad de números pares ingresados es de: ", contador3)
print("La cantidad de números impares ingresados es de: ", contador4)
print("La cantidad de números ingresados multiplos de 8 es de: ", contador5)

#Ejercicio 55
n = int(input("Ingresa un número positivo, 0 para salir: "))
contador1 = 0
contador2 = 0
contador3 = 0
contador4 =0
while n !=0:
    # Numero leidos
    if n != 0:
        contador4 = contador4 + 1
        pass
    #Números pares
    if n % 2 == 0:
        contador1 = contador1 + 1
        if contador1 == 10:
            break
    #Números 5
    if n == 5:
        contador2 = contador2 +1
        if contador2 == 20:
            break
    # Números Impares
    if n !=5:
        if n % 2 != 0:
            contador3 = contador3 + 1
            if contador3 == 10:
                break
    n = int(input("Ingresa un número positivo, 0 para salir: "))

print("La cantidad de números pares ingresados es de: ", contador1)
print("La cantidad de números impares ingresados es de: ", contador3)
print("La cantidad de números ingresados = 5 es de: ", contador2)
print("La cantidad de números leidos es de: ", contador4)

#Ejercicio 56
n = int(input("ingresa un número para conocer sus factores: "))
for i in range(1,n+1):
    if n % i == 0:
        print(i)

#Ejercicio 57
cadena = input("Ingresa una palabra: ")
print("La inversa de la cadena ingresada es: ",cadena[::-1])

#Solución 2
cadena = str(input("ingresa una palabra: "))
for i in range(len(cadena)-1,-1,-1):
    print(cadena[i],end ="")

#Ejercicio 58
n = int(input("Ingresa un numero: "))
s = 0
for i in range(1,n+1):
    for j in range (1,i+1):
        print(j,end="")
    print()

#Ejercicio 68
while True:
    try:
        n1= int(input("Ingresa un numero Willy: "))
        n2= int(input("ingresa un numero Willy: "))
        if n2 != 0:
            print(n1/n2)
            break
        if n2 == 0:
            print("Madre mía Willy, no puedes dividir por cero")
    except:
        print("Madre mía Willy, debes ingresar un número")





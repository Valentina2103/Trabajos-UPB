#Ejercicios dias de la semana

#Forma 1
diasdelasemana = [0,"lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
dia = int(input("Ingrese el numero de un dia de la semana, del 1 al 7 \n "))
if dia == 6 or dia == 7:
    temp = "y es festivo"
else:
    temp = ""
print("El dia es {0} {1}".format(diasdelasemana[dia],temp))


#Forma 2
dias = [0,"lunes","martes","miercoles","jueves","viernes","festivo","festivo"]
dia = int(input(" presiona 1 : para iniciar \n presiona 0 : para finalizar\n"))
while dia != 0 :
    try:
        dia = int(input("ingresa un dia de la semana (1 a 7) y (0 para salir)"))
        if dia != 0:
            if dia < 0 or dia > 7 :
                print("por favor ingresa un numero entre 1 y 7")
            elif dia > 0 and dia <=5:
                temp ="."
                print("el dia es {0} {1}".format(dias[dia],temp))
            elif dia == 6 or dia == 7:
                print("es festivo")
        else:
            print("fin")
    except:
            print("ingresa un valor valido")



#Ejercicio Calculadora

def sumar(): #Definimos la función sumar
    x = a + b
    print (("Resultado"), (x))
def restar():#Definimos la función restar
    x = a - b
    print (("Resultado"), (x))
def multiplicar():#Definimos la función multiplicar
    x = a * b
    print (("Resultado"), (x))
def dividir():#Definimos la función dividir
    x = a / b
    print (("Resultado"), (x))

##########################################-2-###################################################
while True: #Utilizamos un ciclo while true, ciclo que se seguirá repitiendo mientras sea verdadero, es decir mientras el ciclo no sea detenido internamente.

    try: #Intentamos obtener los datos de entrada
        a = int(input("Ingresa el primer número: \n")) #Se ingresa un tipo de dato tipo entero, que va a guardarse en la variable a

        b = int(input("Ingresa el segundo número: \n"))# Se ingresa un tipo de dato tipo entero, que va a guardarse en la variable b

        print (("Que cálculo quieres realizar entre"), (a), ("y"), (b), ("?\n")) #Se muestra por pantalla la frase “Que cálculo quieres realizar entre” a y b, que en este caso serian los valores ingresados por el usuario.
        op = str(input(""" #Ofrecemos las opciones de cálculo que van a llamar a las funciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n"""))
    except: #En caso de error:
        print ("Error")
        op = '?'
##########################################-3-##################################################
    if op == '1':# Si el usuario elige opción 1 llamamos a la función sumar
        sumar()
        break


    elif op == '2':#Si el usuario elige opción 2 llamamos a la función restar
        restar()
        break
    elif op == '3':# Si el usuario elige opción 3 llamamos a la función multiplicar
        multiplicar()
        break
    elif op == '4':#Si el usuario elige opción 4 llamamos a la función dividir
        dividir()
        break
    else:
        print ("""Has ingresado un numero de opción erróneo""") #En caso que el número no
                                                                         #se encuentre


#Ejercicio tablas de multiplicar

def imprimir_tabla(numero):
    # Se supone que las tablas llegan hasta el 10
    LIMITE = 10
    # Comenzar en 1
    contador = 1
    while contador <= LIMITE:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        # Incrementar contador para no caer en ciclo infinito
        contador = contador + 1

# Probar función
imprimir_tabla(1)
#Ejercicio 1
n = int(input("Ingrese el tamaño del arreglo: ")) #Solicitamos al usuario el tamaño, o la cantidad de valores que tendrá el arreglo
m = int(input("Ingrese un múltiplo: ")) #Solicitamos al usuario el número sobre el cual se calcularan los múltiplos del arreglo
a = [] #El arreglo inicia vacío
for i in range (1,n+1):
 a.append(i*m) #Se llena al arreglo
print (a) #Imprimimos por pantalla el arreglo final



#Ejercicio 2
A = int(input("Ingresa el tamaño de los arreglos: ")) #Solicitamos al usuario que ingrese el tamaño de los arreglos
B = [] #El arreglo B inicia vacío
C = [] #El arreglo C inicia vacío
for i in range (0,A):
 B.append(input("Ingresa el nombre de las personas: ")) #Segun el rango de i, el arreglo B, se está llenando con los nombres que ingresa el usuario
print (B) #Se imprime el arreglo B
for j in range (0,A): #Segun el rango de j, se llena el arreglo C, con la longitud de los nombres ingresados en el arreglo B
 C.append(len(B[j]))
print (C) #Se imprime el arreglo C


#Ejercicio 3
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje"] #Se crea una lista con las diferentes materias
scores = [] #El arreglo esta vacío
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?: ") #Le solicitamos al usuario que ingrese la nota de cada materia, segun el orden de la lista
    scores.append(score) #Se llena el arreglo scores con el valor ingresado por el usuario
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado: " + scores[i]) #Segun el rango de i, en la longitud de la lista subjects, se imprime el nombre de curso y su nota correspondiente

#Palindromo
def palindromo(palabra):
    if palabra == palabra[::-1]:
        print("La palabra ingresada es un palíndromo")
    else:
        print("La palabra ingresada NO es un palíndromo")

word = input("Ingresa una palabra: ")
palindromo(word)


#Abecedario
lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
#Se toma "a" como la posición 1
for i in range(len(lista), 1,-1):
    if i%3 == 0:
        lista.pop(i-1) #Se elimina un un elemento de la lista
print (lista)


#Funcion len()
def longitud(palabra):
    print("La longitud de la frase ingresada es: ", len(palabra))

word = input("Ingresa una frase: ")
longitud(word)



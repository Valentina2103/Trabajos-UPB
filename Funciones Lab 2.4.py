#Funciones

#Por nombre
a= 30
b=10
def resta (a,b):
    return a - b
print(resta(a,b))


#Por posición
def resta1(a,b):
    return a-b
print(resta1(30,10))


#Parámetros por defecto
def resta2(a= None , b= None):
    if a == None or b == None:
        print("Error, debes enviar dos valores a la función")
        return
    return a -b

print(resta2(50,49))


#Argumentos Indeterminados

#Por posición
def indeterminados(*args):
    for arg in args:
        print(arg)

indeterminados("Hola Valentina",21,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])


#Por posición y nombre
def super_funcion(*args,**kwargs):
    total = 0
    for arg in args:
        total = total + arg
    print("Sumatoria =", total)
    for kwarg in kwargs:
        print(kwarg,"=",kwargs[kwarg])

super_funcion(50,-1,1.56,10,20,300,cms="Plone",Edad="38")

#Función Max
print(max(2, 3))
print(max([1, 2, 3]))
print(max('a', 'b', 'c'))

#Función min
print(min(2, 3))
print(min([1, 2, 3]))
print(min('a', 'b', 'c'))

#Función divmod
print(divmod(5,2))
print(divmod(13.5,2.5))
q,r = divmod(13.5,2.5)
print(q)
print(r)

#Nuevas funciones

#Funcion Pow
print(pow(10,-2))
print(pow(2, 3))
n = pow(10, 2)
print(n)

#Funcion Len
print(len("mensaje secreto"))
print(len(["a","b","c"]))
print(len(range(1, 100, 7)))

#Funcion help
print(help(len))
print(help())

#print("Hola mundo")

#numero = 5

#print(numero)

#cadena1 = "Hola "
#cadena2 = "mundo"

#cadenanueva = cadena1 + cadena2

#print(cadenanueva)

#numero1 = 3
#numero2 = 2

#suma = numero1 + numero2

#print(suma)

#print(type(suma))
#print(type(cadenanueva))

#numerodecimal = 3.5

#print(type(numerodecimal))

#suma1 = suma + numerodecimal

#print(suma1)

#suma1 = str(suma1)
#print(suma1 + numerodecimal) daria error no se puede sumar un string con un float

#suma1 = int(suma1) esto daria un error por que el valor deberia ser un float

#suma1 = float(suma1)

#print(suma1+numerodecimal)

#imprimir variables en una cadema

#nombre = "Erwil"
#nombre = nombre.upper

#print("Buenos dias "+ nombre)
#print("Buenos dias "+ str(nombre))

# .format
#nombreupr = nombre.upper()

#print(nombreupr)
#edad = 24

#print("Buenos dias {}, feliz {}´s cumpleaños ".format(nombreupr,edad))

#resultado = 10/3

#print("El resultado es: {r}".format(r=resultado))
#print("El resultado es: {r:1.3f}".format(r=resultado)) Este para imprimir solo 3 decimales

#f-strings

#print(f"Buenos dias {nombre}, feliz {edad}´s Cumpleaños")

#Entrada por teclado

#imput()

#print("Introduce un nombre")
#entrada = input()
#print("Hola, {name}".format(name=entrada))

#Ejercicio
#Crear una variable "cadena" que contiene el texto "Esto es un 
#texto de ejemplo " Según la posicion de cada letra en la cadena
#calcular que valores (x,y) hay que poner para seleccionar solo 
#la palabra "texto"
#cadena[x:y] = "texto"

#cadena = "Esto es un texto de ejemplo"
#print(cadena[11:16])

#Ejercicio

#1.- Crear una variable "cadena" que contiene el texto "Esto es un texto de ejemplo"
#2._ Crear una variable "logitud" que contiene la longitud de la variable "cadena" 
#3._ Crear una variable "strlongitud" que contiene el calor de "longitud" pero convertida a cadena de caracteres o string
#4._ Crear una variable "mayusculas" que contiene la variable "cadena" en mayusculas
#5._ Crear una variable "resultado" que concatene "mayusculas" con el texto "tiene la longitud de " y "strlongitud"

#cadena = "Esto es un texto de ejemplo"
#longitud = len(cadena)
#print(longitud)
#strlongitud = str(longitud)
#mayusculas = cadena.upper()

#resultado = mayusculas + " tiene la longitud de " + strlongitud

#print(resultado)

#Ejercicio

#Crear una variable "numero1" que contiene el valor 5 
#Crear una variable "numero2" que contiene el valor 8 
#Crear una variable "suma" que contiene la suma de los numeros anteriores 
#Imprimir por pantalla el resultado, utilizando la funcion "print"

#numero1 = 5
#numero2 = 8
#suma = numero1 + numero2

#print("El resultado de sumar {} mas {} es {}".format(numero1,numero2,suma))

#Ejercicio

#1.- Imprime por pantalla el texto "Intoduce el primer numero"
#2._ Crear una variable "dato1" con el primero valor introducido en el paso anterior.
#3._ Imprime por pantalla el texto "Intoduce el segundo numero"
#4._ Crear una variable "dato2" con el segundo valor introducido en el paso anterior.
#5._ Convertir la variable "dato1" en una variable numerica denominada "numero1"
#6._ Convertir la variable "dato2" en una variable numerica denominada "numero2"
#7._ Crear la variable "suma" con la suma de "numero1" y "numero2"
#8._Convertir la variable "suma" en una variable de texto denominada "strSuma"
#9._ Crear la variable "resultado" con la concatenacion de "La suma es " y "strSuma"
#10._ Imprimir el valor de resultado

#print("Intoduce el primer numero")
#dato1 = input()
#print("Intoduce el segundo numero")
#dato2 = input()

#numero1 = int(dato1)
#numero2 = int(dato2)

#suma = numero1 + numero2

#strsuma = str(suma)

#resultado =  "La suma es: "+strsuma

#print(resultado)

#Operadores aritmeticos

numero1 = 10
numero2 = 5

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
resto = numero1 % numero2
cociente = numero1 // numero2
potencia = numero1 ** numero2

#print(f"La suma es: {suma}")
#print(f"La resta es: {resta}")
#print(f"La multiplicacion es: {multiplicacion}")
#print(f"La division es: {division}")
#print(f"La resto es: {resto}")
#print(f"La cociente es: {cociente}")
#print(f"La potencia es: {potencia}")

#Operadores de asignacion (=, += -=, *=, /=, **=)

#numero = 5
#print(numero)

#numero = numero + 4
#print(numero)

#numero += 4
#print(numero)

#numero -= 4
#print(numero)

#numero *= 4
#print(numero)

#numero /= 4
#print(numero)

#numero **= 4
#print(numero)

#Operadores de comparacion (==, !=, >, <, >=, <=)

#numero1 = 5
#numero2 = 3

#print(numero1 == numero2)

#lista = ["rojo", "verde", "azul"]

#clases objetos y funciones

class ClaseSillas:
    color = "blanco"
    precio = 100

objeto1 = ClaseSillas()

#print(objeto1.color)
#print(objeto1.precio)

class ClasePersona:
    def __init__(self, nombre,edad ):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print('Hola, me llamo {} y tengo {} años'.format(self.nombre, self.edad))

persona = ClasePersona("Juan", 37)

#print(persona.nombre)
#print(persona.edad)

#persona.saludar()

#Ejercicio 
#Crear una clase coche que tengas estos atributos:
#Marca, Color, Combustible y Cilindrada
#
#Crear la funcion init que asigna los parametros de la clase a los atributos de la clase
#Crear otra funcion mostrarCararteristicas() que mediante print muestre por pantalla las caracteristicas q tiene el coche
#Crear un objeto carrobomba de la clase Carro con los atributos: "chevy", "azul", "gasoil", "1.6"
#Ejecutar la funcion mostrarCararteristicas() del objeto coche1


class CocheBomba:
    def __init__(self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    
    def mostrarCararteristicas(self):
        print(f"marca: {self.marca}")
        print(f"color: {self.color}")
        print(f"combustible: {self.combustible}")
        print(f"cilindrada: {self.cilindrada}")

carrobomba = CocheBomba("chevy", "azul", "gasoil", 1.6)

#carrobomba.mostrarCararteristicas()

#Ejercicio 2
#Hacer una funcion landa que calcule la media de tres nostas

media_de_notas = lambda nota1, nota2, nota3 : (nota1 + nota2 + nota3) / 3

#print(media_de_notas(20, 19, 18))







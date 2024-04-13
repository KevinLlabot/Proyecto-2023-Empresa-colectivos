import math



print("a) Calcular perimetro de triangulo")
print("b) Calcular perimetro de cuadrado")
print("c) Calcular perimetro de rectangulo")
print("d) Calcular perimetro de circulo")
print("e) salir")


opcion = ""

while opcion != "e":

    opcion = input("Ingrese una opcion: ")

    if opcion == "a":
        lado1 = int(input("Ingrese el primer lado: "))
        lado2 = int(input("Ingrese el segundo lado: "))
        lado3 = int(input("Ingrese el tercer lado: "))

        perimetro = lado1 + lado2 + lado3
        print("El perimetro es: ", perimetro)

    elif opcion == "b":
        lado = int(input("Ingrese lado: ")) 
        perimetro = lado * 4

        print("El perimetro es: ", perimetro)  

    elif opcion == "c":
        base = int(input("Ingrese la base del rectangulo: ")) 
        altura = int(input("ingrese la altura del rectangulo: "))   
        perimetro = base * 2 + altura * 2
        print("El perimetro es: " , perimetro)

    elif opcion == "d":
        radio = int(input("Ingrese radio del circulo: ")) 
        perimetro = 2 * 3.14 * radio
        print("El perimetro es: ", perimetro)

    else:
        print("El programa a finalziado...")    

import os, time
os.system("cls")

print("Calculador de edad mínima y máxima de la persona con la que puedes salir o tener sexo.")
time.sleep(3)

edad = float(input("\nIntroduce tu edad: "))
edad2 = float(input("Introduce la edad de la persona con quien quieres estar: "))
os.system("cls")

edad_minima = edad - edad / 3.2
edad_maxima = edad + edad / 3.2
if edad <= 20:
    edad_minima = edad - edad / 9

if edad2 < edad_minima or edad2 > edad_maxima:
    print("Lo siento, no deberías intentar nada con esa persona ya que tiene ", int(edad2), " años\ny tu rango de edad está entre", int(edad_minima), " años y ", int(edad_maxima), " años.")
    if edad2 > edad_maxima:
        print("\nTrata de buscar a alguien menor.")
    else:
        print("\nTrata de buscar a alguien mayor.")
elif edad2 >= edad_minima and edad2 <= edad_maxima:
    print("Felicidades, esa persona está en el rango perfecto ya que tu rango de edad está entre", int(edad_minima), " años y ", int(edad_maxima), " años.\n¿A qué esperas? ¡Ve con esa persona!")
elif (edad2 < 18 and edad >= 40) or (edad2 >= 42 and edad <= 19):
    print("Enfermo.")
    time.sleep(3)
    os.system("cls")
else:
    print("Ha ocurrido un error. Saliendo del programa...")
    time.sleep(4)
    os.system("cls")
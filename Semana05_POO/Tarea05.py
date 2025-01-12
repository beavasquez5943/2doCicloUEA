from operator import truediv

import math

def calcular_area_circulo(radio_cm):
    area = math.pi * (radio_cm ** 2) #formula basica para calcular el area de un circulo
    return area #return resultado final

def convertir_a_metros(radio_cm):
    radio_metros =radio_cm/100 #conversion cm a metros del area
    return radio_metros # return radio en metros

#datos entrada: radio en cm
radio_cm = float(input("introduce el RADIO del circulo en CM"))
#verificacion que el radio sea un numero postivo
if radio_cm>0:
    area_cm2=calcular_area_circulo(radio_cm)#area en cm cuadrados
    radio_metros = convertir_a_metros(radio_cm)#conversion a metros por funciones


    #print de resultados
    print(f"\nEl radio del círculo es: {radio_cm} cm")
    print(f"el radio del circulo en metros es: {radio_metros:.2f} m")
    print(f"el area del circulo es:  {area_cm2:.2f} cm²")

else:
    #devolucion si el numero no es un positivo
    print("el radio debe ser un numero positivo")


todo_bien =  True
print(f"\n¿Ejecución exitosa? {todo_bien}")#boolean para comprobar que la ejecucion sea la correcta
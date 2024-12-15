#funcion ingreso de temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range (7):#ingreso de temperaturas una diaria
        temp=float(input(f"Ingrese la temperatura del dia {i + 1}:"))
        temperaturas.append(temp)
    return temperaturas
#funcion calcular promedio semanal
def calcular_promedio (temperaturas):
    suma_temperaturas=sum(temperaturas)
    promedio=suma_temperaturas/len(temperaturas)
    return promedio

#funcion principal
def main ():
    temperaturas=ingresar_temperaturas()#ingreso de temperaturas diarias
    promedio_semanal=calcular_promedio(temperaturas)#promedio semanal
    print( f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}°C" )#resultado


if __name__ == "__main__":
    main()




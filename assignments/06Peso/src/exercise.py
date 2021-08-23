def main():
    #escribe tu código abajo de esta línea
    peso_inicial = float(input("Ingresa tu peso inicial en kilos: "))
    peso_final = float(input("Ingresa el peso deseado en kilos: "))
    meses = int(input("Ingresa la cantidad de meses que estaras en el proceso: "))
    kg = (peso_inicial - peso_final)/meses
    print ("lo que debes bajar por mes es: " + str(kg))



if __name__ == '__main__':
    main()

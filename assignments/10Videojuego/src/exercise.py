def main():
    #escribe tu código abajo de esta línea
    juegos_nuevos = int(input("Ingrese la cantidad de juegos nuevos que comprará: "))
    juegos_usados = int(input("Ingrese la cantidad de juegos usados que comprará: "))
    total = juegos_nuevos *1000 + juegos_usados*350
    print ("El total de la compra es: " + str(total))




if __name__ == '__main__':
    main()

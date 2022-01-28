peso = float (input('Ingrese su peso en kg: '))
estatura = float (input('Ingrese su estatura en metros: '))
total = (peso / (pow(estatura, 2)))
print('Tu indice de masa corporal es de: ',"{:.2f}".format(total)) 
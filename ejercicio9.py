inversion = float (input('Con que cantidad desea empezar a invertir: '))
interes = float (input('De cuanto va a ser el interes anual: '))
duracion = int (input('Cuantos años desea hacer la inversion: '))

total = str(((inversion * interes/100))*duracion)
print('El total de intereses generados en ', duracion, 'años es de ', total)
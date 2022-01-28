payasos = int (input('Ingrese la cantidad de payasos vendidos: '))
mu = int (input('Ingrese la cantidad de muñecas vendidos: '))
peso1 = 112 * payasos
peso2 = 75 * mu
totalpeso = peso1 + peso2
totalve = payasos + mu
print('En el ultimo pedido se vendieron un total de', totalve, 'y el peso total del paquete es de',totalpeso,'g')
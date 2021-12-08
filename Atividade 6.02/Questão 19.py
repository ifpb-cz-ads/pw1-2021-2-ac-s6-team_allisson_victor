#19) Altere o programa abaixo de forma a imprimir o menor elemento da lista.

lista = [10,7,2,4]
menor = lista[0]
for elemento in lista:
	if elemento < menor:
    		menor = elemento
print(menor)
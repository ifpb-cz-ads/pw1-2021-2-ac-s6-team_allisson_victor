#13) Escreva um programa que leia números inteiros do teclado. O programa deve ler os números 
# até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, 
# assim como a soma e a média aritmética.
i = 1
cont = 0
soma = 0
print ("Para parar de digitar numero digite 0 !")
while i != 0:
    num = int(input("Digite um numero: "))
    i = num
    if(num!=0):
        cont = cont +1
        soma = soma + num

media = soma / cont

print("Voce digitou ",cont," numeros")
print("A soma de todos os numero digitados é ",soma)
print("A media desses numero é ",media)
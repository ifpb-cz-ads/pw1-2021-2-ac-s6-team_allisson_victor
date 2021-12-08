aux = 1
escolha = 0
Total = 0
while aux != 0:
     Codigo = int(input("Informe o valor do produto, para encerrar a soma digite 0:"))
     if Codigo == 1 or Codigo == 2 or Codigo == 3 or Codigo == 5 or Codigo == 9 or Codigo == 0:
        if Codigo == 1 :
            escolha = 0.50 
        if Codigo == 2 :
            escolha = 1.0 
        if Codigo == 3 :
            escolha = 4.0 
        if Codigo == 5 :
            escolha = 7.0 
        if Codigo == 9 :
            escolha = 8.0
        Total += escolha 
        if Codigo == 0:
           aux = Codigo 
     else :
         print("Valor invalido")
print("Valor tota: %2.f"%Total)               
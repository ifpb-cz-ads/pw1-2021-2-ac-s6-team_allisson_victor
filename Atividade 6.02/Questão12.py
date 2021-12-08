Divida = float(input("Informe o valor da divida:"))
Juros = float(input("Informe o valor da porcentagem do juros:"))
ValorM= float(input("Informe o valor pago mensalmente:"))
aux = 0
TotalJuros = 0
ValorAtualDivida = Divida
while ValorAtualDivida > 0 :
    TotalJuros += ValorAtualDivida*(Juros/100)
    ValorAtualDivida += TotalJuros
    ValorAtualDivida -= ValorM
    aux += 1
    if ValorAtualDivida > Divida:
        ValorAtualDivida = 0
        print("Você nunca terminara de pagar sua divida! (F)")
if ValorAtualDivida != 0 :
    print("Voce ira demorar",aux,"meses para pagar sua divida de valor:%.2f"%Divida)
    print("Voce ira pagar de juros ao final da divida:%.2f"%TotalJuros)
Valor = float(input("Informe o valor do deposito:"))
Juros = float(input("Informe o valor da taxa do juros"))
ValorMensal = Valor
TotalDoJuros = 0
for n in range(12):
    TotalDoJuros += ValorMensal*(Juros/100)
    ValorMensal += TotalDoJuros
    print("Valor Mensal:%.2f"%ValorMensal)
ValorTotal = ValorMensal - Valor
print("Total ganho em Juros:%.2f"%ValorTotal)   
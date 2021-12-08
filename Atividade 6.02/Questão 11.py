#11) Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. 
# Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de 
# juros do mês seguinte.

Valor = float(input("Informe o valor do deposito: "))
Juros = float(input("Informe o valor da taxa do juros: "))
TotalDoJuros = 0
ValorMensal = Valor
aux = 0
for n in range(12):
    if aux==0:
        TotalDoJuros += ValorMensal*(Juros/100)
        ValorMensal += TotalDoJuros
        print("Valor Mensal:%.2f"%ValorMensal)
    if aux == 1:
        mensalmente = float(input("Informe o valor do deposito:"))
        TotalDoJuros +=  ValorMensal*(Juros/100)
        ValorMensal += TotalDoJuros + mensalmente
        print("Valor Mensal:%.2f"%ValorMensal)
    aux = 1
ValorTotal = ValorMensal - Valor
print("Total ganho em Juros: %.2f"% ValorTotal)
salarioMensal = float(input("Digite seu salário mensal:"))
horasSemana = float(input("Quantas horas você trabalha na semana?:"))
horasMes = horasSemana * 4
salarioHora = salarioMensal/horasMes
print(f"Seu salário por hora é de R${salarioHora:.2f}")

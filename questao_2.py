salario = float(input("Digite o Salario: "))

vendas = float(input("Digite as vendas: "))

vendas1 = (vendas*5/100)
vendas2 = (((vendas-1500)*7/100)+1500*(5/100))
if vendas<=1500:
  print(f"Sua comissão será de 5%, totalizando R$", vendas1)
  print(f"Seu salario mais a comissão de 5% será de R$", (salario+vendas1))

else:
  print(f"Sua comissão será de R$", vendas2)
  print(f"Seu salario mais a comissão será de R$", (salario+vendas2))

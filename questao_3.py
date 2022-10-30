
a = 15000
b = 45000
c = 65000
ano = 0


while a<=b:
    a += a*0.1
    b += b * 0.05
    ano += 1

print(f"Ano A igualará ou ultrapassará a população de B em ", ano, " anos")

while ((a-c)/c)<=0.23:  
    a += a*0.1
    c += c * 0.025
    ano += 1

print(f"A população A ultrapassará a população de C em 23% em  ", ano, " anos")




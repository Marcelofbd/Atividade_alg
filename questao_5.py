n = int(input("Digite um número inteiro maior ou igual a 50: "))
h=0
s=0
p=0
n_max=n

while n > 1:

    if n%2 == 0:
        h += (n*2-1)/n
        s -= n/(n*n)
    if n%2 == 1:
        h -= (n*2-1)/n
        s += n/(n*n)
    n -= 1
c, pot = 0, 1

while True:
    
    while c != n_max:
        c +=1
        mult = c
        tt = 0
        while (mult != 1):
            if c % mult == 0:
                tt += 1
            mult -= 1
        if tt == 1:
            p += c/pot**3
            pot += 2
    if c == n_max:
        break


print (f"O valor de H é de: ", h)
print (f"O valor de S é de: ", s)
print (f"O valor de P é de: ", p)
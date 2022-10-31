sequencia_c = 0
sequencia_c_max = 0
sequencia_i = 0
sequencia_i_max = 0
x = 1

num1 = int(input(f'Digite o número {x}: '))
while (x < 150):

    x +=1
    num2 = int(input(f'Digite o número {x}: '))

    if num1 < num2:
        sequencia_c += 1

        if sequencia_c >= sequencia_c_max:
            sequencia_c_max = sequencia_c + 1

    if num1 > num2:
        sequencia_c = 0

    if num1 == num2:
        sequencia_i +=1

        if num1 > elem_igual:
            elem_igual = num1

        if sequencia_i >= sequencia_i_max:
            sequencia_i_max = sequencia_i + 1

    if num1 != num2:
        sequencia_i = 0

    num1 = num2

if (sequencia_c_max > 0):
    print(f"A maior sequência consecutivaé de: ", sequencia_c_max)

if (sequencia_i_max > 0):
    print(f"A maior sequência consecutiva de números constantes é: ",sequencia_i_max)

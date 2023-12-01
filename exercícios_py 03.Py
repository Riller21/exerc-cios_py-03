número = int(input("Insira um número: "))

if número <= 0:
    print("Número invalido" )
else:
    if número % 2 == 0: #usando operador modulo (%) para achar o resto da divisao do número por dois. Se o resto for zero, o número é par.
        print("O número",número,"é par.")
    else:
        print("O número",número,"é impar.")
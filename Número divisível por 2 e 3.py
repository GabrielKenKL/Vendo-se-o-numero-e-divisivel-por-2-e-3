print("Verificando se o número é divisível por 2 e 3...")
print("Digite seu número:")

#declarar.
n1 = int(input())

#início.
if n1 % 2 == 0 and n1 % 3 == 0:
    print("O número" , n1 , "é divisível por 2 e 3.")
elif n1 % 2 == 0 and n1 % 3 != 0:
    print("O número" , n1 , "é divisível por 2, mas não é divisível por 3.")
elif n1 % 2 != 0 and n1 % 3 == 0:
    print("O número" , n1 , "é divisível por 3, mas não é divisível por 2.")
else:
    print("O número" , n1 , "não é divisível por 2 e nem por 3.")
#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
n=int(input("Me diga um número correspondente a um dia da semana:\n"))
if n==2:
    print("Segunda!")
elif n==3:
    print("Terça!!")
elif n==4:
    print("Quarta!")
elif n==5:
    print("Quinta!")
elif n==6:
    print("Sexta!")
elif n==7:
    print("Sabado")
elif n==1:
    print("Domingo")
else:
    print("Valor invalido!")
import math

entrada= input("Estas en un programa que et mostra els divisors de un nombre que tu tries, desitges continuar pitge qualsevol nombre, si desitges sortir prem 'q': ")
while entrada !="q":
    nombre= int(input("Digues un nombre per dir-te els seus divisors: "))
    for i in range (1,nombre):
        if nombre%i==0:
            print(f"{i} és divisor de {nombre}")
    entrada=input("Si desitges contiunar prem qualsevol nombre, per sortir prem 'q'")

print ("Adeu")
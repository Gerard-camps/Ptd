num1= int(input("Digues un nombre qualsevol i et dire si es parell o senar: "))
num2= int(input("Digues un altre nombre qualsevol i et dire si els dos son parells o senars: "))

if num1%2 ==0 and num2%2 ==0:
    print("Els dos nombres son pars")
elif num2%2 !=0 and num1%2 != 0:
    print("Els dos nombres son imparells")
elif num1%2 ==0 and num2%2 != 0:
    print(f"El primer nombre{num1}, es parell i el nombre {num2} es imparell. ")
else:
    print(f"El primer nombre{num2}, es parell i el nombre {num1} es imparell. ")
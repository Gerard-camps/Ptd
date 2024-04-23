nota= int(input("Digues la nota que has trat al darrer examen: "))

if nota < 5:
    print("La teva nota es INSUFICIENT. ")
elif nota >= 5 and nota < 6:
    print("La teva nota es un SUFICIENT. ")
elif nota >= 6 and nota < 7:
    print("La teva nota es un BÉ. ")
elif nota >=7 and nota < 9:
    print("La teva nota és un NOTABLE. ")
else:
    print("La teva nota es un EXCEL·LENT. ")
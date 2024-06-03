entrada= input("Estas en un programa que et mostra els multriples de un nombre que tu tries, desitges continuar pitge qualsevol nombre, si desitges sortir prem 'q': ")
while entrada !="q":
    k= int(input("Digues un nombre per dir-te els seus multriples: "))
    n= int(input("Fins quin nombre vols que et digui els multriples del nombre anterior?"))

    for i in range(k,n+1,k):
        print(f"{i} és multriple de {k}")
    entrada=input("Si desitges contiunar prem qualsevol nombre, per sortir prem 'q'")

print ("adeu")
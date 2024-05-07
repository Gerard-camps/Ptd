resposta_usuari= input("Estas en un programa que suma els nombre fins el nombre que tu desitges per exemple 1+1=2 2+2=4 fins al nombre que diguis, si destigues sortir del programa pitja la tecla 'q': ")
while resposta_usuari != "q":
    suma=0
    n= int(input("Digues un nombre i anire sumant els nombres fins arribar al teu nombre: "))
    for i in range (n):
        suma+=i
    print(f"{suma}")
    resposta_usuari=input("Si desitges sortir perm la tecla 'q': ")

print("Has sortit")
resposta_usuari = input("Prem qualsevol tecla per a començar i 'q' per a sortir del programa")

usuari =(input("Escriu l'usuari: "))

contrasenya =(input("Escriu la contrasenya: "))

while resposta_usuari != "q":
    if usuari != "gerardcamps":
        print("L'usuari no es correcta")
    else:
        print("L'usuari és correcta")

    if contrasenya != "fernandez":
        print("La contraenya no es correcta")
    else: 
        print("La contrasenya es correcta")
    resposta_usuari = input("Prem qualsevol tecla per a començar i 'q' per a sortir del programa")

print("Benvingut a l'escriptori ")

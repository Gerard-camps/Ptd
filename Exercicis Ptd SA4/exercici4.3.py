print("Estas en un programa on els 0's son canviats per x")
resposta_usuari=input("Si vols entrar prem qualsevol tecla sinos pitja 'q' per sortir")
while resposta_usuari != 'q':
    nombre = input("Escriu el nombre que vols utilitzar: ")
    nombre_nou=""
    for i in range(len(nombre)):
        lletra=nombre[i]
        lletra=lletra.lower()
        if not (lletra == '0'):
            nombre_nou+=lletra
        else:  
            nombre_nou+="x"  
    nombre_nou = nombre_nou.upper()
    print(nombre_nou) 
    resposta_usuari=input("Si vols entrar prem qualsevol tecla sinos pitja 'q' per sortir")

print("Adeu")
    
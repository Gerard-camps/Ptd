correu_usuari= input("Escriu aqui el teu correu: ")
nom_usuari=""
domini=""
dns=""
for i in range(len(correu_usuari)):
    caracter=correu_usuari[i]
    if caracter!="@":
        nom_usuari+=caracter
    else:
        break
for a in range (len(correu_usuari)):
    a+=i+1
    caracter=correu_usuari[a]
    if caracter!=".":
        domini+=caracter
    else:
        break
for e in range (len(correu_usuari)):
    e+=a+1
    caracter=correu_usuari[e]
    dns+=caracter
    if e>= (len(correu_usuari)-1):
        break
    

print(f"Nom d'usuari: {nom_usuari}")
print(f"Nom del domini: {domini}")
print(f"Dns: {dns}")
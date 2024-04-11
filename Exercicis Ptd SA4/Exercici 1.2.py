nombre= int(input("Escriu un multriple de 3: "))
resultat= nombre%3
while resultat != 0:
    print(f"El nombre {nombre}, que has escollit no es multriple de 3.")
    resultat = int(input("Escriu un multriple de 3: "))%3
print("Aquest si és multriple de 3!")
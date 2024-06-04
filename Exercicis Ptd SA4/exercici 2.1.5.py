entrada= input("Si vols contiuneuar amb el programa pitja qualsevol tecla, sino pirem 'q'. ")
nombre= int(input("Digues fins quin nombre vols que faixi una suma alterna: "))

while entrada != "q":
    n=0
    for i in range(1,nombre):
        n+=i*(-1)**(i+1)
    print(n)
    entrada= input("Si vols contiuneuar amb el programa pitja qualsevol tecla, sino pirem 'q'. ")
    nombre= int(input("Digues fins quin nombre vols que faixi una suma alterna: "))
print ("Adeu")
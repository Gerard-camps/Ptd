print("""+================================+
| ¡Benvingut al meu joc, muggle! |
| Introdueix un nombre enter     |
| i encerta el que he            |
| escollit per a tu.             |
|¿Quin és el meu nombre secret?  |
+================================+""")


nombre_jugador= int(input("Digues el nombre secret: "))

nombre_secret= 34375

while nombre_jugador != nombre_secret:

    print("JA JA JA, estas atrapat en el meu bucle! ")
    nombre_jugador= int(input("Digues un altre nombre secret: "))
              
print("Ben fet muggle! Ets lliure")



x= input("Estas en un programa que et mostra la taula de multriplicar que vulguis. Si desitges sortir prem la tecla 'q': ")
while x != "q":
    resposta_usuari= int(input("Digues la taula de multriplicar que vulguis que et mostri: "))
    comptador= 0
    while comptador <= 10:
        print(f"{comptador}*{resposta_usuari}= {comptador*resposta_usuari}")
        comptador+=1
    x= input("Si desitges sortir prem la tecla 'q': ")

print("Adeu")





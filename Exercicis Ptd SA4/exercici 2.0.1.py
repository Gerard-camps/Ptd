x= input("Estas en un programa que el mostra la taula de multriplicar que vulguis. Si desitges sortir prem la tecla 'q': ")

while x!= "q":
    taula= int(input("Digues la taula que vols que et mostri: "))
    for i in range(11):
        print (f"{taula}*{i}= {taula*i}")
    x= input("Si desitges sortir prem la tecla 'q': ")

print("Adeu")
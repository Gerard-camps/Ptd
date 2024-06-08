

print("Estas a un programa que elimina les vocals de una paraula")
input ("si vols entrar al programa pitja qualsevol lletre, sinor prem 'q'")
x= "a"
while x!= 'q':
    paraula = input("Escriu la paraula que vols utilitzar: ")
    paraula_nova=""
    for i in range(len(paraula)):
        lletra=paraula[i]
        lletra=lletra.lower()
        if not (lletra == 'a' or lletra == 'e' or lletra == 'i' or lletra == 'o' or lletra =='u'):
            paraula_nova+=lletra
        else:  
            paraula_nova+=""  
    paraula_nova = paraula_nova.upper()
    print(paraula_nova) 
    x= input("Escriu la paraula que vols utilitzar o q per sortir: ")    

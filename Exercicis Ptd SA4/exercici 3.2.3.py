entrada= input("Estas en un programa que comprova la llei de Collaz, si desitges continuar prem qualsevo, tecla, sino prem 'q': ")

while entrada!= "q":
    cO= int(input("Digues un nombre que no sigui 0 ni negatiu per comprovar la llei: "))
    contador=0
    print(f"El numero de entrada es {cO}") 
    while cO!= 1:
        if cO%2==0:
            cO=cO/2
            contador+=1
        elif cO%2!=0:
            cO=(cO*3)+1 
            contador+=1                           
        print(f"{cO}")
       
    print(f"Ha fet {contador} passes")
    entrada= input("Estas en un programa que comprova la llei de Collaz, si desitges continuar prem qualsevo, tecla, sino prem 'q': ")
print("Adeu")


    

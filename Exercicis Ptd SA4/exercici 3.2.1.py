entrada= input("Desitges entrar a aquest programa? prem qualsevol tecla per entra, prem 'q' per sortir: ")
contrasenya_1= input("Estats a un programa que has de endevinar la contrasenya per sortir, quina es la contransenya: ")
contrasenya_0= "sortir"
while entrada!= "q":
    if contrasenya_1 != contrasenya_0:
        print(f"Resposta {contrasenya_1} incorrecta")
        contrasenya_1= input("Estats a un programa que has de endevinar la contrasenya per sortir, quina es la contransenya: ")
    else:
        break

print("Has sortit")
resposta_usuari= input("Si vols entrar al programa que segons el nombre de capses et diu quants pisos 'una piramida te, prem qualsevol boto, si vols sortir prem 'q': ")
pisos=0
n= int(input("Quantes caixes tenim:"))
capses_2=n
while resposta_usuari != 'q':
    
    
    if pisos>=capses_2:
        break
    else:
        pisos+=1
        capses_2=capses_2-pisos
        

print(f"Té {pisos} pisos i s'han utilitzat {n} capses")

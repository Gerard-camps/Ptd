par1= int(input("Digues un nombre per al paràmetre 1 d'una equació de segon grau: "))
par2= int(input("Digues un nombre per al paràmetre 2 d'una equació de segon grau: "))
par3= int(input("Digues un nombre per al paràmetre 3 d'una equació de segon grau: "))
x1= (-par2+((par1**2)+(par3**2)-4*(par1)*(par3))**1/2)/(2*(par1))
x2= (-par2-((par1**2)+(par3**2)-4*(par1)*(par3))**1/2)/(2*(par1))
if (par1**2)+(par3**2)-4*(par1)*(par3) ==0 :
    print(f"Només te una solució: {x1}")
elif  (par1**2)+(par3**2)-4*(par1)*(par3) >=0 :
    print (f"Té dues solucions: {x1} i {x2}")
else:
    print()
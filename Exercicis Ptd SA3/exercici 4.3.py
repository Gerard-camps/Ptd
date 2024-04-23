num1= int(input("Digues un nombre i et dire quin dia de la setmana és: "))
dia=num1%7
if num1 == 0:
    print(f"El nombre {num1}, és dilluns.")
elif num1 == 1:
    print(f"El nombre {num1}, és dimarts.")
elif num1 == 2:
    print(f"El nombre {num1}, és dimecres.")
elif num1 == 3:
    print(f"El nombre {num1}, és dijous.")
elif num1 == 4:
    print(f"El nombre {num1}, és divendres.")
elif num1 == 5:
    print(f"El nombre {num1}, és disapte.")
elif num1 == 6:
    print(f"El nombre {num1}, és diumenge.")

num1= int(input("Digues un nombre i et dire si has encertat el nombre establert, si t'has pasat o t'has quedat curt: "))
num_est= 12
if num1 > 12:
    print(f"T'has pasat, el nombre{num1} és més gran que l'establert.")
elif num1 < 12:
    print(f"T'has quedat curt, el nombre {num1}, és més petit que l'establert.")
else:
    print("Has encertat el nombre establert.")
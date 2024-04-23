num = int(input("Digues un nombe qualseol i et dire si es parell, senar o 0: "))

if num%2 ==0:
    print(f"Els nombre {num} és parell")
elif num%2 !=0:
    print(f"El nombre {num} és imparell")
else:
    print(f"El nombre {num} és 0")
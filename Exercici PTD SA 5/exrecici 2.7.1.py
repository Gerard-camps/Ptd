any= ["Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "septembre", "Octubre", "Novembre", "Desembre"]

mes = int(input("Digues el mes de l'any amb nombre: "))

if mes < 1 or mes > 7:
    print("No és un dia vàlid")
else:
    print(any[mes - 1])
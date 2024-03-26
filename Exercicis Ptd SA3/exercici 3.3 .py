hores_set = int(input("Quantes hores tereballes a la setmana: "))
if hores_set <= 40 :
    print(f"El que has guanyat aquesta setmana és {hores_set*16} €")
else:
    print(f"Aquesta setmana has guanyat {hores_set*16 + (hores_set-40)*20}")
setmana = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Disapte", "Diumenge"]
dies_feiners=setmana[:-2]
no_feina=setmana[5:]
tots_menosdillidim= setmana [2:]
dim_dij_div=setmana[2:5]
no_diumenge=setmana[:-1]
print(f"Dies defeina: {dies_feiners}")
print(f"Dies no feiners: {no_feina}")
print(f"Dies menos dilluns i dimarts: {tots_menosdillidim}")
print(f"entre setmana: {dim_dij_div}")
print(f"Tots els dies menos diumenge: {no_diumenge}")

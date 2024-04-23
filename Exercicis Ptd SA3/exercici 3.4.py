num_cam= int(input("Quantes camisetes vols comprar: "))
preu_cam= 12
if num_cam>=3:
    print(f"El preu de les camisetes és: {num_cam*preu_cam*0.8} €")
else:
    print(f"El preu de les camisetes és: {num_cam*preu_cam*0.9} €")
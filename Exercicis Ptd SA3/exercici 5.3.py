import random

tirada_daus = random.randint(2,12)
print(f"La tirada és {tirada_daus}")
if tirada_daus == 2 or tirada_daus == 3 or tirada_daus == 12:
    print("Has guanyat. ")
elif tirada_daus == 7:
    print("Has perdut. ")
else:
    print("empat. ")
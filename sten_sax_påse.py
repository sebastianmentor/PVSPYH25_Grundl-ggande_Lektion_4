import random

"""
1 = sten
2 = sax
3 = påse
"""

lista_med_val = ("1", "2", "3")

datorns_poäng = 0
användarens_poäng = 0

print("Välkommen till sten sax påse! Jag kommer spöa skiten ur dig!")
while True:
    datorns_val = random.choice(lista_med_val)
    print(f"Nuvarande poängställning: {datorns_poäng=} {användarens_poäng=}")
    print("Att välja mellan:")
    print("1. Sten")
    print("2. Sax")
    print("3. Påse")
    användarens_val = input("Gör ett val: ")

    #
    if datorns_val == användarens_val:
        print("Oavgjort! Vi spelar igen!")
        continue

    elif användarens_val == "1":
        ##
        if datorns_val == "2":
            print("Du vann!")
            användarens_poäng += 1

        else:
            print("Du förlora!")
            datorns_poäng += 1
        ##
    elif användarens_val == "2":
        ##
        if datorns_val == "3":
            print("Du vann!")
            användarens_poäng += 1

        else:
            print("Du förlora!")
            datorns_poäng += 1
        ##
    elif användarens_val == "3":
        ##
        if datorns_val == "1":
            print("Du vann!")
            användarens_poäng += 1

        else:
            print("Du förlora!")
            datorns_poäng += 1
        ##
    else:
        print("Felaktigt val! Vi kör om!")
    #

    spela_igen = input(f"Vill du spela igen?(y/n)").lower()
    if spela_igen == "n":
        break

 
# Sluttext 
print("Slutgiltliga poängen blev:")
print(f"Datorn fick {datorns_poäng}!")
print(f"Du fick {användarens_poäng}!")

if datorns_poäng == användarens_poäng:
    print("Det blev oavgjort!")
elif datorns_poäng > användarens_poäng:
    print("Datorn vann! Go back to school you looser!")
else:
    print("Du spöa mig! I bow to you master!!!")
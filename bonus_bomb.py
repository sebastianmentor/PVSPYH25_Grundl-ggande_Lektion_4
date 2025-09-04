import time

heltal = input("Ange ett heltal: ")

if (heltal[0]=="-") and heltal[1:].isdigit():
    print("Oj, du kan inte läsa! Vi sa ett positivt heltal!!!")

elif not heltal.isdigit():
    print("Error, det du skrev var inte ett heltal!!!!")

else:
    heltal = int(heltal)
    while heltal >= 0:
        print(heltal)
        heltal = heltal - 1
        time.sleep(1)


counter = 0

while True:
    choice = input("Vill du avsluta? (q)")
    if choice == "q":
        break
    counter += 1

print(f"Vi körde loopen {counter} antal gånger!")
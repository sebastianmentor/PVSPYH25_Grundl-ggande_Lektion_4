########################################
#             Uppgift 3                #
########################################

# heltal = input("Ange ett heltal: ")

# if (heltal[0]=="-") and heltal[1:].isdigit():
#     print("Oj, du kan inte läsa! Vi sa ett positivt heltal!!!")

# elif not heltal.isdigit():
#     print("Error, det du skrev var inte ett heltal!!!!")

# else:
#     heltal = int(heltal)
#     summa = 0
#     while heltal > 0:
#         summa = summa + heltal 
#         heltal = heltal - 1

#     print("Summan blev:", summa)

########################################
#             Uppgift 4                #
########################################

# heltal = input("Ange ett heltal: ")

# if (heltal[0]=="-") and heltal[1:].isdigit():
#     print("Oj, du kan inte läsa! Vi sa ett positivt heltal!!!")

# elif not heltal.isdigit():
#     print("Error, det du skrev var inte ett heltal!!!!")
    
# else:
#     heltal = int(heltal)
#     produkt = 1
#     while heltal > 0:
#         produkt = produkt * heltal 
#         heltal = heltal - 1

#     print("Produkten blev:", produkt)

########################################
#             Uppgift 5                #
########################################

# heltal = input("Ange ett heltal: ")

# if (heltal[0]=="-") and heltal[1:].isdigit():
#     print("Oj, du kan inte läsa! Vi sa ett positivt heltal!!!")

# elif not heltal.isdigit():
#     print("Error, det du skrev var inte ett heltal!!!!")
    
# else:
#     heltal = int(heltal)
#     heltal2 = heltal
#     first = 0
#     second = 1
#     print(f"{first},{second}", end="")
#     while heltal > 0:
#         third = first + second
#         print(f",{third}", end="")
#         # uppdatera de tidigare värdena
#         first = second
#         second = third

#         heltal = heltal - 1
#     print()

#     # med listor
#     fib_seq = [0, 1]
#     # fib(n) = fib(n-1) + fib(n-2)
#     for _ in range(heltal2):
#         new_fib = fib_seq[-1] + fib_seq[-2]
#         fib_seq.append(new_fib)

#     print(fib_seq)

########################################
#             Uppgift 6                #
########################################

# heltal = input("Ange ett heltal: ")

# if (heltal[0]=="-") and heltal[1:].isdigit():
#     print("Oj, du kan inte läsa! Vi sa ett positivt heltal!!!")

# elif not heltal.isdigit():
#     print("Error, det du skrev var inte ett heltal!!!!")
    
# else:
#     heltal = int(heltal)
#     for i in range(1, 11):
#         print(f"{heltal} * {i:<2} = {heltal*i}")

########################################
#             Uppgift 7                #
########################################

# heltal = input("Ange ett heltal: ")

# if (heltal[0]=="-") and heltal[1:].isdigit():
#     print("Oj, du kan inte läsa! Vi sa ett positivt heltal!!!")

# elif not heltal.isdigit():
#     print("Error, det du skrev var inte ett heltal!!!!")
    
# else:
#     N = int(heltal)
     
#     # 2,3,4,5,6,...,N
#     for tal in range(2,N + 1):

#         tal_is_prime = True

#         for devisor in range(2,tal):
#             if tal % devisor == 0:
#                 tal_is_prime = False
#                 break

#         if tal_is_prime:
#             print(f"talet {tal} är ett primtal!")

########################################
#             Uppgift 12               #
########################################

# x,y = input("Skiv int 2 tal separerade med mellanslag: ").strip().split()

lista_med_jämna_tal = []
lista_med_udda_tal = []
lista_med_tal = []

while True:
    nytt_tal = input("Ange ett tal eller q för att avsluta: ")

    if (nytt_tal[0]=="-") and nytt_tal[1:].isdigit():
        lista_med_tal.append(int(nytt_tal))

    elif nytt_tal.isdigit():
        lista_med_tal.append(int(nytt_tal))

    elif nytt_tal == "q":
        break

    else:
        print("Ogiltlig input!!!")

for tal in lista_med_tal:
    if tal % 2 == 0:
        lista_med_jämna_tal.append(tal)
    else:
        lista_med_udda_tal.append(tal)

print(lista_med_jämna_tal)
print(lista_med_udda_tal)

# kolla bubblesort om ni vill försöka implementera en sorteringsalgoritm!
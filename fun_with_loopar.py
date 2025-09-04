lista_med_namn = ["Sebastian", 
                  "Kalle", 
                  "Siv"]

############################
# Skriver ut listan med namn
for namn in lista_med_namn:
    print(namn)
############################

# Skriver ut listan med namn fast namnen baklänges
for namn in lista_med_namn:
    print(namn[::-1])
############################
# Skriver ut listan baklänges
for namn in lista_med_namn[::-1]:
    print(namn)

############################
# Skriver ut listan baklänges och namnen baklänges
for namn in lista_med_namn[::-1]:
    print(namn[::-1])

############################

# for namn in lista_med_namn[::-1]:
#     # reversed_name = "".join(list(reversed(namn)))
#     # reversed_name = namn[::1]
#     reversed_name = namn[::-1]
#     print(reversed_name)

####################################
# Använder range för att få index för att stega igenom listan
for i in range(len(lista_med_namn)):
    print(lista_med_namn[i])

####################################
print("Använder range för att få index för att stega igenom listan baklänges")
sista_indexvärde = len(lista_med_namn)-1
for i in range(sista_indexvärde,-1,-1):
    print(lista_med_namn[i])

###################################

# # Manipulerar listan under körning, riskerar att krascha programmet!
# for i in range(len(lista_med_namn)):
#     namnet = lista_med_namn.pop()
#     # print(namnet[::-1])
#     print(lista_med_namn[i])
print("For-loop med pop")
for namn in lista_med_namn:
    print(namn)
    lista_med_namn.pop()
print(lista_med_namn)


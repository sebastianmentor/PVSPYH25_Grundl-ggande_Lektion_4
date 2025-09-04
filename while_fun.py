# while True:
#     print("Vi kommer köra för evigt!!!!!")

# # Version 1
# guess = input("Gissa vad meningen med livet är?\n")

# while guess != "42":
#     print("Ha!!! Du gissa fel!")
#     guess = input("Igen! Gissa meningen med livet?\n")

# print('Gratulerar!! Du gissa rätt!')

# Version 2

# run_program = True
# while run_program:
#     guess = input("Gissa vad meningen med livet är?\n")

#     if guess == "42":
#         print('Gratulerar!! Du gissa rätt!')
#         run_program = False
#     else:
#         print("Du gissa fel!")

# Version 2.2 with brake
while True:
    guess = input("Gissa vad meningen med livet är?\n")

    if guess == "42":
        print('Gratulerar!! Du gissa rätt!')
        break
    else:
        print("Du gissa fel!")

# messing with loops

# for i in range(100):
#     print(i)
#     if i == 42: break
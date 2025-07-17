# Jednoduchy kalkulator
# a = 10
# b = 3

# sucet = a + b
# rozdiel = a - b 
# sucin = a * b
# podiel = a / b

# zaokruhleny_podiel = round(podiel, 2)

# print(f"sucet cisel {a} a {b} je {sucet}")
# print(rozdiel)
# print(sucin)
# print(zaokruhleny_podiel)

#osetrenie co ak druhe cislo bude nula (ak je prve nulove tak program bude bezat)

# num1 = int(input("zadaj prve cislo"))
# num2 = int(input("zadaj druhe cislo"))

# sucet = num1 + num2
# rozdiel = num1 - num2 
# sucin = num1 * num2

# print(f"sucet cisel {num1} a {num2} je {sucet}")
# print(rozdiel)
# print(sucin)

# if num2 == 0:
#     print ("delenie nulou nie je povolene")
# else:
#     podiel = num1 / num2
#     zaokruhleny_podiel = round(podiel, 2)
#     print(podiel)
#     print(zaokruhleny_podiel)

# pridat moznost ukoncit program (nekonecny cyklus cez while break) a pridanie moznosti vyberu + - * /

# while True:

#     vstup1 = input("Zadaj prve cislo alebo napis stop pre ukoncenie")
#     if vstup1.lower() == "stop":
#         print("Program ukonceny")
#         break

#     vstup2 = input("Zadaj druhe cislo alebo napis stop pre ukoncenie")
#     if vstup2.lower()  == "stop":
#         print("Program ukonceny")
#         break
#     try:
#         num1 = int(vstup1)
#         num2 = int(vstup2)
#     except ValueError:
#         print("Zadal si neplatne cislo. Skus to znova\n")
#         continue
#     while True:
#         vstup3 = input("Vyber jednu z moznosti: +, -, *, /,")
#         if vstup3.lower() == "+":
#              sucet = num1 + num2
#              print(f"sucet {num1} + {num2} = {sucet}")
#              break
        
#         elif vstup3.lower() == "-":
#              rozdiel = num1 - num2
#              print(f"rozdiel cisel {num1} - {num2} je {rozdiel}")
#              break
        
#         elif vstup3.lower() == "*":
#              sucin = num1 * num2
#              print (f"sucin cisel {num1} * {num2} je {sucin}")
#              break
        
#         elif vstup3.lower() == "/":
#              if num2 == 0:
#                  print("delenie nulou nie je povolene")
#              else:
#                 podiel = num1 / num2
#                 zaokruhleny_podiel = round(podiel, 2)
#                 print(f"podiel cisel {num1} / {num2} je {podiel}")
#                 print(f"zaokruhleny podiel na 2 des. miesta je {zaokruhleny_podiel}")
#                 break    

#     print("\nAk chceš zadať nové čísla, pokračuj. Alebo napíš 'stop' pre ukončenie.\n")



# pridat desatine cisla 
while True:

    vstup1 = input("Zadaj prve cislo alebo napis stop pre ukoncenie")
    if vstup1.lower().startswith("stop"):
        print("Program ukonceny")
        break

    if vstup1.strip() == "":
        print("Nic si nezadal \n")
        continue # vrati sa na zaciatok cyklu

    vstup2 = input("Zadaj druhe cislo alebo napis stop pre ukoncenie")
    if vstup2.lower().startswith("stop"):
        print("Program ukonceny")
        break

    if vstup2.strip() == "":
        print("Nic si nezadal \n")
        continue # vrati sa na zaciatok cyklu

    try:
        num1 = int(vstup1)
        num2 = int(vstup2)
    except ValueError:
        try:
            num1 = float(vstup1)
            num2 = float(vstup2)
        except ValueError:
            print("Zadal si neplatne cislo. Skus to znova\n")
            continue 
    while True:
        vstup3 = input("Vyber jednu z moznosti: +, -, *, /,")
        if vstup3.strip() == "":
            print("Nic si nezadal \n")
            continue # vrati sa na zaciatok cyklu
    
        if vstup3.lower() == "+":
             vysledok = num1 + num2
             print(f"sucet {num1} + {num2} = {vysledok}")
             break
        
        elif vstup3.lower() == "-":
             vysledok = num1 - num2
             print(f"rozdiel cisel {num1} - {num2} je {vysledok}")
             break
        
        elif vstup3.lower() == "*":
             vysledok = num1 * num2
             print (f"sucin cisel {num1} * {num2} je {vysledok}")
             break
        
        elif vstup3.lower() == "/":
             if num2 == 0:
                 print("delenie nulou nie je povolene")
             else:
                vysledok = num1 / num2
                zaokruhleny_podiel = round(vysledok, 2)
                print(f"podiel cisel {num1} / {num2} je {vysledok}")
                print(f"zaokruhleny podiel na 2 des. miesta je {zaokruhleny_podiel}")
                break    

    print("\nAk chceš zadať nové čísla, pokračuj. Alebo napíš 'stop' pre ukončenie.\n")

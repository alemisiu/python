print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________prawo
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Witaj w dlugach tadosach grze na pc")    
print("twoja misja to znalezc dlugi tadosa i je odzyskac") 
choice1 = input('przybyles nad skrzyzowanieidz  w  "lewo" lub "prawo".\n').lower()
if choice1 =="lewo":
    choice2 = input('przybyles  nad jezioro za ktora jest wyspa pelna zlota tadosa nacisnij  "plyn" by przeplynac rzeke lub "czekaj" by poczekac na lodz by sie tam dostac\n').lower()
    if choice2 == "czekaj":
        choice3 = input("przybywasz zeby sciagnac dlugi z tadosa ale jest ich trzech jeden ma niebieska koszulke drugi czerwona trzeci czarna ktorego wybierasz\n").lower()
        if choice3 == "czerwona":
            print("tadosowi zepsulo sie mikro a ty umarles ze starosci czekajac az mu sie naprawi")
        elif choice3 == "czarna":
            print("tados znowu w huja cie zrobil")
        elif choice3 =="niebieska":
            print("gratulacje udalo ci sie sciagnac wszystkie dlugi tadosow ")
        else:
            print("nie wybrales zadnego z trzech tadosow wszyscy sa wkurwieni i zabijaja cie")
    else:
      print("Probowales przeplynac przez rzeke ale tados juz tam na ciebie czekal a te obiecane nagrody to bylo gowno tadosowskie pomalowane na zloto smutne")
else:
    print("Doznales piekna tadosowskiego")
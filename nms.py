import os as os
#Définition des couleurs BASH
class color:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    reset = '\033[0m'
    blue = '\033[0;34m'
program = f"{color.yellow}Program: {color.reset}"
def positive():
    print(f"{program}{color.green}[mods activés]")
    print(f"{program}liste des mods:")
    files = os.listdir("/home/elouandeschamps/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/No Man's Sky/GAMEDATA/PCBANKS/MODS")
    for name in files:
        print(f"{color.blue}-{color.reset}{name}")
try:
    #Activation des mods
    test = os.path.join("""/home/elouandeschamps/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/No Man's Sky/GAMEDATA/PCBANKS/""", ".DISABLEMODS.TXT")
    test2 = os.path.join("""/home/elouandeschamps/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/No Man's Sky/GAMEDATA/PCBANKS""", "DISABLEMODS.TXT")
    os.rename(test, test2)
    positive()
except FileNotFoundError:
    #Désactivation des mods
    request1 = input(f"{program}Désactiver les mods? (y/n) ")
    if request1 == "y":
        test = os.path.join("""/home/elouandeschamps/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/No Man's Sky/GAMEDATA/PCBANKS/""", ".DISABLEMODS.TXT")
        test2 = os.path.join("""/home/elouandeschamps/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/No Man's Sky/GAMEDATA/PCBANKS""", "DISABLEMODS.TXT")
        os.rename(test2, test)
        print(f"{program}{color.red}[mods désactivés]")
    else:
        positive()

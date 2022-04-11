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
    print(f"{program}{color.green}[mods activés]{color.reset}")
    print(f"{color.yellow}liste des mods:")
    files = os.listdir("/home/elouandeschamps/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/No Man's Sky/GAMEDATA/PCBANKS/MODS")
    for name in files:
        print(f"{color.blue}-{color.reset}{name}")


files0 = os.listdir("/home/elouandeschamps/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/No Man's Sky/GAMEDATA/PCBANKS")

if ".DISABLEMODS.TXT" in files0:
    request = input(f"{program}Mods désactivés, souhaitez vous les activer? (y/n) ")
    if request == "y":
        test = os.path.join("""/home/elouandeschamps/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/No Man's Sky/GAMEDATA/PCBANKS/""", ".DISABLEMODS.TXT")
        test2 = os.path.join("""/home/elouandeschamps/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/No Man's Sky/GAMEDATA/PCBANKS""", "DISABLEMODS.TXT")
        os.rename(test2, test)
        positive()
    else:
        print(f"{program}{color.red}[mods désactivés]")
elif "DISABLEMODS.TXT" in files0:
    request = input(f"{program}Mods activés, souhaitez vous les desactiver? (y/n) ")
    if request == "y":
        test = os.path.join("""/home/elouandeschamps/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/No Man's Sky/GAMEDATA/PCBANKS/""", ".DISABLEMODS.TXT")
        test2 = os.path.join("""/home/elouandeschamps/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/No Man's Sky/GAMEDATA/PCBANKS""", "DISABLEMODS.TXT")
        os.rename(test, test2)
        print(f"{program}{color.red}[mods désactivés]")
    else:
        positive()
else:
    print(f"{program}disablemods non trouvé")

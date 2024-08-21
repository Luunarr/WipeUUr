# ═══════════════════════════════════════════════════════════════════════════════
#
#      _    _ _            _   _ _   _                 _              _ 
#     | |  | (_)          | | | | | | |               | |            | |
#     | |  | |_ _ __   ___| | | | | | |_ __   ______  | |_ ___   ___ | |
#     | |/\| | | '_ \ / _ \ | | | | | | '__| |______| | __/ _ \ / _ \| |
#     \  /\  / | |_) |  __/ |_| | |_| | |             | || (_) | (_) | |
#      \/  \/|_| .__/ \___|\___/ \___/|_|              \__\___/ \___/|_|
#              | |                                                      
#              |_|                                                      
#
#                          Version: 0.5.5#Wip
#
# ═══════════════════════════════════════════════════════════════════════════════
#
#                         Owner : @Lunar
#                   Collaborator : @NomFascinant
#
# ═══════════════════════════════════════════════════════════════════════════════
#
# Description:
#        WipeUUr is a command-line utility designed to help users maintain 
#        their system's cleanliness. Although still in its early development 
#        phase, it offers a variety of functions to keep your system running 
#        smoothly. WipeUUr allows you to clear browser histories, empty the 
#        recycle bin, flush the DNS cache, clean temporary files, and defragment 
#        your hard drive. Additionally, it provides commands to retrieve disk 
#        and operating system information. For users seeking technical support 
#        or more information about the tool, WipeUUr also offers options to 
#        connect to a Discord support channel, access the GitHub repository, 
#        or view the developer's GitHub profile.
#
# ═══════════════════════════════════════════════════════════════════════════════
#
# Features:
#        - Display help menu with available commands
#        - Clear web history, recycle bin, and temporary files
#        - Flush DNS cache
#        - Defragment the hard drive
#        - Retrieve disk, OS, and PC information
#        - Fetch detailed system information
#        - Connect to Discord for technical support
#        - Access the GitHub repository and developer's profile
#
# ═══════════════════════════════════════════════════════════════════════════════
#                     Copyright (c) 2024 Lunar
#
# License:
#        This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
#
# Contact:
#        For any questions or feedback, please reach out to:
#                GitHub: https://github.com/Luunarr/WipeUUr
#                Discord: https://discord.gg/zACVRwCSve
#
# ═══════════════════════════════════════════════════════════════════════════════


from Features.Utils import *
from Features.Fonction import *
init(autoreset=True)
Menu = None

# ═══════════════════════════════════════════════════════════════════════════════

try:
    with open("Features\Config.json", "r") as f:
        data = json.load(f)
        Menu = data["Menu"]
        Requirements = data["Requirements"]
        if Requirements == "True":
            try:
                subprocess.run(r"pip install -r Features\requirements.txt", shell=True, check=True)
            except subprocess.CalledProcessError:
                pass
        else:
            pass
except:
    pass


# ════════════════════════════ Principal Def ════════════════════════════════════

def MenuPrint(MenuChoice):
    MenuActions = {
        "1": asciiprint,
        "2": menuAscii_2001,
        "3": simpleMenuAsciiArt3,
    }
    action = MenuActions.get(MenuChoice, asciiprint)
    action()



# ══════════ Cleaning ═════════════════

def Cleaning():
    os.system("cls")
    while True:
        cleaning_menuAscii_2001()
        Wi = input(prompt)

        if Wi in ["1", "Clearhist", "clearhist", "ch", "CH"]:
            clearhistW()
            input()
            os.system("cls")

        elif Wi in ["cls", "clr"]:
            os.system("cls")


        elif Wi in ["2","clear","Clear"]:
            clearbinW()    
            input()
            os.system("cls")

        elif Wi in ["3","clearbin","Clearbin","cb"]:
            clearbinW()
            input()
            os.system("cls")

        elif Wi in ["4","Tempfiles","tempfiles","tf"]:
            clearbinW()
            input()
            os.system("cls")

        elif Wi in ["5","Flushdns","flushdns","fd"]:
            clearbinW()
            input()
            os.system("cls")

        elif Wi in ["6","Defrag","defrag","df"]:
            clearbinW()
            input()
            os.system("cls")

        elif Wi == "exit":
            break


# ══════════ Sys Infos ═════════════════

def SysInfo():
    os.system("cls")
    while True:
        sysinfo_menuAscii_2001()
        Wi = input(prompt)

        if Wi in ["cls", "clr"]:
            os.system("cls")

        elif Wi in ["1","fetch","Fetch", "ft"]: 
            fetchW()    
            input()
            os.system("cls")

        elif Wi in ["2","fullf","Fullf", "FullFetch", "ff"]:
            fullfW()   
            input()
            os.system("cls")

        elif Wi in ["3","MyOs","myos", "mo", "MO"]:
            iosW()   
            input()
            os.system("cls")

        elif Wi in ["4","MyDisk","mydisk", "md"]:
            idiskW()   
            input()
            os.system("cls")

        elif Wi in ["5","Network","network", "nk"]:
            input()
            os.system("cls")
  

        elif Wi == "exit":
            break

# ══════════ Extras ═════════════════

def Extras():
    os.system("cls")
    while True:
        extras_menuAscii_2001()
        Wi = input(prompt)

        if Wi in ["cls", "clr"]:
            os.system("cls")

        elif Wi in ["1","info","Info", "inf"]: 
            infoW()    
            input()
            os.system("cls")

        elif Wi in ["2","Github","github", "gh"]:
            space()

            webbrowser.open("https://github.com/Luunarr/WipeUUr")  
            print(f"{l} {bright}{cyan}https://github.com/Luunarr/WipeUUr {reset}")

            space()
            input()
            os.system("cls")


        elif Wi in ["3","Support","support", "supp", "sp"]:

            space()

            webbrowser.open("https://discord.gg/zACVRwCSve")  
            print(f"{l} {bright}{cyan}https://discord.gg/zACVRwCSve {reset}")

            space()
            input()
            os.system("cls")

        elif Wi in ["4","MyGithub","MYGITHUB", "mygithub", "mgh"]:
            space()

            webbrowser.open("https://github.com/Luunarr")    
            print(f"{l} {bright}{cyan}https://github.com/Luunarr {reset}")

            space()
            input()
            os.system("cls")


        elif Wi == "exit":
            break

# ══════════ 22 Cleaning 22 ═════════════════

def Cleaning22():
    os.system("cls")
    while True:
        simpleCleaningAsciiArt3()
        Wi = input(prompt)

        if Wi in ["1", "Clearhist", "clearhist", "ch", "CH"]:
            clearhistW()
            input()
            os.system("cls")

        elif Wi in ["cls", "clr"]:
            os.system("cls")


        elif Wi in ["2","clear","Clear"]:
            clearbinW()    
            input()
            os.system("cls")

        elif Wi in ["3","clearbin","Clearbin","cb"]:
            clearbinW()
            input()
            os.system("cls")

        elif Wi in ["4","Tempfiles","tempfiles","tf"]:
            clearbinW()
            input()
            os.system("cls")

        elif Wi in ["5","Flushdns","flushdns","fd"]:
            clearbinW()
            input()
            os.system("cls")

        elif Wi in ["6","Defrag","defrag","df"]:
            clearbinW()
            input()
            os.system("cls")

        elif Wi == "exit":
            break


# ══════════ 22 Sys Infos 22 ═════════════════

def SysInfo22():
    os.system("cls")
    while True:
        simpleSysInfoAsciiArt3()
        Wi = input(prompt)

        if Wi in ["cls", "clr"]:
            os.system("cls")

        elif Wi in ["1","fetch","Fetch", "ft"]: 
            fetchW()    
            input()
            os.system("cls")

        elif Wi in ["2","fullf","Fullf", "FullFetch", "ff"]:
            fullfW()   
            input()
            os.system("cls")

        elif Wi in ["3","MyOs","myos", "mo", "MO"]:
            iosW()   
            input()
            os.system("cls")

        elif Wi in ["4","MyDisk","mydisk", "md"]:
            idiskW()   
            input()
            os.system("cls")

        elif Wi in ["5","Network","network", "nk"]:
            input()
            os.system("cls")
 

        elif Wi == "exit":
            break

# ══════════ 22 Extras 22 ═════════════════

def Extras22():
    os.system("cls")
    while True:
        simpleExtraAsciiArt3()
        Wi = input(prompt)

        if Wi in ["cls", "clr"]:
            os.system("cls")

        elif Wi in ["1","info","Info", "inf"]: 
            infoW()    

        elif Wi in ["2","Github","github", "gh"]:
            space()

            webbrowser.open("https://github.com/Luunarr/WipeUUr")  
            print(f"{l} {bright}{cyan}https://github.com/Luunarr/WipeUUr {reset}")

            space()
            os.system("cls")

        elif Wi in ["3","Support","support", "supp", "sp"]:

            space()

            webbrowser.open("https://discord.gg/zACVRwCSve")  
            print(f"{l} {bright}{cyan}https://discord.gg/zACVRwCSve {reset}")

            space()
            os.system("cls")

        elif Wi in ["4","MyGithub","MYGITHUB", "mygithub", "mgh"]:
            space()

            webbrowser.open("https://github.com/Luunarr")    
            print(f"{l} {bright}{cyan}https://github.com/Luunarr {reset}")

            space()
            input()
            os.system("cls")


        elif Wi == "exit":
            break


# ═══════════════════════════════════════════════════════════════════════════════

def WipeUUr():  

    MenuPrint(Menu)

    while True: 
        if Menu == "1":
            while True:
                Wi = input(prompt)

                if Wi in ["h", "H", "help", "Help"]:
                    helpW()

                elif Wi == "exit":
                    exit()

                elif Wi in ["cls", "clr"]:
                    MenuPrint(Menu)


                elif Wi == "clear":
                    clearW()

                elif Wi == "github":

                    space()

                    webbrowser.open("https://github.com/Luunarr/WipeUUr")  
                    print(f"{l} {bright}{cyan}https://github.com/Luunarr/WipeUUr {reset}")

                    space()

                elif Wi == "mygithub":

                    space()

                    webbrowser.open("https://github.com/Luunarr")    
                    print(f"{l} {bright}{cyan}https://github.com/Luunarr {reset}")

                    space()

                elif Wi == "info":
                    infoW()

                elif Wi == "support":

                    space()

                    webbrowser.open("https://discord.gg/zACVRwCSve")  
                    print(f"{l} {bright}{cyan}https://discord.gg/zACVRwCSve {reset}")

                    space()

                elif Wi == "clearhist":
                    clearhistW()

                elif Wi == "clearbin":
                    clearbinW()

                elif Wi == "flushdns":
                    flushdnsW() 

                elif Wi == "tempfiles":
                    tempfilesW()  

                elif Wi == "defrag":
                    defragW()  

                elif Wi == "idisk":
                    idiskW() 

                elif Wi == "ios":
                    iosW()  

                elif Wi == "fetch":
                    fetchW() 

                elif Wi == "fullf":
                    fullfW() 

        elif Menu == "2":
            while True:
                os.system("cls")
                MenuPrint(Menu)
                Wi = input(prompt)

                if Wi in ["1", "Cleaning", "cleaning", "clng", "clg"]:
                    Cleaning()

                elif Wi in ["2", "SysInfo", "sysinfo", "si", "SI"]:
                    SysInfo()

                elif Wi in ["3", "Extras", "extras", "Ex", "ex"]:
                    Extras()

                elif Wi in ["exit", "quitter", "leave"]:
                    exit()

        elif Menu == "3":
            while True:
                os.system("cls")
                MenuPrint(Menu)
                if Wi in ["1", "Cleaning", "cleaning", "clng", "clg"]:
                    Cleaning22()

                elif Wi in ["2", "SysInfo", "sysinfo", "si", "SI"]:
                    SysInfo22()

                elif Wi in ["3", "Extras", "extras", "Ex", "ex"]:
                    Extras22()

                elif Wi in ["exit", "quitter", "leave"]:
                    exit()



# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    WipeUUr()

# ═══════════════════════════════════════════════════════════════════════════════
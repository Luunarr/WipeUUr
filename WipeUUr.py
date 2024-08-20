##################################################
#                    WipeUUr
#                    By Lunar
#                  Version: 0.1#Wip
#
#   Description:
#   WipeUUr is a command-line utility designed to clean up
#   your system by clearing browser histories, emptying
#   the recycle bin, and flushing the DNS cache. This tool
#   is in its early development phase and aims to provide
#   a simple yet effective way to maintain your system's
#   cleanliness.
#
#   Copyright (c) 2024 Lunar
#
#   License:
#   This project is licensed under the Apache License 2.0 - see
#   the LICENSE file for details.
#
#   Contact:
#   For any questions or feedback, please reach out to:
#   GitHub: https://github.com/Luunarr/WipeUUr
#   Discord: https://discord.gg/zACVRwCSve
##################################################

import os 
import subprocess
import winshell
import webbrowser
from colorama import *

init(autoreset=True)

p = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Style.RESET_ALL}"
m = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}]{Style.RESET_ALL}"
c = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.YELLOW}/{Fore.WHITE}]{Style.RESET_ALL}"
i = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.MAGENTA}>{Fore.WHITE}]{Style.RESET_ALL}"
e = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.CYAN}~{Fore.WHITE}]{Style.RESET_ALL}"
h = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}]{Style.RESET_ALL}"

tagV = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}0.1#Wip{Fore.WHITE}]{Style.RESET_ALL}"
tagA = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}By Lunar{Fore.WHITE}]{Style.RESET_ALL}"

prompt = f"{i} {Style.BRIGHT}{Fore.CYAN}Wipe{Fore.RED}UU{Fore.CYAN}r {Fore.RED}:{Style.RESET_ALL} "

asciiW = f"""{Style.BRIGHT}{Fore.CYAN}     _ _ _ _         {Fore.RED}_____ _____     
    {Fore.CYAN}| | | |_|___ ___{Fore.RED}|  |  |  |  |{Fore.CYAN}___    {Style.BRIGHT}{tagV}{Style.BRIGHT}
    {Fore.CYAN}| | | | | . | -_{Fore.RED}|  |  |  |  |{Fore.CYAN}  _|   {Style.BRIGHT}{tagA}{Style.BRIGHT}
    {Fore.CYAN}|_____|_|  _|___{Fore.RED}|_____|_____|{Fore.CYAN}_|  
    {Fore.CYAN}        |_|  
                        
{h} {Style.BRIGHT}{Fore.CYAN}Type '{Fore.RED}help{Fore.CYAN}' for help{Style.RESET_ALL}"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Winput():
    print("")
    input(f"{i} {Style.BRIGHT}{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

def asciiprint():
    clear()
    print(asciiW)
    print("")
    print("")
    
def WipeUUr():  
    while True: 
        asciiprint()
        Wi = input(prompt)
        if Wi in ["h", "H", "help", "Help"]:
            helpW()
        elif Wi == "exit":
            exit()
        elif Wi == "clear":
            clearW()
        elif Wi == "github":
            webbrowser.open("https://github.com/Luunarr/WipeUUr")  
            print(f"{Style.BRIGHT}{Fore.CYAN}https://github.com/Luunarr/WipeUUr {Style.RESET_ALL}")
            Winput()
        elif Wi == "mygithub":
            webbrowser.open("https://github.com/Luunarr")    
            print(f"{Style.BRIGHT}{Fore.CYAN}https://github.com/Luunarr {Style.RESET_ALL}")
            Winput()
        elif Wi == "info":
            Winfo()
        elif Wi == "support":
            webbrowser.open("https://discord.gg/zACVRwCSve")  
            print(f"{Style.BRIGHT}{Fore.CYAN}https://discord.gg/zACVRwCSve {Style.RESET_ALL}")
            Winput()
        elif Wi == "clearhist":
            clearhistW()
        elif Wi == "clearbin":
            clearbinW()
        elif Wi == "flushdns":
            flushdnsW()  
            
def Winfo():
    asciiprint()
    Info = f"""{Style.BRIGHT}{Fore.CYAN}
                    WipeUUr
                    By Lunar
                  Version: 0.1#Wip

   {Fore.RED}Description:{Fore.CYAN}
   WipeUUr is a command-line utility designed to clean up
   your system by clearing browser histories, emptying
   the recycle bin, and flushing the DNS cache. This tool
   is in its early development phase and aims to provide
   a simple yet effective way to maintain your system's
   cleanliness.

   {Fore.RED}Copyright (c) 2024 Lunar{Fore.CYAN}

   {Fore.RED}License:{Fore.CYAN}
   This project is licensed under the Apache License 2.0 - see
   the LICENSE file for details.

   {Fore.RED}Contact:{Fore.CYAN}
   For any questions or feedback, please reach out to:
   GitHub: {Fore.RED}https://github.com/Luunarr/WipeUUr
   Discord: {Fore.RED}https://discord.gg/zACVRwCSve {Style.RESET_ALL}    """
    print(Info)
    Winput()
      
def helpW():
    asciiprint()
    Help = f"""{h} {Style.BRIGHT}{Fore.CYAN}Commands  Utilities
  {Fore.RED}_________________________________{Fore.CYAN}
  help      {Fore.RED}|{Fore.CYAN}  Display this menu
  clear     {Fore.RED}|{Fore.CYAN}  Start cleaning
  clearhist {Fore.RED}|{Fore.CYAN}  Clean web history
  clearbin  {Fore.RED}|{Fore.CYAN}  Clean recycle bin
  flushdns  {Fore.RED}|{Fore.CYAN}  Clean DNS cache
  exit      {Fore.RED}|{Fore.CYAN}  Exit WipeUUr
  support   {Fore.RED}|{Fore.CYAN}  Get technical support on Discord
  info      {Fore.RED}|{Fore.CYAN}  Display system or application info
  github    {Fore.RED}|{Fore.CYAN}  Access the GitHub repository for this tool
  mygithub  {Fore.RED}|{Fore.CYAN}  Access my personal GitHub profile"""
    print(Help)
    Winput() 
    
def clearW():
    Winput()
    
def clearhistW():
    asciiprint()
    try:
        clearhistWchrome()
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to execute clearhistWchrome")
    try:
        clearhistWedge()
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to execute clearhistWedge")
    try:
        clearhistWfirefox()
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to execute clearhistWfirefox")
    try:
        clearhistWopera()
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to execute clearhistWopera")
    try:
        clearhistWinternetexplorer()
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to execute clearhistWinternetexplorer")
    try:
        clearhistWbrave()
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to execute clearhistWbrave")
    Winput()

def clearbinW():
    asciiprint()
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        print(f"{c} {Style.BRIGHT}{Fore.CYAN}Running 'winshell.recycle_bin()' ...")
        print(f"{p} {Style.BRIGHT}{Fore.CYAN}Your recycle bin has been cleared")
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Your recycle bin can't be cleared")
    Winput()
    
def flushdnsW():
    asciiprint()
    try:
        subprocess.run(["ipconfig", "/flushdns"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{c} {Style.BRIGHT}{Fore.CYAN}Running 'ipconfig /flushdns' ...")
        print(f"{p} {Style.BRIGHT}{Fore.CYAN}Your DNS has been cleared")
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Your DNS can't be cleared")
    Winput()
        
def remove(path):
    try:
        if os.path.exists(path):
            os.remove(path)
            print(f"{c} {Style.BRIGHT}{Fore.CYAN}Deleted {path}")
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to delete {path}")

def clearhistWchrome():
    try:
        asciiprint()
        paths = [
            os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"),
            os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies")
        ]
        for path in paths:
            remove(path)
        print(f"{p} {Style.BRIGHT}{Fore.CYAN}Chrome history cleared")
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to clear Chrome history")

def clearhistWedge():
    try:
        asciiprint()
        paths = [
            os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History"),
            os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cookies")
        ]
        for path in paths:
            remove(path)
        print(f"{p} {Style.BRIGHT}{Fore.CYAN}Edge history cleared")
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to clear Edge history")

def clearhistWfirefox():
    try:
        asciiprint()
        profile_dir = os.path.expanduser("~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
        for profile in os.listdir(profile_dir):
            history_path = os.path.join(profile_dir, profile, "places.sqlite")
            remove(history_path)
        print(f"{p} {Style.BRIGHT}{Fore.CYAN}Firefox history cleared")
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to clear Firefox history")

def clearhistWopera():
    try:
        asciiprint()
        paths = [
            os.path.expanduser("~\\AppData\\Roaming\\Opera Software\\Opera Stable\\History"),
            os.path.expanduser("~\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\History")
        ]
        for path in paths:
            remove(path)
        print(f"{p} {Style.BRIGHT}{Fore.CYAN}Opera history cleared")
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to clear Opera history")

def clearhistWinternetexplorer():
    try:
        asciiprint()
        subprocess.run("RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 255", shell=True)
        print(f"{p} {Style.BRIGHT}{Fore.CYAN}Internet Explorer history cleared")
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to clear Internet Explorer history")

def clearhistWbrave():
    try:
        asciiprint()
        paths = [
            os.path.expanduser("~\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History"),
            os.path.expanduser("~\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cookies")
        ]
        for path in paths:
            remove(path)
        print(f"{p} {Style.BRIGHT}{Fore.CYAN}Brave history cleared")
    except:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}Failed to clear Brave history")
           
if __name__ == "__main__":
    WipeUUr()

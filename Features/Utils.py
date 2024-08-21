from colorama import *
import tempfile
import os
import subprocess
import winshell
import webbrowser
import psutil
import platform
import json
from datetime import datetime
init(autoreset=True)

reset = Style.RESET_ALL
bright = Style.BRIGHT
white = Fore.WHITE
green = Fore.GREEN
red = Fore.RED 
magenta = Fore.MAGENTA
yellow = Fore.YELLOW
cyan = Fore.CYAN
blue = Fore.BLUE
gray = Fore.LIGHTBLACK_EX

p = f"{reset}{bright}{white}[{green}+{white}]{reset}"
m = f"{reset}{bright}{white}[{red}-{white}]{reset}"
c = f"{reset}{bright}{white}[{yellow}/{white}]{reset}"
i = f"{reset}{bright}{white}[{magenta}>{white}]{reset}"
e = f"{reset}{bright}{white}[{cyan}~{white}]{reset}"
l = f"{reset}{bright}{white}[{cyan}Link{white}]{reset}"
h = f"{reset}{bright}{white}[{blue}?{white}]{reset}"
r = f"{reset}{bright}{white}[{blue}*{white}]{reset}"

mention = f"{reset}{blue}@{reset}"

tagV = f"{reset}{bright}{white}[{blue}0.5.5#Wip{white}]{reset}"
tagA = f"{reset}{bright}{white}[{blue}By Lunar{white}]{reset}"

prompt = f"{i} {bright}{cyan}Wipe{red}UU{cyan}r {red}${reset} "

asciiW = f"""{bright}{cyan}     _ _ _ _         {red}_____ _____     
    {cyan}| | | |_|___ ___{red}|  |  |  |  |{cyan}___    {bright}{tagV}{bright}
    {cyan}| | | | | . | -_{red}|  |  |  |  |{cyan}  _|   {bright}{tagA}{bright}
    {cyan}|_____|_|  _|___{red}|_____|_____|{cyan}_|  
    {cyan}        |_|  

{h} {bright}{cyan}Type '{red}help{cyan}' for assistance{reset}"""


menuAscii12332 = """

                          ╔═════════════╗
                       ╔══╣ 1. Cleaning ║
                       ║  ╚═════════════╝
                       ║
                       ║
╔══════════════╗       ║  ╔═════════════╗
║   WipeUUr    ╠═══════╬══╣ 2. Sys Info ║
╚══════════════╝       ║  ╚═════════════╝
                       ║
                       ║
                       ║  ╔═════════════╗
                       ╚══╣ 3. Extras   ║
                          ╚═════════════╝

""".replace("═", f"{cyan}═{reset}").replace("║", f"{cyan}║{reset}").replace("╣", f"{red}╣{reset}").replace("╗", f"{red}╗{reset}").replace("╝", f"{red}╝{reset}").replace("╚", f"{red}╚{reset}").replace("╔", f"{red}╔{reset}").replace("╬", f"{red}╬{reset}").replace("╠", f"{red}╠{reset}")

def menuAscii_2001():
    print(menuAscii12332)



def cleaning_menuAscii_2001():
    print("""

                          ╔═════════════╗
                       ╔══╣ 1. Cleaning ║
                       ║  ╚╦════════════╝
                       ║   ║╔═════════════╗
                       ║   ╠╣ 1. Clearhist╠══╗  ╔═════════════╗
╔══════════════╗       ║   ║╚═════════════╝  ╠══╣ 4. Tempfiles╠══╗
║   WipeUUr    ╠═══════╣   ║╔═════════════╗  ║  ╚═════════════╝ ╔╩════════════╗
╚══════════════╝       ║   ╠╣ 2. Clear    ╠══╣                  ║ 6. Defrag   ║
                       ║   ║╚═════════════╝  ║  ╔═════════════╗ ╚╦════════════╝
                       ║   ║╔═════════════╗  ╠══╣ 5. Flushdns ╠══╝
                       ║   ╠╣ 3. Clearbin ╠══╝  ╚═════════════╝
                       ╚═══╝╚═════════════╝
          

""").replace("═", f"{cyan}═{reset}").replace("╩", f"{red}╩{reset}").replace("╦", f"{red}╦{reset}").replace("║", f"{cyan}║{reset}").replace("╣", f"{red}╣{reset}").replace("╗", f"{red}╗{reset}").replace("╝", f"{red}╝{reset}").replace("╚", f"{red}╚{reset}").replace("╔", f"{red}╔{reset}").replace("╬", f"{red}╬{reset}").replace("╠", f"{red}╠{reset}")

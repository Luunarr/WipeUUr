from colorama import *
import tempfile
import os
import subprocess
import winshell
import webbrowser
import psutil
import platform
from datetime import datetime

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

tagV = f"{reset}{bright}{white}[{blue}0.5#Wip{white}]{reset}"
tagA = f"{reset}{bright}{white}[{blue}By Lunar{white}]{reset}"

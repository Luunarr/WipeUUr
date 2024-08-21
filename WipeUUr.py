##################################################
#                    WipeUUr
#                    By Lunar
#                Version: 0.5#Wip
#
#   Description:
#   WipeUUr is a command-line utility designed to help users maintain their system's 
#   cleanliness. Although still in its early development phase, it offers a variety 
#   of functions to keep your system running smoothly. WipeUUr allows you to clear browser 
#   histories, empty the recycle bin, flush the DNS cache, clean temporary files, and 
#   defragment your hard drive. Additionally, it provides commands to retrieve disk and 
#   operating system information. For users seeking technical support or more information
#   about the tool, WipeUUr also offers options to connect to a Discord support channel, 
#   access the GitHub repository, or view the developer's GitHub profile.
#
#   Features:
#   - Display help menu with available commands
#   - Clear web history, recycle bin, and temporary files
#   - Flush DNS cache
#   - Defragment the hard drive
#   - Retrieve disk, OS, and PC information
#   - Fetch detailed system information
#   - Connect to Discord for technical support
#   - Access the GitHub repository and developer's profile
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

import tempfile
import os
import subprocess
import winshell
import webbrowser
import psutil
import platform

from datetime import datetime
from colorama import *

init(autoreset=True)

p = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Style.RESET_ALL}"
m = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}]{Style.RESET_ALL}"
c = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.YELLOW}/{Fore.WHITE}]{Style.RESET_ALL}"
i = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.MAGENTA}>{Fore.WHITE}]{Style.RESET_ALL}"
e = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.CYAN}~{Fore.WHITE}]{Style.RESET_ALL}"
l = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.CYAN}Link{Fore.WHITE}]{Style.RESET_ALL}"
h = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}]{Style.RESET_ALL}"

tagV = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}0.5#Wip{Fore.WHITE}]{Style.RESET_ALL}"
tagA = f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}By Lunar{Fore.WHITE}]{Style.RESET_ALL}"

prompt = f"{i} {Style.BRIGHT}{Fore.CYAN}Wipe{Fore.RED}UU{Fore.CYAN}r {Fore.RED}${Style.RESET_ALL} "

asciiW = f"""{Style.BRIGHT}{Fore.CYAN}     _ _ _ _         {Fore.RED}_____ _____     
    {Fore.CYAN}| | | |_|___ ___{Fore.RED}|  |  |  |  |{Fore.CYAN}___    {Style.BRIGHT}{tagV}{Style.BRIGHT}
    {Fore.CYAN}| | | | | . | -_{Fore.RED}|  |  |  |  |{Fore.CYAN}  _|   {Style.BRIGHT}{tagA}{Style.BRIGHT}
    {Fore.CYAN}|_____|_|  _|___{Fore.RED}|_____|_____|{Fore.CYAN}_|  
    {Fore.CYAN}        |_|  

{h} {Style.BRIGHT}{Fore.CYAN}Type '{Fore.RED}help{Fore.CYAN}' for assistance{Style.RESET_ALL}"""

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
            print(f"{l} {Style.BRIGHT}{Fore.CYAN}https://github.com/Luunarr/WipeUUr {Style.RESET_ALL}")
            Winput()
        elif Wi == "mygithub":
            webbrowser.open("https://github.com/Luunarr")    
            print(f"{l} {Style.BRIGHT}{Fore.CYAN}https://github.com/Luunarr {Style.RESET_ALL}")
            Winput()
        elif Wi == "info":
            infoW()
        elif Wi == "support":
            webbrowser.open("https://discord.gg/zACVRwCSve")  
            print(f"{l} {Style.BRIGHT}{Fore.CYAN}https://discord.gg/zACVRwCSve {Style.RESET_ALL}")
            Winput()
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

def infoW():
    asciiprint()
    Info = f"""{Style.BRIGHT}{Fore.CYAN}
                    WipeUUr
                    By Lunar
                Version: {Fore.RED}0.5#Wip

    {Fore.RED}Description:{Fore.CYAN}
    WipeUUr is a command-line utility designed to help users maintain their system's 
    cleanliness. Although still in its early development phase, it offers a variety 
    of functions to keep your system running smoothly. WipeUUr allows you to clear browser 
    histories, empty the recycle bin, flush the DNS cache, clean temporary files, and 
    defragment your hard drive. Additionally, it provides commands to retrieve disk and 
    operating system information. For users seeking technical support or more information
    about the tool, WipeUUr also offers options to connect to a Discord support channel, 
    access the GitHub repository, or view the developer's GitHub profile.

    {Fore.RED}Features:{Fore.CYAN}
    - Display help menu with available commands
    - Clear web history, recycle bin, and temporary files
    - Flush DNS cache
    - Defragment the hard drive
    - Retrieve disk, OS, and PC information
    - Fetch detailed system information
    - Connect to Discord for technical support
    - Access the GitHub repository and developer's profile

    {Fore.RED}Copyright (c) 2024 Lunar{Fore.CYAN}

    {Fore.RED}License:{Fore.CYAN}
    This project is licensed under the Apache License 2.0 - see
    the LICENSE file for details.

    {Fore.RED}Contact:{Fore.CYAN}
    For any questions or feedback, please reach out to:
    GitHub: {Fore.RED}https://github.com/Luunarr/WipeUUr
    Discord: {Fore.RED}https://discord.gg/zACVRwCSve {Style.RESET_ALL}"""
    print(Info)
    Winput()

def helpW():
    asciiprint()
    Help = f"""{h} {Style.BRIGHT}{Fore.CYAN} Commands       Utilities
    {Fore.RED}_________________________________{Fore.CYAN}
    help       {Fore.RED}|{Fore.CYAN}  Display this menu
    {Fore.RED}_________________________________{Fore.CYAN}
    clear      {Fore.RED}|{Fore.CYAN}  Start cleaning
    clearhist  {Fore.RED}|{Fore.CYAN}  Clean web history
    clearbin   {Fore.RED}|{Fore.CYAN}  Clean recycle bin
    flushdns   {Fore.RED}|{Fore.CYAN}  Clean DNS cache
    tempfiles  {Fore.RED}|{Fore.CYAN}  Clean temporary files
    defrag     {Fore.RED}|{Fore.CYAN}  Defragment the hard drive
    {Fore.RED}_________________________________{Fore.CYAN}
    idisk      {Fore.RED}|{Fore.CYAN}  Get disk information
    ios        {Fore.RED}|{Fore.CYAN}  Get OS information
    fetch      {Fore.RED}|{Fore.CYAN}  Get PC information
    fullf      {Fore.RED}|{Fore.CYAN}  Get All information
    {Fore.RED}_________________________________{Fore.CYAN}
    exit       {Fore.RED}|{Fore.CYAN}  Exit WipeUUr
    support    {Fore.RED}|{Fore.CYAN}  Get technical support on Discord
    info       {Fore.RED}|{Fore.CYAN}  Display system or application info
    github     {Fore.RED}|{Fore.CYAN}  Access the GitHub repository for this tool
    mygithub   {Fore.RED}|{Fore.CYAN}  Access my personal GitHub profile"""
    print(Help)
    Winput() 

def clearW():
    asciiprint()
    clearbinW()
    clearhistW()
    flushdnsW()
    tempfilesW()
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

def tempfilesW():
    asciiprint()
    print(f"{c} {Style.BRIGHT}{Fore.CYAN}Searching for temporary files to delete...")
    temp_dir = tempfile.gettempdir()
    try:
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"{p} {Style.BRIGHT}{Fore.CYAN}Temporary file {file_path} deleted")
    except Exception as e:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}An error occurred: {e}")
    Winput()

def defragW():
    asciiprint()
    print(f"{c}{Style.BRIGHT}{Fore.CYAN}Starting defragmentation process...")
    try:
        subprocess.run(
            ["powershell", "-Command", "Start-Process", "defrag", "-ArgumentList 'C:'", "-Verb", "RunAs"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
        )
        print(f"{p} {Style.BRIGHT}{Fore.CYAN}Defragmentation process started successfully.")

    except subprocess.CalledProcessError as e:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}An error occurred during defragmentation.")
        print(f"{m} {Style.BRIGHT}{Fore.RED}{e.stderr}")
    except Exception as e:
        print(f"{m} {Style.BRIGHT}{Fore.CYAN}An unexpected error occurred.")
        print(f"{m} {Style.BRIGHT}{Fore.RED}{e}")
    Winput()

def idiskW():
    asciiprint()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    print(f"{h} {Style.BRIGHT}{Fore.CYAN}Disk information :")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Total Memory: {Fore.RED}{memory.total / (1024 ** 3):.2f} GB")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Available Memory: {Fore.RED}{memory.available / (1024 ** 3):.2f} GB")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Memory Usage: {Fore.RED}{memory.percent}%")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Total Disk Space: {Fore.RED}{disk.total / (1024 ** 3):.2f} GB")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Used Disk Space: {Fore.RED}{disk.used / (1024 ** 3):.2f} GB")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Free Disk Space: {Fore.RED}{disk.free / (1024 ** 3):.2f} GB")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Disk Usage: {Fore.RED}{disk.percent}%")
    Winput()

def iosW():
    asciiprint()
    ios = platform.uname()
    print(f"{h} {Style.BRIGHT}{Fore.CYAN}OS information :")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}System: {Fore.RED}{ios.system}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Node Name: {Fore.RED}{ios.node}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Release: {Fore.RED}{ios.release}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Version: {Fore.RED}{ios.version}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Machine: {Fore.RED}{ios.machine}")
    Winput()

def fetchW():
    asciiprint()
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    ios = platform.uname()
    cpuWcount = psutil.cpu_count(logical=False)
    cpuWlogical = psutil.cpu_count(logical=True)
    cpuWfreq = psutil.cpu_freq()
    print(f"{h} {Style.BRIGHT}{Fore.CYAN}PC informationn :")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}System: {Fore.RED}{ios.system}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Node Name: {Fore.RED}{ios.node}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Release: {Fore.RED}{ios.release}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Version: {Fore.RED}{ios.version}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Machine: {Fore.RED}{ios.machine}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Processor: {Fore.RED}{ios.processor}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}CPU Physical Cores: {Fore.RED}{cpuWcount}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}CPU Logical Cores: {Fore.RED}{cpuWlogical}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}CPU Frequency: {Fore.RED}{cpuWfreq.current:.2f} MHz")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Boot Time: {Fore.RED}{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
    Winput()

def fullfW():
    asciiprint()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    ios = platform.uname()
    cpuWcount = psutil.cpu_count(logical=False)
    cpuWlogical = psutil.cpu_count(logical=True)
    cpuWfreq = psutil.cpu_freq()
    print(f"{h} {Style.BRIGHT}{Fore.CYAN}OS Information :")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}System: {Fore.RED}{ios.system}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Node Name: {Fore.RED}{ios.node}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Release: {Fore.RED}{ios.release}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Version: {Fore.RED}{ios.version}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Machine: {Fore.RED}{ios.machine}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Processor: {Fore.RED}{ios.processor}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Boot Time: {Fore.RED}{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
    print("")
    print(f"{h} {Style.BRIGHT}{Fore.CYAN}CPU Information :")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}CPU Physical Cores: {Fore.RED}{cpuWcount}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}CPU Logical Cores: {Fore.RED}{cpuWlogical}")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}CPU Frequency: {Fore.RED}{cpuWfreq.current:.2f} MHz")
    print("")
    print(f"{h} {Style.BRIGHT}{Fore.CYAN}Memory Information :")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Total Memory: {Fore.RED}{memory.total / (1024 ** 3):.2f} GB")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Available Memory: {Fore.RED}{memory.available / (1024 ** 3):.2f} GB")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Memory Usage: {Fore.RED}{memory.percent}%")
    print("")
    print(f"{h} {Style.BRIGHT}{Fore.CYAN}Disk Information :")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Total Disk Space: {Fore.RED}{disk.total / (1024 ** 3):.2f} GB")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Used Disk Space: {Fore.RED}{disk.used / (1024 ** 3):.2f} GB")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Free Disk Space: {Fore.RED}{disk.free / (1024 ** 3):.2f} GB")
    print(f"{p} {Style.BRIGHT}{Fore.CYAN}Disk Usage: {Fore.RED}{disk.percent}%")
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

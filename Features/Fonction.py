# ——————————————————————————————————————————————————— Import ————————————————————————————————————————————————————————

from .Utils import *

# ——————————————————————————————————————————————————— Config JSON ———————————————————————————————————————————————————

with open(os.path.join(os.path.dirname(__file__), "Config.json"), "r") as f:
    data = json.load(f)
    try:
        Browsers = data["Browsers"].split("-") if isinstance(data["Browsers"], str) else data["Browsers"]
    except KeyError:
        Browsers = []
    except json.JSONDecodeError:
        Browsers = []
        
# ——————————————————————————————————————————————————— Clear Fonction ————————————————————————————————————————————————


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ——————————————————————————————————————————————————— Space Fonction ————————————————————————————————————————————————

def space():
    print("")

# ——————————————————————————————————————————————————— AsciiPrint Fonction ———————————————————————————————————————————

def asciiprint():

    clear()
    print(asciiW)
    print("")
    print("")

# ——————————————————————————————————————————————————— InfoWipeUUr Fonction ———————————————s———————————————————————————

def infoW():

    space()

    Info = f"""{bright}{gray}
     _    _ _            _   _ _   _                 _              _ 
    | |  | (_)          | | | | | | |               | |            | |
    | |  | |_ _ __   ___| | | | | | |_ __   ______  | |_ ___   ___ | |
    | |/\| | | '_ \ / _ \ | | | | | | '__| |______| | __/ _ \ / _ \| |
    \  /\  / | |_) |  __/ |_| | |_| | |             | || (_) | (_) | |
     \/  \/|_| .__/ \___|\___/ \___/|_|              \__\___/ \___/|_|
             | |                                                      
             |_|                                                      

                         {cyan}Version: {red}0.5.5#Wip

{red}═══════════════════════════════════════════════════════════════════════════════

{cyan}                        Owner : {mention}{bright}{red}Lunar
{cyan}                  Collaborator : {mention}{bright}{red}NomFascinant

{red}═══════════════════════════════════════════════════════════════════════════════

{red}Description:{cyan}
       WipeUUr is a command-line utility designed to help users maintain 
       their system's cleanliness. Although still in its early development 
       phase, it offers a variety of functions to keep your system running 
       smoothly. WipeUUr allows you to clear browser histories, empty the 
       recycle bin, flush the DNS cache, clean temporary files, and defragment 
       your hard drive. Additionally, it provides commands to retrieve disk 
       and operating system information. For users seeking technical support 
       or more information about the tool, WipeUUr also offers options to 
       connect to a Discord support channel, access the GitHub repository, 
       or view the developer's GitHub profile.

{red}═══════════════════════════════════════════════════════════════════════════════

{red}Features:{cyan}
       - Display help menu with available commands
       - Clear web history, recycle bin, and temporary files
       - Flush DNS cache
       - Defragment the hard drive
       - Retrieve disk, OS, and PC information
       - Fetch detailed system information
       - Connect to Discord for technical support
       - Access the GitHub repository and developer's profile

{red}═══════════════════════════════════════════════════════════════════════════════
                    {red}Copyright (c) 2024 Lunar{cyan}

{red}License:{cyan}
       This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

{red}Contact:{cyan}
       For any questions or feedback, please reach out to:
               GitHub: {red}https://github.com/Luunarr/WipeUUr{cyan}
               Discord: {red}https://discord.gg/zACVRwCSve {reset}"""
    print(Info)

    space()


# ——————————————————————————————————————————————————— HelpWipeUUr Fonction ——————————————————————————————————————————

def helpW():

    space()

    Help = f"""{h} {bright}{gray}

             _          _       
            | |        | |      
            | |__   ___| |_ __  
            | '_ \ / _ \ | '_ \ 
            | | | |  __/ | |_) |
            |_| |_|\___|_| .__/ 
                         | |    
                         |_|    

           {cyan} Commands Overview
{red}═══════════════════════════════════════════════{cyan}

{cyan}              Basic Commands {red}:{cyan}
       help         {red}│{cyan}  Display this help menu
       exit         {red}│{cyan}  Exit WipeUUr

{red}═══════════════════════════════════════════════{cyan}

{cyan}               Cleaning {red}:{cyan}
       clear        {red}│{cyan}  Start cleaning
       clearhist    {red}│{cyan}  Clean web history
       clearbin     {red}│{cyan}  Empty the recycle bin
       flushdns     {red}│{cyan}  Clear DNS cache
       tempfiles    {red}│{cyan}  Delete temporary files
       defrag       {red}│{cyan}  Defragment the hard drive

{red}═══════════════════════════════════════════════{cyan}

{cyan}           System Information {red}:{cyan}
       idisk        {red}│{cyan}  Get disk information
       ios          {red}│{cyan}  Get OS information
       fetch        {red}│{cyan}  Get PC information
       fullf        {red}│{cyan}  Get all information

{red}═══════════════════════════════════════════════{cyan}

{cyan}        Additional Resources {red}:{cyan}
       support      {red}│{cyan}  Get technical support on Discord
       info         {red}│{cyan}  Display system or application info
       github       {red}│{cyan}  Access the GitHub repository for this tool
       mygithub     {red}│{cyan}  Access my personal GitHub profile"""

    print(Help)

    space() 

# ——————————————————————————————————————————————————— ClearWipeUUr Fonction —————————————————————————————————————————

def clearW():

    space()

    try:
        clearbinW()
        clearhistW()
        flushdnsW()
        tempfilesW()
        fullfW()
        print(f"{p} {bright}{cyan}Successfully executed '{red}clear{cyan}'")

    except:
        print(f"{m} {bright}{cyan}Failed to execute '{red}clear{cyan}'")

    space()

# ——————————————————————————————————————————————————— ClearHistory Fonction ——————————————————————————————————————————


def clearhistW():

    space()

    try:
        if "Chrome" in Browsers:
            clearhistWchrome()
            ChromeFinish = True
        elif "Edge" in Browsers:
            clearhistWedge()
            EdgeFinish = True
        elif "Firefox" in Browsers:
            clearhistWfirefox()
            FirefoxFinish = True
        elif "Opera" in Browsers:
            clearhistWopera()
            OperaFinish = True
        elif "Brave" in Browsers:
            clearhistWbrave()
            BraveFinish = True

    except Exception as e:
        if not ChromeFinish:
            print(f"{m} {bright}{cyan}Failed to execute clearhistWchrome")
        elif not EdgeFinish:
            print(f"{m} {bright}{cyan}Failed to execute clearhistWedge")
        elif not FirefoxFinish:
            print(f"{m} {bright}{cyan}Failed to execute clearhistWfirefox")
        elif not OperaFinish:
            print(f"{m} {bright}{cyan}Failed to execute clearhistWopera")
        elif not BraveFinish:
            print(f"{m} {bright}{cyan}Failed to execute clearhistWbrave")
        else:
            print(f"Chrome: {ChromeFinish}\nEdge: {EdgeFinish}\nFirefox: {FirefoxFinish}\nOpera: {OperaFinish}\nBrave: {BraveFinish}\n")
        print(f"An error occurred: {e}")

    space()

# ——————————————————————————————————————————————————— ClearBin Fonction ——————————————————————————————————————————————

def clearbinW():

    space()

    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        print(f"{c} {bright}{cyan}Running 'winshell.recycle_bin()' ...")
        print(f"{p} {bright}{cyan}Your recycle bin has been cleared")

    except:
        print(f"{m} {bright}{cyan}Your recycle bin can't be cleared")

    space()

# ——————————————————————————————————————————————————— FlushDNS Fonction ——————————————————————————————————————————————

def flushdnsW():

    space()

    try:
        subprocess.run(["ipconfig", "/flushdns"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{c} {bright}{cyan}Running 'ipconfig /flushdns' ...")
        print(f"{p} {bright}{cyan}Your DNS has been cleared")

    except:
        print(f"{m} {bright}{cyan}Your DNS can't be cleared")

    space()

# ——————————————————————————————————————————————————— TempFiles Fonction —————————————————————————————————————————————

def tempfilesW():

    space()

    print(f"{c} {bright}{cyan}Searching for temporary files to delete...")
    temp_dir = tempfile.gettempdir()

    try:
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"{p} {bright}{cyan}Temporary file {file_path} deleted")

    except Exception as e:
        print(f"{m} {bright}{cyan}An error occurred: {e}")

    space()

# ——————————————————————————————————————————————————— Defragmentation Fonction ———————————————————————————————————————

def defragW():

    space()

    print(f"{c}{bright}{cyan}Starting defragmentation process...")

    try:
        subprocess.run(
            ["powershell", "-Command", "Start-Process", "defrag", "-ArgumentList 'C:'", "-Verb", "RunAs"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
        )
        print(f"{p} {bright}{cyan}Defragmentation process started successfully.")

    except subprocess.CalledProcessError as e:
        print(f"{m} {bright}{cyan}An error occurred during defragmentation.")
        print(f"{m} {bright}{red}{e.stderr}")

    except Exception as e:
        print(f"{m} {bright}{cyan}An unexpected error occurred.")
        print(f"{m} {bright}{red}{e}")

    space()

# ——————————————————————————————————————————————————— DiskInfo Fonction ——————————————————————————————————————————————

def idiskW():

    space()

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print(f"{h} {bright}{cyan}Disk information :")
    print(f"{p} {bright}{cyan}Total Memory: {red}{memory.total / (1024 ** 3):.2f} GB")
    print(f"{p} {bright}{cyan}Available Memory: {red}{memory.available / (1024 ** 3):.2f} GB")
    print(f"{p} {bright}{cyan}Memory Usage: {red}{memory.percent}%")
    print(f"{p} {bright}{cyan}Total Disk Space: {red}{disk.total / (1024 ** 3):.2f} GB")
    print(f"{p} {bright}{cyan}Used Disk Space: {red}{disk.used / (1024 ** 3):.2f} GB")
    print(f"{p} {bright}{cyan}Free Disk Space: {red}{disk.free / (1024 ** 3):.2f} GB")
    print(f"{p} {bright}{cyan}Disk Usage: {red}{disk.percent}%")

    space()

# ——————————————————————————————————————————————————— OsInfo Fonction ————————————————————————————————————————————————

def iosW():

    space()

    ios = platform.uname()

    print(f"{h} {bright}{cyan}OS information :")
    print(f"{p} {bright}{cyan}System: {red}{ios.system}")
    print(f"{p} {bright}{cyan}Node Name: {red}{ios.node}")
    print(f"{p} {bright}{cyan}Release: {red}{ios.release}")
    print(f"{p} {bright}{cyan}Version: {red}{ios.version}")
    print(f"{p} {bright}{cyan}Machine: {red}{ios.machine}")

    space()

# ——————————————————————————————————————————————————— Pcinfos Fonction ———————————————————————————————————————————————   

def fetchW():

    space()

    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    ios = platform.uname()
    cpuWcount = psutil.cpu_count(logical=False)
    cpuWlogical = psutil.cpu_count(logical=True)
    cpuWfreq = psutil.cpu_freq()

    print(f"{h} {bright}{cyan}PC informationn :")
    print(f"{p} {bright}{cyan}System: {red}{ios.system}")
    print(f"{p} {bright}{cyan}Node Name: {red}{ios.node}")
    print(f"{p} {bright}{cyan}Release: {red}{ios.release}")
    print(f"{p} {bright}{cyan}Version: {red}{ios.version}")
    print(f"{p} {bright}{cyan}Machine: {red}{ios.machine}")
    print(f"{p} {bright}{cyan}Processor: {red}{ios.processor}")
    print(f"{p} {bright}{cyan}CPU Physical Cores: {red}{cpuWcount}")
    print(f"{p} {bright}{cyan}CPU Logical Cores: {red}{cpuWlogical}")
    print(f"{p} {bright}{cyan}CPU Frequency: {red}{cpuWfreq.current:.2f} MHz")
    print(f"{p} {bright}{cyan}Boot Time: {red}{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

    space()

# ——————————————————————————————————————————————————— FullInfo Fonction ——————————————————————————————————————————————

def fullfW():

    space()

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    ios = platform.uname()
    cpuWcount = psutil.cpu_count(logical=False)
    cpuWlogical = psutil.cpu_count(logical=True)
    cpuWfreq = psutil.cpu_freq()

    print(f"{h} {bright}{cyan}OS Information :")
    print(f"{p} {bright}{cyan}System: {red}{ios.system}")
    print(f"{p} {bright}{cyan}Node Name: {red}{ios.node}")
    print(f"{p} {bright}{cyan}Release: {red}{ios.release}")
    print(f"{p} {bright}{cyan}Version: {red}{ios.version}")
    print(f"{p} {bright}{cyan}Machine: {red}{ios.machine}")
    print(f"{p} {bright}{cyan}Processor: {red}{ios.processor}")
    print(f"{p} {bright}{cyan}Boot Time: {red}{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
    print("")
    print(f"{h} {bright}{cyan}CPU Information :")
    print(f"{p} {bright}{cyan}CPU Physical Cores: {red}{cpuWcount}")
    print(f"{p} {bright}{cyan}CPU Logical Cores: {red}{cpuWlogical}")
    print(f"{p} {bright}{cyan}CPU Frequency: {red}{cpuWfreq.current:.2f} MHz")
    print("")
    print(f"{h} {bright}{cyan}Memory Information :")
    print(f"{p} {bright}{cyan}Total Memory: {red}{memory.total / (1024 ** 3):.2f} GB")
    print(f"{p} {bright}{cyan}Available Memory: {red}{memory.available / (1024 ** 3):.2f} GB")
    print(f"{p} {bright}{cyan}Memory Usage: {red}{memory.percent}%")
    print("")
    print(f"{h} {bright}{cyan}Disk Information :")
    print(f"{p} {bright}{cyan}Total Disk Space: {red}{disk.total / (1024 ** 3):.2f} GB")
    print(f"{p} {bright}{cyan}Used Disk Space: {red}{disk.used / (1024 ** 3):.2f} GB")
    print(f"{p} {bright}{cyan}Free Disk Space: {red}{disk.free / (1024 ** 3):.2f} GB")
    print(f"{p} {bright}{cyan}Disk Usage: {red}{disk.percent}%")

    space()

# ——————————————————————————————————————————————————— Remove Fonction ———————————————————————————————————————————————

def remove(path):

    try:
        if os.path.exists(path):
            os.remove(path)
            print(f"{c} {bright}{cyan}Deleted {path}")

    except:
        print(f"{m} {bright}{cyan}Failed to delete {path}")

# ——————————————————————————————————————————————————— ClearHistory&Cookies Fonction ——————————————————————————————————

def clearhistWchrome():
    
    try:
        paths = [
            os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"),
            os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies")
        ]
        for path in paths:
            remove(path)
        print(f"{p} {bright}{cyan}Chrome history cleared")

    except:
        print(f"{m} {bright}{cyan}Failed to clear Chrome history")


def clearhistWedge():

    try:
        paths = [
            os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History"),
            os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cookies")
        ]
        for path in paths:
            remove(path)
        print(f"{p} {bright}{cyan}Edge history cleared")

    except:
        print(f"{m} {bright}{cyan}Failed to clear Edge history")

def clearhistWfirefox():

    try:
        profile_dir = os.path.expanduser("~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
        for profile in os.listdir(profile_dir):
            history_path = os.path.join(profile_dir, profile, "places.sqlite")
            remove(history_path)
        print(f"{p} {bright}{cyan}Firefox history cleared")

    except:
        print(f"{m} {bright}{cyan}Failed to clear Firefox history")

def clearhistWopera():

    try:
        paths = [
            os.path.expanduser("~\\AppData\\Roaming\\Opera Software\\Opera Stable\\History"),
            os.path.expanduser("~\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\History")
        ]
        for path in paths:
            remove(path)
        print(f"{p} {bright}{cyan}Opera history cleared")

    except:
        print(f"{m} {bright}{cyan}Failed to clear Opera history")

def clearhistWbrave():

    try:
        paths = [
            os.path.expanduser("~\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History"),
            os.path.expanduser("~\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cookies")
        ]
        for path in paths:
            remove(path)
        print(f"{p} {bright}{cyan}Brave history cleared")

    except:
        print(f"{m} {bright}{cyan}Failed to clear Brave history")

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
import subprocess
import random
try:
    var = random.randint(0,4)
    if var == 0:
        print("    _         _                        _            ")
        print("   / \  _   _| |_ ___  _ __ ___   __ _| |_ ___ _ __ ")
        print("  / _ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \ '__|")
        print(" / ___ \ |_| | || (_) | | | | | | (_| | ||  __/ |   v.2.0.0")
        print("/_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|_|   By @gasmat")
        print()
    if var == 1:
        print("   #                                                          ")
        print("  # #   #    # #####  ####  #    #   ##   ##### ###### #####  ")
        print(" #   #  #    #   #   #    # ##  ##  #  #    #   #      #    # ")
        print("#     # #    #   #   #    # # ## # #    #   #   #####  #    # ")
        print("####### #    #   #   #    # #    # ######   #   #      #####  ")
        print("#     # #    #   #   #    # #    # #    #   #   #      #   #  v.2.0.0")
        print("#     #  ####    #    ####  #    # #    #   #   ###### #    # By @gasmat")
    if var == 2:
        print("               _                        _            ")
        print("    /\        | |                      | |           ")
        print("   /  \  _   _| |_ ___  _ __ ___   __ _| |_ ___ _ __ ")
        print("  / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \ '__|")
        print(" / ____ \ |_| | || (_) | | | | | | (_| | ||  __/ |   v.2.0.0")
        print("/_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|_|   By @gasmat")
    if var == 3:
        print("    \          |                         |             ")
        print("   _ \   |   | __|  _ \  __ `__ \   _` | __|  _ \  __| ")
        print("  ___ \  |   | |   (   | |   |   | (   | |    __/ |   v.2.0.0")
        print("_/    _\\__,_|\__|\___/ _|  _|  _|\__,_|\__|\___|_|   By @gasmat ")
    if var == 4:
        print("   _       _                  _           ")
        print("  /_\ _  _| |_ ___ _ __  __ _| |_ ___ _ _ ")
        print(" / _ \ || |  _/ _ \ '  \/ _` |  _/ -_) '_| v.2.0.0")
        print("/_/ \_\_,_|\__\___/_|_|_\__,_|\__\___|_|   By @gasmat")
    print()
    print("Updater for OS that have apt for package manager")
    print("[+] Updating repository...")
    subprocess.run("sudo apt update", shell=True)
    print("[+] Updating metagoofil...")
    subprocess.run("sudo apt install -y metagoofil", shell=True)
    print("[+] Updating whois...")
    subprocess.run("sudo apt install -y whois", shell=True)
    print("[+] Updating deep magic...")
    subprocess.run("sudo apt install -y dmitry")
    print("[+] Updating hping3...")
    subprocess.run("sudo apt install -y hping3", shell=True)
    print("[+] Updating nikto...")
    subprocess.run("sudo apt install -y nikto", shell=True)
    print("[+] Updating wafw00f...")
    subprocess.run("sudo apt install -y wafw00f", shell=True)
    print("[+] Updating httrack...")
    subprocess.run("sudo apt install -y httrack", shell=True)
    print("[+] Updating hydra...")
    subprocess.run("sudo apt install -y hydra", shell=True)
    print("[+] Updating aircrack-ng...")
    subprocess.run("sudo apt install -y aircrack-ng", shell=True)
    print("[+] Updating Automater")
    subprocess.run("cd ..", shell=True)
    subprocess.run("sudo su", shell=True)
    subprocess.run("mv Automater Automater.bak", shell=True)
    subprocess.run("git clone https://github.com/MattiaG-afk/Automater.git", shell=True)
    subprocess.run("rm -rf Automater.bak", shell=True)

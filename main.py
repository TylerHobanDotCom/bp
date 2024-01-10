# Spectre's RCON Battle Pass Grinder
# Version 1
# https://github.com/TylerHobanDotCom/bp
# If you paid for this script, you have been scammed and should immediately demand a refund. You may not remove this notice.
# This script is released into the public domain, with the only conditions being a) absolutely no warranty is provided b) this line and the above notice must remain in place and unedited.
# Copyleft 2024

# Put your RCON settings (the ones from launch options) here:

port = 1337
password = "password"

# If you don't know what launch options to use, here:
# -usercon +developer 1 +contimes 0 +ip 0.0.0.0 +sv_rcon_whitelist_address 127.0.0.1 +sv_quota_stringcmdspersecond 1000000 +rcon_password password +hostport 1337 +net_start

# If you use the above example, PLEASE change the password to something other than password. Although these options restrict access to your local PC it is still best practice to change it.
# Also, don't put the # in your launch options lol.

# To install and use, download the colorama and rcon libraries from pip.
# $pip install rcon
# $pip install colorama
# $py ./main.py


from colorama import Fore, Back, Style, init
from rcon import Client
import time
import traceback

def sendcommand(command):
    with Client("127.0.0.1", port, passwd=password) as client:
        response = client.run(command)
        print(response)
def jobchanger():
    print("Executing jobchanger function")
    try:
        while True:
            command = "darkrp citizen"
            sendcommand(command)
            time.sleep(30.1)
            command = "darkrp rpsplayerboi"
            sendcommand(command)
            time.sleep(30.1)
            print(Style.RESET_ALL + "Use" + Fore.YELLOW + " CTRL+C " + Style.RESET_ALL + "to return to main menu.")
    except:
        mainmenu()
def weaponbuyer():
    print("Executing weaponbuyer function")
    try:
        while True:
            command = "say /buy water"
            sendcommand(command)
            time.sleep(5)
            print(Style.RESET_ALL + "Use" + Fore.YELLOW + " CTRL+C " + Style.RESET_ALL + "to return to main menu.")
    except:
        mainmenu()

def shipmentbuyer():
    print("Executing shipmentbuyer function")
    try:
        while True:
            command = "darkrp buyshipment water"
            sendcommand(command)
            time.sleep(5)
            print(Style.RESET_ALL + "Use" + Fore.YELLOW + " CTRL+C " + Style.RESET_ALL + "to return to main menu.")
    except:
        mainmenu()
def ammobuyer():
    print("Executing ammobuyer function")
    try:
        while True:
            command = "darkrp buyammo ammo_stungun"
            sendcommand(command)
            time.sleep(1)
            print(Style.RESET_ALL + "Use" + Fore.YELLOW + " CTRL+C " + Style.RESET_ALL + "to return to main menu.")
    except:
        mainmenu()
def doorbuyer():
    print("Executing doorbuyer function")
    try:
        while True:
            command = "darkrp toggleown"
            sendcommand(command)
            time.sleep(1)
            print(Style.RESET_ALL + "Use" + Fore.YELLOW + " CTRL+C " + Style.RESET_ALL + "to return to main menu.")
    except:
        mainmenu()
def prop():
    print("Executing prop function")
    try:
        while True:
            command = "gm_spawn models/hunter/plates/plate.mdl"
            sendcommand(command)
            time.sleep(0.2)
            command = "gmod_undo"
            sendcommand(command)
            time.sleep(1)
            print(Style.RESET_ALL + "Use" + Fore.YELLOW + " CTRL+C " + Style.RESET_ALL + "to return to main menu.")
    except:
        mainmenu()

def death():
    print("Executing death function")
    try:
        while True:
            command = "kill"
            sendcommand(command)
            time.sleep(1)
            command = "+attack"
            sendcommand(command)
            command = "-attack"
            sendcommand(command)
            time.sleep(5)
            print(Style.RESET_ALL + "Use" + Fore.YELLOW + " CTRL+C " + Style.RESET_ALL + "to return to main menu.")
    except:
        command = "-attack"
        sendcommand(command)
        mainmenu()


def lockpick():
    print("Executing lockpick function")
    try:
        while True:
            command = "+attack"
            sendcommand(command)
            time.sleep(20.1)
            command = "-attack"
            sendcommand(command)
            time.sleep(5)
            print(Style.RESET_ALL + "Use" + Fore.YELLOW + " CTRL+C " + Style.RESET_ALL + "to return to main menu.")
    except:
        command = "-attack"
        sendcommand(command)
        mainmenu()
def prolockpick():
    print("Executing prolockpick function")
    try:
        while True:
            command = "+attack"
            sendcommand(command)
            time.sleep(10.1)
            command = "-attack"
            sendcommand(command)
            time.sleep(3)
            print(Style.RESET_ALL + "Use" + Fore.YELLOW + " CTRL+C " + Style.RESET_ALL + "to return to main menu.")
    except:
        command = "-attack"
        sendcommand(command)
        mainmenu()

def mainmenu():
    print(Fore.BLUE + "Welcome to Spectre's RCON BP Grinder! (Version 1)")
    print(Fore.RED + "This script is currently a WIP! If you find bugs or issues, make sure to tell me.\nIf you paid for this script, you have been scammed and should immediately demand a refund. You may not remove this notice.\n" + Style.RESET_ALL)
    print("Special thanks to " + Fore.GREEN + "Volento" + Style.RESET_ALL + " and " + Fore.GREEN + "Brandonian" + Style.RESET_ALL + " for inspiration.\n")

    options_functions = {
        'Job Changer': jobchanger,
        'Weapon Buyer (change your job to bartender)': weaponbuyer,
        'Shipment Buyer (change your job to bartender)': shipmentbuyer,
        'Ammo Buyer': ammobuyer,
        'Door Buyer (look at an unowned door)': doorbuyer,
        'Prop Placer': prop,
        'Auto Death': death,
        'Auto Lockpick (look at a door with your lockpick at an angle where your crosshair will be over it when it is opened and shut or a fading door not owned by you)': lockpick,
        'Auto Pro Lockpick (look at a door with your pro lockpick at an angle where your crosshair will be over it when it is opened and shut)': prolockpick
    }

    options = list(options_functions.keys())

    user_input = ''

    input_message = "Pick an option:\n"

    for index, item in enumerate(options):
        input_message += f'{index + 1}) {item}\n'

    print(Fore.RED + "WARNING! DO NOT use Auto Lockpick/Pro Lockpick if you are Staff.\nIf for any reason you die you will respawn and start spamming physgun, \nfor a normal player this is inconsequential but as a staff member\nit can be disruptive or even trap players in spawn!" + Style.RESET_ALL)

    input_message += 'Your choice: '

    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)

    selected_option = options[int(user_input) - 1]

    options_functions[selected_option]()



mainmenu()
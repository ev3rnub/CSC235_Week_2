# Chad Verbus
# CSC235 - Python
# 11162025

import os
import random
import re
from time import sleep

# regex
employee_id_pattern : re.Pattern = re.compile(r'^[\d]{6}$')
# state
isrunning: bool = False
powerOn: bool = True
automationOn: bool = True
automationMenu: bool = False
enemyPresent: bool = False
modelsPresent: bool = False
# points
powerPoints: int = 1000
modelsReady: int = 0
modelsDeployed: int = 0
tickValue: int = 1
outpostHP: int = 100
materialPoints: int = 1000
# badguys
enemyPoints: int = 0

#turn
turn: int = 0
# uername
userName: str = ""



# map
# battle indicator
defenderMap = "------------------------------[ "
mapDivider = "|"
enemyMap = " ]------------------------------"

defenderArray = list(defenderMap)
enemyArray = list(enemyMap)
movementArray = []

#robots
someEnemy: dict = {
    "m": "#",
    "loc": int
}
someDefender: dict = {
    "m": "@",
    "loc": int
}
# Main function, Main Loop
def main():
    global isrunning
    global userName
    while isrunning:
        global turn
        if turn == 0:
            print(red_output("ENTER EID ----------------------- Example: 123123, has to be 6 digits\n"))
            print(yellow_output("EID REQUIRED ---------------------------------- Pending Authorization\n"))
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            getInput: str = input(green_output("""AutoOutpostTerm19|Login>> """))
        else:
            getInput: str = input(green_output(f"{userName} - AutoOutpostTerm19|Main>> "))

        if getInput == "exit" or getInput == "q" or getInput == "quit":
            inputFilter("goodbye")
            isrunning = False
        #     IF input matches 6 digits, start the automation menu.
        elif employee_id_pattern.fullmatch(getInput):
            newTurn()
            userName = getInput
            start_auto_menu()
        else:
            powerTick(1)
            newTurn()
            inputFilter(getInput)

#input filter, trigger on keywords etc.
def inputFilter(name):
    global turn
    global userName
    match name:
        case "goodbye":
            print(green_output("---------------------------------------------------------------------"))
            print(yellow_output(f"LOGGING OUT ----------------------------------------------{userName}"))
            print(green_output("---------------------------------------------------------------------"))
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            userName = ""
            turn = 0
        case "information":
            print("---------------------------------------------------------------------")
            print("SPONSORING CORP-- ------------------------------- -- Verbose Robotics")
            print("HULL -- ----------------------------------------------- -- Outpost 13")
            print("ORBIT -- ----------------------------------------------- -- Moon:Kata")
            print("AUTHORITY -- --------------------------------------------- -- Katikin")
            print("MAX OCCUPANTS (O2) -- ------------------------------------------ -- 1")
            print("Robot Models--------------------------------------------------------1")
            print("Production------------------------------------------------1 per cycle")
            print("Model 0 ---------------------------------------------------------DORA")
            print("Type 0 ------------------------------------------------------- Type D")
            print("Series 2------------------------------------------------------- Rev 2")
            print("Parts ------------------------------------------------------------- 6")
            print("  |------------------------------------------------------------H-Unit")
            print("  |------------------------------------------------------------T-Unit")
            print("  |---------------------------------------------------------L-Unit x2")
            print("  |---------------------------------------------------------A-Unit x2")
            print("Materials Req-------------------------------------------------------4")
            print("     |------------------------------------------------------Metal x47")
            print("     |----------------------------------------------------Ceramic x21")
            print("     |-------------------------------------------------Scientific x29")
            print("     |-------------------------------------------------Electronic x63")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
        case "status":
            print("---------------------------------------------------------------------")
            if outpostHP:
                print(f"HP --------------------------------------------------------------{outpostHP}")
            else:
                print("HP -------------------------------------------------------------UNKNOWN")
            if automationOn:
                print("AUTOMATION STATUS ------------------------------------------------ON")
            else:
                print("AUTOMATION STATUS ------------------------------------------------OFF")
            if powerOn:
                print("POWER STATUS -----------------------------------------------------ON")
            else:
                print("POWER STATUS -----------------------------------------------------OFF")
            if powerPoints:
                print(f"POWER -----------------------------------------------------------{powerPoints}")
            else:
                print("POWER POINTS ----------------------------------------------------0")
            if materialPoints:
                print(f"MATERIALS -------------------------------------------------------{materialPoints}")
            else:
                print("MATERIAL POINTS ------------------------------------------------0")
            if modelsReady:
                print(f"MODELS READY ----------------------------------------------------{modelsReady}")
            else:
                print("MODELS READY ----------------------------------------------------0")
            if modelsDeployed:
                print(f"MODELS DEPLOYED ------------------------------------------------{modelsDeployed}")
            else:
                print("MODELS DEPLOYED ------------------------------------------------0")
            if enemyPoints:
                print(f"ENEMY ROBOTS ----------------------------------------------------{enemyPoints}")
            else:
                print("ENEMY ROBOTS ----------------------------------------------------0")
            print(f"TURNS -----------------------------------------------------------{turn}")
            print(defenderMap + mapDivider + enemyMap)
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
        case "help menu":
            inputFilter("help")
        case "help":
            print(yellow_output("---------------------------------------------------------------------"))
            print(yellow_output("-----------------------------HELP MENU-------------------------------"))
            print(yellow_output("---------------------------------------------------------------------"))
            print(yellow_output("INFO MENU ------- Type 'information' to display the information menu."))
            print(yellow_output("STATUS MENU --------------- type 'status' to display the status menu."))
            print(yellow_output("AUTOMATION MENU --- type 'automation' to display the automation menu."))
            print(yellow_output("POWER MENU ------------------ type 'power' to display the power menu."))
            print(yellow_output("LOGOUT ------------------------------------ type '/logout' to logout."))
            print(yellow_output("LOGIN ------------------------------------ type '/login' to login."))
            print(yellow_output("QUIT -------------- Type 'quit|q|exit' to quit and exit the terminal."))
            print(yellow_output("---------------------------------------------------------------------"))
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
            print("\n\n\n")
        case "/login":
            inputFilter("goodbye")
        case "/logout":
            inputFilter("goodbye")
        case "power":
            if userName:
                power_menu()
            else:
                turn = 0
                main()
                return
        case "automation":
            if userName:
                automation_menu()
            else:
                turn = 0
                main()
                return
        case "q":
            isrunning = False
        case "quit":
            isrunning = False
        case "exit":
            isrunning = False
        case _:
            if turn > 3:
                if name == "":
                    inputFilter("status")
            else:
                inputFilter("help")

# when this ticks, power is generated, if powerOn is true, automationOn is true, someResult is true, and otherResult is
# true, increment the modelReady variable by 1. Alternatively displays power capacity warning.
def autoTick():
    global powerPoints
    global modelsReady
    if powerOn:
        powerPoints += 5
        if automationOn:
            if powerPoints > 5:
                someResult = take_power(10)
                if someResult:
                    otherResult = take_material(6)
                    if otherResult:
                        modelsReady += 1
                        print(cyan_output("Robot Ready ------------------------- DORA Type-D Defensive"))
                        print(cyan_output("Updated Main Inventory ------------------- Models Ready + 1"))
                        print("\n\n\n")
                        print("\n\n\n")
                        print("\n\n\n")
                        print("\n\n\n")
                        print("\n\n\n")
                        print("\n\n\n")
                        print("\n\n\n")
                        print("\n\n\n")


            else:
                print(red_output("Power Capacity ------------------------- {powerPoints}"))
                print(red_output("WARN --------------------------------------Power is low"))
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")

# When this is called it increases the outposts power points by amt.
def powerTick(amt:int):
    global powerPoints
    global materialPoints
    if automationOn:
        if powerOn:
            if  materialPoints > 5:
                materialPoints -= 5
                powerPoints += amt
            else:
                print(red_output("Power Capacity ------------------------- {powerPoints}"))
                print(red_output("WARN --------------------------------------Power is low"))
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")

#decrements the materials
def take_material(amt:int) -> bool:
    global materialPoints
    if materialPoints < 0:
        materialPoints = 0
        return False
    else:
        someResult = take_power(1)
        if someResult:
            materialPoints -= amt
            return True

#decrements the power points
def take_power(amt:int) -> bool:
    global powerPoints
    if powerPoints < 0:
        powerPoints = 0
        return False
    else:
        powerPoints -= amt
        return True
#increments turn
def newTurn():
    global turn
    turn += 1

# First menu after logging in, displays the main interface with options to start the automation menu, power menu, or
# quit.
def start_auto_menu():
    #global userName
    global turn
    turn += 1
    print(f"----------------------AUTHORIZATION GRANTED {userName}-----------------")
    print("-----------------------------------------------------------------------")
    print(f"-------MOTD; All Systems Operational, Employee ID: -------- {userName}")
    print("--------------Please enter a command from the following list-----------")
    print("-- type (1). --------------------------------------automation Interface")
    print("-- type (2). -------------------------------------------power Interface")
    print("-- type (3). -----------------------------------------problem Interface")
    print("-- type (4|q|e|exit|quit). -----------------------------------------EXIT")
    print("-----------------------------------------------------------------------")
    print("\n\n\n")
    print("\n\n\n")
    print("\n\n\n")
    print("\n\n\n")
    print("\n\n\n")
    print("\n\n\n")
    print("\n\n\n")
    print("\n\n\n")
    getInput: str = input(green_output("{userName} - AutoOutpostTerm19|RobotProduction>> "))
    match getInput:
        case "1":
            automation_menu()
        case "2":
            power_menu()
        case "3":
            problem_menu()
        case "4" | "q" | "quit" | "exit":
            isrunning = False
        case _:
            inputFilter(getInput)
            
# problem menu
def problem_menu():
    someProblemDict: Dict[str, str] = {
        "Problem 1": "Power stability due to load/demand.",
        "Problem 2": "Robot manufactoring line is slow due to ongoing maintenence."
    }
    problemMenu = True
    while problemMenu:
        print("-----------------------------------------------------------------------")
        print(f"{userName}--------------AutoOutpostTerm19 Problems---------------------")
        print("-----------------------------------------------------------------------")
        print("----------- Please enter a command from the following list ------------")
        print("-- type (1). ---------------------------------------------View Problems")
        print("-- type (2|quit|q|exit|e). ----------------------------------------EXIT")
        print("-----------------------------------------------------------------------")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        someInput = input(green_output("{userName} - AutoOutpostTerm19|RobotProduction|Problems>> "))
        match someInput:
            case "1":
                print("-----------------------------------------------------------------------")
                print(f"{userName}--------------AutoOutpostTerm19 Problems---------------------")
                print("-----------------------------------------------------------------------")
                print("------------------------ List of unresovled problems ------------------")
                print(f"Problem 1 -----------------------{someProblemDict["Problem 1"]}")
                print(f"Problem 2 -----------------------{someProblemDict["Problem 2"]}")
                print("-- type (2|quit|q|exit|e). ----------------------------------------EXIT")
                print("-----------------------------------------------------------------------")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                someInput = input(green_output("{userName} - AutoOutpostTerm19|RobotProduction|Problems|View>> "))
            case "2" | "exit" | "q" | "quit":
                print("Exiting AutoOutpostTerm19")
                problemMenu = False;
                start_auto_menu()
            case _:
                print("Invalid Input")
# power menu
def power_menu():
    global powerOn
    global powerMenu
    powerMenu = True
    global userName
    while powerMenu:
        print("-----------------------------------------------------------------------")
        print(f"{userName}--------------AutoOutpostTerm19 Power---------------------")
        print("-----------------------------------------------------------------------")
        print("----------- Please enter a command from the following list ------------")
        print("-- type (1). ---------------------------------------------Configuration")
        print("-- type (2|quit|q|exit|e). ----------------------------------------EXIT")
        print("-----------------------------------------------------------------------")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        someInput = input(green_output("{userName} - AutoOutpostTerm19|RobotProduction|Power>> "))
        if someInput == "exit" or someInput == "q" or someInput == "quit":
            isrunning = False
            powerMenu = False
        while powerMenu:
            if powerOn:
                print("Power Status: -------------------------- ON")
                print("1. -------------------------------------OFF")
                print("2. ------------------------------------EXIT")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                moreInput = input(green_output("{userName} - AutoOutpostTerm19|RobotProduction|Power|Config>> "))
                match moreInput:
                    case "1":
                        powerOn = False
                    case "2":
                        print("Exiting AutoOutpostTerm19")
                        powerMenu = False;
                        start_auto_menu()
                    case _:
                        print("Invalid Input")
            else:
                print("Power Status: --------------------------OFF")
                print("1. --------------------------------------ON")
                print("2. ------------------------------------EXIT")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                moreInput = input(green_output("{userName} - AutoOutpostTerm19|RobotProduction|Power|Config>> "))
                match moreInput:
                    case "1":
                        powerOn = True
                    case "2":
                        powerMenu = False
                    case _:
                        print("Invalid Input")

# automation menu
def automation_menu():
    global automationOn
    global userName
    global powerOn
    global isrunning
    global automationMenu
    automationMenu = True
    while automationMenu:
        print("-----------------------------------------------------------------------")
        print(f"AutoOutpostTerm19 Automation----------------------------------{userName}")
        print("-----------------------------------------------------------------------")
        print("----------- Please enter a command from the following list ------------")
        print("-- type (1). ---------------------------------------------Configuration")
        print("-- type (2|quit|q|exit|e). -----------------------------------------EXIT")
        print("-----------------------------------------------------------------------")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        someInput = input(green_output("{userName} - AutoOutpostTerm19|Automation>> "))
        if someInput == "exit" or someInput == "q" or someInput == "quit":
            isrunning = False
            automationMenu = False
        while automationMenu:
            if automationOn:
                print("Automation Status: --------------------- ON")
                print("1. -------------------------------------OFF")
                print("2. ------------------------------------EXIT")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                moreInput = input(green_output("{userName} - AutoOutpostTerm19|Automation|Config>> "))
                match moreInput:
                    case "1":
                        automationOn = False
                    case "2":
                        print("Exiting AutoOutpostTerm19")
                        automationMenu = False
                        start_auto_menu()
                    case _:
                        print("Invalid Input")
            else:
                print("Automation Status: -------------------- OFF")
                print("1. --------------------------------------ON")
                print("2. ------------------------------------EXIT")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                print("\n\n\n")
                moreInput = input(f"{userName} - AutoOutpostTerm19|Automation|Config>> ")
                match moreInput:
                    case "1":
                        if powerOn:
                            print("\n\n\n")
                            print("\n\n\n")
                            print("\n\n\n")
                            print("\n\n\n")
                            print("\n\n\n")
                            print("\n\n\n")
                            print("\n\n\n")
                            print("\n\n\n")
                            print("Power Status: --------------------------------------ON")
                            print("Powering Automtion Platform: ----------- COMING ONLINE")
                            automationOn = True
                            print("Automtion --------------------------------- NOW ONLINE")
                        else:
                            print("Power Status: -------------------------------------OFF")
                            print("Please turn on power before turning on automation.")
                            automationMenu = False
                            start_auto_menu()
                    case "2":
                        start_auto_menu()
                        automationMenu = False
                    case _:
                        print("Invalid Input")
#FUTURE
def read_help_text(aType):
    match aType:
        case "def":
            display_help_text("python_def_method.txt")
        case "if":
            display_help_text("python_if_statement.txt")
        case "match":
            display_help_text("python_match_statement.txt")
        case _:
            print("For help, type 'help', else quit, or q to exit.")
#FUTURE
def display_help_text(aFile):
    cnt :int = 0
    with open(aFile, "r") as file:
        lines = file.readlines()
    for line in lines:
        print(line)
        cnt += 1
        if cnt == 17:
            getInput = input("Press enter to continue or type 'q' to quit:")
            if getInput == 'q':
                break
            else:
                cnt = 0
            print(line)

# colorize terminal output
def green_output(someData) -> str:
    GREEN = "\x1b[32m"
    processedData = GREEN + someData + GREEN
    return processedData
# red
def red_output(someData) -> str:
    RED = "\x1b[31m"
    processedData = RED + someData + RED
    return processedData
# white
def white_output(someData) -> str:
    WHITE = "\x1b[38;2;255;255;255m"
    processedData = WHITE + someData + WHITE
    return processedData
# gray
def gray_output(someData) -> str:
    GRAY = "\x1b[37m"
    processedData = GRAY + someData + GRAY
    return processedData
#bold
def yellow_output(someData) -> str:
    YELLOW = "\x1b[33m"
    processedData = YELLOW + someData + YELLOW
    return processedData
#blue
def cyan_output(someData) -> str:
    CYAN = "\x1b[36m"
    processedData = CYAN + someData + CYAN
    return processedData
# reset
def reset_output(someData) -> str:
    RESET = "\x1b[0m"
    processedData = RESET + someData + RESET
    return processedData


# First Menu after starting. Checks for our scripts name in main, then clears the screen, prints text, sets running
# to true, and calls our internal main() function.
if __name__ == '__main__':
    os.system("clear")
    print(cyan_output("Welcome to Verbose Hominid:AutoOutpostTerm19. A Robot Production Control Terminal Simulation\n"))
    print(cyan_output("This is an early prototype text based control terminal. For my text based RPG.\n"))
    print("To play, make up an employee ID and enter it, Go into the Power Menu, turn power on, then production on\n")
    print("Then goto the Automation Menu, and turn on the automation interface, exit the automation menu, then exit to main menu.\n")
    print("This terminal would control the generation of Verbose Robotics Dora Type D defense series sentry hominid robot\n")
    print("On the main interface, each input, or pressing Enter advances the production of robots by 1 turn.\n")
    print("No point to this simulation, I ran out of time :(. However I can use this as a model for a example. \n")
    #fake connecting to use a for loop
    someString = "Connecting to Outpost #19"
    for i in range(4):
        print(cyan_output(f"{someString}"))
        someString = someString + "."
        sleep(1)
        os.system("clear")
    isrunning = True
    main()
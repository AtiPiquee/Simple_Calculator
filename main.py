from colorama import Fore

def calculator():
    print(Fore.RED + " ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ ")
    print("██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗")
    print("██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝")
    print("██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗")
    print("╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║")
    print(" ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝")
    print(Fore.YELLOW)
    global choice
    choice = int(input("Addition [1] | Soustraction [2] | Multiplication [3] | Division [4] : "))


def addition():
    numone = int(input(Fore.MAGENTA + "Entrez un premier nombre : "))
    numtwo = int(input(Fore.BLUE + "Entrez un second nombre : "))
    result = numone + numtwo
    print(Fore.CYAN + "Le résultat est : ", str(result))
    input()
    calculator()

def soustraction():
    numone = int(input(Fore.MAGENTA + "Entrez un premier nombre : "))
    numtwo = int(input(Fore.BLUE + "Entrez un second nombre : "))
    result = numone - numtwo
    print(Fore.CYAN + "Le résultat est : ", str(result))
    input()
    calculator()

def multiplication():
    numone = int(input(Fore.MAGENTA + "Entrez un premier nombre : "))
    numtwo = int(input(Fore.BLUE + "Entrez un second nombre : "))
    result = numone * numtwo
    print(Fore.CYAN + "Le résultat est : ", str(result))
    input()
    calculator()

def division():
    numone = int(input(Fore.MAGENTA + "Entrez un premier nombre : "))
    numtwo = int(input(Fore.BLUE + "Entrez un second nombre : "))
    result = numone / numtwo
    print(Fore.CYAN + "Le résultat est : ", str(result))
    input()
    calculator()

choice = 0
calculator()
if choice == 1:
    addition()

elif choice == 2:
    soustraction()

elif choice == 3:
    multiplication()


elif choice == 4:
    division()

else:
    print(Fore.RED + "Error")
    input()
    calculator()
from colorama import Fore
import os

def calculator():
    print(Fore.RED + """██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝""")
    print(Fore.YELLOW)
    global choice
    choice = int(input("Addition [1] | Soustraction [2] | Multiplication [3] | Division [4] : "))


def addition():
    numone = int(input(Fore.MAGENTA + "Entrez un premier nombre : "))
    numtwo = int(input(Fore.BLUE + "Entrez un second nombre : "))
    result = numone + numtwo
    print(Fore.CYAN + "Le résultat est : ", str(result))
    input()
    os.system("cls")
    main()

def soustraction():
    numone = int(input(Fore.MAGENTA + "Entrez un premier nombre : "))
    numtwo = int(input(Fore.BLUE + "Entrez un second nombre : "))
    result = numone - numtwo
    print(Fore.CYAN + "Le résultat est : ", str(result))
    input()
    os.system("cls")
    main()

def multiplication():
    numone = int(input(Fore.MAGENTA + "Entrez un premier nombre : "))
    numtwo = int(input(Fore.BLUE + "Entrez un second nombre : "))
    result = numone * numtwo
    print(Fore.CYAN + "Le résultat est : ", str(result))
    input()
    os.system("cls")
    main()

def division():
    numone = int(input(Fore.MAGENTA + "Entrez un premier nombre : "))
    numtwo = int(input(Fore.BLUE + "Entrez un second nombre : "))
    result = numone / numtwo
    print(Fore.CYAN + "Le résultat est : ", str(result))
    input()
    os.system("cls")
    main()

def main():
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
        main()

if __name__ == "__main__":
    main()

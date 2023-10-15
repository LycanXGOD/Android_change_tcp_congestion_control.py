import subprocess
from colorama import Fore, Style
import time

def set_tcp_congestion_control(settings):
    #LycanTweaks
    command = f"sudo sh -c 'echo \"{settings}\" > /proc/sys/net/ipv4/tcp_congestion_control'"
    subprocess.call(command, shell=True)

def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

def clear_screen():
    # Lycantweaks
    subprocess.call("clear", shell=True)

def main():
    #LycanTweaks
    congestion_settings = [
        "bbr",
        "wvegas",
        "olia",
        "vegas",
        "cubic",
        "lia",
        "hybla",
        "bic",
        "reno",
        "yeah"
    ]

    # LycanTweaks
    colors = [Fore.MAGENTA, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.CYAN]

    while True:
        #LycanTweaks
        clear_screen()

        #LycanTweaks
        print("\n▀█▀ █▀▀ █▀█   ▀█▀ █░█░█ █▀▀ ▄▀█ █▄▀ █▀")
        print("░█░ █▄▄ █▀▀   ░█░ ▀▄▀▄▀ ██▄ █▀█ █░█ ▄█>LycanTweaks")
        print("\nSelect a TCP congestion algorithm: \n")

        # LycanTweaks
        for i, algorithm in enumerate(congestion_settings, start=1):
            color = colors[i % len(colors)]
            print_colored(f"({i}) {algorithm}", color)

        # LycanTweaks
        print_colored("[11] INFO•", Fore.CYAN)

        # LycanTweaks
        print_colored("(b) Back", Fore.YELLOW)
        print_colored("(x) Exit", Fore.RED)

        # LycanTweaks
        selection = input("\n(1/2/3/4/5/6/7/8/9/10/11/a/x/): ").strip()
        if selection.isdigit():
            selection = int(selection)
            if 1 <= selection <= len(congestion_settings):
                selected_setting = congestion_settings[selection - 1]
                set_tcp_congestion_control(selected_setting)
                clear_screen()  # LycanTweaks
                print_colored(f"¡TCP SUCCESSFULLY CHANGED!", Fore.GREEN)
                time.sleep(3)  # LycanTweaks
            elif selection == 11:
                # LycanTweaks
                clear_screen()
                print_colored("Información: Aquí puedes seleccionar el algoritmo de congestión TCP que desees.", Fore.CYAN)
                time.sleep(3)  # LycanTweaks
            else:
                print_colored("Selección no válida. Por favor, elija un número válido.", Fore.RED)
                time.sleep(3)  # LycanTweaks
        elif selection.lower() == "b":
            print_colored("Volviendo al menú principal...", Fore.YELLOW)
            time.sleep(3)  # LycanTweaks
        elif selection.lower() == "x":
            print_colored("Saliendo del programa...", Fore.RED)
            break
        else:
            print_colored("Selección no válida. Por favor, elija una opción válida.", Fore.RED)
            time.sleep(3)  # LycanTweaks

if __name__ == "__main__":
    main()

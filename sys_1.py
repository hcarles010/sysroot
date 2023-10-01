print("███▄ ▄███▓▓█████  ▄████▄")
print("▓██▒▀█▀ ██▒▓█   ▀ ▒██▀ ▀█")
print("▓██    ▓██░▒███   ▒▓█    ▄")
print("▒██    ▒██ ▒▓█  ▄ ▒▓▓▄ ▄██▒")
print("▒██▒   ░██▒░▒████▒▒ ▓███▀ ░")
print("░ ▒░   ░  ░░░ ▒░ ░░ ░▒ ▒  ░")
print("░  ░      ░ ░ ░  ░  ░  ▒")
print("░      ░      ░   ░")
print("       ░      ░  ░░ ░")
p = 123
import subprocess
from colorama import Fore, Back, Style
while p == 123:
    command = input(Fore.BLUE + "<+>" + Style.RESET_ALL)
    if command == 'hakfy':
        while p ==123:
            wifi = input(Fore.RED + "<<WK>>" + Style.RESET_ALL)
            if wifi == "start":
                subprocess.run(["airmon-ng", "start", "wlan0"])
            elif wifi == "stop":
                subprocess.run(['airmon-ng', 'stop', 'wlan0mon'])    
            elif wifi == 'clear':
                subprocess.run(["clear"])
            elif wifi == 'xf':
                subprocess.run(['figlet', '"WKrakFy"'])
            elif wifi == 'ifconfig':
                subprocess.run(['ifconfig'])
            elif wifi == 'arp':
                subprocess.run(['arp-scan', '--localnet'])
            elif wifi == 'injek':
                bssid_pun = input(Fore.YELLOW + "Punto de accseso:" + Style.RESET_ALL)
                bssid_cli = input(Fore.CYAN + "Cliente de iyeccion:" + Style.RESET_ALL)
                value = input("Cantidad de inyecciones:")
                subprocess.run(['aireplay-ng','-0',value,'-a',bssid_pun,'-c',bssid_cli,'wlan0mon',])
            elif wifi == 'help':
                print(Fore.MAGENTA + """
                    start: Cambia el estado de la targeta de red a modo monitor
                    stop: Realiza la accion contraria a start
                    clear: Borra todo el contenido de la terminal
                    xf: Imprime en pantalla la erramienta acual
                    ifconfig: Muestra informacion detallada sobre los adaptadores de red
                    arp: Escanea en busca de dispositivos en tu misma red wifi o en un punto de acceso que as creado
                    exit: Sale de la rama anterior
                    injek: Inicia el proseso de inyeccion de paquetes  """)
            elif wifi == 'exit' or 'cd ..':
                break
                    
            else:
                print(Back.RED + "Invalid" + Style.RESET_ALL)                   
    elif command == "clear":
        subprocess.run(['clear'])
    elif command == "xf":
        subprocess.run(['figlet', '"SYS"'])
    elif command == 'nmap':
        while p == 123:
            ara = input(Fore.GREEN + '<<M>>' + Style.RESET_ALL)
            if ara == 'clear':
                subprocess.run(['clear'])
            elif ara == 'help':
                print(Fore.CYAN + """
                    clear: Limpia la terminal
                    exit: Sale de la rama actual
                    set-map: Establece la ip de ataque
                    run: Ejecuta el atake a la ip asignada
                    
                    """)    
            elif ara == 'xf':
                subprocess.run(['figlet', '"nmap-a"'])
            elif ara == 'set-map':
                map1 = input(Fore.RED + '>>>' + Style.RESET_ALL)
            elif ara == 'run':
                subprocess.run(['nmap',map1])
            elif ara == 'exit' or 'cd ..':
                break
    else:
        print(Back.RED + 'Invalid' + Style.RESET_ALL)    
                
            
            
                    
    
                    
            
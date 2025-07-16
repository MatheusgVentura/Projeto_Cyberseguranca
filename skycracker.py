import os
from tools.ping import ping
from tools.nmap_scan import nmap_scan
from tools.nikto_scan import nikto_scan
from tools.hydra_attack import hydra_attack
from tools.netstat import netstat
from tools.dns_lookup import dns_lookup
from tools.john_the_ripper import john_the_ripper
from tools.sqlmap_scan import sqlmap_scan
from tools.dirb_scan import dirb_scan

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from termcolor import colored

def banner():
    print(colored(r"""
      ██████████████████████████████████████████████████
      ███▄─▄███─▄▄─█─▄▄─█▄─▄▄▀█▄─█─▄█─▄▄─█▄─▄▄─█▄─▄▄▀███
      ████─██▀█─██─█─██─██─▄─▄██─▄▀██─██─██─▄█▀██─▄─▄███
      ██▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀██

              SKYCRACKER - Cybersecurity Toolkit
    """, 'green'))
    print(colored("""
    [1] Ping um servidor
    [2] Escanear portas (Nmap)
    [3] Verificar vulnerabilidades (Nikto)
    [4] Brute Force com Hydra
    [5] Exibir serviços ativos (Netstat)
    [6] Checagem de DNS (nslookup)
    [7] Quebrar hashes (John the Ripper)
    [8] Scan de SQL Injection (SQLMap)
    [9] Brute force de diretórios (Dirb)
    [0] Sair
    """, 'yellow'))

def main():
    while True:
        clear()
        banner()
        opcao = input(colored("Escolha uma opção: ", 'blue'))

        if opcao == "1":
            ping()
        elif opcao == "2":
            nmap_scan()
        elif opcao == "3":
            nikto_scan()
        elif opcao == "4":
            hydra_attack()
        elif opcao == "5":
            netstat()
        elif opcao == "6":
            dns_lookup()
        elif opcao == "7":
            john_the_ripper()
        elif opcao == "8":
            sqlmap_scan()
        elif opcao == "9":
            dirb_scan()
        elif opcao == "0":
            print(colored("Saindo...", 'red'))
            break
        else:
            print(colored("Opção inválida.", 'red'))

        input(colored("\nPressione Enter para continuar...", 'blue'))

if __name__ == "__main__":
    main()

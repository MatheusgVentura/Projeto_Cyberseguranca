import subprocess

def nmap_scan():
    target = input("Digite o IP ou domínio do alvo: ")
    print("\n[1] Varredura padrão")
    print("[2] Varredura stealth (TCP SYN Scan - nmap -sS)")
    tipo = input("Escolha o tipo de varredura: ")
    if tipo == "2":
        subprocess.run(["nmap", "-sS", target])
    else:
        subprocess.run(["nmap", target])

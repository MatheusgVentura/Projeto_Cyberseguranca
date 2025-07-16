import subprocess

def hydra_attack():
    service = input("Digite o serviço (ex: ssh, http): ")
    target = input("Digite o IP ou domínio do alvo: ")
    user = input("Digite o nome de usuário: ")
    wordlist = input("Digite o caminho da wordlist: ")
    subprocess.run(["hydra", "-l", user, "-P", wordlist, target, service])

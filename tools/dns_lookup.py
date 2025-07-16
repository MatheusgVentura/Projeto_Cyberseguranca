import subprocess

def dns_lookup():
    domain = input("Digite o domínio: ")
    subprocess.run(["nslookup", domain])

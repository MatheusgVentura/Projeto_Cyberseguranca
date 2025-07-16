import subprocess

def nikto_scan():
    target = input("Digite o endereço do servidor web (ex: http://exemplo.com): ")
    subprocess.run(["nikto", "-h", target])

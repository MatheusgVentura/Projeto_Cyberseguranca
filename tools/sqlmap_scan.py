import subprocess

def sqlmap_scan():
    url = input("Digite a URL do alvo: ")
    subprocess.run(["sqlmap", "-u", url, "--batch"])

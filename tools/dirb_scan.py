import subprocess

def dirb_scan():
    url = input("Digite a URL do alvo: ")
    subprocess.run(["dirb", url])

import subprocess

def ping():
    host = input("Digite o endereço do servidor: ")
    subprocess.run(["ping", host])

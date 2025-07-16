import subprocess

def john_the_ripper():
    hash_file = input("Digite o caminho do arquivo de hash: ")
    wordlist = input("Digite o caminho da wordlist: ")
    subprocess.run(["john", f"--wordlist={wordlist}", hash_file])

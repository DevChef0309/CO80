import socket
import time

print("© 2020 https://github.com/DevChef0309")
print("by DevChef0309")

IP = input("[+] ENTREZ L'IP DE LA CIBLE: ")
PORT = 80
VOTRE_IP = input("[+] ENTREZ L'IP ATTAQUANTE (VOTRE IP): ")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    print(f"[+] TRAITEMENT EN COURS SUR {IP}:{PORT}")
    print(f"[+] PORT 80: HTTP://{IP}")
except:
    print("[-] ERREUR DE CONNEXION")
    print(f"[-] VEUILLEZ VERIFIER VOS INFORMATIONS : IP DE LA CIBLE: {IP}:{PORT} | VOTRE IP: {VOTRE_IP}")


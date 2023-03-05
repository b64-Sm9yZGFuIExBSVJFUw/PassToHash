#!/usr/bin/python3.9
import os #"clear"
import hashlib #Pour hasher
import crypt #Avec sel
from urllib.request import urlopen #Requetes de pages internet
from termcolor import colored #Couleurs

prompt="$[PassToHash]$~ "

def main():
	# ========================== DEMANDE TYPE D'ENTREE =========================
	print(colored("[1]: Decrypter avec une liste de 10 millions de mots de passes" ,"magenta"))
	print(colored("[2]: Decrypter en utilisant un fichier contenant des mots de passes\n" ,"magenta"))

	choix1 = int(input(prompt+"Choix? "))

	if(choix1 != 1 and choix1 != 2):
		print(colored("[ERREUR] Choix incorrect, fin du programme...\n\n", "red"))
		quit()

	os.system("clear")

	# ========================== DEMANDE TYPE DE HASH =========================
	print(colored(banner,"green"))
	print(colored("MD5/SHA1/SHA224/SHA256/SHA512 Decrypt by Sun God Azayr\n\n","yellow"))
	print(colored("[1]: Decrypter un hash MD5" ,"magenta"))
	print(colored("[2]: Decrypter un hash SHA1" ,"magenta"))
	print(colored("[3]: Decrypter un hash SHA224","magenta"))
	print(colored("[4]: Decrypter un hash SHA256","magenta"))
	print(colored("[5]: Decrypter un hash SHA512\n","magenta"))

	choix2 = int(input(prompt+"Choix? "))

	if(choix2 < 1 or choix2 > 5):
		print(colored("[ERREUR] Choix incorrect, fin du programme...\n\n", "red"))
		quit()


	if choix2 == 1:
		type_hash = "MD5"
	elif choix2 == 2:
		type_hash = "SHA1"
	elif choix2 == 3:
		type_hash = "SHA224"
	elif choix2 == 4:
		type_hash = "SHA256"
	else: #==5
		type_hash = "SHA512"

	hash = input(prompt+"Entrez un hash "+type_hash+": ")

	if(choix1 == 1):
		#Liste vers les mdp (Hash à vérif)
		print(colored(prompt+"Connexion vers la liste des 10 millions de mots de passes...\n", "yellow"))
		passlist = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), 'utf-8')

		for mdp in passlist.split("\n"):
			print(colored(prompt+"Essai pour le mot de passe "+mdp+"...","yellow"))
			if type_hash == "MD5":
				mdp_hash = hashlib.md5(bytes(mdp, 'utf-8')).hexdigest()
			elif type_hash == "SHA1":
				mdp_hash = hashlib.sha1(bytes(mdp, 'utf-8')).hexdigest()
			elif type_hash == "SHA224":
				mdp_hash = hashlib.sha224(bytes(mdp, 'utf-8')).hexdigest()
			elif type_hash == "SHA256":
				mdp_hash = hashlib.sha256(bytes(mdp, 'utf-8')).hexdigest()
			else: #SHA512
				mdp_hash = hashlib.sha512(bytes(mdp, 'utf-8')).hexdigest()


			if hash == mdp_hash:
				print(colored(prompt+"MOT DE PASSE TROUVE: "+mdp+"\n","green"))
				quit()


	else: #Choix : 2
		nom_fichier = input(prompt+"Entrez le nom du fichier contenant les mots de passes: ")
		try:
			fichier = open(nom_fichier, "r")
		except:
			print(colored("[ERREUR] Le fichier "+nom_fichier+" n'existe pas !","red"))
			quit()

		for mdp in fichier.readlines():
			mdp = mdp.strip("\n")
			print(colored(prompt+"Essai pour le mot de passe "+mdp+"...","yellow"))

			if type_hash == "MD5":
				mdp_hash = hashlib.md5(bytes(mdp, 'utf-8')).hexdigest()
			elif type_hash == "SHA1":
				mdp_hash = hashlib.sha1(bytes(mdp, 'utf-8')).hexdigest()
			elif type_hash == "SHA224":
				mdp_hash = hashlib.sha224(bytes(mdp, 'utf-8')).hexdigest()
			elif type_hash == "SHA256":
				mdp_hash = hashlib.sha256(bytes(mdp, 'utf-8')).hexdigest()
			else: #SHA512
				mdp_hash = hashlib.sha512(bytes(mdp, 'utf-8')).hexdigest()

			if hash == mdp_hash:
				print(colored(prompt+"MOT DE PASSE TROUVE: "+mdp+"\n","green"))
				quit()

	print(colored(prompt+"\nMot de passe non trouvé...\n", "red"))

os.system("clear")

banner=("   ___             _____                      _\n"
        "  / _ \__ _ ___ __/__   \___   /\  /\__ _ ___| |__\n"
        " / /_)/ _` / __/ __|/ /\/ _ \ / /_/ / _` / __| '_ \ \n"
        "/ ___| (_| \__ \__ / / | (_) / __  | (_| \__ | | | |\n"
        "\/    \__,_|___|___\/   \___/\/ /_/ \__,_|___|_| |_|\n")

print(colored(banner, "green"))
print(colored("MD5/SHA1/SHA224/SHA256/SHA512 Decrypt by b64-Sm9yZGFuIExBSVJFUw\n\n","yellow"))

main()
print("\n")

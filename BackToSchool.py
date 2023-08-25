import socket
import re 
import sys
import math 

def extract_first_number(texte):
	match_X = re.search(r'square root of (\d+)', texte)
	if match_X:
		X = int(match_X.group(1))
	else:
		sys.exit("First number wasn't found !")
	return X

def extract_second_number(texte):
	match_Y = re.search(r'multiply by (\d+)', texte)
	if match_Y:
		Y = int(match_Y.group(1))
	else:
		sys.exit("Second number wasn't found !")
	return Y
	
# Paramètres
HOST = 'challenge01.root-me.org'  # Hostname
PORT = 52002        			  # Port du serveur

# Créer le socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Reception de la réponse
response = s.recv(1000).decode()
print(response)

#Extraction des deux nombres
X = extract_first_number(response)
Y = extract_second_number(response)

#Calcul du résultat à envoyer
result = round((math.sqrt(X)*Y),2)
print(result)

#Envoie du message
message = str(result) + '\n'
s.send(message.encode())

#Réception du flag
response = s.recv(1000).decode()
print(response)

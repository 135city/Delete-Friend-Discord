import discord
import requests

token = input("Ton token ici : ")

user_token = token

headers = {
    "Authorization": user_token
}

response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)

for friend in response.json():
    # Stocke le nom de l'ami
    friend_name = friend['user']['username']
    
    # Supprime l'ami
    response = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers)

    # Affiche le nom de l'ami supprimé au lieu du statut de la réponse
    print(f"Ami supprimé : {friend_name}")

# Affiche le nombre d'amis restants
response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)
print(f"Amis restants : {len(response.json())}")
import os
import json
from os import path

#def checkfiles():

if not os.path.exists('../logs/'):
    os.makedirs('../logs/')

if not path.exists('config/config.json'):
    jsonstructure = {} # Platzhalter
    jsonstructure['discord'] = []
    wronginput = False
    print("Möchtest du das automatisierte Setup nutzen? y/n")
    input1 = input()

    if input1 == "y" or input1 == "Y":
        token = input("Bitte geben Sie den Token ein: ")
        IDcategoryvoice = int(input("Bitte geben Sie die ID der Voicecategory ein: "))
        IDchannelcommand = int(input("Bitte geben Sie die ID des Commandchannels ein: "))
        IDchannelverificate = int(input("Bitte geben Sie die ID des Verifizierchannels ein: "))
        IDchanneladmin = int(input("Bitte geben Sie die ID des Adminchannels ein: "))
        IDgrpverificate = int(input("Bitte geben Sie die ID der Verifizierengruppe ein: "))
        IDgrpYT = int(input("Bitte geben Sie die ID der Youtube-Gruppe ein: "))
        IDgrpYTGold = int(input("Bitte geben Sie die ID der Youtube-Gold-Gruppe ein: "))
        IDgrpYTDiamant = int(input("Bitte geben Sie die ID der Youtube-Diamant-Gruppe ein: "))
        DBhost = input("Bitte geben Sie den DB-Host ein: ")
        DBuser = input("Bitte geben Sie den DB-Benutzer ein: ")
        DBpasswd = input("Bitte geben Sie das DB-Passwort ein: ")
        DBdatabase = input("Bitte geben Sie den DB-Namen ein: ")
        pterodactyl_domain = input("Bitte geben Sie die Pterodactyl Domain ein (Form: https://example.com/ | optional): ")
        pterodactyl_api_key = input("Bitte geben Sie den Pterodactyl API Key ein (optional): ")

        jsonstructure['discord'].append({
        'token': token,
        'IDcategoryvoice': IDcategoryvoice,
        'IDchannelcommand': IDchannelcommand,
        'IDchannelverificate': IDchannelverificate,
        'IDchanneladmin': IDchanneladmin,
        'IDgrpverificate': IDgrpverificate,
        'IDgrpYT': IDgrpYT,
        'IDgrpYTGold': IDgrpYTGold,
        'IDgrpYTDiamant': IDgrpYTDiamant,
        'DBhost': DBhost,
        'DBuser': DBuser,
        'DBpasswd': DBpasswd,
        'DBdatabase': DBdatabase,
        'pterodactyl_domain': pterodactyl_domain,
        'pterodactyl_apikey': pterodactyl_api_key
        })

    elif input1 =="n" or input1 == "N":

        jsonstructure['discord'].append({
        'token': 'Platzhalter',
        'IDcategoryvoice': 123,
        'IDchannelcommand': 123,
        'IDchannelverificate': 123,
        'IDchanneladmin': 123,
        'IDgrpverificate': 123,
        'IDgrpYT': 123,
        'IDgrpYTGold': 123,
        'IDgrpYTDiamant': 123,
        'DBhost': 'Platzhalter',
        'DBuser': 'Platzhalter',
        'DBpasswd': 'Platzhalter',
        'DBdatabase': 'Platzhalter',
        'pterodactyl_domain': '',
        'pterodactyl_apikey': ''
        })

    else:
        wronginput = True
        print("Falsche eingabe")

    if not wronginput:
        if not os.path.exists('config'):
            os.mkdir('config')
        with open('config/config.json', 'w') as outfile:
            json.dump(jsonstructure,outfile, indent=4)
        print("Config erfolgreich erzeugt")

if not os.path.exists('whitelist/youtube/paths.txt'):
    if not os.path.exists('whitelist'):
        os.mkdir('whitelist')
    if not os.path.exists('whitelist/youtube'):
        os.mkdir('whitelist/youtube')
    paths = open("whitelist/youtube/paths.txt", "a")
    paths.close()
    paths = open("whitelist/youtube/pterodactyl.txt", "a")
    paths.close()

if not os.path.exists('whitelist/twitch/paths.txt'):
    if not os.path.exists('whitelist'):
        os.mkdir('whitelist')
    if not os.path.exists('whitelist/twitch'):
        os.mkdir('whitelist/twitch')
    paths = open("whitelist/twitch/paths.txt", "a")
    paths.close()
    paths = open("whitelist/twitch/pterodactyl.txt", "a")
    paths.close()

if not os.path.exists('blacklist/discord/badwords.txt'):
    if not os.path.exists('blacklist'):
        os.mkdir('blacklist')
    if not os.path.exists('blacklist/discord'):
        os.mkdir('blacklist/discord')
    paths = open("blacklist/discord/badwords.txt", "a")
    paths.close()

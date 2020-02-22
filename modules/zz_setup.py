import os
#import os.path
import json
#import datetime
#import logging
#import mysql.connector
from os import path

def checkfiles():

    if not os.path.exists('../logs/'):
        os.makedirs('../logs/')

    if not path.exists('../config/config.json'):
        jsonstructure = {} # Platzhalter
        jsonstructure['discord'] = []
        wronginput = False
        print("Möchtest du das automatisierte Setup nutzen? y/n")
        input1 = input()

        if input1 == "y" or input1 == "Y":
            print("Bitte geben Sie den Token ein:")
            token = input()
            print("Bitte geben Sie die ID der Voicecategory ein:")
            IDcategoryvoice = int(input())
            print("Bitte geben Sie die ID des Commandchannels ein:")
            IDchannelcommand = int(input())
            print("Bitte geben Sie die ID des Verifizierchannels ein:")
            IDchannelverificate = int(input())
            print("Bitte geben Sie die ID des Adminchannels ein:")
            IDchanneladmin = int(input())
            print("Bitte geben Sie die ID der Verifizierengruppe ein:")
            IDgrpverificate = int(input())
            print("Bitte geben Sie die ID der Youtube-Gruppe ein:")
            IDgrpYT = int(input())
            print("Bitte geben Sie die ID der Youtube-Gold-Gruppe ein:")
            IDgrpYTGold = int(input())
            print("Bitte geben Sie die ID der Youtube-Diamant-Gruppe ein:")
            IDgrpYTDiamant = int(input())
            print("Bitte geben Sie den DB-Host ein:")
            DBhost = input()
            print("Bitte geben Sie den DB-Benutzer ein:")
            DBuser = input()
            print("Bitte geben Sie das DB-Passwort ein:")
            DBpasswd = input()
            print("Bitte geben Sie den DB-Namen ein:")
            DBdatabase = input()

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
            'DBdatabase': DBdatabase
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
            'DBdatabase': 'Platzhalter'
            })

        else:
            wronginput = True
            print("Falsche eingabe")
        if not wronginput:
            with open('../config/config.json', 'w') as outfile:
                json.dump(jsonstructure,outfile, indent=4)
            print("Config erfolgreich erzeugt")

    if not path.exists('../whitelist/paths.txt'):
        paths = open("../whitelist/paths.txt", "a")
        paths.close()

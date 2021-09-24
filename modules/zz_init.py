import json
import datetime
import logging
import mysql.connector

class config():
    def __init__(self):
        with open('config/config.json') as json_file:
            jsonstructure = json.load(json_file)
            for p in jsonstructure['discord']:
                self.token = p['token']
                self.IDcategoryvoice = p['IDcategoryvoice']
                self.IDcategorytext = p['IDcategorytext']
                self.IDchannelstandard = p['IDchannelstandard']
                self.IDchannelcommand = p['IDchannelcommand']
                self.IDchannelverificate = p['IDchannelverificate']
                self.IDchanneladmin = p['IDchanneladmin']
                self.IDchannellogs = p['IDchannellogs']
                self.IDchannelanfrage = p['IDchannelanfrage']
                self.IDgrpverificate = p['IDgrpverificate']
                self.IDgrpnotify = p['IDgrpnotify']
                self.IDgrpYT = p['IDgrpYT']
                self.IDgrpYTGold = p['IDgrpYTGold']
                self.IDgrpYTDiamant = p['IDgrpYTDiamant']
                self.IDgrpMod = p['IDgrpMod']
                self.IDguildCommunity = p['IDguildCommunity']
                self.ArrayIDgrpsubyoutube = p['ArrayIDgrpsubyoutube']
                self.ArrayIDgrpsubtwitch = p['ArrayIDgrpsubtwitch']
                self.ArraynoFilter = p['ArraynoFilter']
                self.DBhost = p['DBhost']
                self.DBuser = p['DBuser']
                self.DBpasswd = p['DBpasswd']
                self.DBdatabase = p['DBdatabase']
                self.pterodactyl_domain = p['pterodactyl_domain']
                self.pterodactyl_apikey = p['pterodactyl_apikey']

    def get_token(self):
        return self.token
    def get_IDcategoryvoice(self):
        return self.IDcategoryvoice
    def get_IDcategorytext(self):
        return self.IDcategorytext
    def get_IDchannelstandard(self):
        return self.IDchannelstandard
    def get_IDchannelcommand(self):
        return self.IDchannelcommand
    def get_IDchannelverificate(self):
        return self.IDchannelverificate
    def get_IDchanneladmin(self):
        return self.IDchanneladmin
    def get_IDchannellogs(self):
        return self.IDchannellogs
    def get_IDchannelanfrage(self):
        return self.IDchannelanfrage
    def get_IDgrpverificate(self):
        return self.IDgrpverificate
    def get_IDgrpnotify(self):
        return self.IDgrpnotify
    def get_IDgrpYT(self):
        return self.IDgrpYT
    def get_IDgrpYTGold(self):
        return self.IDgrpYTGold
    def get_IDgrpYTDiamant(self):
        return self.IDgrpYTDiamant
    def get_IDgrpMod(self):
        return self.IDgrpMod
    def get_IDguildCommunity(self):
        return self.IDguildCommunity
    def get_ArrayIDgrpsubyoutube(self):
        return self.ArrayIDgrpsubyoutube
    def get_ArrayIDgrpsubtwitch(self):
        return self.ArrayIDgrpsubtwitch
    def get_ArraynoFilter(self):
        return self.ArraynoFilter
    def get_DBhost(self):
        return self.DBhost
    def get_DBuser(self):
        return self.DBuser
    def get_DBpasswd(self):
        return self.DBpasswd
    def get_DBdatabase(self):
        return self.DBdatabase
    def get_pterodactyl_domain(self):
        return self.pterodactyl_domain
    def get_pterodactyl_apikey(self):
        return self.pterodactyl_apikey

mydb = mysql.connector.connect(
    host=config().get_DBhost(),
    user=config().get_DBuser(),
    passwd=config().get_DBpasswd(),
    database=config().get_DBdatabase(),
    auth_plugin='mysql_native_password'
)

def logger():
    day = datetime.datetime.now()

    logfile = 'logs/discord' + '_' + str(day.year) + '_' + str(day.month) + '_' + str(day.day) + '.log'
    logger = logging.getLogger('discord')
    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler(filename=logfile, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

def getdb():
    return(mydb)

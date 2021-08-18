import json
import datetime
import logging
import mysql.connector
import re

class Config():
    def __init__(self, static_files, dynamic_files):
        for filename, alias in static_files:
            self.readFile(filename, alias)

        for filename, alias in dynamic_files:
            ending = splitted[-1] if len( (splitted := filename.split('.')) ) > 1 else ''

            self.readFile(filename, alias, ending)

            self.__setattr__(alias + "_add", (lambda line : self.appendLine(filename, alias, line)))
            self.__setattr__(alias + "_remove", (lambda line : self.removeLine(filename, alias, line)))

    def appendLine(self, filename, alias, line):
        self.__getattribute__(alias).append(self.removeNewline(line))

        self.appendLine_(filename, line)

    def appendLine_(self, filename, line):
        with open(filename, 'a') as open_file:
            open_file.write(line+'\n' if len(line) > 0 and line[-1] != '\n' else line)

    def removeLine(self, filename, alias, line):
        try:
            self.__getattribute__(alias).remove(self.removeNewline(line))

        except:
            pass

        self.removeLine_(filename, alias)

    def removeLine_(self, filename, alias):
        with open(filename, 'w') as open_file:
            for line in self.__getattribute__(alias):
                open_file.write(line+'\n' if len(line) > 0 and line[-1] != '\n' else line)

    def readFile(self, filename, alias, ending=None):
        if ending == None:
            ending = splitted[-1] if len( (splitted := filename.split('.')) ) > 1 else ''

        with open(filename, 'r') as open_file:
            if ending == "json":
                try:
                    self.__setattr__(alias, json.load(open_file))
                except:
                    return
            else:
                    self.__setattr__(alias, [ self.removeNewline(line) for line in open_file ])

    def removeNewline(self, text):
        return text[:-1] if len(text) > 0 and text[-1] == "\n" else text

config = Config(
    [
        ('config/config.json', 'main'),
        ('welcome/discord/welcome.txt', 'welcome_messages'),
        ('whitelist/youtube/paths.txt', 'wlytPaths'),
        ('whitelist/twitch/paths.txt', 'wltPaths'),
        ('whitelist/youtube/pterodactyl.txt', 'wlytPterodactyl'),
        ('whitelist/twitch/pterodactyl.txt', 'wltPterodactyl')
    ],
    [
        ('blacklist/discord/badwords.txt', 'badwords')
    ]
)

mydb = mysql.connector.connect(
    host=config.main['DBhost'],
    user=config.main['DBuser'],
    passwd=config.main['DBpasswd'],
    database=config.main['DBdatabase'],
    auth_plugin='mysql_native_password'
)

#welcome_messages_count = len(welcome_messages)

def logger():
    day = datetime.datetime.now()

    logfile = 'logs/discord' + '_' + str(day.year) + '_' + str(day.month) + '_' + str(day.day) + '.log'
    logger = logging.getLogger('discord')
    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler(filename=logfile, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

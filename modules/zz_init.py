import json
import datetime
import logging
import mysql.connector
import re

class Config():
    def __init__(self, static_files, dynamic_files):
        for file in static_files:
            self.readFile(file)

        for file in dynamic_files:
            fileWithoutEnd, ending = (''.join(splitted[:-1]), splitted[-1]) if len( (splitted := file.split('.')) ) > 1 else (splitted[0], '')

            self.readFile(file, fileWithoutEnd, ending)

            self.__setattr__(fileWithoutEnd + "_add", (lambda line : self.appendLine(file, fileWithoutEnd, line)))
            self.__setattr__(fileWithoutEnd + "_remove", (lambda line : self.removeLine(file, fileWithoutEnd, line)))

    def appendLine(self, filename, fileWithoutEnd, line):
        self.__getattribute__(fileWithoutEnd).append(line)

        self.appendLine_(filename, line)

    def appendLine_(self, filename, line):
        with open(filename, 'a') as open_file:
            open_file.write(line)

    def removeLine(self, filename, fileWithoutEnd, line):
        try:
            self.__getattribute__(fileWithoutEnd).remove(line)

        except:
            pass

        self.removeLine_(filename, fileWithoutEnd)

    def removeLine_(filename, fileWithoutEnd):
        with open(filename, 'w') as open_file:
            for line in self.__getattribute__(fileWithoutEnd):
                open_file.write(line)

    def readFile(self, filename, fileWithoutEnd=None, ending=None):
        if fileWithoutEnd == None or ending == None:
            fileWithoutEnd, ending = (''.join(splitted[:-1]), splitted[-1]) if len( (splitted := filename.split('.')) ) > 1 else (splitted[0], '')

        with open(filename, 'r') as open_file:
            if ending == "json":
                try:
                    self.__setattr__(fileWithoutEnd, json.load(open_file))
                except:
                    continue
            else:
                self.__setattr__(fileWithoutEnd, open_file.readlines())

config = {}

with open('config/config.json') as json_file:
    jsonstructure = json.load(json_file)
    for p in jsonstructure['discord']:
        config = p

mydb = mysql.connector.connect(
    host=DBhost,
    user=DBuser,
    passwd=DBpasswd,
    database=DBdatabase,
    auth_plugin='mysql_native_password'
)

welcome_messages = []
with open("welcome/discord/welcome.txt", "r") as file:
    for line in file:
        welcome_messages.append(line)
welcome_messages_count = len(welcome_messages)

whitelist_youtube_paths = []
with open("whitelist/youtube/paths.txt", "r") as file:
    for line in file:
        whitelist_youtube_paths.append(line)

whitelist_twitch_paths = []
with open("whitelist/twitch/paths.txt", "r") as file:
    for line in file:
        whitelist_twitch_paths.append(line)

whitelist_pterodactyl_youtube_paths = []
with open("whitelist/youtube/pterodactyl.txt", "r") as file:
    for line in file:
        whitelist_pterodactyl_youtube_paths.append(line)

whitelist_pterodactyl_twitch_paths = []
with open("whitelist/twitch/pterodactyl.txt", "r") as file:
    for line in file:
        whitelist_pterodactyl_twitch_paths.append(line)

badwords = []
badwords_filename = "blacklist/discord/badwords.txt"
with open(badwords_filename", "r") as file:
    for line in file:
        badwords.append(line)

def addBadword(word):
    badwords.append(word+"\n")

    with open(badwords_filename, "a") as file:
        file.write(word+"\n")

def removeBadword(word):
    word_safe = word.strip() + "\n"

    if word_safe not in badwords:
        return

    badwords.remove(word_safe)

    with open(badwords_filename, "w") as file:
        for badword in badwords:
            file.write(badword)

def logger():
    day = datetime.datetime.now()

    logfile = 'logs/discord' + '_' + str(day.year) + '_' + str(day.month) + '_' + str(day.day) + '.log'
    logger = logging.getLogger('discord')
    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler(filename=logfile, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

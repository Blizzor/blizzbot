import json
import datetime
import logging
import mysql.connector

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

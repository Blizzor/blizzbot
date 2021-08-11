#import discord
import mysql.connector
from modules import zz_init

mycursor = zz_init.mydb.cursor()

#create database
mycursor.execute("CREATE DATABASE blizzbot")

#create table
mycursor.execute("CREATE TABLE mcnames (id INT AUTO_INCREMENT PRIMARY KEY, discord_id BIGINT, minecraft_name TINYTEXT, uuid TINYTEXT, isWhitelistedYoutube BOOLEAN, isWhitelistedTwitch BOOLEAN)")

mycursor.execute("CREATE TABLE ranking (id INT AUTO_INCREMENT PRIMARY KEY, discord_id BIGINT, points INT)")

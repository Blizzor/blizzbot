#import discord
import mysql.connector
from modules import zz_init

mydb = mysql.connector.connect(
    host=zz_init.config['DBhost'],
    user=zz_init.config['DBuser'],
    passwd=zz_init.config['DBpasswd'],
    database=zz_init.config['DBdatabase'],
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

#create database
mycursor.execute("CREATE DATABASE blizzbot")

#create table
mycursor.execute("CREATE TABLE mcnames (id INT AUTO_INCREMENT PRIMARY KEY, discord_id BIGINT, minecraft_name TINYTEXT, uuid TINYTEXT, isWhitelistedYoutube BOOLEAN, isWhitelistedTwitch BOOLEAN)")

mycursor.execute("CREATE TABLE ranking (id INT AUTO_INCREMENT PRIMARY KEY, discord_id BIGINT, points INT)")

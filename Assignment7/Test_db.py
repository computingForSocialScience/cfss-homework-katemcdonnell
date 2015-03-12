import pymysql
import pandas as pd
from fetchArtist import *
from analyzeNetworks import *
from artistNetworks import *
import requests
import random
import csv


dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')
		
c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS playlists 
(id integer primary key auto_increment, rootArtist VARCHAR (100))
ENGINE=MyISAM DEFAULT CHARSET=utf8;""")

c.execute("""CREATE TABLE IF NOT EXISTS songs 
(id integer primary key auto_increment, playlistid integer, songOrder integer, artistName VARCHAR (100), albumName VARCHAR (100), trackName VARCHAR (100)) 
ENGINE= MyISAM DEFAULT CHARSET=utf8;""")

q = """INSERT INTO playlists (rootArtist) VALUES (%s) """
c.execute(q)
lastID = c.lastrowID


f= open ('sample_playlist.csv')
csvfile= unicodecsv.reader(f)
header=True
        
for i in csvfile:
    print i
    playlistId = lastID
    songOrder= 1
    artistName= i[0]
    albumnName = i[1]
    trackName = i[2]
        
      
sql = """INSERT INTO songs (playlistId, songOrder, artistName, albumName, trackName) VALUES (%s,%s,%s,%s,%s) """
c.execute(sql)
songOrder += 1
    
c.commit()
c.close()
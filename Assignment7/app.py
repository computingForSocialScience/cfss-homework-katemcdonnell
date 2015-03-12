#from flask import Flask, render_template, request, redirect, url_for
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

#app = Flask(__name__)

def createNewPlaylist(artistname):
    
    EL=writeEdgeList(fetchArtistId(artistname), 2, 'makeplaylist.csv')
    
    random_node_list = []
    DG= pandasToNetworkX('makeplaylist.csv')
    for x in range(0,30):
        random_node = randomCentralNode(DG)
        random_node_list.append(random_node)
    
    print random_node_list
    #return random_node_list
    #print createNewPlaylist('Beck')
    random_album_dict = {}
    random_albumID_list = []
    random_song_dict = {}
    random_artist_name_dict = {}

    for random_node in random_node_list:
        url1= 'https://api.spotify.com/v1/artists/' + random_node + '/albums'
        req = requests.get(url1)
        data1= req.json()
        random_album_dict[random_node] = data1['items'][0]['name']
        
        random_albumID_list.append(data1['items'][0]['id'])
        
    for albumID in random_albumID_list:
        url2 = 'https://api.spotify.com/v1/albums/' + albumID + '/tracks'            
        #print "hey url2 is", url2
        req = requests.get(url2)
        data2= req.json()
        random_song_dict[random_node] = data2['items'][0]['name']
        random_artist_name_dict[random_node] = data2['items'][0]['artists'][0]['name']
        
        f = open('playlist.csv', 'w')
        f.write(u'artist_name , album_name, track_name\n')

        for random_node in random_node_list:
            f.write(u'"' + str(random_artist_name_dict[random_node]) +  '" , "' +str(random_album_dict[random_node])  + '" + "' + random_song_dict[random_node] + '" \n')
        f.close()
        


        
    #print random_albumID_list
''''
I started working on this portion of the code over here but moved into 'Test_db.py' 

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
'''        
       
createNewPlaylist('Beck')

         


@app.route('/')
def make_index_resp():
    # this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    return(render_template('index.html'))


@app.route('/playlists/')
def make_playlists_resp():
    
    c = db.cursor()
    sql="""SELECT id, rootArtist from playlists"""
    c.execute(sql)
    playlists= c.fetchall()
    return render_template('playlists.html',playlists=playlists)
#Since nothing is working, I can't check to see if this works but had everything worked perfectly
#this is what I would have written for this part. 

@app.route('/playlist/<playlistId>')
def make_playlist_resp(playlistId):
    
    c=db.cursor()
    sql ="""SELECT songOrder, artistName, albumName, Trackname from songs """
    c.execute(sql)
    songs=c.fetchall()
    return render_template('playlist.html',songs=songs)

#Same as above, I'm not sure if this would work but this would have been my starting point referencing the slides.


@app.route('/addPlaylist/',methods=['GET','POST'])
def add_playlist():
    if request.method == 'GET':
        # This code executes when someone visits the page.
        return(render_template('addPlaylist.html'))
    elif request.method == 'POST':
        # this code executes when someone fills out the form
        artistName = request.form['artistName']
        createNewPlaylist(artistName)
        return(redirect("/playlists/"))



if __name__ == '__main__':
   app.debug=True
   #app.run()
'''
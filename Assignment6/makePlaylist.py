import sys
import requests
import csv
import numpy as np
from fetchArtist import *
from analyzeNetworks import *
from artistNetworks import *
#from fetchAlbums import *
import pandas as pd

for i in sys.argv[1:]:
    writeEdgeList(fetchArtistId(i),2, 'edgeList.csv')
    masterDF_edgeList = readEdgeList('edgeList.csv')
    
for i in sys.argv[2:]:
    writeEdgeList(fetchArtistId(i), 2 , 'edgeList.csv')
    DF_edgeList = readEdgeList('edgeList.csv')
    masterDF_edgeList = combineEdgeList(masterDF_edgelist, DF_edgeList)

random_node_list = []
DG= pandasToNetworkX(masterDF_edgeList)
for x in range(0,30):
    random_node = randomCentralNode(DG)
    random_node_list.append(random_node)

random_album_dict = {}
random_albumID_list = []
random_song_dict = {}
random_artist_name_dict = {}

for random_node in random_node_list:
    url1= 'https://api.spotify.com/v1/artists/' + random_node + '/albums'
    req = request.get(url1)
    data1= req.json()
    random_album_dict[random_node] = data1['items'][0]['name']
    random_albumID_list.append(data1['items'][0]['id]'])
    for albumID in random_albumID_list:
        url2 = 'https://api.spotify.com/v1/artists/' + albumID + '/tracks'
        req = requests.get(url2)
        data2= req.json()
        
        random_song_dict[random_node] = data2['items'][0]['name']
        random_artist_name_dict[random_node] = data2['items'][0]['atists'][0]['name']

f = open('playlist.csv', 'w')
f.write(u'artist_name , album_name, track_name\n')

for random_node in random_node_list:
    f.write(u'"' + random_artist_name_dict[random_node] +  '" , "' +random_album_dict[random_node]  + '" + "' + random_song_dict[random_node] + '" \n')
f.close()     

#Fetch artist networks    




#for artist in ID_Depth:
    
        
    # fetch artist networks 
    
    #combine artist networks into one
    
    #fetch random node
    
    #for artist ID's fetch album and song from ID
    
    #Print 30 from different artists.
        
        
    
    
    
    
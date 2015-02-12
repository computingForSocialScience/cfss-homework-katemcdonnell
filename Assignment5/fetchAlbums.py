import requests
from datetime import datetime
from fetchArtist import *

def fetchAlbumIds(artist_id):
    url= 'https://api.spotify.com/v1/artists/' + artist_id + '/albums?market=US&album_type=album'
    req= requests.get(url)
    
    data=req.json()
    
    albums=[]
    for item in data['items']:
        albums.append(item['id'])
    
    return albums
 
fetchAlbumIds('1GjWNGbMtHDQ7CNYf2d7cw')

#Using the Spotify API, take an artist ID and 
#returns a list of album IDs in a list
    



def fetchAlbumInfo(album_id):
    url= 'https://api.spotify.com/v1/albums/' + album_id
    req=requests.get(url)
    
    data=req.json()
    
    album_info={}
    
    album_info['artist_id'] = data['artists'][0]['id']
    album_info['artist'] = data['artists'][0]['name']
    album_info['name']= data['name']
    album_info['popularity']= data['popularity']
    album_info['year']= data['release_date'][0:4]
    
    return album_info
if __name__ == '__main__':
    print fetchAlbumInfo('6TGigQgG3PAcVjojd2Br3u')

    
    #Using the Spotify API, take an album ID 
    #and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    #pass


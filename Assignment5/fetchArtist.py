import sys
import requests
import csv

def fetchArtistId(name):
    url='https://api.spotify.com/v1/search?q=' + name +'&type=artist'
    req=requests.get(url)
    
    data=req.json()

    if not req.ok:
        print "error: " + data['error']['message']
        return "error :" + data['error']['message']
    
    artistID=data['artists']['items'][0]['id']
    return artistID

fetchArtistId('Beck')

    
    #"""Using the Spotify API search method, take a string that is the artist's name, 
    #and return a Spotify artist ID.
    

def fetchArtistInfo(artist_id):
    url='https://api.spotify.com/v1/artists/' + artist_id 
    #print url
    req=requests.get(url)
    ArtistInfo={}
    
    data=req.json()
    
    ArtistInfo['Followers'] = data['followers']['total']
    ArtistInfo['genres'] = data['genres']
    ArtistInfo['name'] = data['name']
    ArtistInfo['popularity'] = data['popularity']
    ArtistInfo['id'] = data['id']
    
    return ArtistInfo

if __name__ == '__main__':
    print fetchArtistInfo(fetchArtistId('Beck'))

# "if __name__ == '__main__" will only print the function if you call this file. Allows
#you to call file in other .py files without printing this function everytime. 
    


#Using the Spotify API, takes a string representing the id and returns a dictionary including the keys 'followers', 'genres',  'id', 'name', and 'popularity'.
    
    #pass   


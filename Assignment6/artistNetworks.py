import sys
import requests
import csv
from fetchArtist import *
import pandas as pd


def getrelatedArtists(artistID):
    url= 'https://api.spotify.com/v1/artists/' + artistID + '/related-artists'
    #print url
    req=requests.get(url)
    
    data=req.json()
    
    relatedArtists= []
    for item in data['artists']:
        relatedArtists.append(item['id'])
        
    return relatedArtists

#print getrelatedArtists(fetchArtistId('Beck'))
    
def getDepthEdges(artistID, depth):
    if depth==0:
        return []
    
    related_artist= getrelatedArtists(artistID)
    tpl_lst= []
    
    for artist in related_artist:
        tpl_lst.append((artistID, artist))

    for artist_relatedartist in tpl_lst:
        tpl_lst= set(tpl_lst)
        tpl_lst = list(tpl_lst)
        tpl_lst= tpl_lst + getDepthEdges(artist_relatedartist[1], depth-1)
        
        
    return tpl_lst 


#print getDepthEdges(fetchArtistId('Beck'), 2)

def getEdgeList(artistID, depth):
    
    df=pd.DataFrame(getDepthEdges(fetchArtistId('name'), depth))
    df.columns = ['artist' , 'related artist']
    
    return df
    
#print getEdgeList('Beck', 2)

def writeEdgeList(artistID, depth, filename):
    
     EL=getEdgeList(artistID, depth).to_csv(filename, index=False)
     
     return EL
   

#print writeEdgeList('Beck', 2, 'Beck_csv2')
#writeEdgeList('Iron and Wine', 3, 'ironwine_csv')    
#writeEdgeList('Bay City Rollers', 2, 'bcr_csv')   


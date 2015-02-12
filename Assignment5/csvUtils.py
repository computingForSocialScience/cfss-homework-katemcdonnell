from io import open
from fetchArtist import *
from fetchAlbums import *

def writeArtistsTable(artist_info_list):
    f = open('artists.csv','w')
    f.write(u'ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY\n')
    
    for ArtistInfo in artist_info_list:
        f.write("" + ArtistInfo['id'] + ","+ ArtistInfo['name']+ "," + str(ArtistInfo['followers']) +"," + str(ArtistInfo['popularity']))
    f.close()
        
    
def writeAlbumsTable(album_info_list):
    f= open('albums.csv','w')
    f.write(u'ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY\n')
    
    for album_info in album_info_list:
        print "the album info dict is", album_info
        f.write(''+album_info['artist_id']+','+ album_info['album_id'] + ',' + album_info['name']+',' +album_info['year'])
    f.close()
# I keep returning an empty dictionary and no using the dictionary in the other .py files. 
artist_info_list=[]
for artist in['Beck']:
    artist_info_list.append(fetchArtistInfo(fetchArtistId(artist)))
    
album_info_list = []
for artist in ['Beck']:
    artist_id = fetchArtistId(artist)
    album_info_list.append(fetchAlbumInfo(fetchAlbumIds(fetchArtistId(artist))[0]))
    
    
writeArtistsTable(artist_info_list)

writeAlbumsTable(album_info_list)    


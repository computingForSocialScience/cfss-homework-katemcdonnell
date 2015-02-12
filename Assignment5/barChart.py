import unicodecsv as csv
import matplotlib.pyplot as plt

def getBarChartData():
    f_artists = open('artists.csv')
    f_albums = open('albums.csv')
# This opens the csv files

    artists_rows = csv.reader(f_artists)
    albums_rows = csv.reader(f_albums)
# these lines equate artist_rows and album_rows with
# the opened csv files. where the artists csv is now represented 
#by artists_rows and albums csv by albums_rows
    artists_header = artists_rows.next()
    albums_header = albums_rows.next()

    artist_names = []
#creates an empty list called artist_names
    
    decades = range(1900,2020, 10)
    decade_dict = {}
    for decade in decades:
        decade_dict[decade] = 0
  #creates a dictionary for the decades of the release dates   
    for artist_row in artists_rows:
        if not artist_row:
            continue
        #if there is a blank space in the file continue on    
        artist_id,name,followers, popularity = artist_row
        artist_names.append(name)

    for album_row  in albums_rows:
        if not album_row:
            #if blank continue on
            continue
        artist_id, album_id, album_name, year, popularity = album_row
        for decade in decades:
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)):
                decade_dict[decade] += 1
                #adds a key (decade) to the decades code. Assigns the album years into decades.
                break

    x_values = decades
    y_values = [decade_dict[d] for d in decades]
    #labels the x and y axis
    return x_values, y_values, artist_names

def plotBarChart():
    x_vals, y_vals, artist_names = getBarChartData()
    # calls the previous function
    
    fig , ax = plt.subplots(1,1)
    ax.bar(x_vals, y_vals, width=10)
    ax.set_xlabel('decades')
    ax.set_ylabel('number of albums')
    ax.set_title('Totals for ' + ', '.join(artist_names))
    plt.show()


    

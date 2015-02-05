import csv
import sys

def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)

#permits = readCSV("permits_hydepark.csv")

#print permits[0][129]

#for row in permits:
    #print row[129]
    
#Part 3.1
def get_avg_latlng(permit_file):
    permits = readCSV(permit_file)
    sumLng=0.
    sumLat=0.
    for row in permits:
        sumLng= sumLng + float(row[128])
        sumLat = sumLat + float(row[129])
        
    avgLng= sumLng/len(permits)
    avgLat= sumLat/ len(permits)
    return avgLng, avgLat
                   
#get_avg_latlng()

# Part 3.2

def zip_code_barchart(permit_file):
    permits = readCSV(permit_file)
    zip_lst=[]
    zip_count_dict={}

    for tple in permits:
        if tple[28] != "":
            zip_lst.append(tple[28][0:5])
            
        if tple[35] != "":
            zip_lst.append(tple[35][0:5])
        if tple[42] != "":
            zip_lst.append(tple[42][0:5])
        if tple[49] != "":
            zip_lst.append(tple[49][0:5])
        if tple[56] != "":
            zip_lst.append(tple[56][0:5])
        if tple[63] != "":
            zip_lst.append(tple[63][0:5])
        if tple[70] != "":
            zip_lst.append(tple[70][0:5])
        if tple[77] != "":
            zip_lst.append(tple[77][0:5])
        if tple[84] != "":
            zip_lst.append(tple[84][0:5])
        if tple[91] != "":
            zip_lst.append(tple[91][0:5])
        if tple[98] != "":
            zip_lst.append(tple[98][0:5])
        if tple[105] != "":
            zip_lst.append(tple[105][0:5])
        if tple[112] != "":
            zip_lst.append(tple[112][0:5])
        if tple[119] != "":
            zip_lst.append(tple[119][0:5])
        if tple[126] != "":
            zip_lst.append(tple[126][0:5])

            for zp in zip_lst:
                zip_count_dict[zp]=0
            for zp in zip_lst:
                if zp in zip_count_dict:
                    zip_count_dict[zp] += 1
            
    print zip_lst
    print zip_count_dict
    print zip_count_dict.keys()

zip_code_barchart('permits_hydepark.csv')

#if __name__=="__main__":
    #a,b=get_avg_latlng(sys.argv[1])
    #print a,b
    #zip_code_barchart(sys.argv[1])
    
    
###make a dictionary of the zipcode counts by looping over the ziplist where the key is the zipcode (zp) and the value is the zipcode count###


## I got the code above to work in office hours but trying to run it again later I keep getting an error that says "list index out of range" for line 89. Because I can't get the code to produce a dictionary, I can't use that dictionary to create my histogram below. So I wrote out the code for how I would have done it had it all worked perfectly. 


import numpy as np
import matplotlib.pyplot as plt


N=len(zip_count_dict)
x= zips_in_illinois.keys()
y= zips_in_illinois.values()

width=0.35

fig, ax = plt.subplots()
rects1= ax.bar(x,y,width,colour='b', yerr=y)

ax.set_ylabel('Zip Code Counts')
ax.set_xlabel('Zip Codes')
ax.set_title('Contractor Zip Codes')

plt.savefig('Zip_code_histogram.jpg')
    
    
    
        
        
        
        
        
        
        








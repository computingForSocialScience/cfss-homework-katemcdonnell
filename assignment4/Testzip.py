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

permits = readCSV("permits_hydepark.csv")

def zip_code_barchart():
    permits = readCSV("permits_hydepark.csv")
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


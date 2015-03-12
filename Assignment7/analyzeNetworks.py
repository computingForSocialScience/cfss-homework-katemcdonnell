import csv
import requests
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from artistNetworks import *


def readEdgeList(filename):
    
    df=pd.read_csv(filename)
    
    if len(df.columns)!= 2:
        print 'warning  dataframe contains more than 2 columns'
        df_2col = pd.read_csv(filename, usecols=('artist' , 'related artist'))
        #when I created my csv files I named the columns 'artist' and 'related
         #  artists' that's why I used those arguments. 
        return df_2col
    
    else:
        return df

#print readEdgeList('test_csv')
#print readEdgeList('bcr_csv')

def degree(edgelist, in_or_out):
    
    EL= readEdgeList(edgelist)
# I kept getting an error that said edgelist not define for the lines below
# so I defined it here as readEdgeList. The problem is that now the data frame has more than two columns and I get the warning called in the readEdgeList function. Does this mean that I am also only seeing two of the columns and there are more? 

    
    if in_or_out == 'out':
        return EL['artist'].value_counts()
    
    elif in_or_out == 'in':
        return EL['related artist'].value_counts()
    
    else:
        return ' warning, you messed up'


#print degree(readEdgeList('test_csv'), 'in' )

def combineEdgelist(edgelist1, edgelist2):
    
    EL1 = pd.read_csv(edgelist1)
    EL2 = pd.read_csv(edgelist2)
    #EL1 = readEdgeList('edgelist1')
    #EL2 = readEdgeList('edgelist2')
    
    #return type(EL1)
    
    combinedEdgeList = EL1.append(EL2)
    
    combinedEdgeList.drop_duplicates()
    
    return combinedEdgeList

#print combineEdgelist('test_csv', 'bcr_csv')

def pandasToNetworkX(edgeList):
    
    EL= pd.read_csv(edgeList)
    #print EL
    DG=nx.DiGraph()
    
    for column1, column2 in EL.to_records(index=False):
        DG.add_edge(column1, column2)
        
        nx.draw(DG, with_labels=False)
        #circLayout= nx.layout.circular_layout(DG)
        #nx.draw(DG, pos=circLayout, with_labels=False)
        
    
    return DG
    #plt.show()
    #plt.savefig() 
        
    #return DG.nodes()
#printed the nodes in terminal to see if it was working

#pandasToNetworkX('test_csv')

def randomCentralNode(inputDiGraph):
    
    eigenvector_nodes_dict= nx.eigenvector_centrality(inputDiGraph)
    normal_denominator = 0
    #print eigenvector_dict
    
    for node in eigenvector_nodes_dict:
    		#print node
    		#print eigen_nodes_dict[node]
    		normal_denominator += eigenvector_nodes_dict[node]
    		#print normal_denominator
    for node in eigenvector_nodes_dict:
    	newval = eigenvector_nodes_dict[node]/normal_denominator
    	eigenvector_nodes_dict[node] = newval
    	#return eigen_nodes_dict
    random_node = np.random.choice(eigenvector_nodes_dict.keys(), p=eigenvector_nodes_dict.values())
    return random_node
    
#print randomCentralNode(pandasToNetworkX('test_csv'))


    
    


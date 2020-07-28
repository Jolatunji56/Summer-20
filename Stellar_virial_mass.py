import pynbody
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Loads snapshot
s = pynbody.load ('/data/h258/stampedetesting/glenna/h258.cosmo50cmb.3072gst1bwdK1BH.000128')

f =  open("BH_halo_file.dat", "w+")

#Put the units in a right way 
s.physical_units()

#Initiates a halo catalogue object for the given snapshot
h = s.halos()

#Function to find Black hole (BH)
def findBH(s):
    """A function that returns particles whose property is less than max, returns the lenght if BHs."""
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
#print BH

#Function to find the halos that the galaxy is in
def findBHhalos(s):
    """returns the indexes (ID-number) of host halos for each BHs"""
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos

BHhalos = findBHhalos(s)
#print BHhalos

#sorting the halos, indexes/indecis are like an exact address
currenthalo = np.argsort(BHhalos)
#print BHhalos[currenthalo]

def getz(s):
    """returns redshift of halos""" 
    return s.properties['z']

def gettime(s):
    """returns time formation of halos"""
    return pynbody.analysis.cosmology.age(s)

for i in currenthalo:

    #which halo are we on?
    currenthalo = BHhalos[i]
    #print 'current halo: ', currenthalo

    #print i
    
    #put the galaxy you care about in the center of the simulation
    pynbody.analysis.angmom.faceon(h[currenthalo])
    

    #this is the position of black hole
    BHposition=BH['pos']

    #printing the position of black hole
    #print BHposition
    
    #putting the x-values into a column
    BHx= BHposition[[i],0]
    #print "x postion", BHx

    #putting the y-values into a column
    BHy= BHposition[[i],1]
    #print "y position", BHy

    #putting the z-values into a column
    BHz= BHposition[[i],2]
    #print "z position", BHz

    #the .5 is the square root , this is the distance formula
    distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
    #print 'this is the distance :'
    #print "this is the distance :", distance

    #variables to finding stellar masses and halo masses
    starmass = h[currenthalo].s['mass'].sum()
    gasmass = h[currenthalo].g['mass'].sum()
    virialmass = starmass+gasmass+h[currenthalo].d['mass'].sum()
    data = [currenthalo, BH['iord'][i], gettime(s),getz(s), BH['mass'][i], BH['r'][i], float(starmass), float(gasmass), float(virialmass)] 
        
        

    data= str(data)
    data= data[1:-1]
    f.write(data+'\n')
    
    print data

f.close()

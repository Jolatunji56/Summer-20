
import pynbody
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np

#Loads snapshot
s = pynbody.load ('/data/h258/stampedetesting/glenna/h258.cosmo50cmb.3072gst1bwdK1BH.000128')

#Put the units in the right way
s.physical_units()

#initiates a halo catalogue object for the given snapshot
h = s.halos()

#print len(h) #__ Returns the number of halo in snapshot


#Function for finding BH
def findBH(s):
    """A function that returns particles whose property is less than max, Returns the len of BHs."""
    BH = s.stars[(pynbody.filt.LowPass('tform',0.0))]
    return BH

def findBHhalos(s):
    """returns the index of host halos for each BHs"""
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos

BHhalos = findBHhalos(s)

current_halo = np.argsort(findBHhalos)


print current_halo


#prints BHs 
BH = findBH(s)



#prints BHs position
BH_position = BH['pos']


BH_ID = BH['iord']


#print h_ID



#print (type(BH_tform))


#print BH['mass']

#print(s.families(), s.loadable_keys,())

#print(BH)

#print(BH_position)

#print BHhalos

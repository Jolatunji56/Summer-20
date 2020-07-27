
import pynbody
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
    """returns the indexes (ID-number) of host halos for each BHs"""
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos

def gettime(s):
    Time = pynbody.analysis.cosmology.age(s)
    return Time

BH = findBH(s)
BHhalos = findBHhalos(s)
Time = gettime(s)

# sorts BHhalos and returns ordered indices
currenthalo = np.argsort(BHhalos)
#print currenthalo


#print "value of currentHalo is ", currenthalo
#print "value of BHhalos is", BHhalos


#prints BHs id (iord is a loadable key for BHs id) 
BH_ID = BH['iord']

#created empty list to append variable in them in other to make a dictionary for table
Sorted_Indx = []
BHs_ID = []
Halo_ID = []
Distance_cnt = []
BHs_mass = []
Starmass = []
Gasmass = []
Virialmass =[]


for i in currenthalo:

    thishalo = BHhalos[i] # [i] is every element of the indicies sort (currenthalo) for BHhalos ID
    #print thishalo, i #prints BHhalos ID alonside thier index


    #puts the galaxy(halo)in the center of the simulation for analysis
    pynbody.analysis.angmom.faceon(h[thishalo])

    #passing in position key and slicing values for each co-ordinates
    BH_position = BH['pos']

    BHx = BH_position[[i],0] #prints all x_positions for BHs

    BHy = BH_position[[i],1] #prints all y_positions for BHs

    BHz = BH_position[[i],2] #prints all z_positions for BHs

    #locationg distance from center(cnt), using the distance formula
    Dist_cnt = (((BHx **2) + (BHy ** 2) + (BHz ** 2)) ** 0.5) #taking center position (intial postion x1,y1,z1) to be (0,0,0)

    #removes bracket since it's a 1-dim array
    Dist_cnt = Dist_cnt[0]

    starmass = h[currenthalo].s['mass']
    print starmass
    gasmass = h[currenthalo].g['mass'].sum()
    virialmass = starmass+gasmass+h[currenthalo].d['mass'].sum()


    
    #print Dist_cnt
    
    Sorted_Indx.append(i)
    BHs_ID.append(BH['iord'][i])
    Halo_ID.append(thishalo)
    Distance_cnt.append(Dist_cnt)
    BHs_mass.append(BH['mass'][i])
    Get_t.append(gettime(s))
    Starmass.append(starmass)
    Gasmass.append(gasmass)
    Virialmass.append(virialmass)

    


data = {'Sorted_Indx':Sorted_Indx, 'BHs_ID':BHs_ID,'Halo_ID':Halo_ID,'Distance_cnt(kpc)':Distance_cnt, 'BHs_mass(Msol)':BHs_mass, 'star_mass':float(Starmass), 'gas_mass':float(Gasmass), 'virial_mass':float(Virialmass)}

#print(data)


df = pd.DataFrame(data)
#print(df)

#df.to_csv('/home/josh/Research-F19/Summer-20/BHs_data_file.csv')










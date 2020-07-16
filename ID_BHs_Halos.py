
import pynbody
import matplotlib
matplotlib.use('agg')
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

BH = findBH(s)
BHhalos = findBHhalos(s)


currenthalo = np.argsort(BHhalos)
#print BHhalos[currenthalo]

#prints BHs id (iord is a loadable key for BHs id) 
BH_ID = BH['iord']
BH_ID = BH['iord']
Iden_num = []
BHs_ID = []
Halo_ID = []
Distance_cnt = []
BHs_mass = []

print len(currenthalo)


for i in currenthalo:

    currenthalo = BHhalos [i]
    #print currenthalo
   # print (i)  #prints identity number of BH

    pynbody.analysis.angmom.faceon(h[currenthalo])

    BH_position = BH['pos']

    BHx = BH['pos'][tuple([i],0)] #prints all x_positions for BHs

    BHy = BH['pos'][tuple([i],1)] #prints all y_positions for BHs

    BHz = BH['pos'][tuple([i],2)] #prints all z_positions for BHs

    #locationg distance from center(cnt), using the distance formula
    Dist_cnt = (((BHx **2) + (BHy ** 2) + (BHz ** 2)) ** 0.5) #taking center position (intial postion x1,y1,z1) to be (0,0,0)


    Iden_num.append(i)
    BHs_ID.append(BH['iord'][i])
    Halo_ID.append(currenthalo)
    Distance_cnt.append(Dist_cnt)
    BHs_mass.append(BH['mass'][i])

    


data = {'Iden_num':Iden_num, 'BHs_ID':BHs_ID,'Halo_ID':Halo_ID,'Distance_cnt(kpc)':Distance_cnt, 'BHs_mass(Msol)':BHs_mass}

#print(data)

df = pd.DataFrame(data)

df.to_csv('/home/josh/Research-F19/Summer-20/BHs_data_file.csv')

print(df)










    

    






#print (BH_position)
#print (BH_x)
#print Dist_cnt.type()




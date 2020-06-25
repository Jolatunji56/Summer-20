

import pynbody
import matplotlib as plt

#Loads snapshot
s = pynbody.load ('/data/h258/stampedetesting/glenna/h258.cosmo50cmb.3072gst1bwdK1BH.000040')

#Put the units in the right way
s.physical_units()

#initiates a halo catalogue object for the given snapshot
h = s.halos()

#Function for finding BH
def findBH(s):
    """A function that returns particles whose property is less than max """
    BH = s.stars[(pynbody.filt.LowPass('tform',0.0))]
    return BH
BH = findBH(s)
BH_position = BH['pos']
print BH['mass']
print(s.families(), s.loadable_keys,())
print (BH)
print(BH_position)

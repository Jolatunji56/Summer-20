
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

#Function for finding BH
def findBH(s):
    """A function that returns particles whose property is less than max """
    BH = s.stars[(pynbody.filt.LowPass('tform',0.0))]
    return BH

#prints BHs 
BH = findBH(s)

#prints BHs position
BH_position = BH['pos']

# Assigned var for time formed for each BHS
BH_tform= BH['tform']*(-1) #___ multiplied by (-1) to make sense of reality and give positive time, because simulation returns the time formed for BHs as ngative

BH_ID = BH['iord']

#print (type(BH_tform))

t_form = np.array([BH_tform])

print (t_form)
plt.hist(t_form, bins='auto')
plt.show()
plt.title('Histogram plot for BHs formation time')
plt.xlabel('Formation time of BHs')
plt.ylabel('Frequency')

#plt.savefig("BHist.png")

#print BH['mass']

#print(s.families(), s.loadable_keys,())

#print(BH)

#print(BH_position)



from eeg_microstates13 import *



filename=[]
filename1 = ["data_Subject00_1_1.edf","data_Subject01_1_1.edf","data_Subject02_1_1.edf","data_Subject03_1_1.edf","data_Subject04_1_1.edf","data_Subject05_1_1.edf","data_Subject06_1_1.edf","data_Subject07_1_1.edf","data_Subject08_1_1.edf","data_Subject09_1_1.edf","data_Subject10_1_1.edf","data_Subject11_1_1.edf","data_Subject12_1_1.edf","data_Subject13_1_1.edf","data_Subject14_1_1.edf","data_Subject15_1_1.edf","data_Subject16_1_1.edf","data_Subject17_1_1.edf","data_Subject18_1_1.edf","data_Subject19_1_1.edf","data_Subject20_1_1.edf","data_Subject21_1_1.edf","data_Subject22_1_1.edf","data_Subject23_1_1.edf","data_Subject24_1_1.edf","data_Subject25_1_1.edf","data_Subject26_1_1.edf","data_Subject27_1_1.edf","data_Subject28_1_1.edf","data_Subject29_1_1.edf","data_Subject30_1_1.edf"]
filename2 = ["data_Subject00_1_2.edf","data_Subject01_1_2.edf","data_Subject02_1_2.edf","data_Subject03_1_2.edf","data_Subject04_1_2.edf","data_Subject05_1_2.edf","data_Subject06_1_2.edf","data_Subject07_1_2.edf","data_Subject08_1_2.edf","data_Subject09_1_2.edf","data_Subject10_1_2.edf","data_Subject11_1_2.edf","data_Subject12_1_2.edf","data_Subject13_1_2.edf","data_Subject14_1_2.edf","data_Subject15_1_2.edf","data_Subject16_1_2.edf","data_Subject17_1_2.edf","data_Subject18_1_2.edf","data_Subject19_1_2.edf","data_Subject20_1_2.edf","data_Subject21_1_2.edf","data_Subject22_1_2.edf","data_Subject23_1_2.edf","data_Subject24_1_2.edf","data_Subject25_1_2.edf","data_Subject26_1_2.edf","data_Subject27_1_2.edf","data_Subject28_1_2.edf","data_Subject29_1_2.edf","data_Subject30_1_2.edf"]
filename3 = ["data_Subject00_1_3.edf","data_Subject01_1_3.edf","data_Subject02_1_3.edf","data_Subject03_1_3.edf","data_Subject04_1_3.edf","data_Subject05_1_3.edf","data_Subject06_1_3.edf","data_Subject07_1_3.edf","data_Subject08_1_3.edf","data_Subject09_1_3.edf","data_Subject10_1_3.edf","data_Subject11_1_3.edf","data_Subject12_1_3.edf","data_Subject13_1_3.edf","data_Subject14_1_3.edf","data_Subject15_1_3.edf","data_Subject16_1_3.edf","data_Subject17_1_3.edf","data_Subject18_1_3.edf","data_Subject19_1_3.edf","data_Subject20_1_3.edf","data_Subject21_1_3.edf","data_Subject22_1_3.edf","data_Subject23_1_3.edf","data_Subject24_1_3.edf","data_Subject25_1_3.edf","data_Subject26_1_3.edf","data_Subject27_1_3.edf","data_Subject28_1_3.edf","data_Subject29_1_3.edf","data_Subject30_1_3.edf"]
filename4 = ["data_Subject00_1_4.edf","data_Subject01_1_4.edf","data_Subject02_1_4.edf","data_Subject03_1_4.edf","data_Subject04_1_4.edf","data_Subject05_1_4.edf","data_Subject06_1_4.edf","data_Subject07_1_4.edf","data_Subject08_1_4.edf","data_Subject09_1_4.edf","data_Subject10_1_4.edf","data_Subject11_1_4.edf","data_Subject12_1_4.edf","data_Subject13_1_4.edf","data_Subject14_1_4.edf","data_Subject15_1_4.edf","data_Subject16_1_4.edf","data_Subject17_1_4.edf","data_Subject18_1_4.edf","data_Subject19_1_4.edf","data_Subject20_1_4.edf","data_Subject21_1_4.edf","data_Subject22_1_4.edf","data_Subject23_1_4.edf","data_Subject24_1_4.edf","data_Subject25_1_4.edf","data_Subject26_1_4.edf","data_Subject27_1_4.edf","data_Subject28_1_4.edf","data_Subject29_1_4.edf","data_Subject30_1_4.edf"]
filename5 = ["data_Subject00_1_5.edf","data_Subject01_1_5.edf","data_Subject02_1_5.edf","data_Subject03_1_5.edf","data_Subject04_1_5.edf","data_Subject05_1_5.edf","data_Subject06_1_5.edf","data_Subject07_1_5.edf","data_Subject08_1_5.edf","data_Subject09_1_5.edf","data_Subject10_1_5.edf","data_Subject11_1_5.edf","data_Subject12_1_5.edf","data_Subject13_1_5.edf","data_Subject14_1_5.edf","data_Subject15_1_5.edf","data_Subject16_1_5.edf","data_Subject17_1_5.edf","data_Subject18_1_5.edf","data_Subject19_1_5.edf","data_Subject20_1_5.edf","data_Subject21_1_5.edf","data_Subject22_1_5.edf","data_Subject23_1_5.edf","data_Subject24_1_5.edf","data_Subject25_1_5.edf","data_Subject26_1_5.edf","data_Subject27_1_5.edf","data_Subject28_1_5.edf","data_Subject29_1_5.edf","data_Subject30_1_5.edf"]
filename6 = ["data_Subject00_1_6.edf","data_Subject01_1_6.edf","data_Subject02_1_6.edf","data_Subject03_1_6.edf","data_Subject04_1_6.edf","data_Subject05_1_6.edf","data_Subject06_1_6.edf","data_Subject07_1_6.edf","data_Subject08_1_6.edf","data_Subject09_1_6.edf","data_Subject10_1_6.edf","data_Subject11_1_6.edf","data_Subject12_1_6.edf","data_Subject13_1_6.edf","data_Subject14_1_6.edf","data_Subject15_1_6.edf","data_Subject16_1_6.edf","data_Subject17_1_6.edf","data_Subject18_1_6.edf","data_Subject19_1_6.edf","data_Subject20_1_6.edf","data_Subject21_1_6.edf","data_Subject22_1_6.edf","data_Subject23_1_6.edf","data_Subject24_1_6.edf","data_Subject25_1_6.edf","data_Subject26_1_6.edf","data_Subject27_1_6.edf","data_Subject28_1_6.edf","data_Subject29_1_6.edf","data_Subject30_1_6.edf"]
filename7 = ["data_Subject00_1_7.edf","data_Subject01_1_7.edf","data_Subject02_1_7.edf","data_Subject03_1_7.edf","data_Subject04_1_7.edf","data_Subject05_1_7.edf","data_Subject06_1_7.edf","data_Subject07_1_7.edf","data_Subject08_1_7.edf","data_Subject09_1_7.edf","data_Subject10_1_7.edf","data_Subject11_1_7.edf","data_Subject12_1_7.edf","data_Subject13_1_7.edf","data_Subject14_1_7.edf","data_Subject15_1_7.edf","data_Subject16_1_7.edf","data_Subject17_1_7.edf","data_Subject18_1_7.edf","data_Subject19_1_7.edf","data_Subject20_1_7.edf","data_Subject21_1_7.edf","data_Subject22_1_7.edf","data_Subject23_1_7.edf","data_Subject24_1_7.edf","data_Subject25_1_7.edf","data_Subject26_1_7.edf","data_Subject27_1_7.edf","data_Subject28_1_7.edf","data_Subject29_1_7.edf","data_Subject30_1_7.edf"]
filename8 = ["data_Subject00_1_8.edf","data_Subject01_1_8.edf","data_Subject02_1_8.edf","data_Subject03_1_8.edf","data_Subject04_1_8.edf","data_Subject05_1_8.edf","data_Subject06_1_8.edf","data_Subject07_1_8.edf","data_Subject08_1_8.edf","data_Subject09_1_8.edf","data_Subject10_1_8.edf","data_Subject11_1_8.edf","data_Subject12_1_8.edf","data_Subject13_1_8.edf","data_Subject14_1_8.edf","data_Subject15_1_8.edf","data_Subject16_1_8.edf","data_Subject17_1_8.edf","data_Subject18_1_8.edf","data_Subject19_1_8.edf","data_Subject20_1_8.edf","data_Subject21_1_8.edf","data_Subject22_1_8.edf","data_Subject23_1_8.edf","data_Subject24_1_8.edf","data_Subject25_1_8.edf","data_Subject26_1_8.edf","data_Subject27_1_8.edf","data_Subject28_1_8.edf","data_Subject29_1_8.edf","data_Subject30_1_8.edf"]


filename.append(filename1)
filename.append(filename2)
filename.append(filename3)
filename.append(filename4)
filename.append(filename5)
filename.append(filename6)
filename.append(filename7)
filename.append(filename8)


mbappe=np.array([])
arr =np.array([])  
datasto =np.array([])
L_individual =np.array([],dtype='i')  
L_group=np.array([],dtype='i')  
for i in range(2):
    
    for j in range(30):
        chs, fs, data_raw = read_edf(filename[i][j])
        data = bp_filter(data_raw, f_lo=1, f_hi=35, fs=fs)
        data_norm = data - data.mean(axis=1, keepdims=True)
        data_norm /= data_norm.std(axis=1, keepdims=True)
        datasto=np.append(datasto,data_norm)
        # --- GFP peaks ---
        gfp = np.nanstd(data, axis=1)
        gfp2 = np.sum(gfp**2) # normalizing constant
        gfp_peaks = locmax(gfp)
            # GFP peaks
        gfp_values = gfp[gfp_peaks]

t_ = np.arange(100)
fig, ax = plt.subplots(2, 1, figsize=(15,4), sharex=True)
z=[]
a=[]
y=[]
j=[]

ayut=[]      
cm = plt.cm.seismic
fig, axarr = plt.subplots()
fig, axarr = plt.subplots(1, 2, figsize=(20,5))
# importing matplot lib
import matplotlib.pyplot as plt
import numpy as np
 
# importing movie py libraries
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
 
# numpy array
x = np.linspace(-2, 2, 200)
 
# duration of the video
duration = 20
u=1

 
# method to get frames
def make_frame(t):
            # clear
            # clear
            
            ayut.append(t)
            
            axarr[0].imshow(eeg2map(data_norm[int(t), :]), cmap=cm, origin='lower')
            axarr[1].plot(t_[0:duration],gfp[0:duration],'b', lw=2)
            axarr[1].plot(t_[int(t)],gfp[int(t)],'r', lw=2)
            plt.xlabel("time", fontsize=20, fontweight="bold")
            plt.ylabel("GFP(standard deviation)", fontsize=20, fontweight="bold")
                        # returning mumpy image
            return mplfig_to_npimage(fig)
 
# creating animation
animation = VideoClip(make_frame, duration = duration)
 
# displaying animation with auto play and looping
animation.ipython_display(fps = 1, loop = True, autoplay = True)


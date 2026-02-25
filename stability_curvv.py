# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# variables
freq = 44100
re_list1 = [] # list to store reynold's numbers
rms_list = [] # list to store rms values
energy_ratio_list = [] # list to store the energy ratios    

# we introduce a target band in this, which is basically looking for a specific spike
target_band = [220, 250] 

# dict for reynold's number
re_map = {
    15: 1565.85, 20: 2087.80, 25: 2609.75, 30: 3131.70,
    35: 3653.65, 40: 4175.60, 43: 4488.77, 45: 4697.55,
    47: 4906.33, 50: 5219.50, 53: 5532.67
}

# now we open each file in for loop
for file_num, reyn in re_map.items():
    
    # declare the file name
    filename = str(file_num) + ".xlsx"

    # read the data
    df1 = pd.read_excel(filename, header=None)

    # here we use iloc ( integer location)
    # it just grabs data taking row and column number and params
    signal = df1.iloc[:, 0].to_numpy()

    # calcualte the rms 
    rms_vals = np.sqrt(np.mean(signal**2))

    # calculate the power spectrum
    freqs, psd = welch(signal, fs=freq, nperseg=4096)
    
    # now we calculate the energy ratio
    # we find the indices for our target band
    idx_band = np.where((freqs >= target_band[0]) & (freqs <= target_band[1])) # no.where just looks for specific numbers

    # sum of energy in the band:
    energy_in_band = np.sum(psd[idx_band])

    # we have to avoid the high freq noise so we take the sum upto 500Hz
    idx_total = np.where(freqs <= 500)
    total_energy = np.sum(psd[idx_total])

    # we calculate the energy ratio
    ratio = energy_in_band/ total_energy

    # now we store all the values
    re_list1.append(reyn)
    rms_list.append(rms_vals)
    energy_ratio_list.append(ratio)

    
# now we plot the curvv
plt.figure(figsize=(10, 6))

# plot energy v/s reynold's number
plt.plot(re_list1, energy_ratio_list, '-o', linewidth=2, color='red')

plt.title("Stability Curve: Onset of Thermoacoustic Instability")
plt.xlabel("Reynolds Number")
plt.ylabel("Energy Ratio (200-280 Hz / Total)")
plt.grid(True)

# Add a text label pointing to the jump
plt.annotate('Onset of TAI', xy=(3653, 0.05), xytext=(2500, 0.2),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.show()

"""
The energy ratio should be around 0.05 to 0.5
any ratio around 0.9 or around 1 is just basically 
TAI in disguise
"""
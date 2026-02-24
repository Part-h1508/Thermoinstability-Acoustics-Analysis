# imports 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# varaibles
Freq = 44100
sampling_freq = 1/Freq


# declaring a dict for reynolds number
re_map = {
    15: 1565.85, 
    20: 2087.80, 
    25: 2609.75, 
    30: 3131.70,
    35: 3653.65, 
    40: 4175.60, 
    43: 4488.77, 
    45: 4697.55,
    47: 4906.33, 
    50: 5219.50, 
    53: 5532.67
}

# now we loop thru every number in the 
# given reynold's number dict

for file_num, reyn in re_map.items():
    file_name = str(file_num) + ".xlsx"

    # now we open the file using pandas
    df1 = pd.read_excel(file_name, header=None, names=['Amplitude']) # defining the data frame

    # now we extract the signal from the dataframe
    signal = df1['Amplitude'].to_numpy()

    # now we calculate the frequency spectrum 
    # nperseg = 4096 gives highest resolution
    freqs, psd = welch(signal, fs=Freq, nperseg=4096)

    # now we plot it using log scale.
    plt.semilogy(freqs, psd, label=f"Re: {reyn}")

# formatting the graph
plt.title("Frequency Spectrum Waterfall")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power Spectral Density")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') # moves legend outside to keep graph clean
plt.xlim(0, 500) # zoom in on the low frequencies where TAI lives
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.tight_layout()
plt.show()

"""

from the graph we can tell that:
1) The dark blue line at bottom is flat and low, its background nose which is just flame burning 
2) the orange, red, red green lines are entering the transition mode as the Re is increased
3) the top lines (Cyan) is a screaming image of the last tone, which is TAI frequency


upon examining, the frequency indiacting the onset of TAI is between 230-240Hz
235 to be prescise

If we look closely, there is another peak at around 460Hz indicating harmonic frequency
which is valid with the primary one (230x2 = 460)
"""

# imports 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# variables
Freq = 44100
# we only need to compare the two extremes to see the difference
target_files = [15, 53]

# declaring a dict for reynolds number
re_map = {
    15: 1565.85, 
    53: 5532.67
}

# determine a fig size
plt.figure(figsize=(12, 6))

# now we dig thru the our target files
for i, file_num in enumerate(target_files):
    # set the file name
    filename = str(file_num) + ".xlsx"
    
    # open the data frame
    df = pd.read_excel(filename, header=None)

    # we look for target values in our opened files
    signal = df.iloc[:, 0].to_numpy()
    
    # we normalize the signal
    signal = signal - np.mean(signal)
    
    # now we calculate the autocorr map
    # "mode='full'" compares the signal to itself at every possible time shift
    result = np.correlate(signal, signal, mode='full')
    
    # keep only the positive lags (the second half of the array)
    result = result[result.size // 2:]
    
    # normalize so the peak at Lag 0 is always 1.0 (100% correlation)
    result = result / result[0]
    
    # now we create a time lag vector 
    # we want to see the first 0.1 seconds of memory
    lags = np.arange(len(result))
    time_lags = lags / Freq
    
    # plotting the graph
    plt.subplot(1, 2, i+1)
    
    # we only plot the first 0.05 seconds (approx 2200 points)
    # otherwise the waves get too squished to see
    zoom_points = int(0.05 * Freq)
    
    plt.plot(time_lags[:zoom_points], result[:zoom_points], linewidth=2)
    
    # Formatting
    plt.title(f"Re: {re_map[file_num]}")
    plt.xlabel("Time Lag (seconds)")
    plt.ylabel("Correlation Coefficient")
    plt.ylim(-1.1, 1.1) # Correlation is always between -1 and 1
    plt.grid(True)
    
    # Add a reference line at 0 
    plt.axhline(0, color='black', linewidth=1, linestyle='--')

plt.suptitle("Autocorrelation", fontsize=16)
plt.tight_layout()
plt.show()
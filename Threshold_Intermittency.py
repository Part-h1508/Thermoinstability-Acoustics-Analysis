# imports 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# variables
Freq = 44100
re_list = []
theta_values = []

# dict for reynold's number
re_map = {
    15: 1565.85, 20: 2087.80, 25: 2609.75, 30: 3131.70,
    35: 3653.65, 40: 4175.60, 43: 4488.77, 45: 4697.55,
    47: 4906.33, 50: 5219.50, 53: 5532.67
}

# --- STEP 1: SET THE THRESHOLD ---
# We use the Laminar file (15) to set our baseline "quiet" level
df_quiet = pd.read_excel("15.xlsx", header=None)
quiet_signal = df_quiet.iloc[:, 0].to_numpy()
threshold = 3 * np.std(quiet_signal) # Common threshold: 3x Standard Deviation

# now we loop thru all files to calculate Capital Theta
for file_num, reyn in re_map.items():
    filename = str(file_num) + ".xlsx"
    df = pd.read_excel(filename, header=None)
    signal = df.iloc[:, 0].to_numpy()
    
    # --- STEP 2: APPLY THE FORMULA (Ni / N) ---
    # Ni = Number of points where absolute pressure > threshold
    Ni = np.sum(np.abs(signal) > threshold)
    N = len(signal)
    
    capital_theta = Ni / N
    
    # store values
    re_list.append(reyn)
    theta_values.append(capital_theta)

# now we plot Theta v/s Reynolds number
plt.figure(figsize=(10, 6))
plt.plot(re_list, theta_values, '-s', color='green', linewidth=2)

plt.title("Threshold Intermittency (Theta) vs Reynolds Number")
plt.xlabel("Reynolds Number")
plt.ylabel("Theta (Ni / N)")
plt.grid(True, alpha=0.3)
plt.show()

"""
ACCORDING TO YI AND GUTMARK:
1) If Theta is near 0: The flame is stable/laminar.
2) If Theta is between 0.2 and 0.8: The flame is intermittent (bursting).
3) If Theta is near 1: The flame is in full TAI.
"""
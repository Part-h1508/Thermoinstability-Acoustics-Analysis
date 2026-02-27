import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# variables
Freq = 44100

# re mapping based on your file list
# instructions from Prof. De: Show Re as the operating condition
re_map = {
    15: 1565.85, 20: 2087.80, 25: 2609.75, 30: 3131.70, 
    35: 3653.65, 40: 4175.60, 43: 4488.77, 45: 4697.55, 
    47: 4906.33, 50: 5219.50, 53: 5532.67
}

# Using the stable Re: 1565.85 case as the noise reference
baseline_df = pd.read_excel("15.xlsx", header=None)
baseline_signal = baseline_df.iloc[:, 0].to_numpy()
std_baseline = np.std(baseline_signal)

# TAI Threshold: 3 times the standard deviation
threshold_tai = 2.4* std_baseline    

re_list = []
theta_list = []

# process files in order
for file_num in sorted(re_map.keys()):
    re_val = re_map[file_num]
    filename = f"{file_num}.xlsx"
    
    df = pd.read_excel(filename, header=None)
    signal = df.iloc[:, 0].to_numpy()
    
    # calculate Theta (Ni/N)
    # ni is the number of points exceeding the 3-sigma threshold
    ni = np.sum(np.abs(signal) > threshold_tai)
    theta = ni / len(signal)
    
    re_list.append(re_val)
    theta_list.append(theta)
    # print(f"Re: {re_val:.2f} | Theta: {theta:.6f}")

# plotting
plt.figure(figsize=(10, 6))
plt.plot(re_list, theta_list, 'ro-', linewidth=1.5, markersize=6)

plt.title("Theta (Θ) vs Reynolds Number (TAI)")
plt.xlabel("Reynolds Number (Re)")
plt.ylabel("Theta (Θ)")
plt.grid(True, alpha=0.3)

# Highlight transition per your previous stability curves
plt.annotate('Onset of TAI', xy=(4175, 0.01), xytext=(3000, 0.05),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1))

plt.tight_layout()
plt.show()
# Thermoacoustic Instability (TAI) Analysis Suite
This repository contains a Python-based analysis suite for identifying the onset of **Thermoacoustic Instability (TAI)** 
in a combustion system. Using acoustic pressure data across varying **Reynolds Numbers (Re)**, this project maps the 
transition from stable laminar combustion to self-sustained periodic oscillations.

## 📊 Repository Structure
The following scripts handle the end-to-end signal processing and visualization:
* **`Freq_finder.py`**: Utilizes Power Spectral Density (PSD) to identify the dominant "scream" frequency at **~235 Hz**.
* **`stability_curvv.py`**: Calculates the **Energy Ratio** (Target Band / Total Energy) to visualize the S-Curve of stability across Reynolds numbers.
* **`pdf_analysis.py`**: Compares the Probability Density Function (PDF) of the signal against a Gaussian distribution to prove the transition from noise to a sine wave.
* **`auto_corr.py`**: Measures the system "memory," showing the shift from rapid decay (laminar) to eternal oscillation (TAI).
* **`phase_space.py`**: Reconstructs the system's phase space to visualize the emergence of a **Limit Cycle (Donut Plot)** at high Reynolds numbers.


## 📈 Key Analysis Results


### 1. Frequency Transition
The system exhibits background noise at low Reynolds numbers. As $Re$ increases, a dominant peak emerges at **235 Hz**, 
with a secondary harmonic at **460 Hz** (2x frequency), confirming periodic resonance.

### 2. The Stability Jump
The stability curve reveals a bifurcation point. Beyond $Re \approx 4000$, the acoustic energy shifts from being distributed 
across many frequencies to being concentrated almost entirely in the instability band.

### 3. Limit Cycle Dynamics
PDF and Phase Space analysis confirm the onset of TAI. While laminar flow ($Re: 1565$) appears as a stochastic "fuzzy ball," 
the TAI state ($Re: 5532$) forms a structured "donut," indicating deterministic, periodic behavior.


## 🛠️ Setup & Data
* **Requirements**: Python 3.x, NumPy, Pandas, Matplotlib, SciPy.
* **Data**: The analysis is performed on raw Excel data files (e.g., `15.xlsx` through `53.xlsx`), sampled at **44,100 Hz**.

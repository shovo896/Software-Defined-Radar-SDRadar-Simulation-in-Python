#  Software-Defined Radar (SDRadar) Simulation in Python

This project simulates a basic radar system entirely in software using Python. It uses signal processing techniques such as pulse generation, matched filtering, and Doppler shift analysis to estimate the  distance and **velocity of a virtual target.



##  Features

-  Chirp signal generation
-  Target echo simulation with configurable distance and speed
-  Doppler shift and delay-based signal processing
- Real-time visualization of transmitted/received signals
-  Accurate distance and velocity estimation



## Technologies Used

- Python 3.x
- NumPy
- Matplotlib
- Signal processing techniques: FFT, correlation, time delay, Doppler effect



###  Installation

1. Clone this repository:

bash
git clone https://github.com/shovo896/sdradar-simulation.git
cd sdradar-simulation

pip install numpy matplotlib
python main.py
The console will output the estimated distance and velocity. Matplotlib will show a visual comparison of the transmitted and received signals.

 How It Works
Transmitter: Generates a chirp signal (linear frequency modulation).

Target: Simulates object reflection with time delay and Doppler shift.

Receiver: Processes the echo to estimate:

Distance from time delay

Velocity from frequency shift

Visualization: Plots both signals and displays estimates.

Estimated Distance: 99.85 meters
Estimated Velocity: 29.97 m/s


 Educational Value
This project is ideal for students learning:

Radar systems & signal theory

Doppler effect in remote sensing

Python signal processing with NumPy

Software-defined simulations for embedded systems

 Future Improvements
Add multiple targets with varying speeds

Noise modeling (e.g., AWGN)

Range-Doppler heatmap

Real-time GUI using PyQt5locity: 29.97 m/s



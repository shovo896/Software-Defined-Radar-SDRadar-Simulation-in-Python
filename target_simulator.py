import numpy as np

C = 3e8  # Speed of light

def simulate_echo(tx, t, target_distance=100, target_velocity=30, fs=10e3):
    delay = 2 * target_distance / C
    doppler_shift = 2 * target_velocity / C * fs

    delay_samples = int(delay * fs)
    echo = np.roll(tx, delay_samples)
    echo *= np.cos(2 * np.pi * doppler_shift * t)  # Apply Doppler shift

    return echo

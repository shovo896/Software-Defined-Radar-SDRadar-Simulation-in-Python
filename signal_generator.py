import numpy as np

def generate_chirp(fs=10e3, T=1e-3, f0=1e3, f1=2e3):
    t = np.arange(0, T, 1/fs)
    chirp = np.cos(2 * np.pi * ((f1 - f0) / (2 * T) * t**2 + f0 * t))
    return chirp, t

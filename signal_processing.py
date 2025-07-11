import numpy as np

def estimate_distance_velocity(tx, rx, fs=10e3):
    correlation = np.correlate(rx, tx, mode='full')
    delay_samples = np.argmax(correlation) - len(tx) + 1
    distance = (delay_samples / fs) * 3e8 / 2

    # Doppler estimation (FFT-based)
    fft_rx = np.fft.fft(rx)
    fft_tx = np.fft.fft(tx)
    freq_shift = np.argmax(np.abs(fft_rx - fft_tx))
    velocity = (freq_shift * 3e8) / (2 * fs)

    return distance, velocity

import matplotlib.pyplot as plt


def plot_results(tx, rx, distance, velocity):
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.title("Transmitted and Received Signal")
    plt.plot(tx, label='Tx')
    plt.plot(rx, label='Rx', alpha=0.7)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.title(f"Estimated Distance: {distance:.2f} m | Velocity: {velocity:.2f} m/s")
    plt.bar(['Distance (m)', 'Velocity (m/s)'], [distance, velocity])

    plt.tight_layout()
    plt.show()

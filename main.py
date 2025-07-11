from signal_generator import generate_chirp  #main generator file
from target_simulator import simulate_echo
from signal_processing import estimate_distance_velocity
from visualization import plot_results

# 1. Generate radar pulse (chirp)
tx_signal, t = generate_chirp()

# 2. Simulate moving target
rx_signal = simulate_echo(tx_signal, t, target_distance=100, target_velocity=30)

# 3. Process signals
distance, velocity = estimate_distance_velocity(tx_signal, rx_signal)

# 4. Visualize results
plot_results(tx_signal, rx_signal, distance, velocity)



# import ngspice
# import pyspice as sp

# # Create a new circuit
# circuit = sp.Circuit('Example Circuit')

# # Add components to the circuit
# circuit.R1 = sp.Resistor(1, '1', '2')  # Resistor R1 with 1 ohm resistance between nodes 1 and 2
# circuit.V1 = sp.VoltageSource('1', '2', 'DC', 10)  # Voltage source V1 with 10 volts DC between nodes 1 and 2
# circuit.R2 = sp.Resistor(2, '2', '0')  # Resistor R2 with 2 ohms resistance between nodes 2 and 0 (ground)

# # Create an NGSpice simulation
# sim = ngspice.Ngspice()
# sim.load(circuit)

# simulator = circuit.simulator(temperature=25, nominal_temperature=25, simulator='ngspice-shared', simulator_args=['-b'])

# # Access simulation results
# v1_voltage = sim.get_node_voltage('1')
# v2_voltage = sim.get_node_voltage('2')
# i_r1 = sim.get_branch_current('R1')

# # Print the results
# print("Voltage at node 1:", v1_voltage)
# print("Voltage at node 2:", v2_voltage)
# print("Current through R1:", i_r1)


import numpy as np
import  matplotlib.pyplot as plt

# Rc Circuit parameters
R = 100.0
C = 100.0e-6
v_source = 5.0
dt = 1.0e-6
t_end = 0.1

times = np.arange(0, t_end, dt)

v_c = np.zeros_like(times)

for i in range(1, len(times)):
    v_c[i] = v_source * (1- np.exp(-times[i]/(R*C)))
idx_6321 = np.abs(v_c - 0.6321 * v_source).argmin()
time_6321 = times[idx_6321]

idx_99 = np.abs(v_c - 0.99 * v_source).argmin()
time_99 = times[idx_99]

plt.plot(times, v_c, label='Capacitor Voltage')

plt.scatter(time_6321, v_c[idx_6321],  label='63.21% of Vsource', color='blue')

plt.annotate(f"{time_6321:.6f} s", (time_6321, v_c[idx_6321]), textcoords="offset points", xytext=(0,-20), ha = 'center')

plt.xlabel('Time(s)')
plt.ylabel('Capacitor Voltage(V)')
plt.title('RC Circuit Charging')
plt.legend()
plt.grid(True)
plt.show()
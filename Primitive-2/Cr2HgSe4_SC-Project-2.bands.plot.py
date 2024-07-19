import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"
plt.rcParams["figure.figsize"]=(8, 6)

# load data
data = np.loadtxt('Cr2HgSe4_SC-Project-2.bands.out.dat.gnu')

k = np.unique(data[:, 0])
bands = np.reshape(data[:, 1], (-1, len(k)))

for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, alpha=0.5, color='k')
plt.xlim(min(k), max(k))

# Fermi energy
plt.axhline(8.0051, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)

# High symmetry k-points (new coordinates)
high_symmetry_points = [0.0000, 1.2247, 1.8371, 2.3371, 3.3978, 4.0101, 4.4432, 5.8351, 6.8351, 7.7011]
for point in high_symmetry_points:
    plt.axvline(point, linewidth=0.75, color='k', alpha=0.5)

# text labels
plt.xticks(ticks= high_symmetry_points, 
           labels=['$\Gamma$', 'L', 'K', 'X', 'W', 'U', 'V', 'Y', 'Z', '$\Gamma$'])
plt.ylim(-10,24)
plt.ylabel("Energy (eV)")
plt.text(2.3, 5.6, 'Fermi energy', fontsize='small')

# Save the figure as a PDF
plt.savefig('band_structure.pdf', format='pdf')

plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Load data and ignore lines with "*******" or starting with "#"
def data_loader(fname):
    energy = []
    pdos = []
    with open(fname, 'r') as file:
        for line in file:
            if "*******" not in line and not line.startswith('#'):
                values = line.split()
                energy.append(float(values[0]))
                pdos.append(float(values[1]))
    return np.array(energy), np.array(pdos)

energy_Cr, pdos_Cr_d = data_loader('Cr2HgSe4_SC-Project-2.Cr-d.PDOS.dat')
energy_Hg, pdos_Hg_d = data_loader('Cr2HgSe4_SC-Project-2.Hg-d.PDOS.dat')
energy_tot, pdos_tot = data_loader('Cr2HgSe4-SC-SC-Project-2.DOS.dat')

# Find the minimum length among the energy arrays
min_length = min(len(energy_Cr), len(energy_Hg), len(energy_tot))

# Truncate arrays to the minimum length
energy_Cr = energy_Cr[:min_length]
pdos_Cr_d = pdos_Cr_d[:min_length]
energy_Hg = energy_Hg[:min_length]
pdos_Hg_d = pdos_Hg_d[:min_length]
energy_tot = energy_tot[:min_length]
pdos_tot = pdos_tot[:min_length]

# Make plots
plt.figure(figsize=(10, 6))

plt.plot(energy_Cr, pdos_Cr_d, linewidth=0.75, color='#FF6347', label='Cr d-orbital')
plt.plot(energy_Hg, pdos_Hg_d, linewidth=0.75, color='#4682B4', label='Hg d-orbital')
plt.plot(energy_tot, pdos_tot, linewidth=0.75, color='#2E8B57', label='Total DOS')

plt.xlabel('Energy (eV)')
plt.ylabel('DOS')
plt.axvline(x=0, linewidth=0.5, color='k', linestyle=(0, (8, 10)), label='Fermi energy')
plt.xlim(min(energy_Cr), max(energy_Cr))
plt.fill_between(energy_Cr, 0, pdos_Cr_d, where=(energy_Cr < 0), facecolor='#FF6347', alpha=0.25)
plt.fill_between(energy_Hg, 0, pdos_Hg_d, where=(energy_Hg < 0), facecolor='#4682B4', alpha=0.25)
plt.fill_between(energy_tot, 0, pdos_tot, where=(energy_tot < 0), facecolor='#2E8B57', alpha=0.25)

plt.legend(frameon=False)
plt.show()


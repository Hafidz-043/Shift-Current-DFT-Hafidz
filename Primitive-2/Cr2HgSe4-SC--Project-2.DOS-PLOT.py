import numpy as np
import matplotlib.pyplot as plt

# Memuat data dari file teks menggunakan np.loadtxt
filename = 'Cr2HgSe4-SC-SC-Project-2.DOS.dat'
data = np.loadtxt(filename)

# Memisahkan kolom-kolom dari data
energi = data[:, 0]
dosup = data[:, 1]  # DOS atas (dosup(E))
dosdw = data[:, 2]  # DOS bawah (dosdw(E))

# Menentukan energi minimum dan maksimum
energi_min = energi.min()
energi_max = energi.max()

# Menampilkan energi minimum dan maksimum
print(f'Energi minimum: {energi_min:.2f} eV')
print(f'Energi maksimum: {energi_max:.2f} eV')

# Nilai Fermi energy
efermi = 8.004

# Plotting DOS terhadap energi yang dikoreksi dengan nilai Fermi
plt.figure()
plt.plot(energi, dosup, label='dosup(E)', c='b')  # Plot DOS atas dengan warna biru
plt.plot(energi, dosdw, label='dosdw(E)', c='r')  # Plot DOS bawah dengan warna merah
plt.axvline(x=efermi, color='g', linestyle='--', label='Fermi Energy')  # Garis vertikal untuk Fermi energy (warna hijau)
plt.xlabel('E (eV)')
plt.ylabel('Density of States')
plt.title('Density of States')
plt.legend()
plt.grid(True)
plt.xlim(energi_min, energi_max)  # Batas sumbu x
plt.ylim(-10, max(dosup.max(), dosdw.max()) * 1.1)  # Batas sumbu y, tambahkan sedikit ruang di atas nilai maksimum DOS

# Menyimpan plot sebagai PDF
plt.savefig('Cr2HgSe4-DOS-Picture-1.pdf', format='pdf')

# Menampilkan plot
plt.show()

energi_min = energi.min()
energi_max = energi.max()
print(f'Energi minimum: {energi_min:.2f} eV')
print(f'Energi maksimum: {energi_max:.2f} eV')


import matplotlib.pyplot as plt
from scipy.stats import binom
from distribucion_binomial import distribucion_binomial
from distribucion_geometrica import distribucion_geometrica
from distribucion_poisson import distribucion_poisson


##### DISTRIBUCION BINOMIAL #####

# Crear una figura y ejes (subplots) dentro de ella
fig, ejes = plt.subplots(nrows=2, ncols=4, figsize=(12, 8))
ejes = ejes.flatten()

# Generar los diagramas de cajas y histogramas para cada muestra
tamanos = [100, 1000, 10000, 100000]

for i, tamano in enumerate(tamanos):
    distribucion_binomial(tamano, ejes[i], ejes[i + 4])

# Ajustar el espaciado entre los subplots y mostrar la figura
plt.tight_layout()
plt.show()

##### DISTRIBUCION GEOMETRICA #####

# Crear una figura y ejes (subplots) dentro de ella
fig, ejes = plt.subplots(nrows=2, ncols=4, figsize=(12, 8))
ejes = ejes.flatten()

# Generar los diagramas de cajas y histogramas para cada muestra
tamanos = [100, 1000, 10000, 100000]

for i, tamano in enumerate(tamanos):
    distribucion_geometrica(tamano, ejes[i], ejes[i + 4])

# Ajustar el espaciado entre los subplots y mostrar la figura
plt.tight_layout()
plt.show()

##### DISTRIBUCION POISSON #####

# Crear una figura y ejes (subplots) dentro de ella
fig, ejes = plt.subplots(nrows=2, ncols=4, figsize=(12, 8))
ejes = ejes.flatten()

# Generar los diagramas de cajas y histogramas para cada muestra
tamanos = [100, 1000, 10000, 100000]

for i, tamano in enumerate(tamanos):
    distribucion_poisson(tamano, ejes[i], ejes[i + 4])

# Ajustar el espaciado entre los subplots y mostrar la figura
plt.tight_layout()
plt.show()


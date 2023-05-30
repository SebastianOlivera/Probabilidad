import matplotlib.pyplot as plt
from distribucion_binomial import distribucion_binomial
from distribucion_geometrica import distribucion_geometrica
from distribucion_poisson import distribucion_poisson


##### DISTRIBUCION BINOMIAL #####

# Crear una figura y ejes (subplots) dentro de ella y Generar los diagramas de cajas y histogramas para cada muestra
fig, ejes = plt.subplots(nrows=2, ncols=4, figsize=(18, 8))
ejes = ejes.flatten()
tamanos = [100, 1000, 10000, 100000]

for i, tamano in enumerate(tamanos):
    distribucion_binomial(tamano, ejes[i], ejes[i + 4])

plt.tight_layout()
plt.show()

##### DISTRIBUCION GEOMETRICA #####

# Crear una figura y ejes (subplots) dentro de ella y Generar los diagramas de cajas y histogramas para cada muestra
fig, ejes = plt.subplots(nrows=2, ncols=4, figsize=(18, 8))
ejes = ejes.flatten()
tamanos = [100, 1000, 10000, 100000]

for i, tamano in enumerate(tamanos):
    distribucion_geometrica(tamano, ejes[i], ejes[i + 4])

plt.tight_layout()
plt.show()

##### DISTRIBUCION POISSON #####

# Crear una figura y ejes (subplots) dentro de ella y Generar los diagramas de cajas y histogramas para cada muestra
fig, ejes = plt.subplots(nrows=2, ncols=4, figsize=(18, 8))
ejes = ejes.flatten()
tamanos = [100, 1000, 10000, 100000]

for i, tamano in enumerate(tamanos):
    distribucion_poisson(tamano, ejes[i], ejes[i + 4])

plt.tight_layout()
plt.show()

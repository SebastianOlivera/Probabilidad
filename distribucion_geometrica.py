import matplotlib.pyplot as plt
from scipy.stats import geom


# Función para generar una muestra de la distribución geometrica y crear un diagrama de cajas e histograma

def distribucion_geometrica(size, eje_caja, eje_histograma):
    p = 0.08
    muestra = geom.rvs(p, size=size)

    # Crear el diagrama de cajas
    eje_caja.boxplot(muestra)
    eje_caja.set_xlabel('Distribución geometrica')
    eje_caja.set_ylabel('Valores')
    eje_caja.set_title('Diagrama de cajas - Muestra de tamaño {}'.format(size))
    eje_caja.grid(True)

    # Crear el histograma
    eje_histograma.hist(muestra, bins='auto', alpha=0.7)
    eje_histograma.set_xlabel('Número de éxitos')
    eje_histograma.set_ylabel('Frecuencia')
    eje_histograma.set_title('Histograma - Muestra de tamaño {}'.format(size))
    eje_histograma.grid(True)
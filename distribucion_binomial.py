import numpy as np
from scipy.stats import binom


# Función para generar una muestra de la distribución binomial y crear un diagrama de cajas e histograma


def distribucion_binomial(size, eje_caja, eje_histograma):
    p = 0.35
    n = 100
    muestra = binom.rvs(n, p, size=size)

    # Crear el diagrama de cajas
    eje_caja.boxplot(muestra)
    eje_caja.set_xlabel("Distribución Binomial")
    eje_caja.set_ylabel("Valores")
    eje_caja.set_title("Diagrama de cajas - Muestra de tamaño {}".format(size))
    eje_caja.grid(True)

    # Crear el histograma
    eje_histograma.hist(muestra, bins="auto", alpha=0.7)
    eje_histograma.set_xlabel("Número de éxitos")
    eje_histograma.set_ylabel("Frecuencia")
    eje_histograma.set_title("Histograma - Muestra de tamaño {}".format(size))
    eje_histograma.grid(True)

    # Calcular la mediana y la moda
    mediana = np.median(muestra)
    frecuencias = np.bincount(muestra)
    moda = np.argmax(frecuencias)

    # Calculara la media empirica y compararla con la esperanza teorica.
    media_empirica = np.mean(muestra)
    esperanza_teorica = n * p
    diferenciaMedia = abs(esperanza_teorica - media_empirica)

    # Calcular la varianza empírica y compararla con la varianza teórica
    varianza_empirica = np.var(muestra, ddof=1)
    varianza_teorica = n * p * (1 - p)
    diferenciaVarianza = abs(varianza_teorica - varianza_empirica)


    # Imprimir la mediana y la moda
    print("Muestra de tamaño {}:".format(size))
    print("Mediana Binomial:", mediana)
    print("Moda Binomial:", moda)
    print("Media empirica:", media_empirica)
    print("Esperanza teorica:", esperanza_teorica)
    print("Diferencia entre Media empirica y Esperanza teórica:", diferenciaMedia)
    print("Diferencia entre Varianza empírica y Varianza teórica:", diferenciaVarianza)
    print("-------------------------")

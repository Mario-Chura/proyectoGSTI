import ee

def clasificacion_kmeans(ndmi_img, lst_img, zona, n_clusters=4):
    # Combinar NDMI y LST en una sola imagen multibanda
    entrada = ndmi_img.addBands(lst_img)

    # Muestra de entrenamiento aleatoria
    entrenamiento = entrada.sample(
        region=zona,
        scale=30,
        numPixels=5000,
        seed=42
    )

    # Entrenamiento del modelo k-means
    clusterer = ee.Clusterer.wekaKMeans(n_clusters).train(entrenamiento)
    
    # Clasificar la imagen completa
    resultado = entrada.cluster(clusterer).clip(zona)
    return resultado

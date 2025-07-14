import ee

def clasificacion_kmeans(ndmi_img, lst_img, zona, n_clusters=4):
    entrada = ndmi_img.addBands(lst_img)

    entrenamiento = entrada.sample(
        region=zona,
        scale=30,
        numPixels=5000,
        seed=42
    )

    clusterer = ee.Clusterer.wekaKMeans(n_clusters).train(entrenamiento)
    
    resultado = entrada.cluster(clusterer).clip(zona)
    return resultado

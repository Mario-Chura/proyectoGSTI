import ee

def calcular_ndmi(zona, fecha_inicio='2023-01-01', fecha_fin='2023-12-31'):
    coleccion = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                 .filterBounds(zona)
                 .filterDate(fecha_inicio, fecha_fin)
                 .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
                 .map(lambda img: img.normalizedDifference(['B8', 'B11']).rename('NDMI')))
    
    return coleccion.median().clip(zona)

def contar_imagenes_ndmi(zona, inicio, fin):
    coleccion = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                 .filterBounds(zona)
                 .filterDate(inicio, fin)
                 .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)))
    return coleccion.size().getInfo()

def comparar_ndmi(zona, fecha_base_ini, fecha_base_fin, fecha_actual_ini, fecha_actual_fin):
    def ndmi_periodo(fecha_ini, fecha_fin):
        coleccion = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                     .filterBounds(zona)
                     .filterDate(fecha_ini, fecha_fin)
                     .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)))
        
        empty = coleccion.size().eq(0)
        ndmi = coleccion.map(lambda img: img.normalizedDifference(['B8', 'B11']).rename('NDMI'))
        imagen_valida = ndmi.median().clip(zona)
        imagen_nula = ee.Image(0).rename('NDMI').clip(zona)
        
        return ee.Image(ee.Algorithms.If(empty, imagen_nula, imagen_valida))

    ndmi_base = ndmi_periodo(fecha_base_ini, fecha_base_fin)
    ndmi_actual = ndmi_periodo(fecha_actual_ini, fecha_actual_fin)

    cambio_ndmi = ndmi_actual.subtract(ndmi_base).rename('Cambio_NDMI')
    return ndmi_base, ndmi_actual, cambio_ndmi
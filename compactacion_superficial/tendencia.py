import ee

def contar_imagenes_anuales(zona, anio):
    coleccion = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                 .filterBounds(zona)
                 .filterDate(f'{anio}-01-01', f'{anio}-12-31')
                 .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)))
    return coleccion.size().getInfo()

def tendencia_ndmi(zona):
    coleccion = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                 .filterBounds(zona)
                 .filterDate('2019-01-01', '2023-12-31')
                 .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
                 .map(lambda img: img.set('año', ee.Date(img.date()).get('year')))
                 .map(lambda img: img.normalizedDifference(['B8', 'B11']).rename('NDMI')
                      .copyProperties(img, ['system:time_start', 'año'])))

    años = ee.List.sequence(2019, 2023)

    def anualizar(year):
        y = ee.Number(year).toInt()
        ndmi = coleccion.filter(ee.Filter.eq('año', y)).median().rename('NDMI')
        return ndmi.addBands(ee.Image.constant(y).toInt16().rename('año')) \
                .set('system:time_start', ee.Date.fromYMD(y, 6, 1)) \
                .set('year', y)


    coleccion_anual = ee.ImageCollection.fromImages(años.map(anualizar))

    tendencia = coleccion_anual.select(['año', 'NDMI']) \
        .reduce(ee.Reducer.linearFit()) \
        .select('scale') \
        .rename('Tendencia_NDMI') \
        .clip(zona)

    return tendencia
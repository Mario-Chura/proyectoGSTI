import ee

def calcular_lst(zona, fecha_ini='2023-05-01', fecha_fin='2023-10-31'):
    coleccion = (ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
                 .filterBounds(zona)
                 .filterDate(fecha_ini, fecha_fin)
                 .filter(ee.Filter.lt('CLOUD_COVER', 20)))

    def extraer_lst(img):
        lst = img.select('ST_B10').multiply(0.00341802).add(149.0).subtract(273.15)
        return lst.rename('LST').copyProperties(img, img.propertyNames())

    coleccion_lst = coleccion.map(extraer_lst)
    return coleccion_lst.median().clip(zona)

def comparar_lst(zona, fecha_base_ini, fecha_base_fin, fecha_actual_ini, fecha_actual_fin):
    def periodo_lst(fecha_ini, fecha_fin):
        coleccion = (ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
                     .filterBounds(zona)
                     .filterDate(fecha_ini, fecha_fin)
                     .filter(ee.Filter.lt('CLOUD_COVER', 20)))

        def extraer_lst(img):
            lst = img.select('ST_B10').multiply(0.00341802).add(149.0).subtract(273.15)
            return lst.rename('LST').copyProperties(img, img.propertyNames())

        return coleccion.map(extraer_lst).median().clip(zona)

    lst_base = periodo_lst(fecha_base_ini, fecha_base_fin)
    lst_actual = periodo_lst(fecha_actual_ini, fecha_actual_fin)
    cambio_lst = lst_actual.subtract(lst_base).rename('Cambio_LST')

    return lst_base, lst_actual, cambio_lst

import ee
import os
from dotenv import load_dotenv
from compactacion_superficial.zona import get_zona
from compactacion_superficial.ndmi import ndmi_por_anio, comparar_ndmi
from compactacion_superficial.lst import comparar_lst
from compactacion_superficial.clasificacion import clasificacion_kmeans
from compactacion_superficial.tendencia import tendencia_ndmi

load_dotenv()
project_id = os.getenv('EE_PROJECT_ID')
ee.Initialize(project=project_id)

zona = get_zona()

ndmi_2019 = ndmi_por_anio(zona, 2019)
ndmi_2023 = ndmi_por_anio(zona, 2023)
_, _, cambio_ndmi = comparar_ndmi(zona, '2019-05-01', '2019-10-31', '2023-05-01', '2023-10-31')

lst_2019, lst_2023, cambio_lst = comparar_lst(
    zona,
    '2019-05-01', '2019-10-31',
    '2023-05-01', '2023-10-31'
)

clasificacion_img = clasificacion_kmeans(ndmi_2023, lst_2023, zona, n_clusters=4)

tendencia_img = tendencia_ndmi(zona)

exportaciones = [
    ('NDMI_2019', ndmi_2019),
    ('NDMI_2023', ndmi_2023),
    ('Cambio_NDMI_2019_2023', cambio_ndmi),
    ('LST_2019', lst_2019),
    ('LST_2023', lst_2023),
    ('Cambio_LST_2019_2023', cambio_lst),
    ('Clasificacion_KMeans', clasificacion_img),
    ('Tendencia_NDMI_2019_2023', tendencia_img)
]

for nombre, imagen in exportaciones:
    task = ee.batch.Export.image.toDrive(
        image=imagen,
        description=f'Export_{nombre}',
        folder='GEE_exports',
        fileNamePrefix=f'{nombre}_LaJoya',
        region=zona.bounds().getInfo()['coordinates'],
        scale=30,
        crs='EPSG:4326',
        maxPixels=1e13
    )
    task.start()
    print(f'[✓] Exportando {nombre}...')

print("\n Estado en: https://code.earthengine.google.com/tasks")

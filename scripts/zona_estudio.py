import ee
import os
from dotenv import load_dotenv

load_dotenv()
project_id = os.getenv('EE_PROJECT_ID')

ee.Initialize(project=project_id)

zona_estudio = ee.Geometry.Polygon([
    [[-71.625, -16.426], [-71.625, -16.450],
     [-71.595, -16.450], [-71.595, -16.426]]
])

def get_zona():
    return zona_estudio


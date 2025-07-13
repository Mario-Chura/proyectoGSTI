import ee
import os
from dotenv import load_dotenv

load_dotenv()
project_id = os.getenv('EE_PROJECT_ID')
ee.Initialize(project=project_id)

zona_estudio = ee.Geometry.Polygon([[
    [-72.003095, -16.658658],
    [-71.781650, -16.658658],
    [-71.781650, -16.791228],
    [-72.003095, -16.791228],
    [-72.003095, -16.658658]
]])

def get_zona():
    return zona_estudio

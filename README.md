# 🛰️ Monitoreo de Suelos Agrícolas - Proyecto GSTI UNSA

Este proyecto analiza la degradación de suelos agrícolas en zonas seleccionadas de Arequipa mediante imágenes satelitales Landsat multitemporales (2000, 2010, 2022), usando **Google Earth Engine (GEE)** y **Python**.

---

## 📌 Objetivos

- Calcular índices espectrales clave: NDVI, SAVI, NDSI, LST, NDMI, BI.
- Detectar cambios en la cobertura vegetal y condiciones del suelo.
- Generar mapas de riesgo de degradación.
- Exportar resultados para validación y reporte.

---

## 🧱 Requisitos

- Python 3.10 o superior
- Cuenta con acceso habilitado a Google Earth Engine
- Proyecto en Google Cloud vinculado a Earth Engine API

---

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/proyectoGSTI.git
cd proyectoGSTI
```
---

2. Crea entorno virtual

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```
---

3. Instala dependencias

```bash
pip install -r requirements.txt
```
---

4. Autentica Earth Engine

```bash
earthengine authenticate
```
---

5. Crea un archivo .env con ID de proyecto de Google Cloud

```ini
EE_PROJECT_ID=nombre-de-tu-proyecto
```

---

## 📁 Estructura del Proyecto

```bash
proyectoGSTI/
│
├── .env                      # Proyecto GCP (no subir)
├── requirements.txt
├── README.md
├── .gitignore
│
├── scripts/                  # Scripts modulares
│
├── notebooks/
```

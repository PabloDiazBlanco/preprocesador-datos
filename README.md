# 📊 Preprocesador de Datos

El **Preprocesador de Datos** es una aplicación de línea de comandos diseñada para facilitar la preparación y transformación de datasets. La herramienta permite cargar datos desde archivos **CSV, Excel y bases de datos SQLite**, seleccionar columnas de interés, gestionar valores faltantes, transformar datos categóricos, normalizar y escalar variables numéricas, detectar outliers, visualizar el impacto de las transformaciones y, finalmente, exportar el dataset procesado a formatos **CSV o Excel**.

---

## 📁 Organización del Proyecto

El proyecto está estructurado de forma modular para favorecer el mantenimiento y la escalabilidad. La siguiente es la estructura general del repositorio:

```plaintext
preprocesador-datos/
├── .git/                  # Control de versiones con Git
├── venv/                  # Entorno virtual (no incluido en el repositorio)
├── src/                   # Código fuente de la aplicación
│   ├── carga_datos.py                 # Funciones para cargar datasets (CSV, Excel, SQLite) y mostrar información básica
│   ├── deteccion_valores_atipicos.py  # Detección y gestión de outliers mediante el método IQR
│   ├── exportar_datos.py              # Funciones para exportar el dataset preprocesado a CSV o Excel
│   ├── manejo_valores_faltantes.py    # Gestión de valores faltantes con distintas estrategias (eliminación, media, mediana, moda, constante)
│   ├── normalizacion_escalado.py      # Normalización y escalado de variables numéricas (Min-Max Scaling y Z-score Normalization)
│   ├── seleccionar_columnas.py        # Selección de columnas: definición de features y target
│   ├── transformar_datos_categoricos.py  # Transformación de datos categóricos (One-Hot Encoding o Label Encoding)
│   ├── visualizacion_datos.py         # Visualización de datos mediante resúmenes estadísticos y gráficos (histogramas, dispersión, heatmaps)
│   └── main.py                        # Punto de entrada y coordinación del flujo completo de preprocesamiento
├── tests/                 # Pruebas unitarias de cada módulo funcional
│   ├── test_carga_datos.py
│   ├── test_deteccion_valores_atipicos.py
│   ├── test_exportar_datos.py
│   ├── test_manejo_valores_faltantes.py
│   ├── test_normalizacion_escalado.py
│   ├── test_seleccionar_columnas.py
│   ├── test_transformar_datos_categoricos.py
│   └── test_visualizacion_datos.py
├── requirements.txt       # Lista de dependencias del proyecto
├── README.md              # Este archivo, con toda la documentación del proyecto
└── .gitignore             # Archivos y carpetas a excluir del repositorio (e.g., venv/, __pycache__/, archivos CSV/Excel, bases de datos SQLite)
```

---

## 📌 Descripción de los Archivos de Funcionalidades

### 📂 `carga_datos.py`
Contiene funciones para cargar datasets desde archivos **CSV, Excel o bases de datos SQLite**.  
Muestra información básica del dataset, como el número de filas, columnas y una vista previa de los datos.

### 📂 `deteccion_valores_atipicos.py`
Implementa la detección de valores atípicos (**outliers**) en columnas numéricas utilizando el método del **rango intercuartílico (IQR)** y ofrece opciones para eliminarlos o reemplazarlos.

### 📂 `exportar_datos.py`
Permite **exportar el dataset preprocesado** a archivos **CSV o Excel**, solicitando al usuario un nombre para el archivo de salida.

### 📂 `manejo_valores_faltantes.py`
Gestiona los **valores faltantes** en las columnas seleccionadas, ofreciendo estrategias como:
- Eliminación de filas con valores faltantes
- Rellenado con **media, mediana, moda** o un **valor constante**

### 📂 `normalizacion_escalado.py`
Normaliza y escala las variables numéricas utilizando:
- **Min-Max Scaling** (Escala valores entre 0 y 1)
- **Z-score Normalization** (Media 0, desviación estándar 1)

### 📂 `seleccionar_columnas.py`
Permite al usuario **seleccionar** qué columnas del dataset serán:
- **Variables de entrada (features)**
- **Variable de salida (target)**  

Se valida que el **target no se encuentre entre las features**.

### 📂 `transformar_datos_categoricos.py`
Convierte las **columnas categóricas** en representaciones numéricas mediante:
- **One-Hot Encoding**
- **Label Encoding**

### 📂 `visualizacion_datos.py`
Proporciona funciones para **visualizar el dataset** antes y después del preprocesamiento. Incluye:
- **Resúmenes estadísticos**
- **Histogramas**
- **Gráficos de dispersión**
- **Heatmaps de correlación**

### 📂 `main.py`
Es el **punto de entrada** de la aplicación.  
Coordina el flujo completo del preprocesamiento a través de un **menú interactivo**, permitiendo al usuario navegar por las distintas etapas:
1. **Carga de datos**
2. **Preprocesado**
3. **Visualización**
4. **Exportación**



# ⚙️ Instalación y Ejecución del Programa

## ✅ Requisitos Previos
- **Python 3.10 o superior**
- **Git** para el control de versiones
- **venv** (incluido en Python) para la creación de entornos virtuales

## 📅 Pasos de Instalación

### 1️⃣ Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/preprocesador-datos.git
cd preprocesador-datos
```

### 🔹 Windows

```bash
python -m venv venv
venv\Scripts\activate
```


### 🔹 Instalación las dependencias

```bash
pip install -r requirements.txt
```

## 📦 Dependencias

Las principales dependencias del proyecto están listadas en `requirements.txt` e incluyen:

- **pandas**
- **openpyxl**
- **scikit-learn**
- **matplotlib**
- **pytest**





## 🚀 Ejecución del Programa

Con el entorno virtual activado, inicia la aplicación ejecutando:

```bash
python main.py
```

---

## 🖥️ Ejemplo de Uso

Al ejecutar el programa, se despliega un **menú interactivo**.  
A continuación, se muestra un ejemplo de interacción:

```yaml
=============================
Carga de Datos
=============================
Seleccione el tipo de archivo a cargar:
  [1] CSV
  [2] Excel
  [3] SQLite
  [4] Volver al menú principal
Seleccione una opción: 1
Ingrese la ruta del archivo: datos.csv
Datos cargados correctamente.
Número de filas: 150
Número de columnas: 5
Primeras 5 filas:
   Col1  Col2  Col3  Col4  Col5
0  ...   ...   ...   ...   ...
1  ...   ...   ...   ...   ...
...
```

Después de la carga, el usuario puede proceder a:

### 🔹 Preprocesado de Datos:
- Seleccionar columnas
- Manejar valores faltantes
- Transformar datos categóricos
- Normalizar y escalar variables numéricas
- Detectar y gestionar outliers

### 🔹 Visualización:
- Comparar el dataset original con el preprocesado a través de resúmenes estadísticos y gráficos.

### 🔹 Exportación:
- Guardar el dataset preprocesado en formatos **CSV o Excel**.

Cada paso se habilita progresivamente en el menú, garantizando un flujo de trabajo coherente y controlado.

---

## ✅ Pruebas Unitarias

Para verificar que todas las funcionalidades del proyecto funcionan correctamente, ejecuta las pruebas unitarias con:

```bash
pytest
```

Todas las pruebas deben pasar sin errores, confirmando la correcta implementación de cada módulo.

---
# Cinemática y dinámica de robots

Apuntes de **cinemática y dinámica de robots**, publicados con **Jupyter Book 2 (MyST)**.

**Sitio web:** https://jorgedelossantos.github.io/apuntes-robotica/

## Edición y compilación local

Los capítulos están en los archivos `*.ipynb` de la raíz; su orden se define en `myst.yml`. Las macros matemáticas comunes están en `math.yml` y la bibliografía en `references.bib`.

```bash
python -m pip install -r requirements.txt
jupyter book build --html
```

La salida se genera en `_build/html/`. Los notebooks **no se ejecutan durante la compilación**. Para servir el libro localmente, puede utilizarse `jupyter book start`.

## Validación y publicación

El seguimiento de Statcounter se conserva mediante un paso de posprocesamiento, como en los apuntes de Python. Después de compilar el HTML se ejecuta `python scripts/inject_statcounter.py`, antes de validarlo y subirlo a Pages. El script es idempotente y utiliza el proyecto de seguimiento original de robótica.


- Cada pull request hacia `main` genera una vista previa de la publicación y verifica las rutas con `BASE_URL=/apuntes-robotica`; el HTML y los registros quedan disponibles como artifacts de GitHub Actions.
- La integración en `main` activará `.github/workflows/deploy-pages.yml`, que compilará y publicará en GitHub Pages.
- **Antes de la primera publicación con Actions**, configurar **Settings → Pages → Build and deployment → Source: GitHub Actions**. Hasta completar ese cambio, el sitio actual puede seguir publicándose desde la rama `gh-pages`.
- La URL de la página principal se mantiene. No se prevén redirecciones de direcciones antiguas de capítulos.

El comando de validación de rutas de la publicación también puede ejecutarse localmente:

```bash
BASE_URL=/apuntes-robotica jupyter book build --html --strict
python scripts/inject_statcounter.py
BASE_URL=/apuntes-robotica python scripts/check_site.py
```

> En PowerShell, use `$env:BASE_URL = "/apuntes-robotica"` para establecer la variable de entorno antes de ejecutar los comandos.

## Notas de migración

El formato y las rutas de capítulos individuales pueden cambiar respecto a Jupyter Book 1. Los gráficos SVG nuevos de cinemática diferencial y dinámica son reconstrucciones esquemáticas que conviene revisar didácticamente.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Proyecto

Sitio estático en Hugo (sin tema ni proyecto npm) que publica los posters, ponencias y autores del Gabinete de Investigación en Informática y Tecnología, UCSE sede Jujuy. Todo está en español: contenido, claves del front matter, nombres de plantillas, clases CSS, identificadores JS y mensajes de commit. Mantenerlo así.

La identidad visual (tokens de color, tipografía, componentes, reglas del modo oscuro) está en `DESIGN.md` y se implementa en `assets/css/main.css`. Seguirla al tocar estilos.

## Comandos

```sh
python3 scripts/validar_contenido.py          # validación de contenido (CI la corre primero; si sale con 1, no se publica)
hugo server                                   # vista previa local (la búsqueda no funciona: no hay índice de Pagefind)
hugo --minify && npx pagefind --site public   # compilación completa con índice de búsqueda
pip install python-docx && python3 scripts/importar_word.py carpeta_con_docx/ [--sobrescribir]
```

CI (`.github/workflows/deploy.yml`) usa **Hugo extended 0.147.9** y Pagefind 1.3.0; corre con cada push a `main`, a mano y una vez por día (cron). No hay tests ni linters aparte de `validar_contenido.py`.

## Arquitectura

- **Secciones**: `content/posters/<año>/<slug>/index.md` y `content/ponencias/<año>/<slug>/index.md` son page bundles (la imagen o PDF del poster, `miniatura`, fotos y video van junto a `index.md`). Los enlaces permanentes son `/:section/:year/:slug/` según `hugo.toml`, así que `date` define el año de la URL.
- **Los autores se referencian por slug**: `autores`, `directores` y `asesores` en el front matter de un trabajo son listas de nombres de archivo de `content/autores/<slug>.md`. `layouts/_partials/autores-links.html` los resuelve con `site.GetPage "/autores/<slug>"` (si falta el archivo, usa `humanize`); la lista de autores cuenta los trabajos recorriendo esos tres parámetros en todas las páginas. Al agregar un trabajo, crear los archivos de autor que falten.
- **Taxonomías** (`hugo.toml`): `gabinetes`, `eventos`, `palabras-clave`, `tipos`. Los trabajos relacionados se calculan con `palabras-clave` (peso 100) y `gabinetes`.
- **Página de trabajo** (`layouts/single.html`): la comparten posters y ponencias y cambia según `poster_tipo` (`imagen` por defecto, `pdf`, `ninguno`, o `poster_url` externo). `poster_html` apunta a un poster interactivo en `static/posters-html/` que se muestra en un iframe dentro de un diálogo. Las imágenes se redimensionan con `layouts/_partials/miniatura.html` (webp).
- **Búsqueda** con Pagefind: las plantillas marcan `data-pagefind-body`, `data-pagefind-ignore` y spans ocultos `data-pagefind-filter` (Tipo, Año, Gabinete, Evento). Conservarlos al editar plantillas.
- **Galería**: las fotos están en `assets/galeria/` (las procesa Hugo Pipes, no van en `static/`) y se listan en orden en el front matter `fotos:` de `content/galeria/_index.md`.
- **Hoja de QR**: `/qr/` (`layouts/qr/list.html`) es una página A4 imprimible con una tarjeta por trabajo.
- `layouts/` usa la estructura de Hugo ≥0.146 (`_partials/`, `home.html` y `baseof.html` en la raíz). El JS es un único archivo sin dependencias, `assets/js/main.js` (modo oscuro, menú, diálogo de zoom, iframe del poster, visor de la galería); CSS y JS se minifican y llevan huella (fingerprint) en `baseof.html`.
- Goldmark con `unsafe = false`: el HTML crudo dentro del Markdown no se muestra.

## Reglas de contenido que controla `validar_contenido.py`

En posters y ponencias publicados (no borradores) son obligatorios `title`, `autores`, `palabras-clave`, `resumen` y `consentimiento: true`; los posters además necesitan `poster_alt`. Con `resumen_pendiente: true` no se exigen `resumen` ni `palabras-clave`. `enlaces_proyecto` debe ser una lista entre corchetes de URLs http/https. El validador lee el front matter con una expresión regular simple por línea: mantener las claves obligatorias como `clave: valor` en una sola línea y en el nivel superior. Los borradores (`draft: true`) se omiten; `importar_word.py` siempre crea borradores.

## Flujo de Git (según CONTRIBUTING.md)

- Cada push a `main` publica el sitio. Nunca hacer commit ni push directo a `main`: trabajar en una rama `cambios-pendientes-N` y abrir un PR.
- El merge lo hace la persona responsable desde la web de GitHub; nunca desde la línea de comandos ni con herramientas automáticas.
- Conventional Commits en español, en imperativo, sin punto final, de unos 72 caracteres como máximo, con alcance opcional (`poster`, `autores`, `galeria`, `menu`, `scripts`, `contenido`, `css`, `layouts`), por ejemplo `feat(galeria): agregar foto grupal de cierre`. Los títulos de PR siguen el mismo formato. Un cambio por commit.

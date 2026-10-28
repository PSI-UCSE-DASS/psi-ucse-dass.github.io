# Repositorio de Investigación · PSI-UCSE

Sitio estático (Hugo) con los posters, ponencias y autores de la Prosecretaría de Investigación de la UCSE, sede Jujuy.
Marca y diseño: ver `DESIGN.md`. Requisitos: ver el PRD del proyecto.

## Cargar un poster (a mano)

1. Crear la carpeta `content/posters/2026/<slug-del-titulo>/`.
2. Copiar ahí el archivo del poster (`poster.png`, `.jpg` o `.pdf`) y crear `index.md` copiando uno de los ejemplos.
3. Completar título, autores, resumen, palabras clave, `poster_alt`, video (opcional) y `consentimiento: true`.
4. Crear una ficha por autor en `content/autores/<nombre-apellido>.md`.
5. Cambiar `draft: true` a `false` y hacer commit en `main`: el sitio se publica solo en unos minutos.

## Importar desde Word

    pip install python-docx
    python3 scripts/importar_word.py carpeta_con_docx/

Crea fichas en borrador y un `reporte_importacion.txt` con duplicados y faltantes.

## Validar y compilar localmente

    python3 scripts/validar_contenido.py
    hugo server            # vista previa
    hugo --minify && npx pagefind --site public

## Hoja de QR

Con el sitio compilado, abrir `/qr/` e imprimir (una tarjeta por trabajo).

## Publicación

GitHub Actions (`.github/workflows/deploy.yml`) valida, compila con Hugo, indexa con Pagefind y publica en GitHub Pages.

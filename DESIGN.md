# DESIGN.md — Repositorio PSI-UCSE

Identidad visual del repositorio de posters y ponencias de la Prosecretaría de Investigación (PSI) de la UCSE.
Tomada del sitio oficial de la UCSE (sede San Salvador de Jujuy) y de la portada de Facebook UCSE-DASS.
Los valores de color son **aproximados** (salen de capturas); reemplazarlos si llega el manual de marca oficial.

## Principios

1. Se reconoce como UCSE a primera vista: azul marino, azul brillante y amarillo.
2. El poster es el protagonista: interfaz sobria alrededor, color en los acentos.
3. Pensado primero para el celular (acceso por QR en la mesa).
4. Accesible: contraste WCAG 2.1 AA en modo claro y oscuro.

## Tokens de color

```css
:root {
  --azul-marino:  #0B2A55; /* barra superior, pie, títulos */
  --azul-ucse:    #1E4DB7; /* capa sobre fotos, bloques */
  --azul-accion:  #2F7BF5; /* botones, enlaces, borde de tarjetas */
  --celeste:      #1BB3E6; /* bloques gráficos, etiqueta de gabinete */
  --amarillo:     #FFD200; /* acento: botón principal, destacados, foco */
  --fondo:        #FFFFFF;
  --superficie:   #F4F6FA; /* tarjetas */
  --borde:        #DDE3EE;
  --texto:        #1A1A1A;
  --texto-suave:  #4A5568;
}

[data-theme="dark"] {
  --azul-marino:  #E8ECF5; /* títulos pasan a claro */
  --azul-ucse:    #3D6BD6;
  --azul-accion:  #6EA2FF;
  --celeste:      #4CC6EE;
  --amarillo:     #FFD84D;
  --fondo:        #0A1730;
  --superficie:   #12224A;
  --borde:        #24365F;
  --texto:        #E8ECF5;
  --texto-suave:  #A9B4CC;
}
```

Reglas:
- Texto sobre amarillo: siempre `#0B2A55`, nunca blanco.
- Barra superior y pie mantienen fondo azul marino oscuro en ambos modos (`#06204A` en oscuro).
- El modo oscuro sigue `prefers-color-scheme` y recuerda la elección del usuario.

## Tipografía

| Uso | Fuente | Peso | Tamaño (móvil / escritorio) |
| --- | --- | --- | --- |
| Título de portada | Montserrat, MAYÚSCULAS | 700 | 32 / 56 px |
| H1 de página | Montserrat | 700 | 26 / 36 px |
| H2 de sección | Montserrat, MAYÚSCULAS | 700 | 20 / 24 px |
| Cuerpo | Roboto | 400 | 16 / 17 px, interlineado 1.6 |
| Menú, botones, etiquetas | Roboto | 500 | 15 px |

Google Fonts con `display=swap`. Títulos sobre foto: `text-shadow: 0 2px 8px rgba(0,0,0,.45)`.

## Espaciado y forma

- Escala de 8 px (8, 16, 24, 32, 48, 64).
- Ancho máximo de contenido 1200 px; margen lateral 16 px en móvil.
- Radio de tarjetas 4 px (el sitio oficial usa esquinas casi rectas); botones 3 px.
- Sombra de tarjeta: `0 2px 10px rgba(11,42,85,.10)`.

## Componentes

- **Barra superior** (40 px, azul marino): redes a la izquierda; a la derecha botones pequeños "Buscar" (amarillo) y "Sitio UCSE" (azul).
- **Encabezado** blanco (oscuro: superficie): logo UCSE a la izquierda; menú Posters · Ponencias · Autores · Gabinetes · Eventos; botón de modo oscuro. En móvil, menú hamburguesa.
- **Hero de portada**: foto de la sede bajo capa `--azul-ucse` al 80 %, título Montserrat mayúsculas abajo a la izquierda, buscador debajo.
- **Tarjeta de poster**: borde superior 4 px `--azul-accion`, miniatura 4:3, título (2 líneas máx.), autores, etiqueta de gabinete en celeste, ícono de video si tiene pitch.
- **Página de poster**: imagen ampliable a pantalla completa; a la derecha (abajo en móvil) ficha con autores, gabinete, evento, palabras clave, licencia CC BY-NC 4.0, descarga y QR; video pitch debajo.
- **Motivo gráfico**: bloques cuadrados en azul marino, azul, celeste y amarillo con rayado diagonal (de la portada de Facebook), en encabezados de sección y en la hoja de QR.
- **Pie** azul marino: lema "Scientia Deo et Patriae Servire", contacto de la Prosecretaría, licencia y año.
- **Foco visible**: contorno 3 px `--amarillo` con separación de 2 px.

## Hoja de QR imprimible

A4, una tarjeta por poster: título, autores, QR de 4 × 4 cm, URL corta y franja con el motivo gráfico. Fondo blanco para impresión económica.

## Pendiente de confirmar

- Manual de marca oficial (colores y tipografías exactos).
- Autorización de Comunicación institucional para usar el logo.
- Foto de la sede en buena resolución para el hero.

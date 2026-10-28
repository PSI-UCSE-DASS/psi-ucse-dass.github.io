#!/usr/bin/env python3
"""Importa fichas de autores y posters desde documentos Word (.docx).

Uso:
    python3 scripts/importar_word.py carpeta_con_docx/ [--sobrescribir]

Lee, en cada .docx, líneas o tablas con el formato «Campo: valor»:
    Título, Autores (separados por coma, punto y coma o « y »), Director/Directores,
    Carrera, Rol, Resumen, Palabras clave (separadas por coma), Video, Línea de investigación.
Crea fichas en estado borrador (draft: true) en content/autores/ y content/posters/<año>/.
Genera reporte_importacion.txt con duplicados y campos faltantes.
Después de revisar, se edita el archivo y se cambia draft a false.
"""
import argparse
import datetime
import pathlib
import re
import unicodedata

from docx import Document

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ANIO = 2026
EVENTO = "Simposio de Investigación 2026"
GABINETE = "Informática"

CLAVES = {
    "titulo": "titulo", "título": "titulo", "titulo del trabajo": "titulo", "título del trabajo": "titulo",
    "autores": "autores", "autor": "autores", "integrantes": "autores",
    "director": "directores", "directores": "directores", "docente a cargo": "directores", "tutor": "directores",
    "carrera": "carrera", "rol": "rol",
    "resumen": "resumen",
    "palabras clave": "palabras", "palabras claves": "palabras",
    "video": "video", "enlace al video": "video", "pitch": "video",
    "linea de investigacion": "linea", "línea de investigación": "linea",
}


def slug(texto):
    s = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:70] or "sin-titulo"


def y(valor):
    return '"' + valor.replace("\\", "\\\\").replace('"', '\\"') + '"'


def lista(valor):
    return [p.strip() for p in re.split(r"[;,]| y ", valor) if p.strip()]


def leer(docx_path):
    doc = Document(docx_path)
    pares = []
    for p in doc.paragraphs:
        if ":" in p.text:
            k, v = p.text.split(":", 1)
            pares.append((k, v))
    for t in doc.tables:
        for fila in t.rows:
            celdas = [c.text.strip() for c in fila.cells]
            if len(celdas) >= 2 and celdas[0]:
                pares.append((celdas[0].rstrip(":"), celdas[1]))
    datos = {}
    for k, v in pares:
        clave = CLAVES.get(k.strip().lower())
        if clave and v.strip() and clave not in datos:
            datos[clave] = v.strip()
    return datos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("--sobrescribir", action="store_true")
    args = ap.parse_args()
    reporte, vistos = [], {}
    for docx in sorted(pathlib.Path(args.carpeta).glob("*.docx")):
        d = leer(docx)
        if not d.get("titulo"):
            reporte.append(f"{docx.name}: no se encontró el título; se omite")
            continue
        faltan = [c for c in ("autores", "resumen", "palabras", "directores") if not d.get(c)]
        if faltan:
            reporte.append(f"{docx.name}: faltan {', '.join(faltan)}")
        slugs_autores = []
        for nombre in lista(d.get("autores", "")):
            s = slug(nombre)
            slugs_autores.append(s)
            if s in vistos and vistos[s] != nombre:
                reporte.append(f"Posible duplicado: «{nombre}» y «{vistos[s]}»")
            vistos[s] = nombre
            destino = RAIZ / "content" / "autores" / f"{s}.md"
            if destino.exists() and not args.sobrescribir:
                continue
            destino.write_text(
                "---\n"
                f"title: {y(nombre)}\n"
                f"rol: {y(d.get('rol', 'estudiante').lower())}\n"
                f"carrera: {y(d.get('carrera', ''))}\n"
                f'gabinetes: ["{GABINETE}"]\n'
                "consentimiento_publicar: true\n"
                "consentimiento_imagen: false\n"
                "---\n",
                encoding="utf-8",
            )
        directores = []
        for nombre in lista(d.get("directores", "")):
            s = slug(nombre)
            directores.append(s)
            destino = RAIZ / "content" / "autores" / f"{s}.md"
            if not destino.exists():
                destino.write_text(
                    f'---\ntitle: {y(nombre)}\nrol: "docente"\ngabinetes: ["{GABINETE}"]\n'
                    "consentimiento_publicar: true\nconsentimiento_imagen: false\n---\n",
                    encoding="utf-8",
                )
        s = slug(d["titulo"])
        carpeta = RAIZ / "content" / "posters" / str(ANIO) / s
        carpeta.mkdir(parents=True, exist_ok=True)
        destino = carpeta / "index.md"
        if destino.exists() and not args.sobrescribir:
            reporte.append(f"{docx.name}: {destino.relative_to(RAIZ)} ya existe; se omite")
            continue
        palabras = ", ".join(y(p.lower()) for p in lista(d.get("palabras", "")))
        destino.write_text(
            "---\n"
            f"title: {y(d['titulo'])}\n"
            f"slug: {y(s)}\n"
            f"date: {datetime.date(ANIO, 10, 29).isoformat()}\n"
            f"eventos: [{y(EVENTO)}]\n"
            f"gabinetes: [{y(GABINETE)}]\n"
            f"autores: [{', '.join(y(a) for a in slugs_autores)}]\n"
            f"directores: [{', '.join(y(a) for a in directores)}]\n"
            f"palabras-clave: [{palabras}]\n"
            f"linea: {y(d.get('linea', ''))}\n"
            'poster: "poster.png"   # nombre del archivo que se copia en esta carpeta\n'
            'poster_tipo: "imagen"  # imagen | pdf | html\n'
            'poster_alt: ""         # describir el poster para personas con baja visión\n'
            f"video: {y(d.get('video', ''))}\n"
            f"resumen: {y(d.get('resumen', ''))}\n"
            'licencia: "CC BY-NC 4.0"\n'
            "consentimiento: false   # pasar a true solo con el consentimiento firmado\n"
            "draft: true             # pasar a false para publicar\n"
            "---\n",
            encoding="utf-8",
        )
        print("creado", destino.relative_to(RAIZ))
    (RAIZ / "reporte_importacion.txt").write_text("\n".join(reporte) or "Sin observaciones.\n", encoding="utf-8")
    print("\n".join(reporte) or "Sin observaciones.")


if __name__ == "__main__":
    main()

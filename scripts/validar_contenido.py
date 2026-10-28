#!/usr/bin/env python3
"""Valida posters y ponencias antes de publicar.

Bloquea la publicación (código de salida 1) si un trabajo publicado no tiene
consentimiento, texto alternativo, resumen, autores o palabras clave.
Los borradores (draft: true) se omiten.
"""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
OBLIGATORIOS = ["title", "autores", "palabras-clave", "resumen", "consentimiento"]


def front_matter(texto):
    m = re.match(r"^---\n(.*?)\n---", texto, re.S)
    if not m:
        return {}
    datos = {}
    for linea in m.group(1).splitlines():
        if ":" in linea and not linea.startswith((" ", "-")):
            k, v = linea.split(":", 1)
            datos[k.strip()] = v.strip()
    return datos


def main():
    errores, avisos = [], []
    for carpeta in ("posters", "ponencias"):
        for md in sorted((RAIZ / "content" / carpeta).rglob("index.md")):
            fm = front_matter(md.read_text(encoding="utf-8"))
            nombre = md.relative_to(RAIZ)
            if fm.get("draft", "").lower() == "true":
                continue
            for campo in OBLIGATORIOS:
                if not fm.get(campo) or fm.get(campo) in ("[]", '""'):
                    errores.append(f"{nombre}: falta «{campo}»")
            if fm.get("consentimiento", "").lower() not in ("true", "si", "sí"):
                errores.append(f"{nombre}: el consentimiento debe ser true")
            if carpeta == "posters" and not fm.get("poster_alt"):
                errores.append(f"{nombre}: falta «poster_alt» (texto alternativo del poster)")
            if "ejemplo" in md.parent.name:
                avisos.append(f"{nombre}: es un contenido de EJEMPLO, borrarlo antes del evento")
    for a in avisos:
        print("AVISO ", a)
    for e in errores:
        print("ERROR ", e)
    print(f"{len(errores)} errores, {len(avisos)} avisos")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())

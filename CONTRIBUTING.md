# Guía de contribución

## Mensajes de commit: Conventional Commits

Todos los commits se escriben según [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/):

```
<tipo>(<alcance opcional>): <descripción breve en imperativo>

<cuerpo opcional: qué cambia y por qué>
```

Tipos más usados en este repositorio:

| Tipo | Cuándo usarlo | Ejemplo |
|---|---|---|
| `feat` | Una función nueva o contenido nuevo (posters, ponencias, autores, fotos) | `feat(galeria): agregar visor de fotos con teclado` o `feat(contenido): cargar póster de Sánchez` |
| `fix` | Corregir un error | `fix(poster): centrar el póster interactivo en pantalla completa` |
| `docs` | Documentación o guías | `docs: agregar guía de contribución` |
| `style` | Cambios visuales o de formato sin cambiar el comportamiento | `style(css): achicar la foto ampliada` |
| `refactor` | Reordenar código sin cambiar lo que se ve | `refactor(layouts): simplificar el conteo de autores` |
| `chore` | Tareas de mantenimiento, configuración | `chore: actualizar versión de Hugo` |
| `ci` | Flujo de publicación (GitHub Actions) | `ci: cachear imágenes procesadas` |

Reglas:

- Descripción en español, en imperativo y sin punto final (máximo unos 72 caracteres).
- Alcance opcional entre paréntesis, por ejemplo `poster`, `autores`, `galeria`, `menu`, `scripts`.
- Si el cambio rompe algo existente, agregar `!` después del tipo (`feat!:`) y explicarlo en el cuerpo.
- Un cambio por commit, siempre que sea posible.

## Flujo de trabajo

Los cambios se preparan en una rama aparte y se pasan a `main` solo cuando se aprueba la publicación, porque cada cambio en `main` publica el sitio.

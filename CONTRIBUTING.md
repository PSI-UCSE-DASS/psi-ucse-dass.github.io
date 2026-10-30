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

Cada cambio en `main` publica el sitio, por eso `main` solo recibe cambios aprobados, mediante Pull Request.

1. Los cambios se preparan en una rama aparte (`cambios-pendientes-N`) y se suben a GitHub. Nada se sube directamente a `main`.
2. Cuando se aprueba la publicación, se abre un Pull Request hacia `main`. El título del PR también sigue Conventional Commits (por ejemplo `feat(galeria): agregar visor de fotos`).
3. El merge lo hace la persona responsable desde la web de GitHub, no se hace desde la línea de comandos ni por herramientas automáticas.
4. En la página del PR, usar el botón verde **Squash and merge** (o **Merge pull request**) y confirmar. Al hacerlo desde la web con la sesión de GitHub, el commit resultante sale como **Verified**.
5. Al terminar el merge, la acción de publicación (pestaña **Actions**) despliega el sitio automáticamente en unos minutos.

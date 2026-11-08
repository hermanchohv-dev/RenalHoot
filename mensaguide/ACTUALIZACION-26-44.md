# Actualización incremental a MensaGuide 26.44 (349)

Archivo: [MensaGuide-actualizado-26-44.html](MensaGuide-actualizado-26-44.html). Descargar con **Download raw file**. Tamaño: 47.3 MB.

Origen: `MensaGuide.app.zip` aportado por el usuario. Comparación con el conjunto 26.41 (345) de `MensaGuide-revision-completa.html`. La cabecera indica **Actualizado a 08/11/2026**, fecha de esta importación; no representa una revisión clínica independiente.

## Cambios

Se actualizan 137 fichas y se añaden seis. No se elimina ninguna ficha previa.

| Categoría | Modificadas | Nuevas | Total |
|---|---:|---:|---:|
| antimicrobianos | 32 | 0 | 275 |
| microorganismos | 64 | 1 | 891 |
| sindromes | 25 | 0 | 109 |
| profilaxis | 10 | 0 | 83 |
| vacunas | 3 | 0 | 35 |
| aislamiento | 1 | 0 | 4 |
| utilidades | 1 | 1 | 109 |
| abreviaturas | 1 | 4 | 462 |

Novedades: Yanggou tick virus (YGTV); PACTO (riesgo de EI); abreviaturas SVR, RGB, NAC y NAV.

Se mantienen los identificadores anteriores (favoritos y enlaces internos), todos los alias previos, las 621 referencias fotográficas en 435 fichas, los créditos y las 255 estructuras moleculares. Las 134 celdas originales del calendario y de antisépticos no han cambiado. Se conserva íntegro el código de interfaz, búsqueda comercial, CIMA, impresión, secciones e índice, y las 88 calculadoras existentes. Las versiones anteriores permanecen disponibles.

## Verificación y alcance

Se cotejaron los campos de las 1.968 fichas con el SQLite nuevo y se comprobaron todos los destinos de los enlaces internos. Chromium recorrió las 1.968 fichas sin errores de JavaScript, con la conexión desactivada tras cargar el HTML. No hay diferencias de código ni recursos gráficos frente a la última versión: únicamente datos y textos de versión/fecha.

**PACTO se incorpora con su descripción y referencia originales; su calculadora nativa todavía no está implementada.** Son nueve utilidades pendientes en total; las ocho anteriores continúan identificadas como tales. Esta actualización no incluye una nueva validación clínica ni una comparación de los algoritmos nativos de 26.44.

Utilidades pendientes:
- Administración de β-lactámicos IV (concentración y %T > CIM)
- Bacteriemia en neutropenia febril
- BOSS-3 (bacteriemia en neoplasia hematológica)
- Candida score
- Meropenem (dosis en TRR)
- Meropenem y piperacilina/tazobactam, dosis en TRR
- Piperacilina/tazobactam (dosis en TRR)
- Vancomicina, ajuste de dosis
- PACTO (riesgo de EI)

El nuevo microorganismo no tiene una fotografía en la colección actual; no se ha asignado una imagen de otra especie.

Detalle de fichas y campos modificados: [actualizacion-26-44.json](actualizacion-26-44.json). Verificación: [validacion-26-44.json](validacion-26-44.json). Identidades nativas y sus IDs estables en el HTML: [identidades-26-44.json](identidades-26-44.json).

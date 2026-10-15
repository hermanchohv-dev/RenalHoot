# Verdant Flight: conjunto con nombres propios

**Estado: ROM renombradas preparadas. NO es una instalación compatible y validada para el M15.**

[Descargar verdantflight.zip](verdantflight.zip)

El archivo se llama `verdantflight.zip`; las 18 ROM se llaman `VerdantFlight-….rom`.
Sus datos son idénticos a los de la adaptación nativa anterior: el cambio en esta
entrega es de nombres. La pantalla de título sigue mostrando Verdant Flight.

## Por qué aún no se puede instalar en el M15 como juego nuevo

El `maincode_64` aportado contiene un catálogo arcade compilado, con nombres,
tamaños y CRC de las ROM. Sus identificaciones internas incluyen `M18`, `V6.1.4`
y `Aug 6 2025--21:04:09`. No se ha demostrado qué imagen arranca el dispositivo
(`maincode_64` o `maincode_128`), ni su número exacto de versión del emulador.

Se recuperó una copia legible mediante XOR de periodo 64 y se reconstruyeron los
17 registros del conjunto `geminib`. Todos coinciden en tamaño y CRC con las ROM
originales aportadas. La tabla usa `gww2-6c.bin` para el programa principal cuyo
CRC es `cd79c5b3`; el conjunto usado en MAME 0.276 llama a esos datos `g-2.6d`.

No hay una entrada registrada como `verdantflight` en el catálogo examinado.
Crear ese juego con nombres propios necesita una adaptación del emulador del
firmware. Copiar este ZIP renombrado a la tarjeta no proporciona ese controlador.
No se ofrece una modificación del firmware como si estuviera probada.

## Qué se ha verificado

- Integridad del ZIP y 18 nombres con el prefijo `VerdantFlight-`.
- Contenido de cada ROM idéntico a la versión nativa anterior.
- Hashes y tamaños de las 17 ROM que usa la definición de MAME preparada.
- Aplicación simulada del parche de fuentes para MAME 0.276.
- Identificación del catálogo de `maincode_64` y coincidencia de sus 17 registros.

El programa de juego anterior fue probado en MAME 0.276 con el identificador
`geminib`; eso no prueba esta instalación con un identificador nuevo en M15.
El controlador nuevo no se ha compilado ni ejecutado en MAME ni en el dispositivo.

## Archivos

- `verdantflight.zip`: ROM renombradas; requiere controlador compatible.
- `rename-manifest.json`: correspondencia de nombres, tamaños y hashes.
- `verdantflight-mame0276.patch`: alta de un controlador independiente en las
  fuentes de MAME 0.276. No es un parche para `maincode_64` y no se puede instalar
  como controlador externo en el firmware del M15.
- `maincode64-report.json`: observaciones de la copia de firmware y límites.

No se publica ni se modifica el firmware aportado. La inspección Python se
mantiene diferenciada de REA: REA rechazó el formato original desconocido; su
inspector de firmware no pudo ejecutarse sin el proveedor Binwalk. No hubo
una decompilación exitosa de ese firmware mediante REA.

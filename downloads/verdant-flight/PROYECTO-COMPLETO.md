# Verdant Flight: proyecto completo 1.1

[Descargar ZIP completo](https://github.com/hermanchohv-dev/RenalHoot/raw/refs/heads/downloads/gemini-chromatic-v2/downloads/verdant-flight/VerdantFlight-Proyecto-Completo-v1.1.zip)

Incluye código C/Z80, arranque, generación de gráficos, scripts de compilación y pruebas, ROM original aportada como entrada, dependencias documentadas, tres perfiles de ROM, correspondencia completa de nombres y tamaños, capturas JPG, audio FLAC y registros de ejecución. Incluye los ajustes de controles verticales de la edición 1.1.

## Hardware y controlador

El programa se compila para el Z80 de la placa Tecmo de Gemini Wing, emulada mediante el controlador `geminib` de MAME 0.276. No es un ejecutable para la CPU del Game Stick. Conserva el controlador de sonido, la música y las muestras del original aportado.

- `dist/mame0276/geminib.zip`: probado en MAME 0.276. Los CRC modificados generan avisos esperados frente al juego comercial.
- `dist/m15-candidate/geminib.zip`: candidato con los 17 nombres del catálogo recuperado de `maincode_64`, incluido `gww2-6c.bin`. No probado en M15; se desconoce si el firmware acepta CRC modificados.
- `dist/named/verdantflight.zip`: todas las ROM renombradas a VerdantFlight. Requiere un controlador propio; se incluye un parche para MAME 0.276 cuya aplicación se verificó, pero no se compiló ni ejecutó ese controlador. Renombrar archivos no registra un juego nuevo en el M15.

## Pruebas incluidas

MAME: inicio, disparo, cuatro direcciones, habilidades, daño y fin de partida. Segunda batería: tres fases y jefes y victoria, con asistencia externa de RAM expresamente documentada. El juego compilado no incluye esa asistencia. También se incluyen 104 comprobaciones estáticas y la recompilación desde una extracción limpia con ROM idénticas byte por byte.

No se ha ejecutado el juego en una consola M15 ni modificado su firmware. El análisis del firmware se hizo en lectura; no se incluye el firmware completo. Los fallos de las herramientas REA se conservan y se distinguen del análisis posterior con Python.

Consulta `README.md`, `docs/BUILD.md`, `docs/HARDWARE.md`, `docs/M15.md`, `docs/ROM-MAPPING.md` y `docs/TESTS.md` dentro del ZIP. El compilador y MAME se instalan por separado siguiendo las instrucciones.

SHA256 del ZIP: `04e2c7303850e08b6470f2ba31408c204f4281f556baaf5d02addb2356da3e13`.

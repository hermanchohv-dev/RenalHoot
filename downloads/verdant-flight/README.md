# Verdant Flight · Native Arcade Edition


> **Compatibilidad M15 pendiente:** la prueba de esta página corresponde a MAME
> 0.276 de ordenador. El firmware `maincode_64` examinado integra un catálogo
> arcade diferente. El conjunto con nombres propios necesita adaptar ese núcleo.
> [Nombres propios, informe y límites de compatibilidad](nombre-propio/README.md).

Adaptación nativa de Verdant Flight a Z80 sobre el hardware Tecmo que MAME emula
como `geminib`. Usa programa y gráficos nuevos, con música y efectos de las ROM
de sonido originales aportadas. El HTML anterior permanece como versión distinta.

**Descarga de juego:** [geminib.zip](geminib.zip). Mantén ese nombre al descargar.

Guárdalo en una carpeta separada y ejecuta:

```sh
mame geminib -rompath "roms/verdant-flight" -skip_gameinfo
```

El selector del emulador muestra Gemini Wing porque se reutiliza su controlador;
la pantalla de título de la ROM y el juego son Verdant Flight. Hay advertencias de
checksum por las modificaciones intencionadas. No se cambiaron ni ocultaron los
hashes de verificación del emulador.

1 inicia; flechas mueven; botón 1 dispara y botón 2 usa un orbe. Por defecto, Ctrl
y Alt son esos dos botones. Consulta [las instrucciones completas](LEEME-Verdant-Flight.txt).

- [Escuchar una muestra real del audio](Verdant-Flight-musica.mp3).
- [Pantalla de título](title.png).
- [Partida](gameplay.png).
- [Jefe de la segunda fase](boss.png).
- [Fuentes, pruebas y evidencias](Verdant-Flight-MAME-fuentes.zip).

Es una adaptación para la resolución y los recursos del arcade, con pixel art y
cuatro habilidades adaptadas; no reproduce los efectos vectoriales ni todos los
detalles de la versión web. Probada en MAME 0.276. La progresión hasta la victoria
se verificó con estados controlados y protección desde un script externo de pruebas,
no superando una partida manual completa. El script no forma parte de la ROM.

## Nombre y capturas JPG

El nombre de esta edición se mantiene como **Verdant Flight**, visible en su pantalla de título. `geminib` es únicamente el identificador técnico del controlador de MAME y del archivo ZIP necesario para cargarla.

- [Pantalla de título en JPG](Verdant-Flight-titulo.jpg).
- [Partida en JPG](Verdant-Flight-partida.jpg).

Son capturas reales de MAME, ampliadas cuatro veces sin filtrado para facilitar su lectura.

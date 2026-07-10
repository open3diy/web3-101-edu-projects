---
description: "Genera un prompt para crear una imagen conceptual a partir de un texto. Usa cuando necesites crear un prompt para Midjourney u otras herramientas de generación de imágenes basado en contenido del proyecto."
---

# imágenes referencia

1. Dame un prompt para generar una imagen conceptual en base al texto que te pongo a continuación entre comillas, no debes hacer referencia a estilo o formato, solo debes hacer una description lo mas corta posible sobre cómo generar la imagen, como si se lo indicases a un pintor que no sabe de lo que le hablas, solo debes hablarle de conceptos sencillos, por ejemplo, una imagen de un mercado en el atardecer, con frutas, no debes indicarle conceptos técnicos complejos, debes buscar una idea ampliamente conocida, se conciso y recuerda, quiero como resultado el texto para generar la imagen, no quiero la imagen.

2. Una vez tengas ese prompt, no debes darme eso como respuesta, debes usar esta plantilla como respuesta que pongo a continuación. Debes remplazar [COMPLETAR] por el prompt de resultado. Luego debes revisar donde pone "[verde-azulada | azulada-verde | verde-roja | roja-verde | azulado-morado | etc], según evoque la escena debes elegir el tono mas apropiado, si habla de mar, quizás azulado-verde, si es algo mecánica, igual rojo-verde, debes elegir la combinación binaria de colores que te evoque el texto. Esta es la plantilla:

```text
Ilustración digital conceptual ultra detallada en estilo etéreo y onírico, estética suave y luminosa: paleta [verde-azulada | azulada-verde | verde-roja | roja-verde | azulado-morado | etc] con dorados cálidos brillantes, luz volumétrica, -- [COMPLETAR], sensación de transformación fluida, liberación y orden emergente sin centro, atmósfera mágica y acuática, profundidad cinematográfica, altamente estilizado, sin texto, sin personas, sin logos --ar 3:4 --stylize 750 --v 6
```

3. Adicionalmente obtén en el nombre del archivo que le pondrías a esa imagen, en inglés y kebab-case; muestra ese nombre en pantalla en una nueva línea.

4. En base al nombre de archivo del punto 3, basándote en esta plantilla que te pongo a continuación, dame otra línea de resultado, cambiando el [COMPLETAR] por el nombre de archivo del punto 3:

```text
<img src="./assets/[COMPLETAR].png" alt="skins" width="600">
```

---

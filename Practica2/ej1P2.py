
cadena = """NumPy es el paquete fundamental para la computación científica con Python.

Sitio web: https://www.numpy.org
Documentación: https://numpy.org/doc
Lista de correo: https://mail.python.org/mailman/listinfo/numpy-discussion
Código fuente: https://github.com/numpy/numpy
Contribución: https://www.numpy.org/devdocs/dev/index.html
Informes de errores: https://github.com/numpy/numpy/issues
Informar de una vulnerabilidad de seguridad: https://tidelift.com/docs/security
Dispone lo siguiente:

un potente objeto de matriz N-dimensional
funciones sofisticadas (radiodifusión)
herramientas para integrar código C/C++ y Fortran
álgebra lineal útil, transformada de Fourier y capacidades de números aleatorios
Ensayo:

NumPy requiere y . Las pruebas se pueden ejecutar después de la instalación con:pytesthypothesis

python -c 'import numpy; numpy.test()'
Código de conducta
NumPy es un proyecto de código abierto impulsado por la comunidad desarrollado por un grupo diverso de colaboradores. El liderazgo de NumPy ha hecho un fuerte compromiso con la creación de una comunidad abierta, inclusiva y positiva. Lea el Código de conducta de NumPy para obtener orientación sobre cómo interactuar con otros de una manera que haga que nuestra comunidad prospere.

Convocatoria de contribuciones
¡El proyecto NumPy da la bienvenida a su experiencia y entusiasmo!

Siempre se aprecian pequeñas mejoras o correcciones; los problemas etiquetados como "buen primer número" pueden ser un buen punto de partida. Si está considerando contribuciones más grandes al código fuente, contáctenos primero a través de la lista de correo.

Escribir código no es la única forma de contribuir a NumPy. También puedes:

revisar las solicitudes de extracción
ayúdanos a estar al tanto de los problemas nuevos y antiguos
desarrollar tutoriales, presentaciones y otros materiales educativos
mantener y mejorar nuestro sitio web
desarrollar diseño gráfico para nuestros activos de marca y materiales promocionales
traducir el contenido del sitio web
ayudar con el alcance e incorporar nuevos contribuyentes
escribir propuestas de subvenciones y ayudar con otros esfuerzos de recaudación de fondos
Para obtener más información sobre las formas en que puede contribuir a NumPy, visite nuestro sitio web. Si no está seguro de por dónde empezar o cómo encajan sus habilidades, ¡comuníquese con nosotros! Puede preguntar en la lista de correo o aquí, en GitHub, abriendo un nuevo número o dejando un comentario sobre un tema relevante que ya está abierto.

Nuestros canales preferidos de comunicación son todos públicos, pero si primero quieres hablar con nosotros en privado, comunícate con nuestros coordinadores comunitarios en numpy-team@googlegroups.com o en Slack (escribe numpy-team@googlegroups.com para una invitación).

También tenemos una llamada quincenal a la comunidad, cuyos detalles se anuncian en la lista de correo. Le invitamos a unirse.

Si es nuevo en contribuir al código abierto, esta guía ayuda a explicar por qué, qué y cómo involucrarse con éxito.""".split(" ")
import string

for elem in cadena:
    if("https" in elem):
        print(elem)




    
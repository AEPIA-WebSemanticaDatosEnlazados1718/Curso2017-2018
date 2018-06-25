Trabajo final Web semántica y datos enlazados

Alberto Seoane Lista

1º Introducción
================

La web semántica es una extensión de la web actual donde se busca añadir a toda la información, un significado bien definido. La idea es poder definir y enlazar mejor todos los elementos de la web para su posterior mejora en procesos de descubrimiento, automatización, integración y reutilización en aplicaciones. Además cuando nos referimos al enlazado de datos, hablamos de buenas prácticas para publicar y conectar los datos de forma que sean legibles tanto por una máquina como un por humano.

Existen una serie de principios en la web semántica que ayudan en el proceso de la conexión de los datos. Utilizar lenguajes estándar como RDF o Turttle, usar URL's para nombrar los elementos y que sean consultables mediante HTTP, etc.

Actualmente la web semántica tiene tanta importancia, por ejemplo los estamentos públicos comparten sus datos (muchos, no todos ellos) con licencia libre para poder ser utilizados.

En este trabajo realizaremos el proceso de trasformación de los datos para su posterior enlazamiento.

2º Proceso de transformación
============================

2.1 Selección de la fuente de datos, donde se explique el conjunto de datos que se ha seleccionado para transformar, especificando su origen.
---------------------------------------------------------------------------------------------------------------------------------------------

En este paso vamos a seleccionar los datos que vamos a procesar, es importante tener en cuenta una serie de factores, como la procedencia de los datos, que sean reales, y que su licencia nos permita hacer uso de ellos.

Los requisitos que vamos a tener en cuenta para tener para realizar la búsqueda de datos son.

- Que la fuente de datos los proporcione en algún tipo de licencia libre.

- Que los datos sean reales.

- Que el formato sea un estándar priorizando los CSV por ser más fáciles de manejar.

- Que los datos estén en una lengua oficial peninsular.

La fuente de datos en la que se ha realizado la búsqueda es [http://datos.gob.es](http://datos.gob.es) el motivo para elegir este repositorio es que continene un catalogo de datos muy extenso y en castellano, además los datos son sobre regiones españolas porlo que están en castellano la gran mayoría y además se exportan en CSV. 

Tenemos un conjunto de datos que cumple todas nuestras premisas, el conjuto de [datos](http://datos.gob.es/es/catalogo/a14002961-museos-en-la-region-de-murcia) es de museos en la región de Murcia y parece un buen candidato a procesar y enlazar. Por otra parte vemos que tienen una licencia abierta lo cual nos permite su uso.

2.2 Análisis de los datos, explicando que tipo de datos se manejan, su formato, tipos de valores, y en general cualquier aspecto relevante para su transformación y explotación. Este análisis debe incluir la licencia de origen de los datos y la justificación de la licencia a usar en los datos transformados.
-------------------------------------------------------

En primer lugar tenemos que analizar la licencia con la que se publican los datos que se puede ver en la [url](http://datosabiertos.regiondemurcia.es/avisolegal) que establece las siguientes condiciones.

- Está prohibido desnaturalizar el sentido de la información.

- Debe citarse la fuente (el propietario de los datos) de los documentos objeto de reutilización. Esta cita podrá realizarse de la siguiente manera: "Origen de los datos: Propietario de los datos".

- Debe mencionarse la fecha de la última actualización de los documentos objeto de la reutilización, siempre cuando estuviera incluida en el documento original.

- No se podrá indicar, insinuar o sugerir que la Fundación Integra, como titular de la página web o el propietario de los datos, como titular de la información, participan, patrocinan o apoyan la reutilización que se lleve a cabo.

- Deben conservarse, no alterarse ni suprimirse los metadatos sobre la fecha de actualización y las condiciones de reutilización aplicables incluidos, en su caso, en el documento puesto a disposición para su reutilización.

Como uno de los requisitos del trabajo es licenciar los datos con una CC-by podemos utilizarlos cumpliendo los requisitos que expone la región de Murcia y podemos proseguir.

Ahora analizaremos la fuente de los datos especificando que tipos y valores toman así como una pequeña descripción para entender bien los datos con los que estamos trabajando.



| Columna     | Tipo de dato | Descripción                                                                                                                                | Notas                                                                                         |
|-------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Código      | Entero       | Es una clave identificativa                                                                                                                |                                                                                               |
| Nombre      | String       | Es el nombre oficial del museo                                                                                                             | Tiene valores vacíos.                                                                         |
| Dirección   | String       | Dirección completa sin el código posta                                                                                                     | Tiene muchas formaciones distintas, avenida calle, etc y no siguen un estándar.               |
| CP          | Entero       | Código postal                                                                                                                              | Tiene valores vacíos.                                                                         |
| Municipio   | String       | Ayuntamiento al que pertenece el museo                                                                                                     | Tiene valores vacíos                                                                          |
| Pedanía     | String       | Núcleo de población pequeño y con pocos habitantes que depende de un municipio y que está bajo la jurisdicción de un alcalde o de un juez. | Tiene valores vacíos                                                                          |
| Teléfono    | String       | Teléfono o teléfonos de atención                                                                                                           | Tiene valores vacíos, si tiene más de un teléfono de contacto está separado por "/"           |
| FAX         | String       | Número de facsímil                                                                                                                         | Tiene valores vacíos                                                                          |
| Email       | String       | Email de contacto del múseo                                                                                                                | Tiene valores vacíos                                                                          |
| URL Real    | String       | Link original de la página web                                                                                                             | Tiene valores vacíos, algunas están caídas.                                                   |
| URL corta   | String       | abreviatura del anterior                                                                                                                   | Tiene valores vacíos                                                                          |
| Latitud     | float        | coordenada de latitud                                                                                                                      | Tiene valores vacíos y está asociado a Longitud                                               |
| Longitud    | float        | corrdenada de longitud                                                                                                                     | Tiene valores vacíos y está asociado a Latitud                                                |
| Descripción | String       | Descripción que tiene el museo a modo de publicida                                                                                         | Tiene valores vácios, y están en formato HTML extraídos de la propia web                      |
| Foto        | String       | Url de una imágen                                                                                                                          | Este campo esta replicado varias veces hay muchos campos vacíos y algunas fotos están caídas. |

Como comentarios a la explicación de los datos decir que el tratamiento de los datos ha sido el siguiente: En primer lugar se ha realizado una limpieza de los mismos. En primer lugar Descartamos las coordenadas porque al importarlas se han corrompido y ahora mismo son valores nulos, por otra parte las fotos no me han parecido de interés dado que eran URL's, la mitad no funcionales, de servidores no oficiales. Por otra parte se ha separado el campo teléfono en 3 para poder poner los distintos teléfonos.

2.3 Estrategia de nombrado, donde se explique cómo se van a nombrar los recursos tanto del vocabulario a desarrollar como de los datos a generar.
--------------------------------------------------------------------------------------------------------------------------------------------------



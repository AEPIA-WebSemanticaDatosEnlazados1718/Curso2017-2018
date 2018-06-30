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

Para nombrar el vocabulario utilizaremos (/) para los elementos y la (#) para los términos como hemos visto en las clases. La estrategia de nombrado entonces sería así:

- Dominio de las URL's: http://museosdemurciaa.es

- Terminos:  Almacenaremos la ontología en  http://museosdemurciaa.es/ontologia/ y accederemos a cada elemento  http://museosdemurciaa.es/ontologia#TERMINO

- Instacias: para acceder a cada instancia de un termino utilizaremos  http://museosdemurciaa.es/museo/ITEM

2.4 Desarrollo del vocabulario, indicando el proceso de implementación del vocabulario y como este soporta los datos de origen. No se exige una ontología compleja, sino un vocabulario suficiente para describir los conceptos y propiedades de los datos a transformar.
-------------------------------------------------------------

En primer lugar tenemos que identificar los requisitos de nuestro vocabulario, para esto lo dessarrollaremos en forma de preguntas de competencia, como mínimo debería haber una pregunta para cada uno de los datos que nos interesa recuperar, aunque sus combinaciones también pueden ser interesantes. 

- Requisitos funcionales:

-- RF1: ¿Cuál es la dirección del museo?

-- RF2: ¿Código postal del museo?

-- RF3: ¿Municio al que pertenece el museo?

-- RF4: ¿Pedanía a la que pertenece el museo?

-- RF5 ¿Teléfono del museo?

-- RF6 ¿Fax del museo?

-- RF7 ¿Correo electrónico del museo?

-- RF8 ¿Cuál es la página web del museo?

-- RF9 ¿Más detalles del museo?

-- RF10 ¿todos los museos por municipio? ¿y pedanía?

- Requisitos no funcionales:

-- RNF1: La ontología debe estar en español.

-- RNF2: Utilizar formatos estándar.

Ahora podemos proseguir con la extracción de terminos, viendo el dataset y analizando los requisitos podemos extraer los siguientes términos:

- *Museo*:  lugar en que se conservan y exponen colecciones de objetos artísticos, científicos, etc. Sinónimos: galería, exposición, edificio artístico.

- *Dirección*: Lugar donde está establecido un  local o persona.

- *Código postal*: Código de cinco números que demarca una población y distrito para el servicio de correos.

- *Municipio*: Un municipio es una entidad administrativa que puede agrupar una sola localidad o varias y que puede hacer referencia a una ciudad o un pueblo.

- *Pedanía*: Núcleo de población pequeño y con pocos habitantes que depende de un municipio y que está bajo la jurisdicción de un alcalde o de un juez.

- *Teléfono*: Número de localización geoTelefónica.

- *Fax*: Número de localización facsimil.

- *Email*: Dirección de correo electronico.

- *URL*: es un documento o información electrónica capaz de contener texto, sonido, vídeo, programas, enlaces, imágenes y muchas otras cosas, adaptada para la llamada World Wide Web (WWW) y que puede ser accedida mediante un navegador web.

Una vez establecido los términos que vamos a utilizar es necesario hacer una conceptualización del vocabulario. Nuestro vocabulario es muy sencillo, el dominio es Cultura, aunque en aglunos lugares se guarda como Instituciones, pero son las que menos. Un museo tiene una dirección física compuesta por una dirección y un código postar pertenece a un municipio que pertenece a una pedanía. El museo además tiene datos de contacto como teléfono, fax, email y dirección web (URL).

Sabiendo las relaciones existentes entre nuestros términos es necesario modelarlo a través de una ontología, como nuestro dominio es un dominio típico, sobre todo en las relaciones, por lo tanto podemos reutilizar ontologías ya existentes.

En este caso usaremos las más comunes ya que están más probadas y son reutilizadas por muchas más ontologías. Las elegidas son: [*vcard*](http://www.w3.org/2006/vcard/ns) que nos ofrece muchos términos comunes como localizaciones, regiones, etc. [*owl*](http://www.w3.org/2002/07/owl) que nos ofrece las propiedades más comunes. *[rdf](http://www.w3.org/1999/02/22-rdf-syntax-ns) y [rdfx](http://www.w3.org/2000/01/rdf-schema)*. Podemos encontrar las ontologías en las url's proporcionadas

Para cada museo establecemos las siguientes propiedades


| Termino   | Tipo                                                                               | Propiedad                                                                                    |
|-----------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Nombre    | String										 | [http://www.w3.org/TR/rdf-schema#label](http://www.w3.org/TR/rdf-schema#label)               |
| Direccion | [http://www.w3.org/2006/vcard/ns#Address](http://www.w3.org/2006/vcard/ns#Address) | [http://www.w3.org/2006/vcard/ns#hasAddress](http://www.w3.org/2006/vcard/ns#hasAddress)     |
| Email     | [http://www.w3.org/2006/vcard/ns#Email](http://www.w3.org/2006/vcard/ns#Email)     | [http://www.w3.org/2006/vcard/ns#hasEmail](http://www.w3.org/2006/vcard/ns#hasEmail)         |
| Municipio | [http://www.w3.org/2006/vcard/ns#region](http://www.w3.org/2006/vcard/ns#region)   | [http://www.w3.org/2006/vcard/ns#hasRegion](http://www.w3.org/2006/vcard/ns#hasRegion)       |
| Pedania   | [http://www.w3.org/2006/vcard/ns#locality](http://www.w3.org/2006/vcard/ns#locality)| [http://www.w3.org/2006/vcard/ns#hasLocality](http://www.w3.org/2006/vcard/ns#hasLocality)  |
| Fax       | [http://www.w3.org/2006/vcard/ns#fax](http://www.w3.org/2006/vcard/ns#fax)         | [http://www.w3.org/2006/vcard/ns#hasTelephone](http://www.w3.org/2006/vcard/ns#hasTelephone) |
| Telefono  | [http://www.w3.org/2006/vcard/ns#tel](http://www.w3.org/2006/vcard/ns#tel)         | [http://www.w3.org/2006/vcard/ns#hasTelephone](http://www.w3.org/2006/vcard/ns#hasTelephone) |
| URL       | [http://www.w3.org/2006/vcard/ns#url](http://www.w3.org/2006/vcard/ns#url)         | [http://www.w3.org/2006/vcard/ns#hasUrl](http://www.w3.org/2006/vcard/ns#hasUrl)             |




2.5 Proceso de transformación, justificando qué herramientas se han usado para la transformación de los datos y qué pasos se han seguido para su limpieza y adecuación al resultado esperado
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

En primer lugar tenemos que realizar una serie de operaciones para limpiar los datos, eliminamos las columnas latitud y longitud así como foto. estas operaciones las realizamos en una herramienta de hoja de cálculo, pero realmente se pueden hacer en openRefine. Una vez tenemos los datos más o menos limpios creamos un nuevo proyecto en openRefine e importamos los datos desde CSV especificando como separador ";". Ahora tenemos que separar los teléfonos en varias columnas, y ya tendríamos los datos listos para asignar tipos. 

Una vez que comprobamos que los datos han sido cargados correctamente, tenemos que asignar un tipo a cada uno de los datos. A continuación tenemos que encontrar un elemento que pueda identificar inequívocamente cada elemento, para poder generar las URL's, en este caso utilizamos un código porque los nombres pueden corresponder a distintos edificios del mismo museo. A continuación agrupamos celdas similares, esto es una herramienta que proporciona openRefine que permite identificar automáticamente si algunas instancias son las mismas. Para finalizar presentamos la estrategia de nombrado anteriormente citada en el apartado 2.3 y añadimos  las propiedades a los recursos.


2.6 Enlazado, donde se explique qué enlaces se han generado con fuentes externas y mediante qué herramientas.
------------------------------------------------------------------------------------------------------------
Ahora tenemos que observar cuales de nuestras variables son candidadtas a ser enlazadas. Unos buenos candidatos son Muiciipio y Pedanía dado que normalmente los lugares son buenos elementos para enlazar. Por otra parte también podemos enlazar nombre dado que es uno de los datos más importantes pero también es más susceptible de que no sea enlazado correctamente.

Para poder enlazar los datos tenemos que añadir en openRefine un servicio de reconciliación, en nuestro caso usaremos DBpedia dado que está en castellano y es uno de los más usados y completos.

Ahora para reconcilizar con DBpedia nuestros datos tenemos que seleccionar las columnas municipio y pedanía y lo reconciliamos con http://dbpedia.org/ontology/PopulatedPlace. Dejamos por defecto las opciones y enlazamos manualmente aquellas que no encuentre, creamos dos columnas PopulatedPlaceM y PopulatedPlaceP. Además tenemos que establecer la propiedad owl:sameAs para apuntar a los nodos y rdfs:label para nombrar a los nodos municipio y pedania. Ahora enlazaremos la columna nombre, como comentamos anteriormente la columna nombre no tiene una clase a la que podamos enlazar porque cada vocabulario podría ponerlo de una forma distinta. Pero podemos realizar un enlazado sin clase creando la  columna nombreDB con y rdfs:label que apunta a la columna nombre, y tenemos que establecer las relaciones correspondientes identificadas anteriormente: vcard:hasURL apunta a url vcard:hasTelephone apunta a la columna teléfono, etc.


3 Aplicación y explotación, explicando qué funcionalidades aporta la solución desarrollada y cómo ésta hace uso de los datos y enlaces generados para aportar valor al usuario final. En este punto de deben explicar las queries SPARQL o el código en Jena usado para su implementación.
-------------------------------------------------------------------------------------------------

La aplicación es un código muy sencillo que nos permite realizar querys contra nuestro vocabulario (endpoint), para esto hemos configurado un script de R utilizando el paquete ‘SPARQL’ que apunta a nuestro vocabulario y nos permite obtener los datos, primero hemos configurado nuestro endpoint y los vocabularios adicionales.

```
url<- "museosDeMurcia.ttl"

prefix <- c("owl","<http://www.w3.org/2002/07/owl#>",
"rdf","<http://www.w3.org/1999/02/22-rdf-syntax-ns#>",
"rdfx","<http://www.w3.org/2001/rdf-schema#>",
"vcard","<http://www.w3.org/2006/vcard/ns#>",
)
```
ahora simplemente tenemos que definir nuestr query en la variable query de la siguiente forma

```
query<-'SELECT ?nombre LIMIT 10'

```
4 Conclusiones
--------------

El concepto de datos enlazados en la web es realmente bueno, poder tener un macro conjunto de información que tenga un estándar para estar relacionada es muy interesante a la hora de trabajar con grandes volúmenes de datos. En la época actual, la del big data, donde cada organización genera tanta información, establecer protocolos para ordenarla es vital.

No obstante me he encontrado con bastantes problemas a la hora de realizar la propuesta de trabajo, en primer lugar muchos conjuntos de datos están abandonados y sin mantenimiento. Muchos de los recursos recomendados por la red ya no están accesibles. Además la tarea de enlazado reafirmo que no existe información ent todos los dominios, por ejemplo al enlazar nuestros datos , encontramos muy poca información

Como conclusión, los datos enlazados permiten añadir una capa más de eficacia a la búsqueda de información por la red, pero no es una tarea muy explotada. Se sustenta mucho en el concepto de comunidad libre donde la gente comparte sus datos, pero parece que no es suficiente porque muchos proyectos se acaban abandonando cuando ya eran funcionales. Una posible aplicación que proporciene más beneficio económico podría impulsar este tipo de actividades.

5 Bibliografía
==============

[Wikipedia](https://es.wikipedia.org/wiki/Wikipedia:Portada)

Apuntes de la asignatura.





























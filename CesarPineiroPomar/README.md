### Web semántica y datos enlazados
##### César Piñeiro Pomar
##### cesar.pineiro@posgrado.uimp.es
[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png "Creative Commons License")](http://creativecommons.org/licenses/by/4.0/ "Creative Commons License")
------------

### 1 Introducción

La Web Semántica surge como una versión extendida de la Web con la intención de representar una amplia gama de ideas y tecnologías que intentan dar sentido a la gran cantidad de información disponible a través de la Web. El objetivo es proporcionar la información de forma estructurada de forma que tanto las personas como las máquinas pueden hacer uso de ella.

Las Bases de la Web semántica son las ontologías y las anotaciones. Las ontologías, representadas con lenguajes como RDF Schema y OWL, describen de formalmente los datos y las relaciones entre ellos. Las anotaciones, normalmente representadas en formato RDF, permiten describir las instancias de las ontologías y asociarlas a los recursos de la web.

En este trabajo se pondrán en práctica los conocimientos adquiridos en los distintos módulos de la asignatura comenzando con la obtención de los datos hasta la explotación de los mismos.

### 2 Proceso de transformación

#### 2.1 Selección de la fuente de datos
La búsqueda de datos ha sido realizada en el web [datos.gob.es](http://datos.gob.es "datos.gob.es"), una plataforma que organiza y gestiona el catálogo Nacional de Datos Abiertos. La web almacena un amplio conjunto de fuentes de datos en distintos formatos junto con su autor y una licencia. El objetivo de esta práctica es la transformación de un conjunto de datos a datos enlazados, por esa razón en la búsqueda se ha filtrado por conjuntos de datos que no presenten entre los formatos disponibles, una estructura con los datos enlazados.

El [dataset](http://datos.gob.es/es/catalogo/a07002862-registro-de-alojamientos-hoteleros2 "dataset") seleccionado almacena información acerca de un conjunto de alojamientos hoteleros de Castilla y León y ha sido publicado por la Junta de Castilla y León. Los datos están disponibles para descargar directamente, sin necesidad de ponerse en contacto con el autor, únicamente en formato .csv y con una licencia asociada.

#### 2.2 Análisis de los datos
Los datos manejados pertenecen al sector de turismo de la Junta de Castilla y León. La página web únicamente describe los datos como la relación de alojamientos hoteleros de Castilla y León, los datos están en castellano, fue creado en 2012 y con actualizaciones diarias, aunque parece que no ha vuelto a ser actualizado.

 El dataset solo está disponible en formato csv(del inglés comma-separated values), como su nombre indica es un formato para almacenar tablas donde las columnas están separadas con comas y las filas por cambios de línea. Existe una variación del formato csv que hace uso de punto y coma en lugar de coma, esta variación es debido a que en algunos casos, existen columnas formadas por números decimales hacen uso de comas para separar la parte entera de la parte fraccional y es necesario especificar un separador de columnas distinto. Este dataset contiene 22 columnas separadas por puntos y coma y está almacenado usando la codificación ISO-8859-1.

La estructura de los datos por columnas en la fuente de datos es el siguiente: 

Nombre  |  Tipo  |  Valores Vacíos  |  Valores Repetidos  |  Valor Ejemplo  |  Descripción
:------------:  |  :------------:  |  :------------:  |  :------------:  |  :------------:  |  :------------
N.Registro | String | No | No | 05/000003 | Identificador único de cada alojamiento
Tipo | String | No | Sí | Hostal | Nombre del tipo de alojamiento
Categoría | String | Si | Si | 1ª - 1 Estrella | Numero de estrellas del alojamiento
Especialidades | - | - | - | - | Columna vacía sin información
Nombre | String | No | No | EL RASTRO | Nombre del alojamiento
Dirección | String | No | No | PLAZA DEL RASTRO, 1 | Dirección física del lugar en el que se encuentra el alojamiento
C.Postal | Integer | No | Si | 24430 | Código postal de lugar en el que se encuentra el alojamiento.
Provincia | String | No | Si | León | División territorial con carácter administrativo dentro de un estado. En este caso solo denota provincias dentro de Castilla y león
Municipio | String | No | Si | Crémenes | Entidades administrativas regidas bajo un mismo gobierno, por lo que pueden incluirse varias localidades en un mismo municipio
Localidad | String | No | Si | VALDORE | Una división administrativa o territorial formada por un núcleo de población, ya sea una aldea, pueblo, ciudad...
Núcleo | String | Si | Si | VALDORE | Conjunto de edificaciones, constituido por un mínimo de 25 viviendas o 250 habitantes, con ayuntamiento situado dentro del mismo conjunto, y que posee todos los servicios de alumbrado, agua, alcantarillado y teléfono
Teléfono 1 | String | Si | Si | 920352059 | Teléfono principal
Teléfono 2 | String | Si | No | 920352059 | Teléfono adicional
Teléfono 3 | String | Si | No | 600972360 | Teléfono adicional
Email | String | Si | Si | hotel@sanzoilo.com | Correo electrónico
Web | String | Si | Si | www.sanzoilo.com | Página web
Q Calidad | String | Si | Si | Si | Contiene 'Si' en todos los alojamientos que tienen la marca "Q" de Calidad Turística que aporta prestigio, diferenciación, fiabilidad, rigurosidad y promoción
Central Reservas | - | - | - | - | Columna vacía sin información
Plazas | Integer | No | Si | 26 | Número de habitaciones disponibles
GPS.Longitud | Float | Si | No | -4,056811 | Longitud GPS de la ubicación física
GPS.Latitud | Float | Si | No | 40,909942 | Latitud GPS de la ubicación física
accesibles a minusválidos | String | Si | Si | Si | Contiene  'Si'  en todos los alojamientos que son accesibles por personas minusválidas

 La licencia de la fuente de datos está accesible mediante un link en la propia web de descarga. La licencia indica las condiciones que debemos aceptar hacer una obra derivada, explotar los datos y si la misma lo permite, obtener un beneficio económico de ello. La fuente de datos usa la licencia [![Creative Commons License](https://i.creativecommons.org/l/by/3.0/80x15.png "Creative Commons License")](http://creativecommons.org/licenses/by/3.0/ "Creative Commons License") la cual tiene los siguientes derechos y obligaciones.

- **Reconocimiento**: Se debe dar a conocer adecuadamente la autoría de la obra, proporcionar un enlace a la licencia e indicar si se han realizado cambios.

- **Compartir**: Se permite copiar y redistribuir el material en cualquier medio o formato.

- **Transformación**: Se permite remezclar, transformar y crear a partir del material.

- **Obras Derivadas**: Se permiten obras derivadas y con una licencia diferente.

- **Comercial**: Se permite la explotación de la obra incluso para fines comerciales de los que se obtenga beneficio económico.

Las licencias Creative Commons, el autor autoriza el uso de su obra, pero la obra continúa estando protegida, por esa razón se ha optado por mantener el mismo tipo de licencia en su versión 4.

#### 2.3 Estrategia de nombrado

A continuación se pasa a describir la estrategia de nombrado donde se explica cómo se van a nombrar los recursos tanto del vocabulario a desarrollar como de los datos a generar.

- **Dominio**: El dominio elegido como base para la aplicación es http://alojamientoshoteleros.es
- **Formato**: Para definir el acceso a los recursos de nuestra aplicación es necesario elegir el formato de URI a utilizar. En este caso, contamos con un conjunto amplio de datos que podrían ser actualizado en el futuro con nuevos elementos, por esa razón los elementos serán direccionados por la barra inclinada "/".
- **Ruta**: Los elementos se accederán desde http://alojamientoshoteleros.es/alojamiento
- **Patrón**: Los elementos deben seguir el patrón http://alojamientoshoteleros.es/alojamiento/&lt; identificador >

#### 2.4 Desarrollo del vocabulario

#### 2.4.1 Definición de los requisitos
Los requisitos en una aplicación pueden separarse en funcionales y no funcionales. Los requisitos funcionales. Los requisitos funcionales definen una función que debe implementar o dar soporte el sistema, mientras que los requisitos no funcionales son criterios o restricciones que debe cumplir el sistema.

**Requisitos funcionales:**
- RF1: ¿Qué tipos de Alojamientos hay?
- RF2: ¿Qué alojamientos hay en una provincia?, ¿Y en una localidad?
- RF3: Datos de contacto (Teléfono, email y web) de un Alojamiento
- RF4: Dirección de un Alojamiento
- RF5: Categoría de un alojamiento
- RF6: Accesible para minusválidos

**Requisitos no funcionales:**
- RNF1: Las ontologías usadas deben estar estandarizadas
- RNF2: Los datos deben estar enlazados con la dbpedia

#### 2.4.2 Extracción de los términos
Analizando cada uno de los requisitos funcionales se han extraído una lista de los términos necesarios para modelar el sistema:

- **Alojamiento**: Lugar en el que se hospeda temporalmente una persona.
- **Tipo**: Nombre del tipo de alojamiento: Hotel, Apartamento…
- **Categoría**: Tiene como objetivo darte una manera rápida de determinar las amenidades de un hotel mediante una clasificación basada en estrellas.
- **Dirección**: Indicación precisa del lugar donde vive una persona o se encuentra un edificio, establecimiento.
- **Provincia**: División territorial con carácter administrativo dentro de un estado.
- **Localidad**: Una división administrativa o territorial formada por un núcleo de población, ya sea una aldea, pueblo, ciudad...
- **Teléfono**: Numero para llamar al responsable del teléfono.
- **Email**: Dirección virtual para enviar correo a través de internet.
- **Web**: es un documento o información electrónica capaz de contener texto, sonido, vídeo, programas, enlaces, imágenes y muchas otras cosas, adaptada para la llamada World Wide Web (WWW) y que puede ser accedida mediante un navegador web.
- **Accesible para minusválidos**: Avisa de lugares con accesos adaptados especialmente para usuarios de sillas de ruedas, pero también para otros problemas de movilidad.

#### 2.4.3 Identificación y selección de ontologías

Para el desarrollo de la ontología se han utilizado las ontologías vcard, owl, rdf y rdfs que tienen un alto nivel de utilización y permitirán que nuestros datos estén en un modelo lo más estándar posible. Para los detalles más concretos que escapan del alcance de estas ontologías, se han usado ontologías provenientes de la dbpedia por ser una fuente de datos ampliamente usada y con una fuerte comunidad detrás de ella. Para conceptualizar nuestro sistema se han usado las siguientes propiedades.

| Nombre | Ontologia | Acceso | Prefijo
| ------------ | ------------ | ------------ | ------------ |
| vcard | http://www.w3.org/2006/vcard/ns | # | vcard
| owl | http://www.w3.org/2002/07/owl | # | owl
| rdf | http://www.w3.org/1999/02/22-rdf-syntax-ns  | # | rdf
| rdfs |http://www.w3.org/2000/01/rdf-schema  | # | rdfs
|xsd |http://www.w3.org/2001/XMLSchema| # | xsd
| dbpedia | http://dbpedia.org/ontology | / | db

| Término  | Tipo  | Propiedad
| ------------ | ------------ | ------------ |
| Nombre |  xsd:string | rdfs:label
|  Tipo |  vcard:category  | vcard:hasCategory
|  Categoria  |  xsd:float | db:starRating
| Dirección | vcard:street-address | vcard:hasStreetAddress
| Provincia | vcard:region | vcard:hasRegion
| Localidad | vcard:locality | vcard:hasLocality
| Teléfono | vcard:tel | vcard:hasTelephone
| Email | vcard:email | vcard:hasEmail
| Web | vcard:url | vcard:hasURL
| Accesible para <br>minusválidos | xsd:boolean  | db:isHandicappedAccessible

#### 2.5 Proceso de Transformación

Antes de iniciar el proceso de transformación es necesario descargar OpenRefine. En su página oficial podemos descargar su última versión 3.0 y la extensión RDF que nos permite exportar los datos finales en formato RDF. 

Una vez iniciado OpenRefine, el primer paso es cargar el fichero .csv con los datos de alojamientos hoteleros, para ello creamos un nuevo proyecto y seleccionamos el fichero alojamientoshoteleros.csv. Una vez que los datos han sido cargados, podemos comprobar como los datos muestran caracteres extraños, para solucionarlo seleccionamos como codificación del fichero ISO-8859-1. Los datos ahora se muestran de forma correcta, pero en columnas equivocadas, el separador por defecto es la coma, pero debemos seleccionar la opción 'otro' y escribir ';'. Ahora todos los datos están distribuidos en la columna correcta y sin errores de codificación, el último paso es seleccionar un nombre para el proyecto.

Antes de empezar el proceso de transformación, debemos eliminar todas las columnas de la fuente de datos que no aporten información útil para el problema. Las columnas 'Especialidades' y 'Central Reservas' no contienen ningún valor en ninguna de las filas, por esa razón serán las únicas columnas eliminadas de la fuente de datos.

En el proceso de transformación se han realizado los siguientes cambios:

- En la columna Web se han eliminados los espacios al principio y final de cada valor, además las url han sido normalizadas a minúsculas.
- La columna Email ha sido normalizada a minúsculas.
- Los números de teléfonos almacenados presentan tres tipos de formatos: sin espacios, con espacios y con separador. Para unificar los formatos, todos los teléfonos han sido transformados al formato sin espacios.
- Con los teléfonos normalizados, unimos todas las columnas en una única columna llamada Teléfono con los valores separados por ';'.
- La columna categoría almacena un valor numérico asociado a cada categoría seguido del número de estrellas del hotel. Los valores representan información repetida, la categoría 1º tiene una estrella, la categoría 2º tiene dos estrellas, etc. Por esa razón elimina la información referente a las estrellas y se transforma la categoría a valor numérico sin el carácter 'º'.
- La columna N.Registro almacena un identificador único para cada alojamiento, el identificador está formado por dos números separados por una barra inclinada. La columna es perfecta para usar como URI así que para ello vamos a transformar la barra inclinada por un punto. 

#### 2.6 Enlazado

El proceso de enlazado se realizará con la DBpedia, para ello añadimos un servicio de reconciliación basado en SPARQL. En la ventana de opciones, usamos https://dbpedia.org/sparql como URL y Virtuoso como Tipo, el resto de opciones las dejamos por defecto.

En este punto, debemos elegir las columnas que vamos a enlazar con las DBpedia, las columnas elegidas son 'Provincia' y 'Nombre'. Seleccionamos la primer columna e iniciamos el proceso de reconciliación con la DBpedia, nos aparecen una serie de opciones y elegimos enlazar con http://dbpedia.org/ontology/PopulatedPlace . Para la otra columna seguimos el mismo proceso, pero debido a que el nombre de los alojamientos es muy genérico y es difícil seleccionar un candidato, seleccionamos la opción de enlazar sin usar una clase.

En el proceso de enlazado, algunos valores no han podido ser enlazados automáticamente debido a que hay varias opciones y OpenRefine nos pide que tomemos nosotros la decisión final. En el caso de las provincias, el proceso solo falla para los valores 'Ávila' y 'León', los cuales podemos seleccionar de forma manual. En el segundo caso, el proceso es más complicado, la mayoría de los alojamientos no han encontrado ningún dato con los que enlazarse y para el resto seleccionamos enlazar con el valor más probable.

 Una vez que los datos están enlazados, creamos una columna nueva con el valor enlazado de la DBpedia para las dos columnas. A la primera la llamaremos 'PopulatedPlace' y a la segunda 'NombreDBpedia'.

 #### 2.7 Creación del RDF

 En exportar los datos en formato RDF primero debemos definir un esqueleto. El primer paso a realizar es añadir las ontologías mencionadas previamente con sus respectivos prefijos. A continuación, editamos la Base URI con  http://www.alojamientoshoteleros.es/.

El esqueleto RDF estará formado por 3 nodos, los dos primeros estarán formados por las columnas de conciliación de los datos con las URI de la DBpedia y el último estará formado por nuestros datos usando como identificador la columna N.Registro.

Abrimos el menú para editar esqueleto RDF, en el podemos ver que por defecto siempre hay un nodo que procedemos a editar. Seleccionamos como URI la columna 'Provincia' y establecemos como esquema 'db:PopulatedPlace'.  En los atributos establecemos como 'rdfs:label' la columna 'Provincia' y como 'owl:sameAs' la columna'PopulatedPlace'. Ahora debemos crear otro nodo y repetir el proceso anterior. Seleccionamos la columna 'Nombre' como URI, luego otra vez como 'rdfs:label' y terminamos con la columna 'NombreDBpedia' como 'owl:sameAs'.

Creamos otra vez un último nodo, que será el que almacene los datos de los alojamientos. Establecemos la columna 'N.Registro' como URI y las propiedades se irán añadiendo siguiendo la tabla definida en el apartado de ontologías.

Ahora que el esqueleto RDF está definido abrimos exportar y seleccionamos RDF con formato turtle.

### 3 Aplicación y explotación

Para la explotación de los datos se que se han exportado previamente, se ha creado una aplicación de consulta mediante un script Python  y la librería 'rdflib' que puede ser instalada con el comando pip.

El contenido del script es el siguiente:
```python
import rdflib, sys
from rdflib import Graph
from rdflib.plugins import sparql

graph = Graph()
graph.load("alojamientoshoteleros.ttl", format='turtle')

prefix = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX vcard: <http://www.w3.org/2006/vcard/ns#>
PREFIX db: <http://dbpedia.org/ontology/>
"""
try:
    while True:
        try:
            print(prefix)
            print("SparQL>", end="", flush=True)
            query = prefix + "\n".join(sys.stdin.readlines())
            for i, result in enumerate(graph.query(query)):
                print (str(i + 1)+":\t"+str(', '.join(map(lambda x : x or "",result))))
        except Exception as ex:
            print(ex)
except:
    print("\nAborting...")
```
El script permite hace consultas SPARQL contra el fichero ‘alojamientoshoteleros.ttl’ que contiene el RDF, los PREFIX usados en su creación han sido declarados por defecto para simplificar el texto a introducir en las consultas.

A continuación se muestran varias consultas SPARQL, algunas basadas en los requisitos funcionales y otra poco más complejas.

- RF1: ¿Qué tipos de Alojamientos hay?

```
SELECT ?tipo
WHERE {
    ?al vcard:hasCategory ?tipo
}
GROUP BY ?tipo
ORDER BY asc(?tipo)
```

```
1:      Hostal
2:      Hostal Residencia
3:      Hotel
4:      Hotel Apartamento
5:      Hotel Residencia
6:      Motel
7:      Motel Residencia
8:      Pensión
9:      Residencia Apartamento
```

- RF2: ¿Qué alojamientos hay en una provincia?

```
SELECT ?nombre ?tipo
WHERE {
    ?al rdfs:label ?nombre .
    ?al vcard:hasCategory ?tipo .
    ?al vcard:hasRegion ?provincia .
    FILTER(str(?provincia) = "Ávila") .
}
ORDER BY asc(?nombre)
```
La provincia de 'Ávila' puede sustituirse por cualquier otra.

```
1:      ALARDOS DE SAN JUAN, Hotel
2:      ALCANTARA, Hostal Residencia
3:      ALFONSO, Hostal Residencia
....
123:    TOROS DE GUISANDO, Hotel
124:    VENTA RASQUILLA, Hostal
125:    VETTONIA, Hotel Residencia
```

¿Y en una localidad?
```
SELECT ?nombre ?tipo
WHERE {
    ?al rdfs:label ?nombre .
    ?al vcard:hasCategory ?tipo .
    ?al vcard:hasLocality ?localidad .
    FILTER(str(?localidad) = "GARRAY") .
}
ORDER BY asc(?nombre)
```

```
1:      CASA ABEL, Pensión
2:      GOYO GARRAY, Hostal Residencia
3:      LA POSADA DE NUMANCIA, Hotel
4:      NUMANCIA, Pensión
5:      PUENTE DE GARRAY, Hotel
```
- RF3: Datos de contacto (Teléfono, email y web) de un Alojamiento

```
SELECT ?nombre ?tipo ?telef ?email ?web
WHERE {
    ?al rdfs:label ?nombre .
    ?al vcard:hasCategory ?tipo .
    OPTIONAL {?al vcard:hasTelephone ?telef} .
    OPTIONAL {?al vcard:hasEmail ?email} .
    OPTIONAL {?al vcard:hasURL ?web} .
    FILTER(str(?nombre) = "ANTONIO") .
}
ORDER BY asc(?nombre)
```

```
1:      ANTONIO, Hotel, 975300711; 607901635, hotel@hotelantonio.net, www.hotelantonio.net
2:      ANTONIO, Hostal, 975385145; 975385066, ,
```
En este caso hay dos alojamientos con el mismo nombre, el primero tiene todos los datos, pero el segundo carece de correo y página web.

- Alojamientos de la provincia de Ávila con mas de 3 Estrellas y con acceso para minusválidos junto con su teléfono para realizar una reserva. 

```
SELECT ?nombre ?tipo ?telef ?star ?acceso
WHERE {
    ?al rdfs:label ?nombre .
    ?al vcard:hasCategory ?tipo .
    ?al vcard:hasRegion ?provincia .
    OPTIONAL {?al vcard:hasTelephone ?telef} .
    ?al db:isHandicappedAccessible ?acceso .
    ?al db:starRating ?star .
    FILTER(?star > 3) .
    FILTER(str(?provincia) = "Ávila") .
}
ORDER BY asc(?nombre)
```

```
1:      CUATRO POSTES, Hotel, 920220000; 669403083, 4, Si
2:      EL ENCANTO, Hotel, 920337805, 4, Si
3:      EL RONDON, Hotel, 918630460; 609223033, 4, Si
4:      FONTECRUZ AVILA, Hotel, 920359200; 914295330, 4, Si
5:      II CASTILLAS, Hotel, 920219237, 4, Si
6:      MIRADOR DE GREDOS, Hotel, 920500040, 4, Si
7:      PALACIO DE VALDERRABANOS, Hotel, 920211023; 617960035, 4, Si
8:      PARADOR RAIMUNDO DE BORGOÑA, Hotel, 920211340, 4, Si
9:      PUERTA DE GREDOS, Hotel, 920345171, 4, Si
```


### 4 Conclusiones

La tarea de enlazado de datos permite, mediante uso de vocabularios estandarizados, convertir un conjunto de datos aislados heterogéneos a un formato común el cual permite la relación entre ellos. En el desarrollo de esta práctica, mediante la herramienta Openrefine, ha sido  convertida una fuente de datos en formato csv a un conjunto de datos enlazados con la DBpedia en formato RDF.

En la realización de este proceso, la tarea más complicada ha sido realizar un correcto enlazado de los datos. La conciliación de datos entre una fuente de datos local y otra remota, en este caso la DBpedia, es un proceso lento debido al alto número de peticiones con su latencia asociada.

Existen también una serie de problemas asociados al enlazados de datos, distintos autores pueden usar variaciones de una misma palabra, no siempre correctas, a la hora de nombrar un elemento. En el caso del enlazado de provincias, la omisión de algún acento, ha dificultado el enlazado automático.

### 5 Bibliografía
- Apuntes y vídeos de la asignatura.
- Web OpenRefine,  http://openrefine.org, [Online, último acceso Junio 2018].
- LOV Buscador Ontologias, http://lov.okfn.org, [Online, último acceso Junio 2018].
- SPARQL sobre RDF, https://www.w3.org/TR/rdf-sparql-query/ , [Online, último acceso Junio 2018].


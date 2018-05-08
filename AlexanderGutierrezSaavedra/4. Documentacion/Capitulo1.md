**Trabajo de datos enlazados**


        Alexander Guti�rrez Saavedra.

        Mayo 2017.



# Cap�tulo 1.  Proceso de transformaci�n

En este cap�tulo se detalla el proceso de transformaci�n realizado para garantizar la correcta transformaci�n de los datos; desde la selecci�n, dise�o; y publicaci�n de los datos transformados. Siguiendo el aprendizaje del curso es necesario contar con los pasos del ciclo de vida de los datos enlazados: Especificaci�n, Modelado, Generaci�n, Enlazado, Publicaci�n y Explotaci�n. A continuaci�n, se describe detalladamente cada uno de los pasos que aplica, ya que en este trabajo no llegaremos a la publicaci�n

### Especificaci�n

Para realizar el paso de especificaci�n fue necesario partir esta tarea en dos: identificaci�n y an�lisis de la fuente de datos y dise�o de la URI.

Para la identificaci�n de la informaci�n se determin� usar la fuente de datos expuesta por el Open data de la alcald�a de Medell�n, la cual es una entidad que expone datos abiertos de manera asequible y gratuita sin restricci�n alguna. Estos datos cumplen las caracter�sticas de ser un escenario real, estar disponibles y accesibles sin restricci�n, son datos que pueden ser manipulados y procesados de manera autom�tica y adem�s el dominio de los datos, permite enlazarlos con otras entidades gen�ricas.

Los datos manejados bajo esta entidad contienen informaci�n de diferentes �mbitos enmarcados en la ciudad de Medell�n Colombia tales como: h�bitat y medio ambiente, infraestructura, ordenamiento territorial, movilidad, educaci�n, cultura, educaci�n, salud, seguridad, desarrollo econ�mico y poblaci�n.

Para este trabajo se tomaron los datos asociados a la movilidad vehicular con la subcategor�a de accidentes de tr�nsito, registrados por la Secretar�a de Movilidad de la Alcald�a de Medell�n, desde enero 1 del a�o 2017 hasta el 31 de julio del mismo a�o.

Para entender la informaci�n de la data seleccionada, es necesario tener claridad en el concepto de accidente de tr�nsito como un evento, generalmente involuntario, causado m�nimo por un veh�culo en movimiento, el cual genera da�os a personas y/o bienes, que afectan la circulaci�n normal de los veh�culos que se movilizan en la v�a o v�as cercanas a la generaci�n del evento.

A nivel de licencia se identific� que no tiene un tipo de licencia de uso definida, pero si se declara en los t�rminos de uso la usabilidad sin restricci�n1. Tambi�n se identific� que el titular de los datos es Grupo SIG de la Alcald�a Medell�n



Los datos fueron obtenidos en un archivo csv separado por comas, con la informaci�n de los eventos generados alrededor de un accidente (coordenadas de ubicaci�n X, Y, fecha, hora, d�a, periodo, clase, direcci�n, tipo, gravedad, barrio, comuna y dise�o).

El archivo contiene las siguientes caracter�sticas:

| **Nombre** | **Tama�o** | **Filas** | **Tema** |
| --- | --- | --- | --- |
| Accidentalidad\_2017 | 4.7 MB | 24.353 | Accidentes de tr�nsito registrados por la Secretar�a de Movilidad de la Alcald�a de Medell�n |

Analizando la fuente de datos se pudo detectar la informaci�n de la tabla 1:

Tabla 1. Estructura de la data de accidentalidad.

| Columna | Tipo | Comentario/rango | Problemas |
| --- | --- | --- | --- |
| OBJECTID | Long | Identificador �nico | Ninguno |
| X | Double | Coordenada x | Ninguno |
| Y | Double | Coordenada y | Ninguno |
| RADICADO | String (50) | 12 - 1577959 | Ninguno |
| FECHA | Date(8) | 2017/01/01-2017/07/31 | Ninguno |
| HORA | String(8) | �nico | Ninguno |
| DIA | String(36) | �nico | Ninguno |
| PERIODO | String(4) | Solo 2017 | Ninguno |
| CLASE | String(50) | �nico | Ninguno |
| DIRECCION | String(100) | �nico | Ninguno |
| DIRECCION\_ENC | String(500) | �nico | Ninguno |
| TIPO\_GEOCOD | String(50) | �nico | Ninguno |
| GRAVEDAD | String(50) | �nico | Ninguno |
| BARRIO | String(50) | �nico | Ninguno |
| COMUNA | String(50) | �nico | Ninguno |
| DISENO | String(50) | �nico | Ninguno |

Para la creaci�n de la URI se constituy� a partir de:

1. Ra�z de la URI: http://antioquia.opendata.co
2. Nombramiento de recursos: http://antioquia.opendata.co/&lt;nombre\_recurso&gt;/

### Modelado y Generaci�n

Como definici�n de las ontolog�as a usar, se determin� crear una propia basada en la fuente de datos, dado que los datos que all� se maneja son muy propios de este problema y no se encontr� un vocabulario adecuado para las necesidades requeridas. Para la creaci�n de la propia ontolog�a, se ejecutaron los siguientes pasos:

    a. Definir el dominio y el alcance

El dominio de la ontolog�a est� enmarcado con la informaci�n contenida en un accidente de tr�nsito, el cual se entiende como un evento, generalmente involuntario, causado m�nimo por un veh�culo en movimiento, el cual genera da�os a personas y/o bienes, que afectan la circulaci�n normal de los veh�culos que se movilizan en la v�a o v�as cercanas a la generaci�n del evento. Esta ontolog�a nos ayudar� a catalogar un accidente seg�n el tipo, ubicaci�n, gravedad del accidente y fecha de ocurrencia. La ontolog�a nos ayudar� a responder preguntas asociadas a los accidentes de tr�nsito exclusivamente, bajo la informaci�n delimitada explicada anteriormente. Esta ontolog�a ser� usada s�lo para temas de pr�ctica, no tendr� un uso comercial ni de otro tipo.


    b. T�rminos importantes

Algunos de los t�rminos importantes que se usar�n en esta ontolog�a son: accidente, ubicaci�n, radicado, periodo, clase, direcci�n, gravedad, comuna, dise�o, veh�culo.

    c. Definici�n de clases y jerarqu�as

Se definieron algunas clases: Accidente, Ubicaci�n, Direcci�n, Ocurrencia.

    d. Definici�n de propiedades

Para cada clase se definieron algunas propiedades. Para la clase Accidente se tiene: identificador, radicado, clase, gravedad

Para la clase Ubicaci�n se tiene: coordenadaX, CoordenadaY

Para la clase Direcci�n se tiene: nomenclatura, barrio, comuna, dise�o.

Para la clase Momento se tiene: hora, d�a, fecha, periodo.


    e. Implementacion

Se procede con la creaci�n de la ontolog�a, para lo cual se us� la herramienta Prot�g� sobre Windows. All� se realizaron los siguientes pasos:

1. Creaci�n de la URI, seg�n lo definido en el est�ndar de esta ontolog�a.
2. Se crearon las clases, como se ve en la figura 1.


![alt text][img1]

[img1]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image001.png "Figura 1. Clases de la ontolog�a."
*Figura 1. Clases de la ontolog�a.*

3.	Se definieron las propiedades a cada una de las clases. Ver figura 2.

![alt text][img2]

[img2]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image002.png "Figura 2. Propiedades de las clases de la ontolog�a"
*Figura 2. Propiedades de las clases de la ontolog�a.*

4.	Se asignaron las propiedades y tipo de dato a cada una de las clases. Ver figura 3.
 

![alt text][img3]

[img3]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image003.png "Figura 3. Propiedades de las clases de la ontolog�a."
*Figura 3. Propiedades de las clases de la ontolog�a.*

5.	Se crearon las relaciones y se asignaron las clases correspondientes a cada relaci�n, ver figura 4.

![alt text][img4]

[img4]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image004.png "Figura 4. Relaciones y clases asociadas."
*Figura 4. Relaciones y clases asociadas.*

6.	Se crearon instancias de clases con data de ejemplo y tipos de datos, para ver la forma de las relaciones, ver figura 5 y 6.

![alt text][img5]

[img5]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image005.png "Figura 5. Ejemplos de clases dentro de la ontolog�a."
*Figura 5. Ejemplos de clases dentro de la ontolog�a.*


![alt text][img6]

[img6]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image006.png "Figura 6 Grafo de relaciones entre las clases de la ontolog�a." 
*Figura 6. Grafo de relaciones entre las clases de la ontolog�a.*



## Enlazado de datos
Para esta labor se utiliz� el aplicativo LodRefine de la siguiente manera:
1.	Se crea un proyecto nuevo en la herramienta, con los datos del open data de la alcald�a de Medell�n en formato csv. Ver figura 7 y 8.

![alt text][img7]

[img7]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image007.png "Figura 7. Creaci�n del proyecto en LodRefine."
*Figura 7. Creaci�n del proyecto en LodRefine.*


![alt text][img8]

[img8]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image008.png "Figura 8. Proyecto creado en LodRefine." 
*Figura 8. Proyecto creado en LodRefine.*


2.	Se definen las propiedades de importaci�n de los datos (24.352 registros) y se procede a finalizar la creaci�n del proyecto. Figura 9.

![alt text][img9]

[img9]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image009.png "Figura 9. Archivo csv importado correctamente en LodRefine." 
*Figura 9. Archivo csv importado correctamente en LodRefine.*

3.	Se procede con la transformaci�n de los datos para que concuerden los tipos de datos con los ya identificados anteriormente. En la figura 10 se pueden ver las columnas trasformadas en color verde.

![alt text][img10]

[img10]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image010.png "Figura 10. Transformaci�n de columnas en LodRefine." 
*Figura 10. Transformaci�n de columnas en LodRefine.*


4.	Realizamos algunos cambios en la data para corregir valores con la ayuda de los Facet, que fueron cargados con error debido al uso de tildes y �. En la figura 11 se puede observar este cambio.

![alt text][img11]

[img11]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image0011.png "Figura 11. Correcci�n de data en LodRefine." 
*Figura 11. Correcci�n de data en LodRefine.*

5.	Se crearon las columnas CARRERA y CALLE a partir de la columna DIRECCI�N para dar mayor claridad. Ver figura 12.

![alt text][img12]

[img12]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image012.png "Figura 12. Adici�n de columnas nuevas en LodRefine." 
*Figura 12. Adici�n de columnas nuevas en LodRefine.*

6.	Se eliminan las columnas DIRECCI�N, DIRECCION_ENC, ya que estas fueron reemplazadas por CARRERA y CALLE. Ver figura 13.

![alt text][img13]

[img13]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image013.png "Figura 13. Eliminaci�n de columnas en LodRefine."
*Figura 13. Eliminaci�n de columnas en LodRefine.*

Una vez tenemos la data depura, procedemos a la definici�n del mapping entre el esquema de datos definido y la ontolog�a creada en la primera parte. Para ello procedemos de la siguiente forma:

1.	Una vez se transformaron y corrigieron los datos, se procede a la definici�n del mapping. Para ello se carga la ontolog�a creada en LodRefine como se ilustra en la figura 14.


![alt text][img14]

[img14]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image014.png "Figura 14. Carga de ontolog�as en LodRefine."
*Figura 14. Carga de ontolog�as en LodRefine.*




2.	Se define la URI base para los individuos como se ilustra en la figura 15.

![alt text][img15]

[img15]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image015.png "Figura 15. Modificaci�n de la URI en LodRefine."
*Figura 15. Modificaci�n de la URI en LodRefine.*


3.	Se crean las propiedades para cada tipo RDF a�adido. Ver figura 16.


![alt text][img16]

[img16: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image016.png "Figura 16. Adici�n de propiedades en LodRefine."
*Figura 16. Adici�n de propiedades en LodRefine.*




	
4.	Finalmente se exportan los datos en formato turtle. Ver figura 17.
	

![alt text][img17]

[img17]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image017.png "Figura 17. Export de data en formato turtle."
![alt text][img17]

[img17]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image018.png "Figura 17. Export de data en formato turtle."
*Figura 17. Export de data en formato turtle.*

[Cap�tulo 2](https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/Capitulo2.md)
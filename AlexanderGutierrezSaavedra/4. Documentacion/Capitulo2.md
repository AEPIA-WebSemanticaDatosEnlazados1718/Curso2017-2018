**Trabajo de datos enlazados**


        Alexander Guti�rrez Saavedra.

        Mayo 2017.


# Cap�tulo 2 Aplicaci�n y explotaci�n
En cap�tulo se concentra en la explotaci�n de los datos enlazados generados a trav�s de las consultas realizadas utilizando SPARQL. Para realizar esta labor se construy� un programa sencillo en java utilizando las librer�as de Jena y realizando consultas SPARQL. En este ejercicio se realizaron solo consultas con la ontolog�a propia, ya que como se explic� anteriormente la estructura de la data no se habilitaba para usar ontolog�as existentes. A continuaci�n, se describe cada una de las consultas realizadas.



### Consulta de recursos
En esta consulta se buscaron los 10 primeros recursos de la data para cada uno de los recursos definidos (Ubicaci�n, Nomenclatura, Accidente y Momento)
Para su correcto funcionamiento se realizaron los siguientes pasos:
	
	1.	Construcci�n de un modelo vac�o de rdf-jena.
	2.	Lectura del archivo rdf de una ruta local.
	3.	Carga del archivo le�do en el modelo creado en el paso 1.
	
La figura 18 muestra los 3 primeros pasos.

![alt text][img18]

[img18]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image018.png "Figura 18. Pasos iniciales en la realizaci�n de consultas a documentos RDF."
*Figura 18. Pasos iniciales en la realizaci�n de consultas a documentos RDF.*

	4.	Construcci�n de 4 consultas SPQRQL, una por cada tipo de recurso. Ver la figura 19.

![alt text][img19]

[img19]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image019.png "Figura 19. Consultas SPARQL para conocer los recursos por cada tipo en el archivo RDF."
*Figura 19. Consultas SPARQL para conocer los recursos por cada tipo en el archivo RDF.*

	5.	Ejecutar los Queries. Para esto se itera en un ciclo for cada uno de los queries y en otro ciclo por cada resultado, se imprimen los valores correspondientes. En las figuras 20 y 21 se observan estos pasos.

![alt text][img20]

[img20]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image020.png "Figura 20. Ciclos de ejecuci�n de queries SPARQL."
*Figura 20. Ciclos de ejecuci�n de queries SPARQL.*

![alt text][img21]

[img21]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image021.png "Figura 21. Los 10 primeros recursos por tipo."
*Figura 21. Los 10 primeros recursos por tipo.*

### Consulta de informaci�n para un tipo de recurso
En esta consulta se defini� la necesidad de encontrar la clase, gravedad y radicado de un Accidente en el cual la clase sea un incendio. Para lograr esta consulta se realizaron los siguientes pasos:
	
		1. Uso de los pasos de la consulta anterior del 1 al 4.
		2. Construcci�n del query SPARQL. Para ello fue necesario incluir en la sentencia Where los campos a trav�s de los cuales se obliga a traer como resultado al tipo de recurso Accidente, adem�s se definen 3 variables. En la figura 22, se puede observar este paso.

![alt text][img22]

[img22]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image022.png "Figura 22. Consulta SPARQL con creaci�n de variable a partir de otras." 
*Figura 22. Consulta SPARQL con creaci�n de variable a partir de otras.*


		3.	Haciendo uso de la funcionalidad BIND, se crea una nueva variable de respuesta, a partir de las variables definidas en el punto anterior.
		4.	Se hace uso de la funci�n concat, para concatenar los textos y las variables con el fin de generar una variable con este contenido
		5.	Se renombra la nueva variable con el operador AS.
		6.	Se ejecuta el query
		7.	Se imprime en pantalla el resultado. Como se observa en la figura 23 y 24, el resultado del query es el mismo al mirar los datos originales del archivo de Excel.

![alt text][img23]

[img23]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image023.png "Figura 23. Resultado de la Consulta SPARQL con creaci�n de variable a partir de otras." 
*Figura 23. Resultado de la Consulta SPARQL con creaci�n de variable a partir de otras.*

![alt text][img24]

[img24]: https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/imagenes/image024.png "Figura 24. Resultado de filtro en Excel similar a la Consulta SPARQL con creaci�n de variable." 
*Figura 24. Resultado de filtro en Excel similar a la Consulta SPARQL con creaci�n de variable.*

[Cap�tulo 1](https://github.com/alexandergusa/Curso2017-2018/blob/master/AlexanderGutierrezSaavedra/4.%20Documentacion/Capitulo1.md)


 
















# Funcionalidades de SELECT en SQL

La sentencia `SELECT` es una de las instrucciones principales del lenguaje SQL y se utiliza para consultar y recuperar información almacenada en una base de datos. Puede complementarse con diferentes cláusulas que permiten organizar, limitar, agrupar y relacionar los datos obtenidos. Entre estas funcionalidades se encuentran `ORDER BY`, `LIMIT`, `GROUP BY` y los diferentes tipos de `JOIN`.

## Tabla informativa

| Funcionalidad | ¿Qué hace? | ¿Cómo se utiliza? | Ejemplo de uso | Resultado esperado |
|---|---|---|---|---|
| **ORDER BY** | Ordena los registros obtenidos mediante una consulta. | Se indica una o varias columnas y se puede utilizar `ASC` para orden ascendente o `DESC` para descendente. | `ORDER BY precio DESC` | Presenta primero los registros con los precios más altos. |
| **LIMIT** | Restringe la cantidad de registros que devuelve una consulta. | Se coloca al final de la consulta indicando el número máximo de filas que se desea obtener. | `LIMIT 10` | Devuelve como máximo los primeros 10 registros del resultado. |
| **GROUP BY** | Agrupa registros que tienen valores iguales en una o varias columnas. | Se utiliza normalmente junto con funciones como `COUNT()`, `SUM()`, `AVG()`, `MAX()` o `MIN()`. | `GROUP BY categoria` | Agrupa los registros según su categoría y permite realizar cálculos para cada grupo. |
| **INNER JOIN** | Combina registros de dos tablas cuando existe una coincidencia entre ellas. | Se establece una condición que relaciona columnas de ambas tablas, normalmente mediante `ON`. | `Clientes INNER JOIN Pedidos ON Clientes.id = Pedidos.cliente_id` | Muestra únicamente clientes que tienen pedidos relacionados. |
| **LEFT JOIN** | Devuelve todos los registros de la tabla izquierda y los registros coincidentes de la tabla derecha. | Cuando no existe una coincidencia, las columnas correspondientes a la tabla derecha presentan valores `NULL`. | `Clientes LEFT JOIN Pedidos ON Clientes.id = Pedidos.cliente_id` | Muestra todos los clientes, incluso aquellos que no han realizado pedidos. |
| **RIGHT JOIN** | Devuelve todos los registros de la tabla derecha y los registros coincidentes de la tabla izquierda. | Funciona de forma inversa a `LEFT JOIN`. Cuando no existe coincidencia, los campos correspondientes a la tabla izquierda presentan `NULL`. | `Clientes RIGHT JOIN Pedidos ON Clientes.id = Pedidos.cliente_id` | Muestra todos los pedidos, aunque alguno no tenga una coincidencia en la tabla de clientes. |

## Descripción de las funcionalidades

### ORDER BY

`ORDER BY` permite establecer el orden en el que se presentan los registros obtenidos mediante `SELECT`. El orden puede ser ascendente (`ASC`) o descendente (`DESC`). Esta funcionalidad resulta útil cuando se requiere organizar información alfabéticamente, por fechas, precios u otros valores.

### LIMIT

`LIMIT` permite controlar la cantidad máxima de registros que serán mostrados como resultado de una consulta. Es especialmente útil cuando una tabla contiene una gran cantidad de información y solamente se requiere consultar una parte de ella.

### GROUP BY

`GROUP BY` permite reunir registros que poseen valores iguales en una determinada columna. Generalmente se combina con funciones de agregación como `COUNT()`, `SUM()` o `AVG()` para obtener información resumida sobre cada grupo.

### INNER JOIN

`INNER JOIN` relaciona dos tablas y devuelve únicamente aquellos registros para los cuales existe una coincidencia según la condición establecida. Por ejemplo, puede utilizarse para consultar solamente aquellos clientes que tienen pedidos registrados.

### LEFT JOIN

`LEFT JOIN` conserva todos los registros de la tabla indicada a la izquierda de la relación. Cuando existe una coincidencia en la segunda tabla, incorpora su información; cuando no existe, los campos correspondientes aparecen como `NULL`.

### RIGHT JOIN

`RIGHT JOIN` funciona de manera similar a `LEFT JOIN`, pero conserva todos los registros de la tabla ubicada a la derecha. Los registros que no tengan una coincidencia en la tabla izquierda mostrarán valores `NULL` en los campos correspondientes.
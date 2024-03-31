# DOCUMENTACIÓN SOBRE SQL

- Esta documentación está basada en el video del youtuber [Dalto - curso de sql desde cero](https://www.youtube.com/watch?v=DFg1V-rO6Pg&t)
- [Playground sql lite](https://sqlime.org/)
- [Documentación sql](https://www.w3schools.com/sql/default.asp)
## LENGUAJE PARA MANIPULACIÓN DE BASES DE DATOS RELACIONALES:
[![N|sql](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHC2PgWBCh4ty3Ny-_YUhIc3RDZH8dcVAlYg&usqp=CAU)](https://www.sqlite.org/)

### Qué es SQL
Estas son las siglas de _structured query language_ (lenguaje de consultas estructuradas) y básicamente es un lenguaje de programación que nos permite trabajar con bases de datos relacionales.

### Para que sirve
Estas son algunas de las opciones que podemos hacer con SQL, no solo estas, estas son por mencionar algunas:
- Administrar bases de datos (crear, actualizar, leer y eliminar)
- Consultar datos sobre una base de datos para encontrar información específica
- Podemos agregar restricciones y reglas de integridad a una base de datos. Es decir, agregar condiciones para que las bases de datos cumplan con ciertos criterios. Ejemplo: un campo en una tabla no puede estar vacío y debe de ser un valor único.
- Generar informes
- Análisis de datos

### Modelo ER (Con Notación de Chen)

Cuando trabajamos con SQL nos topamos con diferentes conceptos que es importante entender antes de entrar a trabajar con bases de datos. Entonces partiremos de lo más abstracto a lo mas tangible:

- **Entidad**: Es una referencia a cualquier cosa que tengamos en la vida real (Normalmente se representan con tablas).
-- *Ejemplo 1*: Un dibujo de una casa no es la casa en sí, sino la representación de una casa. 
--*Ejemplo 2*: En una tienda en línea las entidades vienen a ser clientes, productos, órdenes de compra, proveedores, etc.

La nomenclatura que se usa para representar las entidades se llama [notación de chen](https://support.microsoft.com/es-es/topic/crear-un-diagrama-con-notaci%C3%B3n-de-base-de-datos-de-chen-75d28eff-2509-4faf-8cd9-3eda5fb4327b#:~:text=La%20notaci%C3%B3n%20de%20base%20de,de%20datos%20o%20ejemplos%20b%C3%A1sicos.) y básicamente es una forma de representar estas entidades y sus relaciones.

Cuando encerramos una palabra en un cuadrado decimos que eso es una entidad. Ahora; una casa puede tener diferentes atributos:

| Entidad | atributo 1 | atributo 2 | atributo 3 | atributo 4 | atributo 5 | atributo 6 |
| ------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| casa | tamaño | dirección | Ambientes | Ubicación | Precio | Propietario |

Los atributos se representan por un óvalo.
![óvalo](https://raw.githubusercontent.com/Kaziuz/learning-sql/main/photos/1.atributos.jpg)

También  existe algo que se llama los atributos **simples, atributos compuestos, atributos multivalor y atributos derivados**:

- **Atributos simples:** Son atributos que tienen datos únicos, no están compuestos por nada más. Por ejemplo en precio de una casa es 100.000 dólares y nada más.

- **Atributos compuestos:** Son atributos que están compuestos de más datos. *Por ejemplo:* en la casa, el atributo ambiente es compuesto, porque; además de ser una habitación, esta habitación puede ser una pieza dormitorio, un comedor, una cocina, una sala, etc… y también tiene un tamaño, puede ser de 50 m x 50 m.
La forma de representar atributos compuestos es sacando una línea ![una línea](https://raw.githubusercontent.com/Kaziuz/learning-sql/main/photos/2.atributoscompuestos.jpg) para identificar sus atributos compuestos.

- **Los atributos multivalor:** son aquellos atributos que tienen más de un valor: *por ejemplo,* en la casa, los atributos multivalor son los ambientes, las ventanas y las puertas. Se representan haciendo un doble óvalo.
![multivalor](https://raw.githubusercontent.com/Kaziuz/learning-sql/main/photos/3.multivalor.jpg)

- **atributos derivados:** se pueden obtener con cualquier otra información: en el caso de la casa son antigüedad y ubicación. Si sabemos la fecha de construcción de la casa podemos saber también  su fecha de antigüedad. Es decir, si sabemos que la casa se construyo el 1 de enero de 2000 y estamos en el 22 de febrero del 2024, sabemos que la antigüedad de la casa es de 24 años. Lo mismo la ubicación, si sabemos la dirección de la casa, podremos saber la ubicación. Los atributos derivados los identificamos con un borde punteado.
![derivados](https://raw.githubusercontent.com/Kaziuz/learning-sql/main/photos/4.attrderivados.jpg)

- **Llaves | keys:** son la forma única de identificar algo como por ejemplo un id. Entonces, un key es un atributo que agregamos para hacerlo único frente a otros elementos: es decir, en un edificio todos los apartamentos son iguales, pero en la base de datos tienen un identificador para hacerlo único y poderlos diferenciar frente al resto.

## PRIMEROS PASOS

### Crear base de datos
Para crear una base de datos usamos la siguiente declaración:
```sql
  CREATE DATABASE databasename;
```
Donde databasename es el nombre de la base de datos.
Entonces un ejemplo real sería:

```sql
  CREATE DATABASE Usuarios;
```

### Consulta, tabla, campo, valor de campo, registro, identificadores

- **Tabla | Table:** Una tabla es una estructura de datos que está compuesta por filas y columnas. *Por ejemplo:* Un ajedrez o la tabla periódica.
Para crear una tabla en una base de datos usamos la siguiente declaración:
```sql
CREATE TABLE table_name (
    columna1 datatype,
    columna2 datatype,
    columna3 datatype,
)
```
El parámetro **columna | campo | field** especifica el nombre de la columna de la tabla. Y el parámetro _datatype_ especifica el tipo de dato que la columna va a manejar. Ejemplo: varchar, integer, date, etc. Más información sobre los [tipos de datos](https://www.w3schools.com/sql/sql_datatypes.asp) para los campos.

El **registro | record** de una tabla son las filas que la componen. Donde se almacena la información de cada columna.
![registro de una tabla](https://aprendelibvrefiles.blob.core.windows.net/aprendelibvre-container/course/access_2007/image/acces07_01_04_l.png)
Ahora cada **celda | field value** que compone cada registro se llama valor del campo, y es como su nombre lo indica, donde se guarda el valor de cada registro para su respectiva columna.

- *Consulta | query:** Normalmente sobre las bases de datos se hacen consultas. Para realizar una consulta y saber qué datos hay, se utiliza la declaración **SELECT**. Se usan para obtener información de una base de datos.

Para seleccionar columnas específicas, escribimos así:
```sql
SELECT column1, column2, ... FROM table_name;
```

Para seleccionar todas las columnas escribimos así:
```sql
SELECT * FROM table_name;
```

Un ejemplo entonces sería así:
```sql
SELECT * FROM usuarios;
```
- **insert | insertar:** Cuando creamos una tabla, normalmente está vacía. Sin filas, sin datos. La declaración **INSERT INTO** se utiliza para insertar nuevas filas o registros en una tabla. Estos registros son posibles insertarlos de dos maneras:
1. Especificar ambos, los nombres de las columnas y sus valores a insertar:
```sql
    INSERT INTO table_name (column1, column2, column3, ...)
    VALUES (value1, value2, value3, ...);
```
2. Cuando se añaden valores para todas las columnas de la tabla, no se necesitan especificar los nombres de las columnas
```sql
    INSERT INTO table_name
    VALUES (value1, value2, value3, ...);
```

Entonces, un ejemplo real para el caso 1 sería así:
```sql
    INSERT INTO usuarios (nombre, apellido, edad)
    VALUES ('Johnny', 'sepúlveda', 36);
```

Para insertar varios registros sería así:
```sql
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES
('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),
('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');
```

- **Delete | borrar:** Si queremos borrar todos los registros|filas de una tabla, lo haríamos así:
```sql
DELETE FROM table_name;
```
Un ejemplo real sería así:
```sql
DELETE FROM usuarios;
```
Hay que tener **cuidado** porque al ejecutar este comando se borran **TODOS** los registros de una tabla, por eso esta sentencia se usa con la declaración **WHERE**









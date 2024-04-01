# DOCUMENTACIÓN SOBRE SQL

- Esta documentación está basada en el video del youtuber [Dalto - curso de sql desde cero](https://www.youtube.com/watch?v=DFg1V-rO6Pg&t)
- [Playground sql lite](https://sqlime.org/)
- [Documentación sql](https://www.w3schools.com/sql/default.asp)
## LENGUAJE PARA MANIPULACIÓN DE BASES DE DATOS RELACIONALES:
[![N|sql](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHC2PgWBCh4ty3Ny-_YUhIc3RDZH8dcVAlYg&usqp=CAU)](https://www.sqlite.org/)

## Conceptos Básicos

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

### Consulta, tabla, campo, valor de campo, registros

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

EL siguiente ejemplo crea una tabla llamada **Persons** que contiene 5 columnas: PersonID, LastName, FirstName, Adders y City
```sql
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    Firstname varchar(255),
    Address varchar(255),
    City varchar(255)
)
```

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

> !Cuidado].
Hay que tener **cuidado** porque al ejecutar este comando se borran **TODOS** los registros de una tabla, por eso esta sentencia se usa con la declaración **WHERE**

## SECCIÓN BASICA

### Identificadores

Los identificadores son campos que nos permiten identificar un registro entero. Existen dos tipos de identificadores: los _primary keys | llaves primarias_ y los _foreing keys | llaves extranjeras_

### Clave primaria (primary key)
1. Una clave primaria es un campo (o combinación de campos) que identifica de manera única cada fila en una tabla.
2. En una tabla, solo puede haber una clave primaria
3. La clave primaria garantiza la integridad de los datos y evita que se ingresen filas duplicadas en la tabla.
4. Se define al momento de crear la tabla usando la cláusula “PRIMARY KEY”
5. Los valores en una clave primaria no pueden ser nulos (null)

En el siguiente ejemplo se crea una tabla _employees_ con una primary key que se llama _employee_id_

```sql
    CREATE TABLE EMPLOYEES (
        employee_id INT PRIMARY KEY,
        last_name VARCHAR(50) NOT NULL,
        first_name VARCHAR(50),
        hire_date DATE,
    )
```

Cuando se crean tablas es comun usar en su clave primaria la palabra clave **AUTO INCREMENT**, esto permite a la columna generar un numero automaticamente incrementable cada vez que una nueva fila es agregada a la tabla para hacer ese registro unico de todos los demas registros.

```sql
CREATE TABLE Persons (
    PersonID int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMATY KEY (PersonID)
)
```

### Clave Foránea (Foreign key)
1. Una clave foránea es un campo (o una combinación de campos) en una tabla que establece una relación con la clave primaria de otra tabla, es decir hace referencia a una clave primaria de otra tabla; es decir: no puede ser una clave foránea si no esta haciendo referencia a una clave primaria de otra tabla. **ES UNA BUENA PRACTICA A UNA COLUMNA QUE VA A CONTENER UNA CLAVE FORANEA PONERLE EL MISMO NOMBRE DE LA COLUMNA A LA QUE VAMOS A HACER REFERENCIA.**
Ejemplo: Si en una tabla usuarios tenemos la columna *id_usuarios* que es una clave primaria, y en otra tabla vamos a tener una columna pacientes, que en realidad es una columna foránea que va a contener ids de los usuarios, entonces no le ponemos pacientes sino **id_usuarios.**
2. Se utiliza para vincular dos tablas entre sí y garantizar la integridad referencial de los datos
3. No necesariamente hay una única clave foránea en una tabla
4. Los valores en una clave foránea pueden ser nulos, lo que indica que la relación es opcional.
5. Se define usando la cláusula **FOREIGN KEY** al momento de crear la tabla.

En el siguiente ejemplo se crea una tabla _Detalles_ con una primary key que se llama _id_ y la foreing key que se toma de la columna producto_id

```sql
CREATE TABLE Detalles (
    id INT PRIMARY KEY,
    producto_id INT,
    cantidad INT,
    FOREIGN KEY (producto_id) REFERENCES Productos(id)
);
```

Ahora un ejemplo para que todo quede mas claro: tenemos dos tablas: una llamada _usuarios_ y otra que se llama _turnos_medicos_

![turnosmediucos](https://raw.githubusercontent.com/Kaziuz/learning-sql/main/photos/turnosMedicos.jpg)

Al momento de crear ambas tablas, las relacionamos por las foreign keys, que serian el **id_usuario**

![tablas relacionadas](https://raw.githubusercontent.com/Kaziuz/learning-sql/main/photos/relacionTablas.jpg)
Para hacer este diagrama usamos la herramienta [dbdiagram](https://dbdiagram.io/)
Para generar esta imagen este fue el script usado:

```
Project aprendiendo {
  database_type: 'sql lite'
  Note: 'Aprendiendo'
}

Table users {
  id_usuario integer [primary key]
  nombre varchar
  apellido varchar
  edad integer
}

Table turnos_medicos {
  id_turno integer
  profesional varchar
  id_usuario integer [ref: - users.id_usuario]
  motivo varchar
  horario varchar
}
```

### Base de datos Northwind

Para obtener una base de datos para poder trabajar usamos [Northwind](Northwind: https://cutt.ly/s44VsfF)

![northwind](https://upload.wikimedia.org/wikiversity/en/thumb/a/ac/Northwind_E-R_Diagram.png/1440px-Northwind_E-R_Diagram.png)

**Analisis de la imagen**
1. La **tabla Customers** esta relacionada con la **tabla Orders** por la clave primaria CustomerID: es decir que ordeno ese cliente
2. La **tabla Employees** esta relacionada con la **tabla Orders** por su clave primaria EmployeeID: es decir cual empleado a vendido a que cliente  
4. En la **tabla shippers** estan las empresas que se encargan del envio del producto, entonces; en esta tabla esta relacionada con la **tabla orders** por el SHipperID: es decir que empresa se encargo de despachar X orden de compra.
5. La **tabla ordersDetails** esta relacionada con la **tabla orders** por medio de una clave foránea OrderID que hace referencia a la clave primaria de la tabla orders: orderID
6. La **tabla Products** esta relacionada con la **tabla OrderDetails** por medio de una clave foranea ProductID que se relacionada con al clave primaria productID de la tabla products

### Operaciones sobre los datos

**Clausula AS**

La clausula **AS** nos permite darle a ua tabla o a una columna un nombre temporal (sobrenombre). Los alias son usados para darle a las columnas nombres mas legibles.

La sintaxis general es asi para una columna:
```sql
SELECT column_name AS alias_column_name FROM table_name;
```
la sintaxis general es asi para una tabla:
```sql
SELECT column_name(s) FROM table_name AS alias_table_name;
```
Un ejemplo mas seria asi:
```sql
SELECT LastName AS apellido from Employees;
```

**Clausula ORDER BY**

La palabra clave **ORDER BY** nos permite ordenar el conjunto de resultados en un orden ascendente o descendente.

La sintaxis es esta:
```sql
SELECT column1, column2, ...
FROM table_name 
ORDER BY column1, column2, ... ASC | DESC
```

Otros ejemplos:

Este comando organiza la tabla por la columna Price desde el mas barato hasta el mas caro ascendentemente
```sql
SELECT * from Products ORDER BY Price ASC
```
Algunas veces va a pasar que los datos tienen valores NULL, si queremos mostrar los valores null al final escribimos la consulta agregandole la palabra clave **NULL LAST** despues del **ASC**
```sql
SELECT * FROM Products 
ORDER BY ProductName ASC NULL LAST
```

**Clausula RANDOM**

La clausula **RANDOM** ordena las columnas de una tabla al azar.

```sql
SELECT * FROM Products ORDEY BY random()
```

**Clausula DISTINCT:**

Se usa para que salgan los valores únicos de una columna.

La sintaxis seria sta:

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

Entonces supongamos que para la columna product name se repiten algunos nombres de productos, entonces para que salgan los únicos nombres y no repetidos escribiriamos la clausula asi:

```sql
SELECT DISTINCT ProductName FROM Products;
```

**Clausula WHERE (CONDICIONES)**

La cláusula **WHERE** es usada para filtrar registros. Es usada para extraer solo aquellos registros que cumplen una condición especifica.

Sintaxis especifica:

```sql
SELECT column1, column2, ... FROM table_name WHERE condition;
```
> IMPORTANTE: no solo se usa **WHERE** con SELECT, tambien se usa con UPDATE, DELETE y otras maás.

Ejemplos:

```sql
— Asi devolveria solo el campo
SELECT ProductName from Products
WHERE ProductID = 14
```

```sql
— Asi devolveria el registro completo
SELECT * FROM Products
WHERE ProductID = 12
```

```sql
— Muestrame todas las opciones que valgan menos de 40 dolares
SELECT * FROM Products
WHERE Price <= 40
```

```sql
— Muestrame todos los productos que valgan mas de 40
SELECT * FROM Products
WHERE Price > 40
```

```sql
— Para borrar un registro especifico
DELETE from turnos_medicos
WHERE id_turno = 16
```

**Clausula WHERE con UPDATE (CONDICIONES)**

La clausula **UPDATE** es usada para modificar un registro existente en una tabla. Se usa en conjunto con la palabra clave **SET** que nos indica que escribamos el nombre de la columna con su nuevo valor

Sintaxis:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
Ejemplo:

```sql
— para actualizar un campo especifico
UPDATE turnos_medicos
SET horario = "4:30 PM"
WHERE id_turno = 15
```

**Operadores Logicos AND, OR Y NOT**

La clausula **WHERE** contiene una serie de operadores que sirven para agregar logica al filtrado.

El operador **AND** es utilizado para filtrar filas basadas en mas de una condicion. Devuelve verdadero si todas las condiciones son verdaderas.

Sintaxis de AND
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```
Ejemplo AND:

```sql
SELECT * from Customers
WHERE CustomerID >= 50 AND CustomerID < 55
```

El operador lógico **OR** devuelve verdadero si cualquiera de las condiciones es verdadera.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```

Ejemplo OR:

```sql
SELECT * FROM Employees
WHERE FirstName = "Nancy" OR FirstName = "Steven"
```

Ejemplo combinando AND y OR:
```sql
— Dame los productos que su precio sea menor a 20 o su categoría sea 6 y que si o si el proveedor sea 7
SELECT * FROM Products
WHERE (Price < 20 OR CategoryID = 6) AND SupplierID = 7
```

El operador lógico **NOT** invierte el valor de verdad de una condición. Es decir: se usa para negar una condicion. Si algo es true entonces lo vuelve false y visceversa.

sintaxis:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```

Ejemplo:
```sql
— Muestrame todos los clientes menos los de usa
SELECT * FROM Customers
WHERE NOT Country = "USA"
```

```sql
— Muestrame todos los clientes menos de lo de usa y los de Francia
SELECT * FROM Customers
WHERE NOT Country = "USA" AND NOT Country = "France"
```

**Clausula LIMIT**
La declaracioón **LIMIT** limita los resultados al numero que se ponga despues de escribir la palabra.

```sql
-- Limitame los resultados a solo 5 registros
SELECT * FROM Customers
WHERE CustomerID >= 50
AND NOT Country = "Germany"
AND NOT Country = "USA"
AND NOT Country = "Argentina"
LIMIT 5
```

**Operador BETWEEN**

EL operador **BETWEEN** selecciona valores en un rango dado. Los valores pueden ser numeros, texto o fechas. El operador es inclusivo, eso significa que el valor del principio y el final seran incluidos.

Sintaxis:

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

Ejemplos:

```sql
— Seleccioname todos los productos donde el precio este entre 20 y 40
SELECT * FROM Products WHERE Price BETWEEN 20 AND 40;
```

```sql
— Seleccioname todos los productos donde el precio
— este entre 20 y 40 y la categoría del producto sea la 6
SELECT * FROM Products WHERE Price BETWEEN 20 AND 40 AND CategoryID = 6
```

El operador between nos sirve tambien para seleccionar rangos de fechas

```sql
— Selecioname todos los empleados que hayan nacido entre 1960 hasta 1970
SELECT * FROM Employees WHERE BirthDate BETWEEN "1960-0-1" AND "1970-0-1"
```

**Operador LIKE**

El operador **LIKE** se utiliza para buscar por un determinado patron en una columna. Es como una expresión regular pero mas básica. LIKE y el operador = son exactamente iguales.

Sintaxis:
```sql
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
```

Ejemplos:

```sql
-- Este ejemplo nos devuelve el registro que estemos buscando segun el nombre despues de LIKE
SELECT * FROM Employees WHERE LastName LIKE "Fuller"
```

```sql
-- Este ejemplo nos devuelve el registro que estemos buscando segun el LIKE, pero si escribimos "Fuller "
-- con este espacio al final ya no funcionara
SELECT * FROM Employees WHERE LastName LIKE "Fuller "
```

```sql
-- Este ejemplo nos devuelve el registro que estemos buscando segun el LIKE
-- La clausala LIKE funciona igual que un =
SELECT * FROM Employees WHERE LastName = "Fuller"
```

 La diferencia entre _=_ y _LIKE_ es que LIKE es usualmente usado junto con dos comodines:

- El signo de porcentage _%_ representa 0, 1 o mas caracteres, lo que significa que puede coincidir con cualquier secuencia de caracteres en la posición donde se encuentra.
- El carácter de guión bajo *_* representa un solo carácter y solo uno. Y puede coincidir con cualquier carácter individual en la posición donde se encuentra. Es decir: el caracter _ hace referencia a cualquier cosa

Veamos algunos ejemplos del uso de LIKE junto con sus comodines:

```sql
-- Seleccioname todos los registros de la tabla Employees donde el nombre tenga 4 letras y comience con una N, tenga un segundo caracter cualquiera y termine en ncy
SELECT * FROM Employees WHERE FirstName LIKE "N_ncy"
```

```sql
-- Seleccioname todos los registros de la tabla Employees donde el nombre comience con M y pueda tener cualquier numero de caracteres despues
SELECT * FROM Employees WHERE FirstName LIKE "M%"
```

```sql
-- Seleccioname todos los registros de la tabla Employees donde el nombre contenga una e y pueda tener cualquier numero de caracteres antes y despues
SELECT * FROM Employees WHERE FirstName LIKE "%e%"
```

```sql
-- Selecioname un nombre que empiece por a, tenga una letra después y luego contenga lo que sea
SELECT * FROM Employees WHERE FirstName LIKE "A_%"
```

**Operadores IS NULL e IS NOT NULL**

El operador **IS NULL** devuelve  solo los valores NULL de la  base de datos en caso de que existan.

```sql
-- Devuelve solo los valores nulos de la base de datos
SELECT * FROM Products WHERE ProductName IS NULL
ORDER BY ProductName ASC
```

Por el contrario el operador **IS NOT NULL** va a devolver todos los valores de la tabla excepto los null.

```sql
-- Devuelveme todos los datos de la tabla product menos los registros null
SELECT * FROM Products WHERE ProductName IS NOT NULL
ORDER BY ProductName ASC
```

**Operador IN**

El operador **IN** en SQL se utiliza principalmente para realizar multiples comparaciones con una lista de valores. Permite verificar si un valor está presente en una lista de valores especificada. Es una abreviación de multiples condiciones **OR**. 

Sintaxis:
El formato basico de una consulta que utiliza el operador IN es esta:

```sql
SELECT column_name(s) 
FROM table_name
WHERE columna IN (valor1, valor2, ..., valorN);
```

> La clausula IN se puede usar en la clausula select, update y delete

Ejemplos:

```sql
-- Devuelveme todos los supplier (proveedores) que tengan los identificadores 3, 4, 5, 6
SELECT * FROM Products WHERE SupplierID IN (3, 4, 5, 6)
```

```sql
-- Devuelveme todos los lastname que sean Fuller o Suyama
SELECT * FROM Employees
WHERE LastName in ("Fuller", "Suyama")
```

## SECCIÓN INTERMEDIA

### Funciones de agregación

Una función de agregación es una funcion que ejecuta un calculo en un grupo de valores y retorna un unico valor. Las funciones de agregacion normalmente son usadas con la clausula **GROUP BY** de la declaración **SELECT**. La clausula **GROUP BY** divide el conjunto de resultados en grupos de valores y las funciones de agregación pueden ser usadas para regresar un solo valor por cada grupo. Las funciones de agregación ignoran los valores NULL excepto **COUNT()**.

Las funciones de agregacion mas utilizadas son:

- **MIN()** - Devuelve el valor mas pequeño dentro de la columna seleccionada
- **MAX()** - Devuelve el valor mas grande dentro de la columna seleccionada
- **COUNT()** - Devuelve el nuúmero de filas | registros en el conjunto
- **SUM()** - Devuelve la suma de una columna numerica
- **AVG()** - Devuelve el promedio de una columna numerica
- **ROUND()** - Redondea un numero a un especifico numero de partes decimales

Ejemplos:

```sql
-- Cuantos empleados hay: esto hace una cuenta de cuantos registros tiene la tabla Employees
SELECT count(LastName) AS Cantidad_de_nombres FROM Employees
```

```sql
-- Sumar todos los precios de la tabla products
SELECT SUM(Price) from Products
```

```sql
-- Dame el promedio del precio de los productos
SELECT AVG(Price) from Products
```

```sql
-- Dame el promedio del precio de los productos y redondea el valor final
SELECT ROUND(avg(Price)) from Products
```

```sql
-- Dame el promedio del precio de los productos, redondea el valor final y ponle un alias a la columna price
SELECT ROUND(avg(Price)) AS Promedio from Products
```

```sql
-- Dame el promedio del precio de los productos y redondea el valor final con 2 decimales y ponle un alias a la columna price
SELECT ROUND(avg(Price), 2) AS Promedio from Products
```

```sql
-- Cual es el precio minimo que tiene la columna price exeptuando los null
SELECT MIN(Price) FROM Products
where ProductName IS NOT NULL
```

```sql
-- Estoy obteniendo el producto con menor precio exeptuando los null
SELECT ProductName, MIN(Price) FROM Products
where ProductName IS NOT NULL
```

```sql
-- Estoy obteniendo el producto con el maximo precio exeptuando los null
SELECT ProductName, max(Price) FROM Products
```

### Clausula GROUP BY

La instrucción **GROUP BY** agrupa filas que tienen los mismos valores en las filas que resumen. Es decir: hace un conteo de cuantos registros hay por la fila que se este agrupando.

La declaración GROUP BY es usado normalmente con funciones de agregación (COUNT(), MAX(), MIN(), SUM(), AVG()) para agrupar los resultados en una o mas columnas.

![groupby](https://www.programiz.com/sites/tutorial2program/files/sql-group-by.png)

En la imagen anterior usando la clausula group by, se devuelve una nueva tabla con el total de clientes por pais.

Sintaxis:

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
```

Ejemplos:

```sql
-- Dame el promedio de cada proveedor
SELECT SupplierID, ROUND(avg(price)) AS promedio FROM Products GROUP BY SupplierID
```

```sql
-- Dame el promedio de cada proveedor menos los valores que sean null
-- Entonces lo que estamos viendo es el promedio del costo de cada categoria
SELECT CategoryID, ROUND(avg(price)) AS promedio FROM products
WHERE CategoryID IS NOT NULL
GROUP BY CategoryID
```

```sql
-- Cual fue el producto que mas se vendio
SELECT ProductID, SUM(Quantity) as Total from OrderDetails
GROUP BY ProductID
ORDER BY Total DESC
LIMIT 1
```

```sql
-- Cual fue el producto que menos se vendio
SELECT ProductID, SUM(Quantity) as Total from OrderDetails
GROUP BY ProductID
ORDER BY Total ASC
LIMIT 1
```

### Clausula HAVING

La clausula **HAVING** fue añadida a SQL porque con la palabra clave **WHERE** no podemos usar funciones de agregación. Entonces, con WHERE podemos filtrar registros, con HAVING podemos filtrar grupos.

Sintaxis:

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```

Ejemplos:

```sql
-- Dame el promedio de cada proveedor menos los valores que sean null
-- Entonces lo que estamos viendo es el promedio del costo de cada categoria
SELECT SupplierID, ROUND(avg(price)) AS promedio FROM products
GROUP BY SupplierID
HAVING promedio > 40
```

```sql
-- Dame cuantas veces se vendio un producto y solo los que se vendieron mas de 50 veces
SELECT ProductID, SUM(Quantity) as Total from OrderDetails
GROUP BY ProductID
HAVING Total > 50
```

La jerarquía para el query seria asi:

> Primero siempre se selecciona (SELECT)
Luego hacemos el filtro (WHERE)
Luego seguiría agrupar registros (GROUP BY)
Luego seguiria usar el (HAVING), que solo se usa para los grupos

```sql
SELECT…. FROM …
WHERE …
GROUP BY …
HAVING …
ORDER BY …
LIMIT …
```

## Subconsultas

Como su nombre lo indica, una subconsulta es una consulta que esta dentro de una consulta. Es decir: una consulta anidada dentro de una consulta más grande. 

Ejecutan una consulta pequeña y con el resultado de esa mini consulta, ejecutan otra consulta que es la principal. Las subconsultas **SIEMPRE** tienen que ser un select, algo que recupera datos: entonces, **las subconsultas siempre consultan la base de datos, no la alteran**
Las subconsultas siempre van (entre parentesis)

![subquery](https://www.mariadbtutorial.com/wp-content/uploads/2019/10/MariaDB-subqueries.png)

Ejemplo básico:

```sql
-- Seleccioname de la tabla OrderDetails el productID y la cantidad que se vendio (Quantity)
-- en la subconsulta, ahora seleccioname el productName de la tabla products,
-- donde el productId de la tabla OrderDetails sea igual al ProductID de la tabla products

SELECT
	ProductID,
	Quantity,
	(SELECT ProductName from Products WHERE OrderDetails.ProductID = ProductID) As ProductName -- Esta es la subconsulta
	from OrderDetails
```


La consulta anterior es igual a esto:

```sql
SELECT
	ProductID,
	Quantity,
	(SELECT ProductName from Products WHERE OD.ProductID = ProductID) As ProductName -- Esta es la subconsulta
	from OrderDetails AS OD 
```
Más ejemplos:

```sql
-- Seleccionamos ProductID y Quantity de la tabla OrderDetails con sobrenombre OD
-- creamos la columna ProductName a partir de la tabla products y OrderDetails
-- creamos la columna precio unitario a partir de la tabla Products y OrderDetails
SELECT
	ProductID,
	Quantity,
	(SELECT ProductName from Products WHERE OD.ProductID = ProductID) As ProductName, -- Esta es la subconsulta1
	(SELECT price from Products where OD.ProductID = ProductID) as PrecioUnitario -- Esta es la subconsulta2
	from [OrderDetails] OD
```

```sql
-- Seleccionamos ProductID y sumamos el total de cantidades vendidas,
-- creamos la columna ProductName a partir de la tabla products y OrderDetails
-- creamos la columna precioXunidad a partir de la tabla Products y OrderDetails
-- ahora creamos la columna totalRecaudado que sale de multiplicar el total_vendido_X_unidad + el precio por unidad
-- Agrupamos por ProductID para que puedan salir los totales recaudados por categoria

SELECT ProductID, SUM(Quantity) as total_vendido_X_unidad,
	(SELECT ProductName from Products WHERE OD.ProductID = ProductID) As ProductName, -- Esta es la subconsulta1
	(SELECT Price from Products where OD.ProductID = ProductID) as PrecioXUnidad, -- Esta es la subconsulta2
	(SUM(Quantity) * (SELECT Price FROM Products WHERE OD.ProductID = ProductID)) as totalRecaudado -- Esta es la subconsulta3
	FROM [OrderDetails] OD
GROUP BY ProductID 
```

```sql
SELECT ProductID, SUM(Quantity) as totalVendidoXunidad,
(SELECT ProductName from Products WHERE OD.ProductID = ProductID) as ProductName,
(SELECT Price from Products WHERE OD.ProductID = ProductID) as PrecioXunidad,
round(SUM(Quantity) * (SELECT Price FROM Products WHERE OD.ProductID = ProductID)) as total_recaudado
FROM [OrderDetails] OD
GROUP BY ProductID
ORDER BY total_recaudado DESC
```

```sql
-- Aqui usamos una subconsulta para seleccionar solo los productos resultantes de la subconsulta price > 40
SELECT ProductID, SUM(Quantity) as totalVendidoXunidad,
(SELECT ProductName from Products WHERE OD.ProductID = ProductID) as ProductName,
round(SUM(Quantity) * (SELECT Price FROM Products WHERE OD.ProductID = ProductID)) as total_recaudado
FROM [OrderDetails] OD
WHERE (SELECT Price from Products WHERE OD.ProductID = ProductID) > 40
GROUP BY ProductID
ORDER BY total_recaudado DESC
```

```sql
-- Las subconsultas tambien pueden ser usadas con from
SELECT ProductName FROM (
	SELECT ProductID, SUM(Quantity) as totalVendidoXunidad,
	(SELECT ProductName from Products WHERE OD.ProductID = ProductID) as ProductName,
	round(SUM(Quantity) * (SELECT Price FROM Products WHERE OD.ProductID = ProductID)) as total_recaudado
	FROM [OrderDetails] OD
	WHERE (SELECT Price from Products WHERE OD.ProductID = ProductID) > 40
	GROUP BY ProductID
	ORDER BY total_recaudado DESC
)
```

```sql
-- Las subconsultas tambien pueden ser usadas con from,
-- Esta tabla creada no esta en ninguna parte, la hemos creado juntando varios datos
-- ahora podemos pedir las columnas y tambien poderlas filtrar
SELECT ProductName, total_recaudado FROM (
	SELECT ProductID, SUM(Quantity) as totalVendidoXunidad,
	(SELECT ProductName from Products WHERE OD.ProductID = ProductID) as ProductName,
	round(SUM(Quantity) * (SELECT Price FROM Products WHERE OD.ProductID = ProductID)) as total_recaudado
	FROM [OrderDetails] OD
	WHERE (SELECT Price from Products WHERE OD.ProductID = ProductID) > 40
	GROUP BY ProductID
	ORDER BY total_recaudado DESC
) where total_recaudado > 100
```

```sql
-- Obtenemos los empleados que vendieron mas que el promedio
-- Selecciona el nombre y apellido de los empleados
SELECT FirstName,LastName,
-- Subconsulta para calcular la suma total de las unidades de los pedidos de cada empleado
(SELECT SUM(od.Quantity) FROM [orders] o, [OrderDetails] od
WHERE o.EmployeeID = e.EmployeeID AND od.OrderID = o.OrderID) as unidades_totales 
FROM [Employees] e
-- Filtra los empleados que tienen un total de unidades menor que el promedio de unidades totales de todos los empleados
WHERE unidades_totales < (SELECT AVG(unidades_totales)
-- Subconsulta para calcular la suma total de las unidades de los pedidos de cada empleado
FROM (
SELECT (SELECT SUM(od.Quantity) FROM [orders] o, [OrderDetails] od
WHERE o.EmployeeID = e2.EmployeeID AND od.OrderID = o.OrderID) as unidades_totales
FROM [Employees] e2
GROUP BY e2.EmployeeID
))
```

### JOINS

Los **Joins** en SQL son una forma de combinar filas de dos o más tablas, basadas en una columna relacionada entre ellas y posteriormente mostrar una sola tabla.
La cláusula Join te permite recuperar datos de varias tablas basándote en un campo común entre ellas.

Hay varios tipos de Join:

- **Cross Join:** En este tipo de Join, todas las celdas se juntan con todas las celdas. Es decir todas las posibilidades se dan. Estamos multiplicando la cantidad de filas que hay en una columna por la cantidad de filas que hay en otra columna.

![crossJoin](https://raw.githubusercontent.com/Kaziuz/learning-sql/main/photos/crossJoin.jpg)

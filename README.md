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

Clave Foránea (Foreign key)
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
Para generar esta imagen este fue el script usado
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

## Base de datos Northwind

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



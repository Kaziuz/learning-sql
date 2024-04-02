import sqlite3
import pandas as pd

square = lambda n : n*n # Vamos a crear una function que potencie un numero al cubo

conn = sqlite3.connect("Northwind.db") # nos conectamos a la db

conn.create_function("square", 1, square) # registramos la function en sql lite (nombre de la function en sqllite, #parametros, function que se le va a pasar)

cursor = conn.cursor() # Establece un objeto para poder ejecutar declaraciones SQL

cursor.execute('''
  SELECT *, square(Price) FROM Products
  ''') # Ejecutamos el query sql con la function que registramos

results = cursor.fetchall()        # Obtenemos el resultado de la consulta
results_df = pd.DataFrame(results) # guardamos el resultado de la consulta en un frame

# liberamos los recursos del computador
cursor.close()
conn.close()

print(results_df)



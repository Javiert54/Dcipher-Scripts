import sqlite3
import pandas as pd

def search_in_all_tables(database_path, search_text):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    # Get all table names
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    
    # crear y borrar el contenido del archivo 'permutaciones.txt' antes de iniciar el bucle
    open('results.txt', 'w').close()
    
    # Iterate over each table
    for table in tables:
        table = table[0]
        # Get all column names
        cur.execute(f"PRAGMA table_info({table});")
        columns = cur.fetchall()

        # Iterate over each column
        for column in columns:
            column = column[1]

            # Execute the search query
            cur.execute(f"SELECT {column} FROM {table} WHERE {column} GLOB '*{search_text}*';")
            results = cur.fetchall()

            # If the search text is found in the current column of the current table
            if results:
                print(f"\nFound '{search_text}' {len(results)} times in table '{table}', column '{column}'. Here are the matching entries:")
                
                with open('results.txt', 'a') as f:
                    f.write(f"\nFound '{search_text}' {len(results)} times in table '{table}', column '{column}'. Here are the matching entries:")
                    
                line=''
                for index, row in enumerate(results):
                    print(f"\n  -{index+1}: ", end='')
                    for rowIndex, element in enumerate(row):
                        
                        print(element, end= "//|#/ ")
                        if isinstance(element, bytes):
                            line += element.decode('latin-1')
                        else:
                            line += element

                        if rowIndex < len(row)-1:
                            line+= '//|#/ '

                with open('results.txt', 'a', encoding='latin-1') as f:
                    f.write(line)



    # Close the connection
    conn.close()

def print_table(database_path, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)

    # Use pandas to read the table into a DataFrame
    df = pd.read_sql_query(f"SELECT * from {table_name}", conn)

    # Print the DataFrame
    print(df)

    # Close the connection
    conn.close()

# Call the function to print the 'conversation' table from 'my_database.db'

dataBase = input('Ruta de la base de datos: ')
text2Find = input('\nIntroduce el texto a buscar en la base de datos: ')
# Call the function to search in all tables of 'my_database.db' for 'my_search_text'
# print_table(dataBase, 'conversation')
search_in_all_tables(dataBase, text2Find)

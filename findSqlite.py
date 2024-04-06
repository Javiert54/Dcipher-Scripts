import sqlite3

def search_in_all_tables(database_path, search_text):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    # Get all table names
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    # Iterate over each table
    for table in tables:
        table = table[0]
        # Get all column names
        cur.execute(f"PRAGMA table_info({table});")
        columns = cur.fetchall()

        # Iterate over each column
        for column in columns:
            column = column[1]
            try:
                # Execute the search query
                cur.execute(f"SELECT {column} FROM {table} WHERE {column} GLOB '*{search_text}*';")
                results = cur.fetchall()

                # If the search text is found in the current column of the current table
                if results:
                    print(f"Found '{search_text}' in table '{table}', column '{column}'. Here are the matching entries:")
                    for row in results:
                        print(row[0])
            except:
                pass

    # Close the connection
    conn.close()

# Call the function to search in all tables of 'my_database.db' for 'my_search_text'
search_in_all_tables(input('Ruta de la base de datos: '), input('\nIntroduce el texto a buscar en la base de datos: '))

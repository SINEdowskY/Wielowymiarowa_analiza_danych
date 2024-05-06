import pyodbc
from abc import ABC

class DB:
    def __init__(self) -> None:
        self._server = None
        self._database = None
        self._username = None
        self._password = None
        self._driver = None
    
    def _connection_str(self) -> str:
        conn_str = f'DRIVER={self._driver};\
            SERVER={self._server}; \
            DATABASE={self._database};\
            UID={self._username};\
            PWD={self._password}'
        return conn_str

    def custom_query(self, query: str):
        with pyodbc.connect(self._connection_str()) as connection:
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.commit()
            print(f"Executed: {query}")
            cursor.close()
            connection.close()

class DBAdmin(DB):
    def __init__(self) -> None:
        self._server = 'localhost'
        self._database = 'master'
        self._username = 'sa'
        self._password = 'YourStrongPassword123'
        self._driver = '{ODBC Driver 17 for SQL Server}'
    
    def custom_db_user(self, login: str, password: str, db: str):
        with pyodbc.connect(self._connection_str()) as connection:
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(f"CREATE LOGIN {login} WITH PASSWORD = '{password}';")
            cursor.execute(f"USE {db};")
            cursor.execute(f"CREATE USER {login} FOR LOGIN {login};")
            cursor.commit()
            cursor.close()
            connection.close()



class DBData(DB):
    def __init__(self) -> None:
        self._server = 'localhost'
        self._database = 'Data'
        self._username = 'WAD169781'
        self._password = 'YourStrongPassword123'
        self._driver = '{ODBC Driver 17 for SQL Server}'
    
    def csv_to_sql_table(self) -> None:
        pass

class DBDataAgg(DB):
    def __init__(self) -> None:
        self._server = 'localhost'
        self._database = 'DataAgg'
        self._username = 'sa'
        self._password = 'YourStrongPassword123'
        self._driver = '{ODBC Driver 17 for SQL Server}'
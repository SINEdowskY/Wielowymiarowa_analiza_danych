from sqlalchemy import create_engine, Engine, text, inspect

class DatabaseMisc:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def database_exists(self, db_name:str) -> bool:
        query = text(f"SELECT COUNT(*) FROM sys.databases WHERE name = '{db_name}'")
        with self.engine.connect() as connection:
            result = connection.execute(query)
            return result.scalar() == 1
    
    def login_exists(self, login: str):
        query = text(f"SELECT COUNT(*) FROM sys.sql_logins WHERE name = '{login}'")
        with self.engine.connect() as connection:
            result = connection.execute(query)
            return result.scalar() == 1
        
    def database_user_exists(self, username: str):
        pass

class Database:
    def __init__(self, username:str, password:str, database:str, server:str) -> None:
        self._server = server
        self._database = database
        self._username = username
        self._password = password
        self._driver = "ODBC Driver 17 for SQL Server"

        self._connection_url = f"mssql+pyodbc://{self._username}:{self._password}@{self._server}:1433/{self._database}?driver={self._driver}"
        
        self._engine = create_engine(self._connection_url, isolation_level="AUTOCOMMIT")
        self.misc = DatabaseMisc(self._engine)

class DatabaseAdmin(Database):
    
    def create_database(self, database_name:str):
        db_exists = self.misc.database_exists(db_name = database_name)
        if db_exists:
            print(f"The database '{database_name}' exists.")
        else:
            with self._engine.connect() as connection:
                connection.execute(text(f"CREATE DATABASE {database_name}"))
                connection.commit()
                print(f"Created Database: {database_name}")
                connection.close()
    
    def drop_database(self, database_name:str):
        db_exists = self.misc.database_exists(db_name = database_name)
        if db_exists:
            with self._engine.connect() as connection:
                connection.execute(text(f"DROP DATABASE {database_name}"))
                connection.commit()
                print(f"Dropped Database: {database_name}")
                connection.close()
        else:
            print(f"The database '{database_name}' does not exist.")
    
    def create_login(self, login:str, password:str):
        user_exists = self.misc.login_exists(login)
        
        if user_exists:
            print(f"The user '{login}' exists.")
        else:
            with self._engine.connect() as connection:
                connection.execute(
                    text(f"CREATE LOGIN {login} WITH PASSWORD = '{password}'")
                )
                connection.commit()
                print(f"Created Login: {login}")
                connection.close()
    
    def drop_login(self, login:str):
        user_exists = self.misc.login_exists(login)

        if user_exists:
            with self._engine.connect() as connection:
                connection.execute(
                    text(f"DROP LOGIN {login}")
                )
                connection.commit()
                print(f"Dropped Login: {login}")
                connection.close()
            
        else:
            print(f"The user '{login}' does not exist.")

    
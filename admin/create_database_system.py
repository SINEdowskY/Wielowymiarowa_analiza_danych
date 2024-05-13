from database import DatabaseAdmin

db = DatabaseAdmin("SA", "YourStrongPassword123", "master", "localhost")

db.create_database("Data")
db.create_database("Data_Clean")
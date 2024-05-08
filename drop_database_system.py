from admin.database import DatabaseAdmin

db = DatabaseAdmin("SA", "YourStrongPassword123", "master", "localhost")

db.drop_database("Data")
db.drop_login("WAD169781")
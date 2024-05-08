from admin.database import DatabaseAdmin

db = DatabaseAdmin("SA", "YourStrongPassword123", "master", "localhost")

db.create_database("Data")
db.create_database("Data_Agg")
db.create_login("WAD169781", "Debil1234567890")
db.create_login("WAD169781", "Debil1234567890")
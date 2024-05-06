from admin.database import DBAdmin

admin = DBAdmin()
admin.custom_query("CREATE DATABASE Data")
admin.custom_query("CREATE DATABASE DataAgg")

admin.custom_db_user("WAD169781", "YourStrongPassword123", "Data")
admin.custom_db_user("WAD169840", "YourStrongPassword123", "Data")

admin.custom_db_user("WAD169781", "YourStrongPassword123", "DataAgg")
admin.custom_db_user("WAD169840", "YourStrongPassword123", "DataAgg")